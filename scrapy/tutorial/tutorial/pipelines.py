# -*- coding: utf-8 -*-
from datetime import datetime
from tutorial.items import Article
from string import whitespace

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class TutorialPipeline(object):
    def process_item(self, article, spider):
        article['lastUpdated'] = article['lastUpdated'].replace("This page was last edited on ",'')
        article['lastUpdated'] = article['lastUpdated'].replace(u"\xa0(UTC)",'').strip('.').strip()
        article['lastUpdated'] = datetime.strptime(article['lastUpdated'], '%d %B %Y, at %H:%M')
        article['text'] = [line for line in article['text'] if line not in whitespace]
        article['text'] = ''.join(article['text'])
        return article
