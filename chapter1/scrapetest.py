# coding: utf-8
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

URL = "http://www.pythonscraping.com/pages/page1.html"
URL = "http://www.pythonscraping.com/dummy/okuyama_page1.html"
URL = "http://www.okuyama.com/pages/page1.html"

def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    except URLError as e:
        print("The server could not be found")
        print(e)
        return None
    else:
        print ("It Worked!!")
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
        #title = bsObj.dummy.dummy
    except AttributeError as e:
        return None
    return title

title = get_title(URL)
if title == None:
    print("Title could not be found")
else:
    print(title)
