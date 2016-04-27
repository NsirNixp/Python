#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: Nsirone
#contact: nsirone@outlook.com
#software: PyCharm Community Edition
#file: peizhibushu.py
#time: 16/4/24 下午12:11
import tornado.ioloop
import tornado.web

def main():
    app = make_app()
    app.listen(8888)
    IOloop.current().start()

if __name__ == '__main__':
    main()
