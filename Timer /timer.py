from sched import scheduler

from apscheduler.schedulers.background import BackgroundScheduler
import time
from datetime import datetime, time as dtime
import Stockdata

# Başlama ve bitiş GMT+03:00 saatleri
start_time = dtime(10, 0, 0)  # 10:00:00
end_time = dtime(18, 0, 0)  # 18:00:00

# Başlama zamanlayıcısı
def start_job(task):
    scheduler = BackgroundScheduler()
    scheduler.add_job(task, "cron", hour=start_time, minute="*")
    scheduler.start()


# Bitiş zamanlayıcısı
def end_job():
    scheduler.shutdown()


# Görevimiz
#  Anlık saati döndürür
def my_task():
    print("Görev çalıştı:", datetime.now().strftime("%H:%M:%S"))


"""
if __name__ == '__main__':


    # Bütün bu tarih ve borsa işlevi durumları kullanıcıdan alınacak Standart değer olarak son 1 ay gösterilebilir.
    start_date = "2023-01-01"
    end_date = "2023-07-31"
    # Başlama zamanlayıcısını başlat, işlem 10:00'da başlayacak ve  görevini devreye sokacak
    start_job(Stockdata.get_stock_market("AAPL",start_date,end_date))

    # Bitiş zamanlayıcısını ayarla, işlem 18:00'da bitecek
    scheduler = BackgroundScheduler()
    scheduler.add_job(end_job, 'cron', hour=end_time, minute='0')
    scheduler.start()

    try:
        # Programın çalışmasını beklemek için döngü
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        # Ctrl+C ile zamanlayıcıları durdur
        scheduler.shutdown()



"""
