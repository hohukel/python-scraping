# coding: utf-8
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import re


pages = set()
def get_links(page_url):
    global pages
    URL = "https://en.wikipedia.org" + page_url
    html = urlopen(URL)
    bs_obj = BeautifulSoup(html)
    try:
        print(bs_obj.h1.get_text())
        print(bs_obj.find(id="mw-content-text").findAll("p")[0])
        print(bs_obj.find(id="ca-edit").find("span").find("a").attrs["href"])
    except AttributeError:
        print("This page is missing something! No worries though!")

    for link in bs_obj.findAll("a",{"href":re.compile("^(/wiki/)")}):
        if link.attrs["href"] not in pages:
            # 新しいリンクに出会った
            new_page = link.attrs["href"]
            print('='*50 + '\n' + new_page)
            pages.add(new_page)
            get_links(new_page)

get_links("")
