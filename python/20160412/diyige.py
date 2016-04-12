# -*- coding:utf-8 -*-
import urllib, urllib2
import httplib

# # 使用urllib2, urllib发送GET请求
# # GET请求
params = {
	'pagesize':20,
	'page':1,
	'tag_id':108,
	'indexType':0
}
params = urllib.urlencode(params)

url = 'http://bangumi.bilibili.com/api/get_season_by_tag_v2?'+params
response = urllib2.Request(url)
req = urllib2.urlopen(response)
html = req.read()
print req.info()
print req.getcode()
print html

# # POST请求
appkey = 'b0ef1dd3f998e7b971cd7adb7ffb6d7c'
params = {
	'phoneno':'18516254259',
	'cardnum':10,
	'key':appkey
}
params = urllib.urlencode(params)
url = 'http://op.juhe.cn/ofpay/mobile/telcheck'
response = urllib2.Request(url, params)
req = urllib2.urlopen(response, params, timeout=40)
html = req.read()
print html

# 使用httplib发送get请求

IP = 'http://op.juhe.cn/ofpay/mobile/telcheck?'
PORT = 80
appkey = 'b0ef1dd3f998e7b971cd7adb7ffb6d7c'
params = {
	'phoneno':'18516254259',
	'cardnum':10,
	'key':appkey
}
params = urllib.urlencode(params)
url = IP + params
print url
httpClient = httplib.HTTPConnection('op.juhe.cn', PORT, timeout=30)
httpClient.request('GET', url)	
response = httpClient.getresponse()
print response.status
print response.reason
print response.read()

# 使用httplib发送post请求

IP = 'http://op.juhe.cn/ofpay/mobile/telcheck'
PORT = 80
appkey = 'b0ef1dd3f998e7b971cd7adb7ffb6d7c'
params = {
	'phoneno':'18516254259',
	'cardnum':10,
	'key':appkey
}
params = urllib.urlencode(params)
httpClient = httplib.HTTPConnection('op.juhe.cn', PORT, timeout=30)
httpClient.request('POST', IP, params)	
response = httpClient.getresponse()
print response.status
print response.reason
print response.read()
