from jk_au.sendEmail import *
import os
# os.system('scrapy crawl school_jk_spider')

from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from jk_au.spiders import school_jk_spider


configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
runner = CrawlerRunner()

d = runner.crawl(school_jk_spider.SchoolJkSpiderSpider)
d.addBoth(lambda _: reactor.stop())
reactor.run()

SendEmailMain()