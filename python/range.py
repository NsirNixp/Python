#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import random
# 创建txt文件

for j in range(0,2):
	f = open(hashlib.sha1('w'+str(j)).hexdigest()+'.txt', 'w')
	f.write(str(random.randint(0,10000456564564645)))
	f.close()


# a = "a test string"
# print hashlib.sha1(a).hexdigest()
