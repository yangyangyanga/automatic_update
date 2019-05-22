from jk_en.sendEmail import *
import os
import sys


# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# print("***********************", os.path.dirname(os.path.abspath(__file__)))
# os.system('scrapy crawl school_jk_spider')

from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from jk_en.spiders import school_jk_apider


configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
runner = CrawlerRunner()

d = runner.crawl(school_jk_apider.SchoolJkSpiderSpider)
d.addBoth(lambda _: reactor.stop())
reactor.run()

SendEmailMain()