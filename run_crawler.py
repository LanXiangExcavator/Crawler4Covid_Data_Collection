import time
from apscheduler.schedulers.blocking import BlockingScheduler
import os

def job2crawl():
    print('start job2crawl')
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    os.system('scrapy crawl covid')
    print('scrapy crawl done --- {}'.format(t))

def job2run_server():
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print('try to run / restart web server on port 8050 --- {}'.format(t))
    os.system('docker run -it -p 8050:8050 --rm scrapinghub/splash')

def job4today():
    print('start job2crawl')
    job_defaults = {
        'max_instances': 5
    }
    scheduler_in_a_day = BlockingScheduler(job_defaults=job_defaults)
    current_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    scheduler_in_a_day.add_job(job2crawl, 'interval', minutes=1, args=[],
                               start_date=current_date + ' 11:30:05', end_date=current_date + ' 12:30:05')
    print('crawler for today starts --- {}'.format(current_date))
    scheduler_in_a_day.start()
    print('crawler for today done --- {}'.format(current_date))



scheduler_manage_days = BlockingScheduler()
scheduler_manage_days.add_job(job4today, 'cron', hour=11, minute=0)
scheduler_manage_days.start()
