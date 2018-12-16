from scrapy import cmdline
from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler()


def fun_min():
    cmdline.execute('scrapy crawl wei'.split())
fun_min()
sched.add_job(fun_min,'interval',days=1)
sched.start()