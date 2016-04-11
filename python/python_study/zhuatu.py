# -*- coding: UTF-8 -*- 
# 这应该是一个爬虫程序
import requests
from bs4 import BeautifulSoup
import random
from datetime import date
import os
import threading
import sys, re

headers = {
	"Referer" : "http://www.mm131.com/",
	"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537."
}

def getMM131Img(siteUrl):
	resp = requests.get(siteUrl)
	resp.encoding = 'gb2312'
	soup = BeautifulSoup(resp.text, 'html5lib')
	dirname = soup.find('div', class_ = 'content').h5.string
	pagecount = soup.find('div', class_ = 'content-page').span.string
	tmpm = re.findall(r'\d+', pagecount)
	piccount = int(tmpm[0])
	imgStr = soup.find('div', class_ = 'content-pic').img['src']
	prefix = imgStr[:imgStr.rfind("/")+1]
	picext = "." + imgStr.split(".")[-1]

	resp.close()

	session = requests.Session()
	for img in [prefix+str(i+1)+picext for i in range(piccount)]:
		name = img.split('/')
		if not dirname:
			dirname = date.today().strftime("%Y%m%d")
		if not os.path.exists("D:\\test\\images\\" + dirname):
			os.mkdir("D:\\test\\images\\" + dirname)
			filename = 'D:\\test\\images\\' + dirname+"\\" + str(random.randrange(1000))

		with open(filename, 'wb') as f:
			print img
			try:
				resp1 = session.get(img, headers=headers, timeout=30, stream=True)
				for chunk in resp1.iter_content(chunk_size=512):
					f.write(chunk)
				resp1.close()
			except:
				print sys.exc_info()

	session.close()
	print "图片下载完成"

if __name__ == "__main__":
	siteUrl = input('图片集url:')
	t = threading.Thread(target = getMM131Img, args = (siteUrl,))
	t.start()