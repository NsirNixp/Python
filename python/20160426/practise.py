#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: Nsirone
#contact: nsirone@outlook.com
#software: PyCharm Community Edition
#file: practise.py
#time: 4/28/16 1:31 AM

import urllib, urllib2

url = 'http://www.bilibili.com'
request = urllib2.Request(url)
response = urllib2.urlopen(request)
html = response.read()
print html