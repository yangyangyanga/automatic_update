from scrapy import cmdline
from jk_ca.sendEmail import *
import os

# os.system('scrapy crawl school_jk_spider')
# os.system('python E:\jk_ca\jk_ca\sendEmail.py')
# cmdline.execute('scrapy crawl school_jk_spider'.split())
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from jk_ca.spiders import school_jk_spider


configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
runner = CrawlerRunner()

d = runner.crawl(school_jk_spider.SchoolJkSpiderSpider)
d.addBoth(lambda _: reactor.stop())
reactor.run()
SendEmailMain()