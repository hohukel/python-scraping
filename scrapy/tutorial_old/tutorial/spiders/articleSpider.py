# coding: utf-8
from scrapy.selector import Selector
from scrapy import Spider
from tutorial.items import Article

class ArticleSpider(Spider):
    name="article"
    allowed_domains = ["en.wikipedea.org","http://news.yahoo.co.jp/"]
    start_urls = ["https://en.wikipedia.org/wiki/Main-Page",
                "https://en.wikipedia.org/wiki/Python_(programming_language)",
                "http://news.yahoo.co.jp/"]

    def parse(self, response):
        # ItemオブジェクトはWebサイトの1ページを表す
        for t in response.xpath('//h1/text()'):
            title = t.extract()
            #print("Title is: "+title)
            item = Article()
            item['title'] = title
            yield item
