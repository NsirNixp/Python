# -*- coding:utf-8 -*-
import urllib2
from lxml import etree
import json

# 搜索修改了埋点计算方式，前端页面se-linkid属性改为累加模式
# 搜素页面url
# url = 'http://172.16.4.217/all?keyword=%E5%90%83%E8%B4%A7%E6%9C%A8%E4%B8%8B'
# 默认取前100页
# 测试环境
# links = ''
# for i in range(100):
# 	# 搜索接口url
# 	try:
# 		url = 'http://172.16.4.217/ajax_api/video?keyword=%E5%90%83%E8%B4%A7%E6%9C%A8%E4%B8%8B&order=totalrank&page=' + str(i+1)
# 		f = urllib2.urlopen(url).read()
# 		print f
# 		f = json.loads(f)
# 		if f['html']:
# 			selector = etree.HTML(f['html'])
# 			links = selector.xpath('//li/a[@target="_blank"]/@se-linkid')
# 			print i+1
# 		else:
# 			print 'No Data'
# 			print i
# 	except Exception, e:
# 		print e
# 	finally:
# 		for j in links:
# 			print j
# print 'Finish'

# 线上回归
links = ''
for i in range(100):
	# 搜索接口url
	try:
		url = 'http://search.bilibili.com/all?keyword=%E5%90%83%E8%B4%A7%E6%9C%A8%E4%B8%8B&order=totalrank&page=' + str(i+1)
		f = urllib2.urlopen(url).read()
		if f:
			selector = etree.HTML(f)
			links = selector.xpath('//li/a[@target="_blank"]/@se-linkid')
			print i+1
		else:
			print 'No Data'
			print i
	except Exception, e:
		print e
	finally:
		for j in links:
			print j
print 'Finish'