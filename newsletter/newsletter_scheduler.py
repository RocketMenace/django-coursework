from apscheduler.schedulers.background import BackgroundScheduler
from .services import NewsletterSender


def start_sending():

    scheduler = BackgroundScheduler()
    scheduler.add_job(NewsletterSender.start, "interval", seconds=10)
    scheduler.start()
