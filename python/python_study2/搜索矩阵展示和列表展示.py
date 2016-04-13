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
import requests
url = 'http://search.bilibili.com/all?keyword=fate'
url1 = 'http://172.16.4.217/all?keyword=fate'
url2 = 'http://www.bilibili.com'
# url3 = 'http://www.baidu.com'

cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(url1)
for item in cookie:
    print 'Name = '+ item.name
    print 'Value = '+ item.value

# import cookielib, urllib2
# filename = 'cookie.txt'
# cookie = cookielib.MozillaCookieJar(filename)
# handler = urllib2.HTTPCookieProcessor(cookie)
# opener = urllib2.build_opener(handler)
# response = opener.open(url3)
# cookie.save(ignore_discard=True, ignore_expires=True)
# try:
#     response = requests.get(url3)
#     cookiea = response.cookies()
#     print type(cookiea)
#     print cookiea
#     cookiea = response.cookies['is_videos_imgleft']
#     if cookiea == '1':
#         print 'youzhegedongxi'
#     else:
#         print 'meiyouzhegedongxi'
# except Exception, e:
#     print e
# finally:
#     print 'ceshiwanbi'