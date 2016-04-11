#-*- coding:utf-8 -*-
import urllib, urllib2
import sys
import requests
import cookielib

cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open('http://search.bilibili.com/all?keyword=fate')
for item in cookie:
    if item.name == 'abtest_search':
        print item.value
