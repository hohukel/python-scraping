# coding: utf-8
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())

def get_links(article_url):
    URL = "https://en.wikipedia.org" + article_url
    try:
        html = urlopen(URL)
    except HTTPError as e:
        print(e)
        return None
    except URLError as e:
        print("The server could not be found")
        print(e)
        return None
    bs_obj = BeautifulSoup(html)
    # divの中でidがbodyContentに設定されている、URLにコロンがない、/wiki/で始まる→人名へのリンク
    return bs_obj.find("div",{"id":"bodyContent"}).findAll("a",{"href":re.compile("^(/wiki/)((?!:).)*$")})

links = get_links("/wiki/Kevin_Bacon")

#while len(links) > 0:
for i in range(10):
    new_article = links[random.randint(0,len(links)-1)].attrs["href"]
    print(new_article)
    links = get_links(new_article)
