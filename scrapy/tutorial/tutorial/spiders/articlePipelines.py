# coding: utf-8
"""
pipelineを使う
"""
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tutorial.items import Article

# CrawlSpiderから継承(Spiderではない)
class ArticleSpider(CrawlSpider):
    name='articlePipelines'

    allowed_domains = ['wikipedia.org'] # このドメイン以外は無視
    start_urls = ['https://en.wikipedia.org/wiki/Benevolent_dictator_for_life']

    # callback引数に指定し関数でページをparseする, ルールは上から順に適用
    rules = [
        Rule(LinkExtractor(allow='(/wiki/)((?!:).)*$'), callback='parse_items', follow=True),
    ]

    def parse_items(self, response):
        article = Article()
        article['url'] = response.url
        # cssセレクタ->子タグ(入れ子のタグ)のtextは無視, xpathセレクタ->子タグのtextも含めて抽出
        article['title'] = response.css('h1::text').extract_first()
        article['text'] = response.xpath('//div[@id="mw-content-text"]//text()').extract()
        article['lastUpdated'] = response.css('li#footer-info-lastmod::text').extract_first()
        return article
