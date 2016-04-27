# -*- coding:utf-8 -*-
import urllib, urllib2
import sys, os
import requests
import json
import hashlib
import time
# 用户信息的cookie 线上
# Cookie = 'DedeUserID=17668003;DedeUserID__ckMd5=8aa32229517ebaac;SESSDATA=574b1bcf%2C1461131799%2C1b41b0bb;_dfcaptcha=26b96f9e4fa9969fc15e7bd78ad210b9;sid=92xvtygd;'
# 用户信息的cookie 测试环境的cookie
Cookie = 'DedeUserID=17668003;DedeUserID__ckMd5=8aa32229517ebaac;SESSDATA=7bf20cf0%2C1464264469%2C9c4bba7a;_dfcaptcha=528f3ca0aea9b76739ab3d2d8d040869;sid=65x6gqm9;'
appkey = '6a29f8ed87407c11'
appsecret = 'd3c5a85f5b895a03735b5d20a273bc57'
# 获取播放历史信息
def get_history():
	# n = 0
	url = 'http://api.bilibili.com/x/v2/history'
	data = {
		'pn':1,
		'ps':129
	}
	data = urllib.urlencode(data)
	url2 = url + '?' + data
	opener = urllib2.build_opener()
	opener.addheaders.append(('Cookie',Cookie))
	f= opener.open(url2)
	response = f.read()
	return response
# 增加播放历史信息
def add_history(i):
	url = 'http://api.bilibili.com/x/v2/history/add'
	data = {
		'aid':i
	}
	response = None

	try:
		data = urllib.urlencode(data)
		opener = urllib2.build_opener()
		opener.addheaders.append(('Cookie',Cookie))
		response = opener.open(url, data)
	except urllib2.URLError, e:
		if hasattr(e, 'code'):
			print 'Error code: ', e.code
		elif hasattr(e, 'reason'):
			print 'Reason: ', e.reason
	finally:
		print response.read()
		if response:
			response.close()
# 清除所有播放历史
def clear_history():
	url = 'http://api.bilibili.com/x/v2/history/clear'
	data = {}
	data = urllib.urlencode(data)
	response = None
	try:
		opener = urllib2.build_opener()
		opener.addheaders.append(('Cookie',Cookie))
		response = opener.open(url, data)
	except urllib2.URLError as e:
		if hasattr(e, 'code'):
			print 'Error code: ', e.code
		elif hasattr(e, 'reason'):
			print 'Reason: ', e.code
	finally:
		print response.read()
		if response:
			response.close()

# 删除单个历史记录
def del_history(aid):
	url = 'http://api.bilibili.com/x/v2/history/del'
	data = {
		'aid':aid
	}
	data = urllib.urlencode(data)
	response = None
	try:
		opener = urllib2.build_opener()
		opener.addheaders.append(('Cookie',Cookie))
		response = opener.open(url, data)
	except urllib2.URLError as e:
		if hasattr(e, 'code'):
			print 'Error code: ', e.code
		elif hasattr(e, 'reason'):
			print 'Reason: ', e.code
	finally:
		print response.read()
		if response:
			response.close()

# 获取单个的稿件信息
def get_archive(aid):
	url = 'http://172.16.0.26:6081/x/archive'
	data = {
		'appkey': appkey,
		'ts': int(time.time()),
		'aid': aid,
		'appsecret': appsecret
	}
	# 排序
	data_sort = urllib.urlencode(sorted(data.iteritems(), key=lambda d: d[0]))
	# MD5加密
	m2 = hashlib.md5()
	m2.update(data_sort + appsecret)
	sign = m2.hexdigest()
	# 完事
	data['sign'] = sign
	params = urllib.urlencode(data)
	url1 = url + '?' + params
	request = urllib2.Request(url1)
	return urllib2.urlopen(request).read()


# history依赖的account-service挂掉
def account_jilv(args):
	a = 0
	b = 0
	for i in range(0, args):
		response = get_history()
		if response['code'] == 0 and response['message'] == 'ok':
			if response['data']:
				a = a+1
		else:
			b = b+1

	f = open('a.txt', 'a')
	f.write('%d, %d ,访问无内容的几率是:%.2f%%\n' %(a, b, (float(b)/float(args))*100))
	f.close()
# history依赖的archive-service挂掉
def archive_jilv(args):
	a = 0
	b = 0
	for i in range(0, args):
		response = get_history()
		if response['code'] == 0 and response['message'] == 'ok':
			if response['data']:
				a = a+1
			else:
				b = b+1

	f = open('a.txt', 'a')
	f.write('%d, %d ,访问无内容的几率是:%.2f%%\n' %(a, b, (float(b)/float(args))*100))
	f.close()
# archive-servie&account-service同时挂掉
def zonghe_jilv(args):
	a = 0
	b = 0
	c = 0
	for i in range(0, args):
		response = get_history()
		if response['code'] == 0 and response['message'] == 'ok':
			if response['data']:
				a = a+1
			else:
				c = c+1
		else:
			b = b+1
	f = open('a.txt', 'a')
	f.write('%d, %d , %d, 访问无内容的几率是:%.2f%%:%.2f%%\n' %(a, b, c,(float(c)/float(args))*100,(float(b)/float(args))*100))
	f.close()

if __name__ == '__main__':
	print get_archive(102)
	print get_archive(104)

# 添加历史记录，然后获取历史记录总数，一一遍历历史记录然后通过单个删除接口删除，算是一个流程
# 	for i in range(50):
# 		add_history(i+101)
# 	html = json.loads(get_history())
# 	print html
# 	a = 0
# 	list = []
# 	for i in html['data']:
# 		print i['aid']
# 		a += 1
# 		list.append(i['aid'])
# 	print '历史总数是: %s'%(a)
# 	for i in list:
# 		del_history(i)

# 增加播放历史 每次增加200个，循环增加200次

	# for i in range(100):
	# 	zonghe_jilv(200)
	# if os.path.isfile('a.txt'):
	# 	f = open('a.txt', 'r')
	# 	readlines = f.readlines()
	# 	sum = 0
	# # 分析log中每次计算的降级几率，计算平均降级几率
	# 	for i in readlines:
	# 		num = float(i.strip('\n').split(':')[1].strip('%'))
	# 		sum = sum + num
	# 	f.close()
	# 	pro = float(sum)/float(100)
	# 	f = open('a.txt', 'a')
	# 	f.write('平均概率是: %.2f%%'%(pro))
	# 	f.close()
	# print '完事'
	
	# 两个服务同时挂掉，分析并计算几率
	# for i in range(100):
	# 	zonghe_jilv(200)
	# if os.path.isfile('a.txt'):
	# 	f = open('a.txt', 'r')
	# 	readlines = f.readlines()
	# 	sum1 = 0
	# 	sum2 = 0
	# 	for i in readlines:
	# 		num1 = float(i.strip('\n').split(':')[1].strip('%'))
	# 		num2 = float(i.strip('\n').split(':')[2].strip('%'))
	# 		sum1 = sum1 + num1
	# 		sum2 = sum2 + num2
	# 	f.close()
	# 	pro1 = float(sum1)/float(100)
	# 	pro2 = float(sum2)/float(100)
	# 	f = open('a.txt', 'a')
	# 	f.write('空平均概率是: %.2f%%, 404平均概率是:%.2f%%'%(pro1,pro2))
	# 	f.close()
	# print '完事'