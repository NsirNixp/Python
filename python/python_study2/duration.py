#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @version: 1.0
# @author: Nsirone
# @license: Apache Licence 
# @contact: nsirone@outlook.com
# @site: http://www.google.com
# @software: PyCharm Community Edition
# @file: duration.py
# @time: 2016/4/27 19:17
import urllib,urllib2
import json
Cookie = 'DedeUserID=17668003;DedeUserID__ckMd5=8aa32229517ebaac;SESSDATA=7bf20cf0%2C1464264469%2C9c4bba7a;_dfcaptcha=528f3ca0aea9b76739ab3d2d8d040869;sid=65x6gqm9;'
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
	response = f.read()
	return response
if __name__ == '__main__':
    for i in range(200):
        add_history(i + 100)

    # print get_history()
    response = json.loads(get_history())
    for i in response['data']:
        print i
        for j in i:
            if j == 'duration':
                print '这个是' + '  ' + j
                print i[j]
            else:
                print '这个不是' + '  ' + j