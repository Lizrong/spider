# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import json
from random import uniform

from scrapy import signals, Request
from scrapy.http import HtmlResponse
from dazhong import settings


class DazhongSpiderMiddleware(object):
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


class DazhongDownloaderMiddleware(object):
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
# 导入chrome选项
from selenium.webdriver.chrome.options import Options
import time
import logging
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
#导入驱动接口
from selenium import webdriver
class SeleniumDownloaderMiddleware(object):
    cookMap = {}
    def __init__(self):
        self.chrome_options = Options()
        # self.chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options)
    def process_request(self,request,spider):

        # 打开浏览器
        # self.driver.get(request.url)

        # 设置日志等级
        logging.basicConfig(level=logging.INFO)

        used_selenium = request.meta.get('used_selenium',False)

        if used_selenium:
            if request.meta.get('pageType','') == 'login':
                username_ = "18091044294"
                password_ = "fan427329"
                #原始的url
                originalUrl = request.url
                try:
                    self.driver.get(originalUrl)
                    # 选择账号登录
                    iframe = self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/iframe')
                    self.driver.switch_to.frame(iframe)  # 切换至登录模块iframe

                    # 选择账号密码登录
                    icon_pc = self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]')
                    icon_pc.click()
                    time.sleep(8)
                    name_login = self.driver.find_element_by_xpath('//*[@id="tab-account"]')
                    name_login.click()
                    time.sleep(10)

                    # 输入用户名,密码
                    username = self.driver.find_element_by_xpath('//input[@id="account-textbox"]')
                    password = self.driver.find_element_by_xpath('//input[@id="password-textbox"]')
                    username.clear()
                    username.send_keys(username_)
                    time.sleep(20)
                    password.clear()
                    password.send_keys(password_)
                    time.sleep(25)
                    # 提交登陆
                    sub_btn = self.driver.find_element_by_xpath('//button[@id="login-button-account"]')
                    sub_btn.click()
                    time.sleep(15)
                    # 切换回主页
                    self.driver.switch_to.default_content()
                except Exception as e:
                        print(e)
                else:
                    request.meta['used_selenium'] = False

        else:
            self.driver.get(request.url)
            time.sleep(uniform(5,10))
            url = self.driver.current_url
            return HtmlResponse(url,body=self.driver.page_source.encode(),status=200)





