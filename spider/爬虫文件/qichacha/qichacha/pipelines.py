# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os
import urllib.request


class QichachaPipeline(object):
    def process_item(self, item, spider):
        for i in item['pdfwei']:
            file_path = 'D:\数据\奇差'
            file_name = i.split('/')[-1]
            try:
                if not os.path.exists(file_path):
                    os.makedirs(file_path)
                filename = '{}{}{}'.format(file_path, os.sep, file_name)
                urllib.request.urlretrieve(i, filename)
            except Exception as e:
                print(e)
        return item



