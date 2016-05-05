#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: Nsirone
#contact: nsirone@outlook.com
#software: PyCharm Community Edition
#file: disange.py
#time: 5/6/16 12:16 AM

import urllib2
for line in urllib2.urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
    print line
    # line = line.decode('utf-8')
    # if 'EST' in line or 'EDT' in line:
    #     print line