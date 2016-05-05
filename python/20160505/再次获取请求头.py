# -*- coding:utf-8 -*-
import urllib
from types import *
def iscontentype(URLorFile, contentType='x'):
	result = 1
	try:
		if type(URLorFile) == StringType:
			file = urllib.urlopen(URLorFile)
		else:
			file = URLorFile

		testType = file.info().getheader('Content-Type')
		if testType and testType.find(contentType) == 0:
			result = 1
		else:
			result = 0

		if type(URLorFile) == StringType:
			file.close()
		return result
	except:
		return 0

if __name__ == '__main__':
	print iscontentype('http://www.baidu.com')