# coding: utf-8
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

"""
chapter1
"""
URL = "http://www.pythonscraping.com/pages/page1.html"
URL = "http://www.pythonscraping.com/dummy/okuyama_page1.html"
URL = "http://www.okuyama.com/pages/page1.html"

try:
    html = urlopen(URL)
except HTTPError as e:
    print("HTTP ERROR")
except URLError as e:
    print("The server could not be found")
else:
    print ("It Worked!!")


bsObj = BeautifulSoup(html.read())
print(bsObj.h1)
print(bsObj.html.body.h1)
print(bsObj.div)
print(bsObj.title)
print(bsObj.html.head.title)

print(bsObj.dummy)
print(bsObj.dummy.dymmmy)

bsObj
bsObj.findAll
bsObj.findAll("title")
bsObj.findAll("title")[0]
bsObj.findAll("title")[0].get_text()
bsObj.findAll("title")[0] == bsObj.title
bsObj.findAll("body")[0].get_text()


"""
chapter2

BeautifulSoupのオブジェクト
- BeautifulSoupオブジェクト: bs_obj
- tagオブジェクト: name_list etc..
- NavigableStringオブジェクト
- Commentオブジェクト
"""

URL = "http://www.pythonscraping.com/pages/warandpeace.html"
html = urlopen(URL)
bs_obj = BeautifulSoup(html)
bs_obj

# fineAll関数を使って特定タグだけ抽出
name_list = bs_obj.findAll("span",{"class":"green"})
name_list
for name in name_list:
    print(name.get_text())

prince_list = bs_obj.findAll("span",{"class":"green"},text="the prince")
prince_list
for prince in prince_list:
    print(prince.get_text())
# "the prince"が何回登場するか
len(prince_list)
green_red_list = bs_obj.findAll("span",{"class":{"green","red"}})

one_name_list = bs_obj.find("span",{"class":"green"})
one_name_list
bs_obj.find("span",{"class":"green"}) == bs_obj.findAll("span",{"class":"green"},limit=1)[0]

"""
2.2.3 木のナビゲーション
"""

URL = "http://www.pythonscraping.com/pages/page3.html"
html = urlopen(URL)
bs_obj = BeautifulSoup(html)
bs_obj
"""
<html>
<head>
<style>
img{
	width:75px;
}
table{
	width:50%;
}
td{
	margin:10px;
	padding:10px;
}
.wrapper{
	width:800px;
}
.excitingNote{
	font-style:italic;
	font-weight:bold;
}
</style>
</head>
<body>
<div id="wrapper">
<img src="../img/gifts/logo.jpg" style="float:left;"/>
<h1>Totally Normal Gifts</h1>
<div id="content">Here is a collection of totally normal, totally reasonable gifts that your friends are sure to love! Our collection is
hand-curated by well-paid, free-range Tibetan monks.<p>
We haven't figured out how to make online shopping carts yet, but you can send us a check to:<br/>
123 Main St.<br/>
Abuja, Nigeria
We will then send your totally amazing gift, pronto! Please include an extra $5.00 for gift wrapping.</p></div>
<table id="giftList">
<tr><th>
Item Title
</th><th>
Description
</th><th>
Cost
</th><th>
Image
</th></tr>
<tr class="gift" id="gift1"><td>
Vegetable Basket
</td><td>
This vegetable basket is the perfect gift for your health conscious (or overweight) friends!
<span class="excitingNote">Now with super-colorful bell peppers!</span>
</td><td>
$15.00
</td><td>
<img src="../img/gifts/img1.jpg"/>
</td></tr>
<tr class="gift" id="gift2"><td>
Russian Nesting Dolls
</td><td>
Hand-painted by trained monkeys, these exquisite dolls are priceless! And by "priceless," we mean "extremely expensive"! <span class="excitingNote">8 entire dolls per set! Octuple the presents!</span>
</td><td>
$10,000.52
</td><td>
<img src="../img/gifts/img2.jpg"/>
</td></tr>
<tr class="gift" id="gift3"><td>
Fish Painting
</td><td>
If something seems fishy about this painting, it's because it's a fish! <span class="excitingNote">Also hand-painted by trained monkeys!</span>
</td><td>
$10,005.00
</td><td>
<img src="../img/gifts/img3.jpg"/>
</td></tr>
<tr class="gift" id="gift4"><td>
Dead Parrot
</td><td>
This is an ex-parrot! <span class="excitingNote">Or maybe he's only resting?</span>
</td><td>
$0.50
</td><td>
<img src="../img/gifts/img4.jpg"/>
</td></tr>
<tr class="gift" id="gift5"><td>
Mystery Box
</td><td>
If you love suprises, this mystery box is for you! Do not place on light-colored surfaces. May cause oil staining. <span class="excitingNote">Keep your friends guessing!</span>
</td><td>
$1.50
</td><td>
<img src="../img/gifts/img6.jpg"/>
</td></tr>
</table>
</div></body></html>
<div id="footer">
© Totally Normal Gifts, Inc. <br/>
+234 (617) 863-0736
</div>
"""

