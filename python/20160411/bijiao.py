# -*- coding:utf-8 -*-

import urllib, urllib2
from urllib2 import HTTPError, URLError
url = 'http://news.163.com/13/0228/19/8OQUTIRP0001124J.html'
wp = urllib.urlopen(url)
content = wp.read()
print '字符串长度: ', len(content)
try:
	data = ''
	qqurl = 'http://news.qq.com/a/20130228/0014data28.htm'
	fqq = urllib2.urlopen(url, data, timeout=30)
	urllib2.urlopen(qqurl, data)
	req = urllib2.Request(qqurl)
	fqq = urllib2.urlopen(req)
	the_page = fqq.read()
	print '网页的字符串长度为: ', len(the_page)
except HTTPError, e:
	print e
except URLError, e:
	print e