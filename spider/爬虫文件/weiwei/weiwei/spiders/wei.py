# -*- coding: utf-8 -*-
import json
import time


import scrapy

from weiwei.items import WeiweiItem
class WeiSpider(scrapy.Spider):
    name = 'wei'
    allowed_domains = ['data.wxb.com']
    def start_requests(self):
        url = 'https://account.wxb.com/?from=https%3A%2F%2Fdata.wxb.com%2Frank'
        yield scrapy.Request(url,callback=self.parse,meta={'used_selenium':True,'pageType':'login'})
    def parse(self, response):
        for a in range(6, 21):
            url = 'https://data.wxb.com/rank?category=' + str(a) + '&page={}'
            for i in range(1, 20):
                fururl = url.format(i)
                yield scrapy.Request(fururl, callback=self.parse)
    def mei_parse(self, response):
        print(">>>>>>>>>>>>>999", response.url)
        mei_urls = response.xpath("//div[@class='wxb-avatar-name']/a/@href").extract()
        print(mei_urls)
        for mei_url in mei_urls:
            url= "https://data.wxb.com"+mei_url
            print("******")
            print(url)
            yield scrapy.Request(url,callback=self.gong_parse)
    def gong_parse(self,response):
        print(">>>>>>>>>>>>>fo",response.url)
        item = WeiweiItem()
        aa= response.xpath("//script[@type='text/javascript'][1]/text()").extract_first().strip('window.__INITIAL_STATE__ = ')
        bb = json.loads(aa)
        dd = bb['details']
        ff = dict(dd)
        detailOverview= ff['detailOverview']
        overviewData =detailOverview['overviewData']
        item['name'] = overviewData['name']
        item['xiaobao_zhi'] = overviewData['index_scores']
        item['fen_si'] = overviewData['fans_num_estimate']
        #更新时间
        item['stat_time'] = overviewData['stat_time']
        #公司名称
        item['company_name'] = overviewData['company']
        #类型
        item['category_name'] = overviewData['category_name']
        mm = ff['postRead']
        gg =mm['echartsData']
        zan = dict(gg)
        #将所有时间放入一个列表中遍历
        time1 =[]
        print(">>>>>>>>>>>>>>>>>>pass")
        for k in zan:
            time1.append(k)
        for i in time1:
            kk =zan[i]
            #时间
            item['time']=i
            #总阅读量
            item['zong_read']=kk['read_num_total']
            #头条阅读量
            item['top_read_num_total']=kk['top_read_num_total']
            #总点赞数
            item['like_num_total']=kk['like_num_total']
            #头条点赞数
            item['top_like_num_total']=kk['top_like_num_total']
            #发文篇数
            item['articles_total']=kk['articles_total']

            yield item