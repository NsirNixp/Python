#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @version: 1.0
# @author: Nsirone
# @license: Apache Licence 
# @contact: nsirone@outlook.com
# @site: http://www.google.com
# @software: PyCharm Community Edition
# @file: diwuge.py
# @time: 2016/5/4 20:11

# 定义清理行为
# try语句和except语句和finally 还有一些常用的error的类型名称，与标准异常相似，大多数异常的命名都是以'Error'结尾

def divide(x, y):
    try:
        result = x/y
    except ZeroDivisionError as e:
        print e
    except TypeError as e:
        print e
    else:
        print 'result is {}'.format(result)
    # finally中的语句肯定会被执行，不管之前有没有捕获异常
    finally:
        print 'executing finally clause~~~'

divide(1,1)
divide(1,0)
divide('1','1')