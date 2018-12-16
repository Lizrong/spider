# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv


class WeixinPipeline(object):
    def open_spider(self,spider):
        self.fp = open('今日12-号文章.csv','w',encoding='utf8',newline="")
        self.writer = csv.writer(self.fp)
        self.writer.writerow(['文章标题','公众号名称','阅读量','类型'])
    def process_item(self, item, spider):
        self.writer.writerow((item['MsgTitle'],item['NickName'],item['ReadNum'],item['CateName']))
        return item
    def close_spider(self,spider):
        self.fp.close()
import pymongo
class MongoPinpeline(object):
    def open_spider(self,spider):
        self.conn = pymongo.MongoClient('localhost',27017)
        #选择数据库
        self.db = self.conn.weixiaobao
        #选择集合
        self.col = self.db.wenzhang
    def process_item(self,item,spider):
        self.col.insert(dict(item))
        return item
    def close_spider(self,spider):
        self.conn.close()