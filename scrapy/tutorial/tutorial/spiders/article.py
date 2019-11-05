# coding: utf-8
import scrapy
from scrapy import Spider
from scrapy.selector import Selector

# 記事ページだけを対象とする
class ArticleSpider(Spider):
    name="article"

    def start_requests(self):
        urls = ["http://en.wikipedia.org/wiki/Python_%28programming_language%29",
                "https://en.wikipedia.org/wiki/Functional_programming",
                "https://en.wikipedia.org/wiki/Monty_Python",
                ]
        return [scrapy.Request(url=url, callback=self.parse) for url in urls]

    def parse(self, response):
        url = response.url
        title = response.css('h1 ::text').extract_first()
        print('URL is ', url)
        print('TITLE is ', title)
        print('-'*50)
