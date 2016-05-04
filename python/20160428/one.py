#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: Nsirone
#contact: nsirone@outlook.com
#software: PyCharm Community Edition
#file: one.py
#time: 4/28/16 9:00 AM

import hashlib
import urllib2, urllib
import time
import os, sys
Cookie = 'a=a;b=b;c=c;'
appkey = 'test'
appkey_secret = 'test_secret'

lines = None
if os.path.isfile('aid.txt') and os.path.isfile('mid.txt'):
	fd_aid = open('aid.txt', 'r')
	fd_mid = open('mid.txt', 'r')
	lines_aid = fd_aid.readlines()
	lines_mid = fd_mid.readlines()


def Sign_params():

	data = {
		'appkey': appkey,
		'appkey_secret': appkey_secret,
		'ts': int(time.time()),
		'name': 'nsirone',
		'pwd': '123456',
		'aid': lines_aid[1].strip('\n'),
		'mid': lines_mid[1].strip('\n')
	}
	data_1 = urllib.urlencode(data)
# 算签名
	m2 = hashlib.md5()
	m2.update(data_1)
	sign = m2.hexdigest()

	data['sign'] = sign
	data_2 = urllib.urlencode(data)
	print data
	url = 'http://domain/x/history'
	url_source = url + '?' + data_2
	print url_source

	opener = urllib2.build_opener()
	opener.addheaders.append(('Cookie', Cookie))
	response = opener.open(url, data)
	html = response.read()
	
if __name__ == '__main__':
	Sign_params()






