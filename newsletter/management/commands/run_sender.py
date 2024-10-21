from django.core.management import BaseCommand
from newsletter.newsletter_scheduler import start_sending

class Command(BaseCommand):

    def handle(self, *args, **options):
        start_sending()
