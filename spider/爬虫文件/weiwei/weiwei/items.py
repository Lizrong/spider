# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeiweiItem(scrapy.Item):
    # 公司名称
    company_name =scrapy.Field()
    # 公众号名称
    name = scrapy.Field()
    #'类型'
    category_name =scrapy.Field()
    time = scrapy.Field()
    zong_read =scrapy.Field()
    top_read_num_total =scrapy.Field()
    like_num_total = scrapy.Field()
    top_like_num_total = scrapy.Field()
    articles_total = scrapy.Field()
    # 小宝指数
    xiaobao_zhi = scrapy.Field()
    # 粉丝数
    fen_si = scrapy.Field()
    # 更新时间
    stat_time = scrapy.Field()