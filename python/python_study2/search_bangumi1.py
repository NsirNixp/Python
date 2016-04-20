#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/4/20 17:28
# @Author  : Nsirone
# @Site    : 
# @File    : search_bangumi1.py
# @Software: PyCharm
import urllib2, urllib
from bs4 import BeautifulSoup
import os

keyword = '23543452352354'
data = {
    'keyword':keyword
}
data = urllib.urlencode(data)
# 综合
# url = 'http://172.16.4.217/all?'+ data
# 番剧
url = 'http://172.16.217/bangumi?' + data
req = urllib2.Request(url)
response = urllib2.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, 'lxml')
if soup.select('.title'):
    for header in soup.select('.title'):
        # 判断是否是番剧，find()返回-1 表示没有找到，返回其他数字表示找的字符串在母字符串中的位置
        if header['se-linkid'].find('bangumi_title') != -1:
            # print header.attrs
            # print type(header) # <class 'bs4.element.Tag'>如果是Tag类型的对象，就有两个属性可以使用，name和attrs, attrs输出的是一个字典dict
            fd = open('a.txt', 'a')
            fd.write(header['title']+'=========================='+keyword+'\n')
            fd.close()
            print header['title']
            # print header['se-linkid']
else:
    fd = open('a.txt', 'a')
    fd.write('没有相关数据====='+keyword+'\n')
    fd.close()
    print '没有相关数据====='+keyword