bs_obj.find("table",{"id":"giftList"})
# 子のタグ
len(list(bs_obj.find("table",{"id":"giftList"}).children))
# 子孫のタグ(imgタグ, spanタグも含まれる)
len(list(bs_obj.find("table",{"id":"giftList"}).descendants))

for child in bs_obj.find("table",{"id":"giftList"}).children:
    print(child)
    print("-"*20)
# 兄弟 (表題行thが抜かれる) -> 「表題行のnext」という解釈
for sibling in bs_obj.find("table",{"id":"giftList"}).tr.next_siblings:
    print(sibling)
    print("-"*20)
# Item Titleが抜かれる -> 「Item Titleのnext」という解釈
for sibling in bs_obj.find("table",{"id":"giftList"}).th.next_siblings:
    print(sibling)
    print("-"*20)
bs_obj.find("table",{"id":"giftList"}).th
bs_obj.find("table",{"id":"giftList"}).th.next_sibling.previous_sibling

bs_obj
# 親(tdタグ)の兄(1つ上のtdタグ)の兄(1つ上のtdタグ)の値
bs_obj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.previous_sibling.get_text()

"""
2.3,4,5 正規表現
"""

URL = "http://www.pythonscraping.com/pages/page3.html"
html = urlopen(URL)
bs_obj = BeautifulSoup(html)

# 余談
bs_obj.findAll("img")
"""
[<img src="../img/gifts/logo.jpg" style="float:left;"/>,
 <img src="../img/gifts/img1.jpg"/>,
 <img src="../img/gifts/img2.jpg"/>,
 <img src="../img/gifts/img3.jpg"/>,
 <img src="../img/gifts/img4.jpg"/>,
 <img src="../img/gifts/img6.jpg"/>]
"""
bs_obj.find("img").next_sibling.next_sibling # <h1>Totally Normal Gifts</h1>

import re
pattern = re.compile("oku[a-z]+[0-9]{4}")
result1 = pattern.match("okuyama0716")
result2 = pattern.match("takafumi")
result1.group()
result2 == None

result3 = re.match("oku[a-z]+[0-9]{4}", "okuyama0716")
result3

# 本題
import re

