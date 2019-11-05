# coding: utf-8
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())

# ページ内で見つかった全ての内部リンクのリストを取り出す
def _get_internal_links(bs_obj, include_url):
    include_url = urlparse(include_url).scheme + "://" + urlparse(include_url).netloc
    internal_links = []
    # "/"で始まる全てのリンクを見つける
    for link in bs_obj.findAll("a",href=re.compile("^(\/|.*"+include_url+")")):
        if link.attrs["href"] is not None:
            if link.attrs["href"] not in internal_links:
                if link.attrs["href"].startswith('/'):
                    internal_links.append(include_url + link.attrs["href"])
                else:
                    internal_links.append(links.attrs["href"])
    return internal_links

# ページ内で見つかった全ての外部リンクのリストを取り出す
def _get_external_links(bs_obj, exclude_url):
    external_links = []
    # 現在のURLを含まないhttpかwwwで始まる全てのリンクを見つける
    for link in bs_obj.findAll("a",href=re.compile("^(http|www)((?!"+exclude_url+").)*$")):
        if link.attrs["href"] is not None:
            if link.attrs["href"] not in external_links:
                external_links.append(link.attrs["href"])
    return external_links

def _get_random_external_link(starting_page):
    html = urlopen(starting_page)
    bs_obj = BeautifulSoup(html)
    external_links = _get_external_links(bs_obj, urlparse(starting_page).netloc)
    if len(external_links) == 0:
        # 外部リンクが見つかるまでWebサイト内をドリルダウン
        print("No external links, looking around the site for one")
        domain = (urlparse(starting_page).scheme+"://"+urlparse(starting_page).netloc)
        internal_links = _get_internal_links(bs_obj, starting_page)
        if len(internal_links) == 0:
            import sys
            print("Also no internal links")
            sys.exit()
        return _get_random_external_link(internal_links[random.randint(0, len(internal_links)-1)])
    else:
        return external_links[random.randint(0, len(external_links)-1)]

def follow_external_only(site):
    external_link = _get_random_external_link(site)
    print("Random external link is: "+external_link)
    follow_external_only(external_link)

# サイトで見つかった全ての外部URLのリストを集める
def get_all_external_link(site_url):
    html = urlopen(site_url)
    domain = (urlparse(site_url).scheme+"://"+urlparse(site_url).netloc)
    bs_obj = BeautifulSoup(html)
    internal_links = _get_internal_links(bs_obj, domain)
    external_links = _get_external_links(bs_obj, domain)

    for link in external_links:
        if link not in ALL_EXT_LINKS:
            ALL_EXT_LINKS.add(link)
            print(link)

    for link in internal_links:
        if link not in ALL_INT_LINKS:
            ALL_INT_LINKS.add(link)
            get_all_external_link(link)

URL = "http://oreilly.com"
#URL = "https://music.apple.com/subscribe?app=music&at=1001l4QJ&ct=314&itscg=10000&itsct=314"
#URL = "https://maps.google.com/maps?hl=en&tab=3l"


ALL_INT_LINKS = set({URL})
ALL_EXT_LINKS = set()

# どちらかの関数を選択
# follow_external_only(URL)
get_all_external_link(URL)

"""
memo
site = URL
starting_page = URL
exclude_url = urlparse(starting_page).netloc

external_links
random.randint(0,1)
external_links[random.randint(0,len(external_links)-1)]
"""
