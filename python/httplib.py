#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httplib2
import urllib2
import re	#正则表达式

class WeiboClass:
	def get_content(self,url,headers,id):
		http = httplib2.Http()
		response,content = http.request(url+str(id),'GET',headers = headers)
		return content.decode('unicode-escape').encode('utf-8')


	def is_company(self,url,headers,id):
		content = self.get_content(url,headers,id)
		