images = bs_obj.findAll("img",{"src":re.compile("\.\.\/img\/gifts\/img.*\.jpg")}
print(images)
#[<img src="../img/gifts/img1.jpg"/>,
# <img src="../img/gifts/img2.jpg"/>,
# <img src="../img/gifts/img3.jpg"/>,
# <img src="../img/gifts/img4.jpg"/>,
# <img src="../img/gifts/img6.jpg"/>]

for image in images:
    print(image["src"])
    print('-'*20)
    # 2.5 属性へのアクセス(aタグimgタグに有効): tag.attrs
    print(image.attrs)
    print('-'*20)
    print(image.attrs["src"])
    print('='*20)
'''
../img/gifts/img1.jpg
--------------------
{'src': '../img/gifts/img1.jpg'}
--------------------
../img/gifts/img1.jpg
====================
../img/gifts/img2.jpg
--------------------
{'src': '../img/gifts/img2.jpg'}
--------------------
../img/gifts/img2.jpg
====================
../img/gifts/img3.jpg
--------------------
{'src': '../img/gifts/img3.jpg'}
--------------------
../img/gifts/img3.jpg
====================
../img/gifts/img4.jpg
--------------------
{'src': '../img/gifts/img4.jpg'}
--------------------
../img/gifts/img4.jpg
====================
../img/gifts/img6.jpg
--------------------
{'src': '../img/gifts/img6.jpg'}
--------------------
../img/gifts/img6.jpg
====================
'''

"""
2.6 ラムダ式
"""

for hoge in bs_obj.findAll(lambda tag: len(tag.attrs) == 1):
    print(hoge)
    print ("-" * 20)
for hoge in bs_obj.findAll(lambda tag: len(tag.attrs) == 2):
    print(hoge)
    print ("-" * 20)

"""
chapter3
"""

"""
3.1 単一ドメインを走査する
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
URL = "https://en.wikipedia.org/wiki/Eric_Idle"
html = urlopen(URL)
bs_obj = BeautifulSoup(html)


bs_obj.find("div",{"id":"bodyContent"}).findAll("a",{"href":re.compile("^(/wiki/)((?!:).)*$")})

# divの中でidがbodyContentに設定されている、URLにコロンがない、/wiki/で始まる→人名へのリンク
for link in bs_obj.find("div",{"id":"bodyContent"}).findAll("a",{"href":re.compile("^(/wiki/)((?!:).)*$")}):
    if "href" in link.attrs:
        print (link.attrs["href"])
"""
3.2 サイト全体をクローリング
"""

bs_obj.findAll("a",{"href":re.compile("^/wiki/.*:")})
print(bs_obj.h1.get_text())
print(bs_obj.find(id="mw-content-text").findAll("p")[0].get_text())
print(bs_obj.find(id="mw-content-text").findAll("p")[1].get_text())
print(bs_obj.find(id="mw-content-text").findAll("p")[2].get_text())
print(bs_obj.find(id="mw-content-text").findAll("p")[-1].get_text())
print(bs_obj.find(id="ca-edit").find("span").find("a").attrs["href"])

"""
3.3 インターネットをクローリング
wikipediaから飛び出す
"""
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import datetime
import random
import re

# urlparseについて
## urllib.request: URLを開いて読む
## urllib.parse: URLを解析する
URL = "https://en.wikipedia.org/wiki/Eric_Idle"
html = urlopen(URL)
html
bs_obj = BeautifulSoup(html.read(), 'html5lib')
bs_obj
# 内部ページ
o = urlparse(URL)
o # ParseResult(scheme='https', netloc='en.wikipedia.org', path='/wiki/Eric_Idle', params='', query='', fragment='')
o.scheme
o.netloc
include_url = o.scheme + "://" + o.netloc #'https://en.wikipedia.org'

bs_obj.findAll("a",href=re.compile("^(\/|.*"+include_url+")"))
link = bs_obj.findAll("a",href=re.compile("^(\/|.*"+include_url+")"))[0]
link.attrs["href"].startswith("/")

bs_obj.findAll("a",href=re.compile("^(.*"+include_url+")"))
link = bs_obj.findAll("a",href=re.compile("^(.*"+include_url+")"))[0]
link.attrs["href"]
link.attrs["href"].startswith("/")

# 外部ページ
bs_obj.findAll("a",href=re.compile("^(http|www).*"))
exclude_url = o.netloc
exclude_url
bs_obj.findAll("a",href=re.compile("^(http|www)((?!"+exclude_url+").)*$"))
bs_obj.findAll("a",href=re.compile("^(http|www)(("+exclude_url+").)*$"))

hoge = set()
hoge.add("piyo")
hoge
fuga = set({"piyo"})
fuga == hoge


def myfunc():
    for i in range(3):
        yield 'okuyaja{}'.format(i)

generator = myfunc()
print(next(generator))
print(next(generator))
print(next(generator))

"""
4.2 さまざまなWebサイトのレイアウトを扱う
"""
import requests
from bs4 import BeautifulSoup

class Content:
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

def getPage(url):
    req = requests.get(url)
    return BeautifulSoup(req.text, 'html.parser')

def scrapeNYTimes(url):
    bs = getPage(url)
    title = bs.find('h1').text
    lines = bs.select('div.StoryBodyCompanionColumn div p')
    body = '\n'.join([line.text for line in lines])
    return Content(url, title, body)

def scrapeBrookings(url):
    bs = getPage(url)
    title = bs.find('h1').text
    # lines = bs.select('div.blog-content.content-column div p')
    body = bs.find('div', {'class', 'post-body'}).text
    return Content(url, title, body)

url_ny = ('https://www.nytimes.com/2018/01/25/'
        'opinion/sunday/silicon-valley-immortality.html')
url_bo = ('https://www.brookings.edu/blog/future-development/2018/01/26/'
        'delivering-inclusive-urban-access-3-uncomfortable-truths/')

content_ny = scrapeNYTimes(url_ny)
print('NYTimes Title: {}'.format(content_ny.title))
print('NYTimes URL: {}'.format(content_ny.url))
print(content_ny.body)

print('-' * 50)

content_bo = scrapeBrookings(url_bo)
print('Brooking Title: {}'.format(content_bo.title))
print('Brooking URL: {}'.format(content_bo.url))
print(content_bo.body)

"""
4.2 さまざまなWebサイトのレイアウトを扱う
→ 共通クラスを扱ってみよう

find関数を使用せずにselect関数を使って情報抽出をおこなう

find(All)関数: HTMLタグを抽出
select関数: cssセレクタを抽出
"""
import requests
from bs4 import BeautifulSoup

# Contains information about website structure 情報を格納せず方法を格納
class Website:
    def __init__(self, name, url, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.titleTag = titleTag
        self.bodyTag = bodyTag

# Common base class for all articles/pages 情報を格納
class Content:
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body
    # Flexible printing function controls output
    def printing(self):
        print ('URL: {}'.format(self.url))
        print ('TITLE: {}'.format(self.title))
        print ('BODY:\n{}'.format(self.body))

class Crawler:
    def getPage(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            print ("url is wrong")
            return None
        return BeautifulSoup(req.text, 'html.parser')

    # Utilty function used to get a content string from a Beautiful Soup
    # object and a selector. Returns an empty string
    # if no object is found for the given selector
    def safeGet(self, page_obj, selector):
        selectedElems = page_obj.select(selector)
        if selectedElems is not None and len(selectedElems) > 0:
            return '\n'.join([elem.get_text() for elem in selectedElems])
        return ''

    # Extract content from a given page URL
    def parse(self, site, url):
        bs_obj = self.getPage(url)
        if bs_obj is not None:
            title = self.safeGet(bs_obj, site.titleTag)
            body = self.safeGet(bs_obj, site.bodyTag)
            if title != '' :
                if body != '':
                    content = Content(url, title ,body)
                    content.printing()
                else:
                    print ("bodyTag is wrong")
            else:
                print ("titleTag is wrong")

siteData = [
    ['O\'Reilly Media', 'http://oreilly.com', 'h1', 'section#product-description'],
    #['Reuters', 'http://reuters.com', 'h1', 'div.StandardArticleBody_body_1gnLA'],
    ['Reuters', 'http://reuters.com', 'h1', 'div.StandardArticleBody_body p'],
    ['Brookings', 'http://www.brookings.edu', 'h1', 'div.post-body'],
    ['Brookings', 'http://www.brookings.edu', 'h1', 'div.post-body'],
    ['New York Times', 'http://nytimes.com', 'h1', 'div.StoryBodyCompanionColumn div p']
]

websites = []
for row in siteData:
    websites.append(Website(row[0], row[1], row[2], row[3]))

crawler = Crawler()
crawler.parse(websites[0], 'http://shop.oreilly.com/product/0636920028154.do')
crawler.parse(
    websites[1], 'http://www.reuters.com/article/us-usa-epa-pruitt-idUSKBN19W2D0')
crawler.parse(
    websites[2],'https://www.brookings.edu/blog/techtank/2016/03/01/idea-to-retire-old-methods-of-policy-education/')
crawler.parse(
    websites[3],'https://www.nytimes.com/2018/01/28/business/energy-environment/oil-boom.html')

"""
4.3 クローラを構造化する
"""

"""
4.3.1 検索によるサイトのクローリング
Crawling through sites with search
"""

import requests
from bs4 import BeautifulSoup

# Contains information about website structure 情報を格納せず方法を格納
class Website:
    def __init__(self, name, url, searchUrl, resultListing, resultUrl, absoluteUrl, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.searchUrl = searchUrl # 検索ページ
        self.resultListing = resultListing # 検索結果のcssセレクタ
        self.resultUrl = resultUrl # 検索結果のhref属性(URL)を保持するcssセレクタ
        self.absoluteUrl = absoluteUrl
        self.titleTag = titleTag
        self.bodyTag = bodyTag

# Common base class for all articles/pages 情報を格納
class Content:
    def __init__(self, topic, url, title, body):
        # topic -> 検索ワード
        self.topic = topic
        self.title = title
        self.body = body
        self.url = url
    # Flexible printing function controls output
    def printing(self):
        print ('New article found for topic: {}'.format(self.topic))
        print ('URL: {}'.format(self.url))
        print ('TITLE: {}'.format(self.title))
        print ('BODY:\n{}'.format(self.body))
        print ('-'*50)

class Crawler:
    def getPage(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            print ("url is wrong")
            return None
        return BeautifulSoup(req.text, 'html.parser')

    # Utilty function used to get a content string from a Beautiful Soup
    # object and a selector. Returns an empty string
    # if no object is found for the given selector
    def safeGet(self, page_obj, selector):
        child_objs = page_obj.select(selector)
        if child_objs is not None and len(child_objs) > 0:
            return child_objs[0].get_text()
        return ''

    # websiteでtopicを検索して見つけたページ全て記憶
    def search(self, topic, site):
        # 検索ページ + 検索ワード -> 検索結果ページ
        bs_obj = self.getPage(site.searchUrl + topic)
        searchResults = bs_obj.select(site.resultListing)
        for result in searchResults:
            url_link = result.select(site.resultUrl)[0].attrs['href']
            # 相対URLの場合絶対URLにする
            if site.absoluteUrl:
                bs_link = self.getPage(url_link)
            else:
                bs_link = self.getPage(site.url+url_link)
            if bs_link is None:
                print('page or URLのどっちかが誤り. Skipping!')
                return
            title = self.safeGet(bs_link, site.titleTag)
            body = self.safeGet(bs_link, site.bodyTag)
            if title != '' :
                if body != '':
                    content = Content(topic, url, title, body)
                    content.printing()
                else:
                    print ("bodyTag is wrong")
            else:
                print ("titleTag is wrong")

crawler = Crawler()

siteData = [
    ['O\'Reilly Media', 'http://oreilly.com', 'https://ssearch.oreilly.com/?q=',
        'article.product-result', 'p.title a', True, 'h1', 'section#product-description'],
    ['Reuters', 'http://reuters.com', 'http://www.reuters.com/search/news?blob=', 'div.search-result-content',
        'h3.search-result-title a', False, 'h1', 'div.StandardArticleBody_body'],
    ['Brookings', 'http://www.brookings.edu', 'https://www.brookings.edu/search/?s=',
        'div.list-content article', 'h4.title a', True, 'h1', 'div.post-body']
]

sites = []
for row in siteData:
    sites.append( Website(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
topics = ['python', 'data science']
for topic in topics:
    print ('='*50)
    print("GETTING INFO ABOUT: "+topic)
    print ('='*50)
    for targetSite in sites:
        print("SITE NAME: "+site.name)
        crawler.search(topic, targetSite)
        print ('-'*50)

"""
site = ['食べログ', 'https://tabelog.com', 'https://ssearch.oreilly.com/?q=',
'article.product-result', 'p.title a', True, 'h1', 'section#product-description']

        self.name = name
        self.url = url
        self.searchUrl = searchUrl
        self.resultListing = resultListing
        self.resultUrl = resultUrl
        self.absoluteUrl = absoluteUrl
        self.titleTag = titleTag
        self.bodyTag = bodyTag
"""


"""
4.3.2 リンクをたどってサイトをクローリングする
- 指定したURLパターンに合致するリンクをたどれるようにする
"""

import requests
from bs4 import BeautifulSoup
import re

# Contains information about website structure 情報を格納せず方法を格納
class Website:
    def __init__(self, name, url, taragetPattern, absoluteUrl, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.taragetPattern = taragetPattern # 目標URLの正規表現
        self.absoluteUrl = absoluteUrl
        self.titleTag = titleTag
        self.bodyTag = bodyTag

# Common base class for all articles/pages 情報を格納
class Content:
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body
    # Flexible printing function controls output
    def printing(self):
        print ('URL: {}'.format(self.url))
        print ('TITLE: {}'.format(self.title))
        print ('BODY:\n{}'.format(self.body))
        print ('-'*50)

class Crawler:
    def __init__(self, site):
        self.site = site
        self.visited = []

    def getPage(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            print ("url is wrong")
            return None
        return BeautifulSoup(req.text, 'html.parser')

    def safeGet(self, page_obj, selector):
        selectedElems = page_obj.select(selector)
        if selectedElems is not None and len(selectedElems) > 0:
            return '\n'.join([elem.get_text() for elem in selectedElems])
        return ''

    # ページのスクレイピング
    def parse(self, url):
        bs = self.getPage(url)
        if bs is not None:
            title = self.safeGet(bs, self.site.titleTag)
            body = self.safeGet(bs, self.site.bodyTag)
            if title != '' :
                if body != '':
                    content = Content(url, title, body)
                    content.printing()
                else:
                    print ("bodyTag is wrong")
            else:
                print ("titleTag is wrong")

    # サイトのクローリング
    def crawl(self):
        # webサイトホームページからページ取得
        bs = self.getPage(self.site.url)
        targetPages = bs.findAll('a', href=re.compile(self.site.taragetPattern))
        for targetPage in targetPages:
            targetPage = targetPage.attrs['href']
            if targetPage not in self.visited:
                self.visited.append(targetPage)
                if not self.site.absoluteUrl:
                    targetPage = self.site.url + targetPage
                self.parse(targetPage)

reuters = Website('Reuters', 'https://www.reuters.com', '^(/article/)',
                  False, 'h1', 'div.StandardArticleBody_body')
crawler = Crawler(reuters)
crawler.crawl()
len(crawler.visited)
print(crawler.visited)

"""
4.3.3 異なる種類のページもクローリングする
"""
class Website:
    def __init__(self, name, url, titleTag):
        self.name = name
        self.url = url
        self.titleTag = titleTag

# 製品ページのスクレイピング用の情報
class ProductWebsite(Website):
    def __init__(self, name, url, titleTag, productNumberTag, priceTag):
        website.__init__(name, url, titleTag)
        self.productNumberTag = productNumberTag
        self.priceTag = priceTag

# 記事ページのスクレイピング用の情報
class ArticleWebsite(Website):
    def __init__(self, name, url, titleTag, bodyTag, dateTag):
        website.__init__(name, url, titleTag)
        self.bodyTag = bodyTag
        self.dateTag = dateTag

"""
5. Scrapy

# 重要
- cssセレクタ->子タグ(入れ子のタグ)は無視, xpathセレクタ->子タグも含めて抽出

RuleとLinkExtractorの引数->84,85ページに記載
"""

"""
6 データを格納する
"""

"""
6.1 メディアファイル
単一ファイルのダウンロード
"""

from urllib.request import urlopen
from urllib.request import urlretrieve # 本章より登場リモートURLから画像をダウンロード
from bs4 import BeautifulSoup
img_local_dir = '/Users/okuyamatakashi/workspace/python-scraping/hohukel/img'
url = 'http://www.pythonscraping.com'
html = urlopen(url)
# bs = BeautifulSoup(requests.get(url).text, 'html.parser')
bs = BeautifulSoup(html, 'html.parser')
print(bs.find('a',{'id':'logo'}))
print(bs.find('a',{'id':'logo'}).find('img'))
print(bs.find('a',{'id':'logo'}).find('img')['src'])
imageLacation = bs.find('a',{'id':'logo'}).find('img')['src']
urlretrieve(imageLacation, '{}/pythonscraping_logo'.format(img_local_dir))

"""
6.1 メディアファイル
内部ファイルを全てダウンロード
"""

def getAbsoluteURL(base_url, source):
    if source.startswith('http://www.'):
        url = 'http://{}'.format(source[11:])
    elif source.startswith('www.'):
        url = 'http://{}'.format(source[4:])
    elif source.startswith('http://'):
        url = source
    else:
        url = '{}/{}'.format(base_url,source)
    if base_url not in url:
        return None

def getDownloadPath(base_url, absolute_url, download_dir):
    path = absolute_url.replace('www.', '').replace(base_url,'')
    path = download_dir + path
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)
    return path


download_dir = '/Users/okuyamatakashi/workspace/python-scraping/hohukel/download'
base_url = 'http://pythonscraping.com'
url = base_url
html = urlopen(url)
# bs = BeautifulSoup(requests.get(url).text, 'html.parser')
bs = BeautifulSoup(html, 'html.parser')
print(bs.findAll(src=True))
print(bs.findAll(src=True)[0])
print(bs.findAll(src=True)[0]['src'])
download_lst = bs.findAll(src=True)
for download_source in download_lst:
    file_url = getAbsoluteURL(base_url, download_source['src'])
    if file_url is not None:
        print(file_url)
file_url = 'http://pythonscraping.com/sites/default/files/lrg_0.jpg'
print('Download to ',getDownloadPath(base_url, file_url, download_dir))
urlretrieve(file_url, getDownloadPath(base_url, file_url, download_dir))


"""
6.2 データをCSVに格納する
"""
import csv
os.getcwd()
csv_dir = '/Users/okuyamatakashi/workspace/python-scraping/hohukel'

csvFile = open('{}/test.csv'.format(csv_dir), 'w+')
try:
    writer = csv.writer(csvFile)
    writer.writerow(('number', 'number plus 2','number times 2'))
    for i in range(10):
        writer.writerow((i, i+2, i*2))
finally:
    csvFile.close()


import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
url = 'https://en.wikipedia.org/wiki/Comparison_of_text_editors'
html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')

table = bs.find('table',{'class':'wikitable'})
rows = table.findAll('tr')

csv_path = '/Users/okuyamatakashi/workspace/python-scraping/hohukel/editors.csv'
with open(csv_path, 'w') as wf:
    writer = csv.writer(wf)
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td','th']):
            csvRow.append(cell.get_text())
        print(csvRow)
        writer.writerow(csvRow)
"""
6.3 MySQL
databaseはscraping、tableはpagesを使っていく
"""

"""
接続確認
"""
import pymysql
# コネクションオブジェクト
conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd=None, db='mysql')
# カーソルオブジェクト
cur = conn.cursor()
cur.execute('USE scraping')
cur.execute('SELECT * FROM pages WHERE id=1')
print(cur.fetchone())

cur.close()
conn.close()

"""実際にスクレイピングしてみる"""
import datetime
import random
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql
random.seed(datetime.datetime.now())

def store(title, content):
    content = content.replace('"',r'\"')
    sql = 'INSERT INTO pages (title, content) VALUES("%s", "%s");'%(title, content)
    try:
        cur.execute(sql)
        cur.connection.commit()
    except:
        print("ERROR SQL: ", sql)

def getLinks(articleUrl):
    url = 'http://en.wikipedia.org' + articleUrl
    html = urlopen(url)
    bs = BeautifulSoup(html, 'html.parser')
    title = bs.find('h1').get_text()
    content = bs.find('div', {'id':'mw-content-text'}).find('p').get_text() # 最初の1段落のみ
    store(title, content)
    return bs.find("div",{"id":"bodyContent"}).findAll("a",{"href":re.compile("^(/wiki/)((?!:).)*$")})

conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock',user='root', passwd=None, db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute('USE scraping;')

links = getLinks('/wiki/Kevin_Bacon')

record_num = 0
try:
    while len(links)>0:
        newArticle = links[random.randint(0, len(links)-1)].attrs['href']
        print (newArticle)
        links = getLinks(newArticle)
        record_num += 1
        if record_num >= 30:
            break

finally:
    cur.execute('select count(*) from pages;')
    record_num = cur.fetchone()[0]
    print('-'*50)
    print("pages table has {} records".format(record_num))
    cur.execute('select id, title from pages;')
    for i in range (record_num):
        print(cur.fetchone())
    cur.close()
    conn.close()

# check
conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock',
                       user='root', passwd='root', db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute('USE scraping;')
ur.close()
conn.close()

#-----------------------------------------------------------------
from urllib.request import urlopen
from bs4 import BeautifulSoup
url = 'https://en.wikipedia.org/wiki/'
html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')
#-----------------------------------------------------------------
url_right = "https://www.nytimes.com/2018/01/25/opinion/sunday/silicon-valley-immortality.html"
url_wrong =  "https://www.nytimes.com/2018/01/25/opinion/sunday/dummy.html"
requests.get(url_right)
requests.get(url_wrong)

websites[0].name
websites[0].url
websites[0].titleTag
websites[0].bodyTag

bs = BeautifulSoup(requests.get('http://shop.oreilly.com/product/0636920028154.do').text, 'html.parser')
selectedElems1 = bs.select('h1')
selectedElems2 = bs.select('section#product-description')

[elem for elem in selectedElems1]
[elem for elem in selectedElems2]
[elem.get_text() for elem in selectedElems1]
[elem.get_text() for elem in selectedElems2]

bs.findAll('h1') == bs.select('h1') # True
bs.findAll('h1')[0].text == bs.select('h1')[0].text # True
bs.find('h1').text == bs.select('h1')[0].text # True
bs.find('h1').get_text() == bs.select('h1')[0].text # True


#-----------------4.3.1------------------------------------------------
requests.get(url_ny)
requests.get(url_bo)
requests.get(url_ny).text
bs_ny = BeautifulSoup(requests.get(url_ny).text, 'html.parser')
bs_bo = BeautifulSoup(requests.get(url_bo).text, 'html.parser')
bs_ny.find('h1').text
bs_bo.find('h1').text
lines_ny = bs_ny.select('div.StoryBodyCompanionColumn div p')
for line_ny in lines_ny:
    pass
line_ny.text

body_ny = '\n'.join(line.text for line in lines_ny)
body_bo = bs_bo.find('div', {'class', 'post-body'}).text
print(body_ny)
print(body_bo)

requests.get(url)
requests.get(url).text

#---------------4.3.2---------------------------------------------
print(reuters.name)
print(reuters.url)
print(reuters.taragetPattern)
print(reuters.absoluteUrl)
print(reuters.titleTag)
print(reuters.bodyTag)

url = reuters.url
bs = BeautifulSoup(requests.get(url).text, 'html.parser')
bs.findAll('a')
bs.findAll('a', href=re.compile('^(/article/)'))
bs.find('a', href=re.compile('^(/article/)'))
bs.find('a', href=re.compile('^(/article/)')).attrs['href']
link_url = url + bs.find('a', href=re.compile('^(/article/)')).attrs['href']
link_bs = BeautifulSoup(requests.get(link_url).text, 'html.parser')

link_bs.select('h1')
'\n'.join([elem.get_text() for elem in link_bs.select('h1')])
link_bs.select('h1')[0].get_text()

link_bs.select('div.StandardArticleBody_body')
'\n'.join([elem.get_text() for elem in link_bs.select('div.StandardArticleBody_body')])
link_bs.select('div.StandardArticleBody_body')[0].get_text()

len([elem.get_text() for elem in link_bs.select('div.StandardArticleBody_body')]) # 1
#---------------4.3.3---------------------------------------------
#---------------5.2---------------------------------------------
urls = ["http://en.wikipedia.org/wiki/Python_%28programming_language%29",
        "https://en.wikipedia.org/wikiFunctional_programming",
        "https://en.wikipedia.org/wikiFunctional_programming",
        ]
urls[-1]

# -*- coding: utf-8 -*-

from scrapy.selector import Selector
from scrapy import Spider
import scrapy
Selector.hoge
#---------------5.3---------------------------------------------
"This page was last edited on 14 September 2019, at 01:50 (UTC).".replace("This page was last edited on ",'')

#---------------5.6---------------------------------------------
from datetime import datetime
from string import whitespace
url = 'https://en.wikipedia.org/wiki/Benevolent_dictator_for_life'
bs = BeautifulSoup(requests.get(url).text, 'html.parser')

lastUpdated = bs.select('li#footer-info-lastmod')[0].text # BeautifulSoupの書き方
# lastUpdated = response.css('li#footer-info-lastmod::text').extract_first()# scrapyの書き方

lastUpdated
lastUpdated = lastUpdated.replace("This page was last edited on ",'')
lastUpdated = lastUpdated.replace(u"\xa0(UTC)",'').strip('.').strip()

lastUpdated
print(lastUpdated)
lastUpdated = datetime.strptime(lastUpdated, '%d %B %Y, at %H:%M')
lastUpdated

datetime.strftime(lastUpdated, 'on %Y-%m(%B)-%d at %H:%M')
#-----------6.1------------------------------------------------------
img_url = 'http://www.pythonscraping.com/sites/default/files/lrg_0.jpg'
img_url.startswith('http://www')
img_url[11:]
'http://{}'.format(img_url[11:])

path = download_dir + img_url.replace('www.', '').replace(base_url,'')
dir = os.path.dirname(path)
dir
if not os.path.exists(dir):
    os.makedirs(dir)
os.path.exists(dir)

download_dir + file_url.replace('www.', '').replace(base_url,'')

#-----------6.2------------------------------------------------------
rows[0].findAll(['tr','th'])
rows[0].findAll(['tr','th'])[0].get_text()
rows[0].findAll(['tr','th'])[1].get_text()
rows[0].findAll(['tr','th'])[2].get_text()
rows[0].findAll(['tr','th'])[3].get_text()
cell = rows[0].findAll(['tr','th'])[3]
len(rows[0].findAll(['tr','th']))
cell
cell.get_text()

csvRow

2 ** 10
10 * (2**11)
5 * (2**5)
3 * (2**3)

#-----------6.3------------------------------------------------------
title = "title from pymysql "
content = "text from pymysql "

sql = 'INSERT INTO pages (title, content) VALUES("%s", "%s");'%(title, content)
print (sql)
cur.execute(sql)
cur.execute('SELECT * FROM pages;')
print(cur.fetchone())
cur.connection.commit()
links[0:2]
len(links)
links[random.randint(0, len(links)-1)].attrs['href']

content = 'been called "words". They'
content.replace('"',r'\"')

"""
6.3.3
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

URL = "https://en.wikipedia.org/wiki/Kevin_Bacon"
html = urlopen(URL)
bs = BeautifulSoup(html, 'html.parser')

# title(textそのもの取得)
title = bs.find('h1')
print(title)
print(title['id'])
print(title.get_text())

# link(tag)取得
regex = '^/wiki/((?!:).)*$'
links = bs.findAll('a',href=re.compile(regex))
print(links)
print(links[0])
print(links[0]['href'])
print(links[0]['title'])
links = [link.attrs['href'] for link in links]
print(links)

import pymysql
conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock',user='root', passwd=None, db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute('USE wikipedia;')

cur.execute('select * from links')
print(cur.rowcount)
print(cur.lastrowid)
for i in range(10):
    print(cur.fetchone())

cur.close()
conn.close()

"""
6.4 メール
行う前に送信に利用するGmailアカウントで「安全性の低いアプリのアクセス」を許可
Googleアカウント「セキュリティ」の下部にて設定する。
- https://myaccount.google.com/security
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time

import smtplib
from email.mime.text import MIMEText

FROM_ADDRESS = 'okuyama1625gcp@gmail.com'
MY_ACCOUNT = 'okuyama1625gcp'
MY_PASSWORD = 'pXx@gCuELuQh'
TO_ADDRESS = 'okuyama1625@gmail.com'
BCC = ''
SUBJECT = 'An email test'
BODY = 'The body of the test email is here'

# msg作成
msg = MIMEText(BODY)
msg['Subject'] = SUBJECT
msg['From'] = FROM_ADDRESS
msg['To'] = TO_ADDRESS

# サーバ接続
server = smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=10)
server.login(MY_ACCOUNT, MY_PASSWORD)
server.send_message(msg)
server.quit()


def sendMail(subject, body):
    msg = MIMEText(body)
    msg['subject'] = subject
    msg['From'] = 'christmas_alerts@pythonscraping.com'
    msg['To'] = 'okuyama1625@gmail.com'
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=10)
        server.login(MY_ACCOUNT, MY_PASSWORD)
        server.send_message(msg)
    finally:
        server.quit()

# ケビンベーコン
URL = "https://en.wikipedia.org/wiki/Kevin_Bacon"
html = urlopen(URL)
bs = BeautifulSoup(html, 'html.parser')

title = bs.find('h1').get_text()
print(title)

regex = '^/wiki/((?!:).)*$'
links = bs.findAll('a',href=re.compile(regex))
links = [link.attrs['href'] for link in links]
print(links)
body = '\n'.join(links)

sendMail(title, body)


# クリスマス
URL = 'https://isitchristmas.com/'
bs = BeautifulSoup(urlopen(URL), 'html.parser')
print(bs.find('a'))
print(bs.find('a', {'id':'answer'}).find('noscript'))
print(bs.find('a', {'id':'answer'}).find('noscript').text)


i = 0
while(bs.find('a', {'id':'answer'}).find('noscript').text in ('NO', u"いいえ")):
    print('It is not Christmas yet')
    time.sleep(5)
    bs = BeautifulSoup(urlopen(URL), 'html.parser')
    i += 1
    if i > 3:
        break

sendMail('It is Christmas!!',
        'According to https://isitchristmas.com, it is Christmas!')
"""
7章 文章を読む
"""

"""
7.2 テキスト
"""
from urllib.request import urlopen
url = 'http://www.pythonscraping.com/'\
      'pages/warandpeace/chapter1.txt'
url
textPage = urlopen(url)
# textページなのでBeautifulSoupでHTMLパースする必要なし
print(textPage.read())
