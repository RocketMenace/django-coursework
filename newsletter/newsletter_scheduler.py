from apscheduler.schedulers.background import BackgroundScheduler
from .services import NewsletterSender


def start_sending():
    sender = NewsletterSender()
    scheduler = BackgroundScheduler()
    scheduler.add_job(sender.start, "interval", seconds=10)
    scheduler.start()
