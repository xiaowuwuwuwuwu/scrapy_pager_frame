# -*- coding: utf-8 -*-

from lxml.html import parse
import scrapy
from bs4 import BeautifulSoup
from scrapy import FormRequest
from scrapy import Request
from scrapy import Selector

from spider.items import SpiderItem

import logging
logger = logging.getLogger(__name__)

class GameSpider(scrapy.Spider):

    #爬虫名称
    name = "tjjspt_spider"

    #允许的域名
    allowed_domains = ["xx.org"]

    header = {
        "xxx": "xxx",
    }

    page = 1

    def start_requests(self):  # 用start_requests()方法,代替start_urls

        #登录
        yield FormRequest(
            url='xx.com',
            method='POST',  # 指定访问方式
            formdata={
                #Form表单提交
                'xx': 'xx',
            },
            dont_filter=True,  # 不进行去重处理
            callback=self.parse
        )

    def parse(self, response):

        #首页
        request = scrapy.Request(
            "xx.com", callback=self.parseItem,dont_filter=True)
        yield request

    def parseItem(self, response):

        item = SpiderItem()

        soup = BeautifulSoup(response.body, 'html.parser', from_encoding='gbk')

        '''
        此处编写获取数据逻辑
        item[title] = title
        ...
        '''

        #如果存在下一页则继续请求
        #parsePager()

    def parsePager(self):

        '''
        此处编写分页逻辑
        request = scrapy.Request("xxx.com?page=1")
        yield = request
        '''

    def engine_stopped(self):

        print('stopped')
