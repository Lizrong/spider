# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import base64
import random

import requests
from scrapy import signals


class WeixinSpiderMiddleware(object):
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


class WeixinDownloaderMiddleware(object):
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

class RandomProxy(object):
    def __init__(self):

        # 代理验证信息
        self.proxy_auth = "lin427329:q3ycvfjk"
        # 代理api接口
        self.proxy_api = "http://dps.kdlapi.com/api/getdps/?orderid=934443400844790&num=10&pt=1&sep=1"
        # 发送代理api请求，获取代理列表
        self.proxy_list = requests.get(self.proxy_api, timeout=180).text.split()

    def process_request(self, request, spider):
        if len(self.proxy_list)==0:
            self.proxy_list = requests.get(self.proxy_api, timeout=60).text.split()

        proxy = self.proxy_list.pop()
        # 对代理验证信息进行base64编码
        base64_userpass = base64.b64encode(self.proxy_auth.encode("utf-8"))
        # 在请求里添加代理
        request.meta['proxy'] = "http://" + proxy
        # 添加代理验证信息
        request.headers['Proxy-Authorization'] = b"Basic " + base64_userpass


    # def __init__(self):
    #     self.ippools_list=[
    #
    #         '124.172.117.189:19812'
    #         '219.133.31.120:26947'
    #         '183.237.194.145:28436'
    #         '183.62.172.50:23485'
    #         '163.125.157.243:17503'
    #         '183.57.42.79:26483'
    #         '202.103.150.70:17251'
    #         '182.254.129.124:15395'
    #         '58.251.132.181:20659'
    #         '112.95.241.76:21948'
    #     ]
    #
    #
    # def process_request(self, request, spider):
    #     self.ip = random.choice(self.ippools_list)
    #     # print('#' * 50)
    #     print('当前使用的ip---%s' % self.ip)
    #     # print('#' * 50)
    #     proxy ='http://'+ self.ip
    #     print(proxy)
    #     request.meta['proxy'] =proxy
    #     request.meta['download_timeout'] = 5
    #     request.headers["Proxy-Authorization"] = proxyAuth
    # def process_exception(self,request,exception,spider):
    #
    #     # print('*'*50)
    #     # print(exception)
    #     # print('*'*50)
    #     self.ippools_list.remove(self.ip)
    #     return request