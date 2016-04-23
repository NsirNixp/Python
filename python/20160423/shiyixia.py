#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: Nsirone
#contact: nsirone@outlook.com
#software: PyCharm Community Edition
#file: shiyixia.py
#time: 16/4/24 上午12:06

# 总结几种常用的python下载文件的方法,具体使用了httplib2,urllib等包,希望有用
# 据我分析的意思是,从读取的文件中每次获取8k的内容,然后分批写到文件中
# 1,大文件下载
import urllib, urllib2

def down_load_file():
    url = 'http://www.bilibili.com'
    file_name = url.split('/')[-1]
    u = urllib2.urlopen(url)
    f = open('a.txt', 'wb')
    meta = u.info()
    file_size = int(meta.getheaders('Content-Length')[0])
    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer_1 = u.read(block_sz)
        if not buffer_1:
            break
        file_size_dl += len(buffer_1)
        f.write(buffer_1)
    f.close()

if __name__ == '__main__':
    down_load_file()