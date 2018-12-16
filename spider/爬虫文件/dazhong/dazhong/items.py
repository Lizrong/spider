# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DazhongItem(scrapy.Item):
    dian_name=scrapy.Field()
    ren_jun = scrapy.Field()
    address = scrapy.Field()
    phone = scrapy.Field()
    hao_ping=scrapy.Field()
    ping_lun =scrapy.Field()