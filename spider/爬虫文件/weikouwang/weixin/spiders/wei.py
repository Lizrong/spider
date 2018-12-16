# -*- coding: utf-8 -*-
import json

import scrapy
from weixin.items import  WeixinItem
class WeiSpider(scrapy.Spider):
    name = 'wei'
    allowed_domains = ['vccoo.com']
    #开始的url
    def start_requests(self):
        url = 'http://www.vccoo.com/'
        yield scrapy.Request(url, callback=self.parse)
    #
    def parse(self, response):
        # 每一类的url
        class_url = response.xpath("//div[@class='topMenu']//li/a/@href").extract()
        for url in class_url:
            a = url.split("?")[1]
            url2 = 'http://www.vccoo.com/leaderboard/?date=2018-12-09&' + str(a)
            print(">>>>>>>>>>>>>>2")
            yield scrapy.Request(url2, callback=self.url_parse)

    def url_parse(self, response):
        print('***************')
        lei = response.xpath("//li[@class='hotArt-menuitem']/a/text()").extract()
        print(lei)
        qiang_url = response.xpath("//a[@class='leaderbNick']/@href").extract()
        print(qiang_url)
        qiang_url1 = dict(zip(lei, qiang_url))
        print(qiang_url1)
        for name, i in qiang_url1.items():
            url3 = 'http://www.vccoo.com' + i
            print(">>>>>>>>>>>>3")
            print(url3)
            yield scrapy.Request(url3, callback=self.de_json,meta={"name":name})

    def de_json(self, response):
        name = response.meta['name']
        for i in range(1, 40):
            url = response.url + "?page=" + str(i)
            print(url)
            print(">>>>>>>>>>>>>>4")
            yield scrapy.Request(url, callback=self.wenzhang,meta={"name":name})

    def wenzhang(self, response):
        item = WeixinItem()
        # 文章标题
        contents = response.xpath("//div[@class='bookTitle']")
        NickName = response.xpath("//div[@class='personalSet-c']/span/text()").extract_first()
        item['NickName'] = NickName

        name = response.meta['name']
        item['CateName'] = name
        for content in contents:
            item['MsgTitle'] = content.xpath(".//a/text()").extract_first()
            ReadNum= content.xpath(".//i[1]/text()").extract_first().strip('阅读')
            item['ReadNum'] =ReadNum

            yield item





