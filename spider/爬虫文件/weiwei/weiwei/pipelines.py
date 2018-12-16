# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv


class WeiweiPipeline(object):
    def open_spider(self,spider):
        self.fp = open('房产家居.csv','w',encoding='utf8',newline="")
        self.writer = csv.writer(self.fp)
        self.writer.writerow([ '公司名称','公众号名称','类型','时间','总浏览量','头条浏览量','总点赞数','头条点赞数',
                               '发文篇数','小宝指数','粉丝数','更新时间'])
    def process_item(self, item, spider):
        self.writer.writerow((item['company_name'],item['name'],item['category_name'],item['time'],item['zong_read'],item['top_read_num_total'],item['like_num_total'],item['top_like_num_total'],item['articles_total'],
                              item['xiaobao_zhi'],item['fen_si'],item['stat_time']))
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
        self.col = self.db.caijing
    def process_item(self,item,spider):
        self.col.insert(dict(item))
        return item
    def close_spider(self,spider):
        self.conn.close()

