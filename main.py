import time
from apscheduler.schedulers.blocking import BlockingScheduler
import os

def job2crawl():
    print('start job2crawl')
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    os.system('scrapy crawl quotes')
    print('scrapy crawl done --- {}'.format(t))
    # 每隔 1分钟 运行一次 job 方法
    # scheduler.add_job(job, 'interval', minutes=1, args=['scrawler done'])
def job4today():
    print('start job2crawl')
    scheduler_in_a_day = BlockingScheduler()
    current_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    scheduler_in_a_day.add_job(job2crawl, 'interval', minutes=1, args=[],
                               start_date=current_date + ' 14:40:05', end_date=current_date + ' 16:40:05')
    print('crawler for today starts --- {}'.format(current_date))
    scheduler_in_a_day.start()


scheduler_manage_days = BlockingScheduler()
scheduler_manage_days.add_job(job4today, 'cron', hour=16, minute=23)
scheduler_manage_days.start()
