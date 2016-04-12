#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time

#获取文件的属性值
def creatfilesize(n):
    local_time = time.strftime("%Y%m%d%H%M%S",time.localtime())
    file_name = str(local_time)+".txt"
    bigFile= open(file_name, 'w')
    bigFile.seek(1024*1024*1024*n) 
    bigFile.write('test')
    #bigFile.write("test")
    bigFile.close()
    print "ALL down !"

if __name__ == '__main__':
    n = input("输入你要生成的文件大小（单位为G）:")
    creatfilesize(n)

    