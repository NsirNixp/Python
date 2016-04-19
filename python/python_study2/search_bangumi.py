#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/4/19 18:03
# @Author  : Nsirone
# @Site    : 
# @File    : search_bangumi.py
# @Software: PyCharm
from lxml import etree
import urllib2, urllib
from bs4 import BeautifulSoup
import os

keyword = '寒蝉鸣泣之时'
data = {
    'keyword':keyword
}
data = urllib.urlencode(data)
url = 'http://172.16.4.217/bangumi?'+ data

req = urllib2.Request(url)
response = urllib2.urlopen(req)
html = response.read()
soup = BeautifulSoup(html)
print soup.head
print '==============================================================='
print soup.title
print '==============================================================='
print soup.p
print soup.p.attrs
print soup.p['class']
print soup.p.get('class')
print soup.p.string
print '==============================================================='
print soup.a
print '==============================================================='
print soup.name
print '==============================================================='
print soup.head.name
# if html:
#     selector = etree.HTML(html)
#     links = selector.xpath('//li/a[@target="_blank"]/@se-linkid')
#     print links
# print html
