#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: Nsirone
#contact: nsirone@outlook.com
#software: PyCharm Community Edition
#file: three.py
#time: 4/28/16 1:07 PM
import urllib

data = {
	'one':1,
	'two':2,
	'three':3,
	'four':4,
	'five':5,
	'six':6,
	'seven':7,
	'eight':8,
	'nine':9,
	'ten':10
}
list1 = [1,3,4,5]
print type(list1)
print type(data)
print data
sorted(data)
print urllib.urlencode(data)
data_sort = urllib.urlencode(sorted(data.iteritems(), key=lambda d: d[0]))
print data_sort
# keys = sorted(data.keys())
# for kw in keys:
# 	print kw, data[kw]


# data = {
# 	'appkey': appkey,
# 	'ts': int(time.time()),
# 	'aid': aid,
# 	'appsecret': appsecret
# }
# # 排序
# data_sort = urllib.urlencode(sorted(data.iteritems(), key=lambda d: d[0]))