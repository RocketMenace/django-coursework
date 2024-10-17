from smtplib import SMTPException

from django.core.mail import send_mail
from django.utils import timezone

from config.settings import EMAIL_HOST_USER
from .models import NewsLetter, DistributionAttempt


class NewsletterSender:
    """Class for handling newsletter sending."""

    def _prepare_list_of_emails(self):
        """Preparing list of emails for the following sending."""
        newsletters = (
            NewsLetter.objects.prefetch_related("recipient")
            .only("recipient", "regularity", "end_date", "status")
            .filter(start_date__lte=timezone.now())
            .filter(status="запущена")
        )
        emails = []
        for newsletter in newsletters:
            for recipient in newsletter.recipient.all():
                emails.append(recipient.email)
        return newsletters, emails

    def _update_status(self):
        """Change status of expired newsletters."""
        newsletters = NewsLetter.objects.only("end_date", "status")
        for newsletter in newsletters:
            if newsletter.end_date < timezone.now():
                newsletter.status = NewsLetter.Status.COMPLETED
                newsletter.save()

    def check_status(self, newsletter):
        """Check status if newsletter."""
        pass

    def _check_regularity(self, newsletters):
        """Check newsletter regularity."""

        for newsletter in newsletters:
            last_sent = (
                DistributionAttempt.objects.only("last_try")
                .filter(newsletter=newsletter)
                .order_by("last_try")
                .first()
            )
            if newsletter.regularity == NewsLetter.Regularity.DAILY:
                next_send_time = last_sent.last_try + timezone.timedelta(
                    days=1,
                )
                newsletter.start_date = next_send_time
                newsletter.save()
            if newsletter.regularity == NewsLetter.Regularity.WEEKLY:
                next_send_time = last_sent.last_try + timezone.timedelta(
                    days=7,
                )
                newsletter.start_date = next_send_time
                newsletter.save()
            if newsletter.regularity == NewsLetter.Regularity.MONTHLY:
                next_send_time = last_sent.last_try + timezone.timedelta(
                    days=31,
                )
                newsletters.update(start_date=next_send_time)

    def _send_newsletter(self, newsletters: list[NewsLetter], emails: list[str]):
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

    def start(self):
        """Pipeline for sending newsletters."""
        sender = NewsletterSender()
        newsletters, emails = sender._prepare_list_of_emails()
        print(newsletters, emails, timezone.now())
        sender._send_newsletter(newsletters, emails)
        sender._check_regularity(newsletters)
        sender._update_status()
