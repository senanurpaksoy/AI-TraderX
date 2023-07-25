from apscheduler.schedulers.background import BackgroundScheduler
import time
from datetime import datetime, time as dtime


# Başlama zamanlayıcısı

def start_job():
    scheduler = BackgroundScheduler()
    scheduler.add_job(my_task, 'cron', hour='10-17', minute='*')
    scheduler.start()

# Bitiş zamanlayıcısı
def end_job():
    # Bitiş zamanlayıcısını ayarla, işlem 18:00'da bitecek
    scheduler = BackgroundScheduler()
    scheduler.add_job(end_job, 'cron', hour='18', minute='0')
    scheduler.shutdown()
# Deneme Task eklendi
def my_task():
    print("Görev çalıştı:", datetime.now().strftime('%H:%M:%S'))
