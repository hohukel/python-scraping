# coding: utf-8
"""
Itemオブジェクトを使わない
"""
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

# CrawlSpiderから継承(Spiderではない)
class ArticleSpider(CrawlSpider):
    name='articles' # articleの進化版

    # start_requests関数の代わりに以下2つを定義
    allowed_domains = ['wikipedia.org'] # このドメイン以外は無視
    start_urls = ['https://en.wikipedia.org/wiki/Benevolent_dictator_for_life']

    # callback引数に指定し関数でページをparseする, ルールは上から順に適用
    rules = [
        Rule(LinkExtractor(allow='(/wiki/)((?!:).)*$'), callback='parse_items', follow=True, cb_kwargs={'is_article': True}),
        Rule(LinkExtractor(allow=r'.*'),callback='parse_items',follow=True,cb_kwargs={'is_article':False})
    ]

    def parse_items(self, response, is_article):
        print("URL is ", response.url)
        # cssセレクタ->子タグ(入れ子のタグ)のtextは無視, xpathセレクタ->子タグのtextも含めて抽出
        title = response.css('h1::text').extract_first()
        #title = response.xpath('//h1/text()').extract_first()
        if is_article:
            url = response.url
            text = response.xpath('//div[@id="mw-content-text"]//text()').extract()
            lastUpdated = response.css('li#footer-info-lastmod::text').extract_first()
            lastUpdated = lastUpdated.replace("This page was last edited on ",'')
            print('Title is ', title)
            #print('Text is ', text)
            print('LastUpdated: ', lastUpdated)
        else:
            print('This is not an article: ', title)
        print('-'*50)
