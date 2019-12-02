# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.item import Item, Field

class SpiderItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    cinema = Field()
    magementname = Field()
    province = Field()
    city = Field()
    code = Field()
    fp = Field()
    ky = Field()
    sj = Field()
    yinmushu = Field()
    urlcode = Field()

    '''
    cinema2 = Field()
    magementname2 = Field()
    province2 = Field()
    city2 = Field()
    code2 = Field()
    fp2 = Field()
    ky2 = Field()
    sj2 = Field()
    yinmushu2 = Field()
    urlcode2 = Field()
    '''