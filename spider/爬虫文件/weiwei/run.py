from apscheduler.schedulers.blocking import BlockingScheduler
from scrapy import cmdline
base = BlockingScheduler()

def fun_min():
    cmdline.execute('scrapy crawl wei'.split())
    # cmdline.execute('scMongoPinpelinerapy crawl wei'.split())
fun_min()
base.add_job(fun_min,'interval',days=1)
base.start()