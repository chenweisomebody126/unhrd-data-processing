# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UnhrdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Item_Code = scrapy.Field()
    Description = scrapy.Field()
    Quantity = scrapy.Field()
    Owner = scrapy.Field()
    Location = scrapy.Field()
