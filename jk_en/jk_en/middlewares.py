# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import re,time
from selenium import webdriver
def clearallSB(str):
    str = ''.join(str)
    str = re.sub(r'\s{2,}', '', str)
    str = ''.join(str)
    str = re.sub(r'<script.+?</script>', '', str)
    return str
def remove_class(var):
        var = ''.join(var)
        # 清洗标签
        clear_class = re.findall(
            '[a-zA-Z\-]+=[\'\"][a-zA-Z0-9\-/\)\(\.\s\;\:\`\~\@\!\#\$\%\^\&\*\_\+\=\,\?\{\}]*[\'\"]', var)
        for i in clear_class:
            var = var.replace(' ' + i, '')
        # 去除a标签
        var = var.replace('<a>', '').replace('</a>', '')
        # 去除注释
        fan_ren_de_biao_qian = re.findall('<!.+?>', var)
        for i in fan_ren_de_biao_qian:
            var = var.replace(i, '')
        var = clear_same_s(var)
        return var
def clear_same_s(strs):
        strs = ''.join(strs).replace("\r", "").replace('\t', "")
        fan_ren_de_kong_ge = re.findall('  ', strs)
        if fan_ren_de_kong_ge != []:
            for i in fan_ren_de_kong_ge:
                strs = strs.replace(i, '')
        strs = strs.split('\n')
        while '' in strs:
            strs.remove('')
        strs = '\n'.join(strs)
        return strs
def runSelenuim(url):
    # 启动谷歌浏览器
    dirver = webdriver.Chrome(r'C:\Users\admin\AppData\Local\Programs\Python\Python36\Lib\site-packages\selenium\chromedriver.exe')
    dirver.get(url)
    # dirver.maximize_window()
    js = "var q=document.documentElement.scrollTop=800"
    dirver.execute_script(js)
    js = "var q=document.documentElement.scrollTop=1300"
    dirver.execute_script(js)
    time.sleep(0.2)
    dirver.quit()
class JkEnSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class JkEnDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
