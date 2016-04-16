#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: Nsirone
#contact: nsirone@outlook.com
#software: PyCharm Community Edition
#file: diyige.py
#time: 16/4/16 下午4:25

import os
import urllib, urllib2

data = {
    'name':'nixuepeng',
    'pwd':'nixuepeng',
    'url':'http://www.baidu.com'
}

data = urllib.urlencode(data)
url = 'http://www.baidu.com'
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
html = response.read()
print html
