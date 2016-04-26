#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: Nsirone
#contact: nsirone@outlook.com
#software: PyCharm Community Edition
#file: disange.py
#time: 16/4/24 上午12:53

# 断点续传下载
# 在使用http协议进行下载只需要在头上设置一下Range的范围就可以进行断点
# 续传下载,当然,首先服务器需要支持断点续传

# 利用python的urllib2模块完成断点续传下载的例子
import urllib2

#req = urllib2.Request('http://www.bilibili.com')
req = urllib2.Request('http://www.python.org/')
req.add_header('Range', 'bytes=0-14')
res = urllib2.urlopen(req)

data = res.read()
print data
print '------'
print 'len:%d'%len(data)
