#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @version: 1.0
# @author: Nsirone
# @license: Apache Licence 
# @contact: nsirone@outlook.com
# @site: http://www.google.com
# @software: PyCharm Community Edition
# @file: disige.py
# @time: 2016/5/4 20:01

# 用户自定义异常

class Myerror(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
    error1 = Myerror
    raise error1(2*2)
except Myerror as e:
    print 'My exception occurred, value: ', e.value


raise Myerror('Oops!')