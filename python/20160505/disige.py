#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: Nsirone
#contact: nsirone@outlook.com
#software: PyCharm Community Edition
#file: disige.py
#time: 5/6/16 12:35 AM

import urllib2

url = 'http://tycho.usno.navy.mil/cgi-bin/timer.pl'
response = urllib2.urlopen(url)
print response.read()
print '============================================================='
for line in urllib2.urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
    print line
