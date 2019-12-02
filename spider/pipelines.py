# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

import MySQLdb
#db = MySQLdb.connect("localhost", "root", "123456", "spider", charset="utf8")

from scrapy.mail import MailSender

class SpiderPipeline(object):

    def open_spider(self, spider):
        
        print('管道初始化...')

    def process_item(self, item, spider):

        '''
        获取item数据
        进行存储
        mysql、file、mongo...
        '''

    # 生成CSV
    def csv(self, data_row):

        path = "本地csv路径"
        with open(path, 'a+') as f:
            csv_write = csv.writer(f)
            csv_write.writerow(data_row)

    def close_spider(self, spider):

        print('管道关闭...')