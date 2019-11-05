# coding: utf-8

"""
6.3.5 MySQLの6次
"""

import re
from urllib.request import urlopen

import pymysql
from bs4 import BeautifulSoup

conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock',user='root', passwd=None, db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute('USE wikipedia;')

# ないURLのinsert & page idの検索
def insertPageIfNotExists(url):
    cur.execute('select * from pages where url = %s', (url))
    if cur.rowcount == 0:
        cur.execute('insert into pages (url) values (%s)',(url))
        conn.commit()
        return cur.lastrowid
    else:
        return cur.fetchone()[0]

def loadPages():
    cur.execute('select * from pages')
    pages = [row[1] for row in cur.fetchall()] # url
    return pages

def insertLink(fromPageId, toPageId):
    cur.execute('select * from links where fromPageId = %s '
                'AND toPageId = %s', (int(fromPageId), int(toPageId)))
    if cur.rowcount == 0:
        cur.execute('insert into links (fromPageId, toPageId) values (%s,%s)',(int(fromPageId), int(toPageId)))
        conn.commit()

# recursion: 再帰
def getLinks(pageUrl, recursionLevel, pages):
    if recursionLevel > 3:
        return
    pageId = insertPageIfNotExists(pageUrl)

    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    regex = '^/wiki/((?!:).)*$'
    links = bs.findAll('a',href=re.compile(regex))
    links = [link.attrs['href'] for link in links]
    for link in links:
        insertLink(pageId, insertPageIfNotExists(link))
        if link not in pages:
            pages.append(link)
            getLinks(link, recursionLevel+1, pages)


if __name__ == '__main__':
    links = getLinks('/wiki/Kevin_Bacon', 0 ,loadPages())
    cur.close()
    conn.close()
