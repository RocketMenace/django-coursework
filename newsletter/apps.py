from django.apps import AppConfig
from time import sleep

class NewsletterConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "newsletter"

    # def ready(self):
    #
    #     from newsletter.newsletter_scheduler import start_sending
    #     sleep(2)
    #     start_sending()
