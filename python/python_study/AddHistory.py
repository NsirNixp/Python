# -*- coding:utf-8 -*-
import urllib, urllib2
import sys
import requests
import json
Cookie = 'DedeUserID=17668003;DedeUserID__ckMd5=8aa32229517ebaac;SESSDATA=574b1bcf%2C1460533466%2C1420f122;_dfcaptcha=83731bc77e0aa6b11c7a0ba4c0e61b5d;sid=lrdqw3on;'
def get_history(i):
	# n = 0
	url = 'http://api.bilibili.com/x/v2/history'
	data = {
		'pn':1,
		'ps':i
	}
	data = urllib.urlencode(data)
	url2 = url + '?' + data
	opener = urllib2.build_opener()
	opener.addheaders.append(('Cookie',Cookie))
	f= opener.open(url2)
	html = f.read()
	# html = json.loads(html)
	print html
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
	except urllib2.URLError as e:
		if hasattr(e, 'code'):
			print 'Error code: ', e.code
		elif hasattr(e, 'reason'):
			print 'Reason: ', e.reason
	finally:
		print response.read()
		if response:
			response.close()

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

if __name__ == '__main__':
	for i in range(5000):
		add_history(i)
