# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy,datetime


class JkEnItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    old_id = scrapy.Field()
    major_name_en = scrapy.Field()
    degree_name = scrapy.Field()
    state_code = scrapy.Field()
    url_now = scrapy.Field()
    url_old = scrapy.Field()
    university = scrapy.Field()
    update_time = scrapy.Field()
    web_label = scrapy.Field()
    web_content = scrapy.Field()
    change_context = scrapy.Field()
def get_item(itemClass):
    item=itemClass()
    item['old_id'] = ''
    item['major_name_en'] = ''
    item['degree_name'] = ''
    item['state_code'] = ''
    item['url_now'] = ''
    item['url_old'] = ''
    item['university'] = ''
    item['update_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    item['web_label'] = None
    item['web_content'] = None
    item['change_context'] = None
    return item