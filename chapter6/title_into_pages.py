# coding: utf-8

"""
6.3.3 Pythonと統合する
wikipediaから30人の情報を引っ張ってきて、scraping.pages(カラム: id, title, content)に格納
"""

import datetime
import random
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql

random.seed(datetime.datetime.now())
conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock',user='root', passwd=None, db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute('USE scraping;')

def store(title, content):
    content = content.replace('"',r'\"') # 奥山が追加した処理
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
    print('insert information of {}'.format(title))
    print (newArticle)
    store(title, content)
    return bs.find("div",{"id":"bodyContent"}).findAll("a",{"href":re.compile("^(/wiki/)((?!:).)*$")})


if __name__ == '__main__':
    links = getLinks('/wiki/Kevin_Bacon')

    record_num = 1
    try:
        while len(links)>0:
            newArticle = links[random.randint(0, len(links)-1)].attrs['href']
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
