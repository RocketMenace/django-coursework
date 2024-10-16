from smtplib import SMTPException

from django.core.mail import send_mail
from django.utils import timezone

from config.settings import EMAIL_HOST_USER
from .models import NewsLetter, DistributionAttempt


def send_newsletter():

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
    for newsletter in newsletters:
        DistributionAttempt.objects.filter(newsletter=newsletter).order_by("-last_try").first()
        # if newsletter.regularity == NewsLetter.Regularity.DAILY and ():
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
        return emails

    def update_status(self):
        """Change status of expired newsletters."""
        pass

    def check_regularity(self, newsletter):
        """Check newsletter regularity."""
        DistributionAttempt.objects.filter(newsletter).orde_by("last_try").first()

    def send_newsletter(self, newsletters:list[NewsLetter], emails:list[str]):

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