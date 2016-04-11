#!/usr/bin/env python
#coding=utf8

import httplib
 
httpClient = None
 
try:
    httpClient = httplib.HTTPConnection('http://bangumi.bilibili.com', 80, timeout=30)
    httpClient.request('POST', '/api/get_season_by_tag_v2?tag_id=108&page=1&pagesize=20&indexType=0')
 
    #response是HTTPResponse对象
    response = httpClient.getresponse()
    print response.status
    print response.reason
    print response.read()
except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()