# _*_ coding: utf-8 _*_

import os
import urllib
import re
import time

url = ""

# 保存一个html文件内容
def getHtml(url):
	file = urllib.urlopen(url)
	html = file.read()
	return html
# 去html文件里匹配响应的url
def getImageList(html):
	reg = 'http[^"}]*?(?:\.jpg|\.png|\.jpeg)'
	imgre = re.compile(reg)
	imgList = re.findall(imgre, html)
	return imgList
# 将图片的url打印到文件中
def printImageList(imgList):
	with open("webImage\url.txt", 'wb+') as f:
		for i in imgList:
			f.write(i + '\r\n')
# 根据url下载源数据
def download(imgList, page):
	x = 1
	for imgurl in imgList:
		print 'Download' + imgurl
		urllib.urlretrieve(imgurl, './webImage/%s_%s.jpg' %(page, x))
		x += 1
	print 'Download file ' + str(x) + ' file\'s end'

# 扯淡
def downImageNum(pagenum):
	page = 1
	pageNumber = pagenum
	while (page <= pageNumber):
		html = getHtml(url)
		imageList = getImageList(html)
		printImageList(imageList)
		download(imageList, page)
		page = page + 1

if __name__ == '__main__':
	os.system('mkdir webImage')
	# url = raw_input("enter the web page \n URL: ")
	url = 'http://www.mm131.com'
	downImageNum(1)
	time.sleep(10)