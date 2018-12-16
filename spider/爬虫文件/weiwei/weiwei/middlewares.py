# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random

from scrapy import signals
from scrapy.http import HtmlResponse


class WeiweiSpiderMiddleware(object):
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


class WeiweiDownloaderMiddleware(object):
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

import base64

proxyServer = "http://http-dyn.abuyun.com:9020"
# 代理隧道验证信息
proxyUser = "HSGX775M8N0WO6VD"
proxyPass = "D25CA976902F497D"
# for Python3
proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass),     "ascii")).decode("utf8")
print(proxyAuth)
class ABProxyMiddleware(object):
    """ 阿布云动态ip代理中间件 """
    def process_request(self, request, spider):
        request.meta["proxy"] = proxyServer
        request.headers["Proxy-Authorization"] = proxyAuth

from selenium.webdriver.chrome.options import Options
import time
from random import uniform
from selenium import webdriver

class SeleniumDownloaderMiddleware(object):
    def __init__(self):
        self.chrome_options = Options()
        # self.chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options)
        # self.login_url = 'https://account.wxb.com/?from=https%3A%2F%2Fdata.wxb.com%2Frank'

    def process_request(self,request,spider):

        # 设置用户名密码
        used_selenium = request.meta.get('used_selenium', False)

        if used_selenium:
            if request.meta.get('pageType', '') == 'login':
                username_ = "18135999936"
                # username_ = "15035455735"
                password_ = "fan427329"
                originalUrl = request.url
                # 点击证号登录
                try:
                    self.driver.get(originalUrl)
                    self.driver.find_element_by_xpath("//h2[@class='col-12 text-center']").click()
                    time.sleep(1)
                    # 输入证号和密码
                    username = self.driver.find_element_by_xpath("//input[@id='email']")
                    password = self.driver.find_element_by_xpath("//input[@id='password']")
                    username.clear()
                    username.send_keys(username_)
                    time.sleep(1)
                    password.clear()
                    password.send_keys(password_)
                    time.sleep(1)
                    # 提交登录
                    self.driver.find_element_by_xpath("//button[@class='btn primary bold']").click()
                    time.sleep(7)
                except Exception as e:
                    print(e)
                else:
                    request.meta['used_selenium'] = False
        else:
            self.driver.get(request.url)

        time.sleep(uniform(10,20))
        content = self.driver.page_source
        url = self.driver.current_url

        return HtmlResponse(url, body=self.driver.page_source.encode(),status=200)

