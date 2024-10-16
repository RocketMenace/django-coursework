from apscheduler.schedulers.background import BackgroundScheduler
from .services import send_newsletter


def start_sending():

    scheduler = BackgroundScheduler()
    scheduler.add_job(send_newsletter, "interval", seconds=10)
    scheduler.start()
