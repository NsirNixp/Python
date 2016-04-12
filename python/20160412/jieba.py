#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-04-12 16:06:33
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import jieba
import os
import sys
print dir(jieba.jieba)

seg_list = jieba.cut('我来到北京清华大学', cut_all=True)
print 'Full Mode:' + '/ '.join(seg_list)

seg_list = jieba.cut('我来到北京那个清华大学', cut_all=False)
print 'Default Mode:' + '/ '.join(seg_list)

seg_list = jieba.cut('她来到了网易航燕大厦')
print ', '.join(seg_list)

seg_list = jieba.os.cut_for_search('小明说是毕业于中国科学院计算所，后在日本精度大学深造')
print ', '.join(seg_list)

