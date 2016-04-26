#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @version: 1.0
# @author: Nsirone
# @license: Apache Licence 
# @contact: nsirone@outlook.com
# @site: http://www.google.com
# @software: PyCharm Community Edition
# @file: diaoyong.py
# @time: 2016/4/26 11:24

# import diyige
from diyige import a

#调用的时候可以使用命令行中的参数，所以可以这样写


# b = diyige.a
if __name__ == '__main__':
    import sys
    print a(int(sys.argv[1]))
