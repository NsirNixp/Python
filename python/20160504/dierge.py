#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @version: 1.0
# @author: Nsirone
# @license: Apache Licence 
# @contact: nsirone@outlook.com
# @site: http://www.google.com
# @software: PyCharm Community Edition
# @file: dierge.py
# @time: 2016/5/4 19:49

import sys
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as e:
    print 'I/O error({0}):{1}'.format(e.errno, e.strerror)
except ValueError as e:
    print 'Could not convert data to an integer'
except:
    print 'Unexpected error: ',sys.exc_info()[0]
    raise