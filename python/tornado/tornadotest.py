#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @version: 1.0
# @author: Nsirone
# @license: Apache Licence 
# @contact: nsirone@outlook.com
# @site: http://www.google.com
# @software: PyCharm Community Edition
# @file: tornadotest.py
# @time: 2016/4/21 13:20

import tornado.ioloop
import tornado.web
class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write('Hello, world')

application = tornado.web.Application([
		(r'/', MainHandler)
	])

if __name__ == '__main__':
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()