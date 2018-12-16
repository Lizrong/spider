# -*- coding: utf-8 -*-
import scrapy
from qichacha.items import QichachaItem

class ChachaSpider(scrapy.Spider):
    name = 'chacha'
    # allowed_domains = ['www.qichacha.com']
    # start_urls = ['http://www.qichacha.com/']
    def start_requests(self):
        url = 'https://www.qichacha.com/elib_research.shtml?p={}'
        for i in range(1,5):
            fulurl =url.format(i)
            yield scrapy.Request(fulurl,callback=self.parse)
    def parse(self, response):
        item = QichachaItem()
        #报告名称
        # name= response.xpath('//table[@class="ntable"]//td/a/text()').extract()
        # for i in name:
        #     print(i)
        #     item['name']=i
        # #报告的url
        baourl= response.xpath('//table[@class="ntable"]//td/a/@href').extract()

        item['pdfwei']=baourl
        yield item
