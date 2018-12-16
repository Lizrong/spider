# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeixinItem(scrapy.Item):
    #文章标题
    MsgTitle = scrapy.Field()
    # 公众号名称
    NickName = scrapy.Field()
    # 类型
    CateName = scrapy.Field()
    # 阅读量
    ReadNum = scrapy.Field()
