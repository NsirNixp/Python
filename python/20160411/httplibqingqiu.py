# -*- coding:utf-8 -*-
import httplib


httpClient = None
httpClient = httplib.HTTPConnection('http://www.bilibili.com', 80 , timeout=30)
httpClient.request('GET', '/login')
response = httpClient.getresponse()
print response.read()