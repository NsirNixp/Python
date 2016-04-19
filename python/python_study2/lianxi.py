#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: Nsirone
#contact: nsirone@outlook.com
#software: PyCharm Community Edition
#file: lianxi.py
#time: 16/4/19 下午9:171
from bs4 import BeautifulSoup
import urllib, urllib2
html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''

soup = BeautifulSoup(html, 'lxml')
# soup = BeautifulSoup(open('index.html'))
print soup.title
print soup.name
print soup.head.name
print soup.head
print soup.a
print soup.p
print soup.p.attrs
print soup.p['class']
print soup.p['name']
print soup.b.string
print soup.b.attrs
print soup.p.string
print type(soup.p.string)
print soup.attrs
print soup.head.contents
print soup.head.contents[0]
print soup.head.children
print '==========================================='
print soup.head.string
print soup.title.string	








