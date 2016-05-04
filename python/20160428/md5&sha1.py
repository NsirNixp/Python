#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: Nsirone
#contact: nsirone@outlook.com
#software: PyCharm Community Edition
#file: md5&sha1.py
#time: 4/28/16 10:14 AM

import hashlib

# md5加密的写法
def get_MD5(source):
	mymd5 = hashlib.md5()
	mymd5.update(source)
	sign = mymd5.hexdigest()
	return sign
# sha1加密的算法
def get_SHA1(source):
	mysha1 = hashlib.sha1()
	mysha1.update(source)
	sign = mysha1.hexdigest()
	return sign