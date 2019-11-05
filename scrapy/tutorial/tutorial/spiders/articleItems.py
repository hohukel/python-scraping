# coding: utf-8
"""
Itemオブジェクトを使ってサイトデータを格納
"""
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tutorial.items import Article

# CrawlSpiderから継承(Spiderではない)
class ArticleSpider(CrawlSpider):
    name='articleItems'

    allowed_domains = ['wikipedia.org'] # このドメイン以外は無視
    start_urls = ['https://en.wikipedia.org/wiki/Benevolent_dictator_for_life']

    # callback引数に指定し関数でページをparseする, ルールは上から順に適用
    rules = [
        Rule(LinkExtractor(allow='(/wiki/)((?!:).)*$'), callback='parse_items', follow=True),
    ]

    def parse_items(self, response, is_article):
        print("URL is ", response.url)
        article = Article()
        article['url'] = response.url
        # cssセレクタ->子タグ(入れ子のタグ)のtextは無視, xpathセレクタ->子タグのtextも含めて抽出
        article['title'] = response.css('h1::text').extract_first()
        article['text'] = response.xpath('//div[@id="mw-content-text"]//text()').extract()
        lastUpdated = response.css('li#footer-info-lastmod::text').extract_first()
        article['lastUpdated'] = lastUpdated.replace("This page was last edited on ",'')
        return article
