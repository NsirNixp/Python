# -*- coding:utf-8 -*-
import urllib, urllib2
import sys, os
import requests
import json

# 用户信息的cookie
Cookie = 'DedeUserID=17668003;DedeUserID__ckMd5=8aa32229517ebaac;SESSDATA=574b1bcf%2C1461131799%2C1b41b0bb;_dfcaptcha=26b96f9e4fa9969fc15e7bd78ad210b9;sid=92xvtygd;'
# 获取播放历史信息
def get_history():
	# n = 0
	url = 'http://api.bilibili.com/x/v2/history'
	data = {
		'pn':1,
		'ps':10
	}
	data = urllib.urlencode(data)
	url2 = url + '?' + data
	opener = urllib2.build_opener()
	opener.addheaders.append(('Cookie',Cookie))
	f= opener.open(url2)
	html = f.read()
	response = json.loads(html)
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
	
	# for i in range(50):
		# add_history(i+101)
	# clear_history()

	# 增加播放历史 每次增加200个，循环增加200次

	# for i in range(100):
	# 	zonghe_jilv(200)
	# if os.path.isfile('a.txt'):
	# 	f = open('a.txt', 'r')
	# 	readlines = f.readlines()
	# 	sum = 0
	# 分析log中每次计算的降级几率，计算平均降级几率
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
	for i in range(100):
		zonghe_jilv(200)
	if os.path.isfile('a.txt'):
		f = open('a.txt', 'r')
		readlines = f.readlines()
		sum1 = 0
		sum2 = 0
		for i in readlines:
			num1 = float(i.strip('\n').split(':')[1].strip('%'))
			num2 = float(i.strip('\n').split(':')[2].strip('%'))
			sum1 = sum1 + num1
			sum2 = sum2 + num2
		f.close()
		pro1 = float(sum1)/float(100)
		pro2 = float(sum2)/float(100)
		f = open('a.txt', 'a')
		f.write('空平均概率是: %.2f%%, 404平均概率是:%.2f%%'%(pro1,pro2))
		f.close()
	print '完事'