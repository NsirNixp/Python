#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: Nsirone
#contact: nsirone@outlook.com
#software: PyCharm Community Edition
#file: dierge.py
#time: 16/4/24 上午12:38
# 这个有时间再看一下

# Tornado是一个编写对http请求响应的框架，作为程序员，你的工作是编写响应特定的条件的
# http请求的响应handler，下面是一个全功能的Tornado应用的基础示例

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado

from tornado.options import define, options
define('port', default=8000, help='run on the given port', type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Wocao')
        self.write(greeting + ', friendly user!')

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r'/', IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
