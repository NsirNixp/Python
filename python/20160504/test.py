#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @version: 1.0
# @author: Nsirone
# @license: Apache Licence 
# @contact: nsirone@outlook.com
# @site: http://www.google.com
# @software: PyCharm Community Edition
# @file: test.py
# @time: 2016/5/4 18:47

while True:
    try:
        x = int(raw_input('Please enter a number: '))
        break
    except ValueError:
        print 'Oops! That was no valid number. Try again....'