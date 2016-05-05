#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @version: 1.0
# @author: Nsirone
# @license: Apache Licence 
# @contact: nsirone@outlook.com
# @site: http://www.google.com
# @software: PyCharm Community Edition
# @file: dierge.py
# @time: 2016/5/5 19:06

import random
print random.choice(['1','2','3'])

print random.sample(xrange(100), 10)    #sampling without replacement 不重复抽样
print random.random()   #random float
print random.randrange(6)   #random integer chosen from range(6)

