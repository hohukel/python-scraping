# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import YahooNewsItem

class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['yahoo.co.jp']
    start_urls = ['http://news.yahoo.co.jp/']

    def parse(self, response):
        # 任意の数字は'\d'で表し,'r'はバックスラッシュがエスケープ文字として判定されるのを防ぐ
        # ::attr(属性名)で属性の値を取得 リンクのURLを取得->::attr(href)
        for url in response.css('ul.topicsList_main a::attr("href")').re(r'/pickup/\d+$'):
            # item = YahooNewsItem()
            # urlを絶対パスに変換
            abs_url = response.urljoin(url)
            #item['item'] = 'hoge'
            # yield scrapy.Request(abs_url, callback=self.parse_topics, meta={'item', item})
            yield scrapy.Request(abs_url, self.parse_topics)

    def parse_topics(self, response):
        print ("welcom")
        #item = response.meta('item')
        item = YahooNewsItem()
        item['title'] = response.css('.tpcNews_title ::text').extract_first()
        item['body'] = response.css('.tpcNews_summary ::text').extract_first()
        item['url'] = response.url
        yield item
