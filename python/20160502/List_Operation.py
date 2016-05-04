#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: Nsirone
#contact: nsirone@outlook.com
#software: PyCharm Community Edition
#file: List_Operation.py
#time: 5/2/16 8:45 AM

import os, sys
from collections import deque

queue = deque(['Eric', 'John', 'Michael'])
print queue
queue.append('Terry')
queue.append('Graham')
print queue
queue.popleft()
print queue
queue.popleft()
print queue
queue.pop()
print queue