#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @version: 1.0
# @author: Nsirone
# @license: Apache Licence 
# @contact: nsirone@outlook.com
# @site: http://www.google.com
# @software: PyCharm Community Edition
# @file: diyige.py
# @time: 2016/5/4 10:32

# 格式化
import math
print 'we r the {} who say "{}"!'.format('knight', 'Ni')
print 'The value of PI is approximately {other:.3f}.'.format(other=math.pi)

table = {
    'Sjoerd':4212,
    'Jack':4098,
    'Dcab':7678
}
for name, phone in table.items():
    print '{0:10}==>{1:10d}'.format(name,phone)

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print 'Jack:{Jack:d}; Sjoerd:{Sjoerd:d}; Dcab:{Dcab:d}'.format(**table)

