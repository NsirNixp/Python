#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @version: 1.0
# @author: Nsirone
# @license: Apache Licence 
# @contact: nsirone@outlook.com
# @site: http://www.google.com
# @software: PyCharm Community Edition
# @file: diliuge.py
# @time: 2016/5/4 20:17

# 预定义的清理行为

# 有些对象定义了标准的清理行为，无论对象操作是否成功，不再需要该对象的时候就会起作用。
# 这段代码的问题在于在代码执行完后没有立即关闭打开的文件，这在简单的脚本里没什么，但是大型
# 应用程序就会出问题，with语句是的文件夹之类的对象确保总能及时准确地进行清理
for line in open('abc.txt'):
    print line


# 修改后为：
with open('abc.txt') as f:
    for line in f:
        print line

# 语句执行后，文件f总会被关闭，即使实在处理文件中的数据时出错也一样
# 其他对象是否提供了预定义的清理行为查看他们的文档