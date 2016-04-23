#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: Nsirone
#contact: nsirone@outlook.com
#software: PyCharm Community Edition
#file: dierge.py
#time: 16/4/24 上午12:38
# 这个有时间再看一下
import os,urlparse
url = 'http://www.baidu.com'
scheme, netloc, path, query, fragment = urlparse.urlsplit(url)
print scheme
print netloc
print path
print query
print fragment
filename = os.path.basename(path)
if not filename:
    filename = 'download.file'