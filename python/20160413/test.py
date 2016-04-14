#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: Nsirone
#contact: nsirone@outlook.com
#software: PyCharm Community Edition
#file: test.py
#time: 16/4/13 下午10:56
# 判断指定的端口是否被占用
import os, socket
def IsOpen(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, int(port)))
        s.shutdown(2)
        print '%d is open' %port
        return True
    except:
        print '%d is down'% port
        return False
if __name__ == '__main__':
    IsOpen('127.0.0.1', 80000)