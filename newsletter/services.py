from smtplib import SMTPException

from django.core.mail import send_mail
from django.utils import timezone

from config.settings import EMAIL_HOST_USER
from .models import NewsLetter, DistributionAttempt


class NewsletterSender:
    """Class for handling newsletter sending."""

    def prepare_list_of_emails(self) -> list[str]:
        """Preparing list of emails for the following sending."""
        newsletters = (
            NewsLetter.objects.prefetch_related("recipient")
            .only("recipient", "regularity")
            .filter(start_date__lte=timezone.now())
            .filter(status="создана")
        )
        emails = []
        for newsletter in newsletters:
            for recipient in newsletter.recipient.all():
                emails.append(recipient.email)
        return newsletters, emails

    def update_status(self, newsletter):
        """Change status of expired newsletters."""
        if newsletter.end_date < timezone.now:
            newsletter.status = NewsLetter.Status.COMPLETED
            newsletter.save()

    def check_status(self, newsletter):
        """Check status if newsletter."""
        pass

    def check_regularity(self, newsletter):
        """Check newsletter regularity."""
        last_sent = (
            DistributionAttempt.objects.filter(newsletter=newsletter)
            .order_by("last_try")
            .first()
        )
        if newsletter.regularity == NewsLetter.Regularity.DAILY:
            next_send_time = last_sent.last_try + timezone.timedelta(
                days=1,
                hours=newsletter.start_date.hour,
                minutes=newsletter.start_date.minute,
            )
        if newsletter.regularity == NewsLetter.Regularity.WEEKLY:
            next_send_time = last_sent.last_try + timezone.timedelta(
                days=7,
                hours=newsletter.start_date.hour,
                minutes=newsletter.start_date.minute,
            )
        if newsletter.regularity == NewsLetter.Regularity.MONTHLY:
            next_send_time = last_sent.last_try + timezone.timedelta(
                days=31,
                hours=last_sent.start_date.hour,
                minutes=last_sent.start_date.minute,
            )
        newsletter.start_date = next_send_time
        newsletter.save()

    def send_newsletter(self, newsletters: list[NewsLetter], emails: list[str]):
        """Sending emails to recipients that's specified in newsletters."""

        for newsletter in newsletters:
            try:
                response = send_mail(
                    subject=newsletter.message.title,
                    message=newsletter.message.body,
                    from_email=EMAIL_HOST_USER,
                    recipient_list=emails,
                    fail_silently=False,
                )
                DistributionAttempt.objects.create(
                    status=DistributionAttempt.Status.SUCCESSFUL,
                    server_response=response,
                    newsletter=newsletter,
                )
            except SMTPException as e:
                DistributionAttempt.objects.create(
                    status=DistributionAttempt.Status.UNSUCCESSFUL,
                    server_response=e.__dict__["smtp_error"],
                    newsletter=newsletter,
                )

    def start():
        newsletters, emails = NewsletterSender.prepare_list_of_emails()
        for newsletter in newsletters:
            NewsletterSender.check_regularity(newsletter)
        NewsletterSender.send_newsletter(newsletters, emails)
        NewsletterSender.update_status(newsletters)
