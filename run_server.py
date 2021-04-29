import time
from apscheduler.schedulers.blocking import BlockingScheduler
import os

### NOTE: run this script with

def job2run_server():
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print('try to run / restart web server on port 8050 --- {}'.format(t))
    os.system('docker run -it -p 0.0.0.0:8050:8050 --rm scrapinghub/splash')

def job4today():
    print('Start job2run_server')
    scheduler_in_a_day = BlockingScheduler()
    current_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    scheduler_in_a_day.add_job(job2run_server, 'interval', minutes=1, args=[],
                               start_date=current_date + ' 11:29:00', end_date=current_date + ' 12:30:05')
    scheduler_in_a_day.start()
    print('job2run_server DONE')

scheduler_manage_days = BlockingScheduler()
scheduler_manage_days.add_job(job4today, 'cron', hour=11, minute=0)
scheduler_manage_days.start()
