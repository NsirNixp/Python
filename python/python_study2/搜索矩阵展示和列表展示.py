#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/4/13 17:39
# @Author  : Nsirone
# @Site    : 
# @File    : 搜索矩阵展示和列表展示.py
# @Software: PyCharm

# 之前的搜索cookie中加入了一个is_videos_imgleft的字段，但是却加入到了.bilibili.com的域名下，现在要切换到search.bilibili.com的域名下可以防止显示的问题
import urllib2
import cookielib
# url = 'http://search.bilibili.com/all?keyword=fate'
# request = urllib2.Request(url)
# response = urllib2.urlopen(request)
# html = response.read()
# print html

cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open('http://search.bilibili.com/all?keyword=fate')
for item in cookie:
  if item.name == 'abtest_search':
       print item.value