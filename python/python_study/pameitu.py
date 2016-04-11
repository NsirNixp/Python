# -*- coding:utf-8 -*-
# import Image
# 爬取美女网站的图片
from PIL import Image
import os
import urllib2
import re
import requests
from lxml import etree

Mozilla_header = {
	'Connection' : 'Keep-Alive',
	'Accept' : 'text/html, application/xhtml+xml, */*',
	'Accept-Language' : 'en-US,en;q=0.8zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
	'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}
links = []
k = 1
# print '请输入最后的页数： '
# endPage = int(raw_input())
endPage = 10
for j in range(1, endPage+1):
	if not os.path.exists('image'):
		os.mkdir('image')
	url = 'http://www.mzitu.com/page/' + str(j)
	req = urllib2.Request(url, headers = Mozilla_header)
	html = urllib2.urlopen(req).read()
	selector = etree.HTML(html)
	links = selector.xpath('//li/a[@target="_blank"]/@href')
	hot = selector.xpath('//li//span[@class="view"]/text()')
	for i in range(len(links)):
		h = ''
		for a in re.findall('\d+', hot[i]):
			h += a
		if int(h)>500000:
			req2 = urllib2.Request(links[i], headers = Mozilla_header)
			html2 = urllib2.urlopen(req2).read()
			selector2 = etree.HTML(html2)
			# page = selector2.xpath('//div[@class="pagenavi"]//span[last()-1]/text()')
			# page = selector2.xpath('//div[@class="pagenavi"]//span/text()')
			page = selector2.xpath('//div[@class="pagenavi"]//a//span//text()')

			break_flag = 0
			for k in range(1, int(page[4])):
				if break_flag:
					break
				req3 = urllib2.Request(links[i]+ '/' + str(k), headers = Mozilla_header)
				html3 = urllib2.urlopen(req3).read()
				selector3 = etree.HTML(html3)
				link_pic = selector3.xpath('//div[@class="main-image"]//@src')
				
				for each in link_pic:
					t = 3
					req4 = urllib2.Request(each, headers= Mozilla_header)
					while (t):
						try:
							image1 = urllib2.urlopen(req4, timeout = 10).read()
							# tmpIm = cStringIO.cStringIO(image1)
							pic_name = 'image/' + each[7:].replace('/','_')
							print each
							print pic_name
							if os.path.exists(pic_name):
								break_flag = 1
								break
							else:
								print '正在下载  %s' %each
								fp = open(pic_name, 'wb')
								fp.write(image1)
								fp.close()
								break
						except:
							t = t - 1
print '下载完毕！'
