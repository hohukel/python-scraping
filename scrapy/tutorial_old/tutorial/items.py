# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# ItemオブジェクトはWebサイトの1ページを表す
# itemはデータを格納するためのオブジェクト Djangoでいうmodelと同じ
class TutorialItem(scrapy.Item):
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()

class Article(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()

class YahooNewsItem(scrapy.Item):
    title = scrapy.Field()
    body = scrapy.Field()
    url = scrapy.Field()
    #headline = scrapy.Field()
