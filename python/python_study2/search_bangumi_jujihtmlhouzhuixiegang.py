#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @version: 1.0
# @author: Nsirone
# @license: Apache Licence 
# @contact: nsirone@outlook.com
# @site: http://www.google.com
# @software: PyCharm Community Edition
# @file: search_bangumi_jujihtmlhouzhuixiegang.py
# @time: 2016/5/5 17:12

import urllib2, urllib
import linecache
import random
from bs4 import BeautifulSoup
import gevent
import gevent.monkey
gevent.monkey.patch_all()
import sys

def Test():
    test_query_file = 'search_wordslib.txt'
    count = len(open(test_query_file,'rU').readlines())
    hellonum=random.randrange(1, count, 1)
    word = linecache.getline(test_query_file,hellonum)
    keyword = word.strip('\n')

    data = {
        'keyword':keyword
    }
    data = urllib.urlencode(data)

    url = 'http://search.bilibili.com/bangumi?' + data
    print url
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html, 'lxml')
    # print soup

    if soup.select('.title') and soup.select('.list'):
        for header in soup.select('.list'):
            if header['href'].find('http://www.bilibili.com/video/') != -1:
                fd = open('a.txt', 'a')
                fd.write(header['href'] + '====================' + keyword + '\n')
                fd.close()
                print header['href']

    else:
        fd = open('a.txt', 'a')
        fd.write('没有相关数据====================' + keyword + '\n')
        fd.close()

def MT_Thread():
    tasks = []
    for i in range(0,2):
        tasks.append(gevent.spawn(Test))
    gevent.joinall(tasks)

if __name__ == '__main__':
    for i in range(int(sys.argv[1])):
        MT_Thread()
