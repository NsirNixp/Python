#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @version: 1.0
# @author: Nsirone
# @license: Apache Licence 
# @contact: nsirone@outlook.com
# @site: http://www.google.com
# @software: PyCharm Community Edition
# @file: disange.py
# @time: 2016/5/4 19:55


# 可以抛出调用的函数内部的异常

def myhandle():
    x = 1/0

try:
    myhandle()
except ZeroDivisionError as e:
    print 'Handling run-time error:', e
finally:
    print '完事儿了'

# raise 语句允许程序员强制抛出一个指定的异常
raise NameError('HiThere')

