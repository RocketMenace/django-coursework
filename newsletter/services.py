from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from .models import NewsLetter, DistributionAttempt
from django.utils import timezone
from smtplib import SMTPException


# Need optimization for list of emails.
def send_newsletter(pk):

    newsletter = NewsLetter.objects.select_related().filter(status="создана").get(pk=pk)
    emails = [recipient.email for recipient in newsletter.recipient.all()]
    try:
        response = send_mail(
            subject=newsletter.message.title,
            message=newsletter.message.body,
            from_email="grizzly18721@yandex.2ru",
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
            server_response=e.__dict__["smtp_code"],
            newsletter=newsletter,
        )
