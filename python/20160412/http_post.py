#!/usr/bin/env python
#coding=utf8

import httplib
import urllib
import socket
from urllib2 import HTTPError, URLError
from httplib import HTTPException
import json
httpClient = None

headers = {
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Language':'zh-CN,zh;q=0.8',
	'Connection':'keep-alive',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'
}
data = {
	'tag_id':108,
	'page':1,
	'pagesize':20,
	'indexType':0
}
data = urllib.urlencode(data)
print data
url = 'http://bangumi.bilibili.com/api/get_season_by_tag_v2?'+data
print url
try:
    httpClient = httplib.HTTPConnection('bangumi.bilibili.com', 80, timeout=30)
    httpClient.request('GET', url, '', headers)
 
    #response是HTTPResponse对象
    response = httpClient.getresponse()
    print response.status
    print response.reason
    print response.read()
except HTTPError, e:
	print e
except URLError, e:
	print e
except HTTPException, e:
	print e
finally:
    if httpClient:
        httpClient.close()