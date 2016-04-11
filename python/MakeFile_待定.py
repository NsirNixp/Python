#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import random

def Make_File(path,size):
	#首先以路径path新建一个文件，并设置模式为写
	fileWriter = open(path,'w')
	#根据文件大小，偏移文件读取位置
	# file.seek(1024*1024*1024*size)
	fileWriter.seek(1024*1024*size)
	#然后在当前位置写入任何内容，必须要写入，不然文件不会那么大
	# file.write('\x00')
	fileWriter.write("哈好好")
	fileWriter.close()

def qianpian(path,size,MaxSize):

	fileContent=open(path,'r')
	fileWriter=open('files/'+hashlib.sha1(str(size)).hexdigest()+'.txt','w')
	buf = fileContent.read(size)
	for size in (0,MaxSize*1024*1024):
		if(size):
			fileWriter.write(buf)
    		buf = fileContent.read(size)
    		fileWriter=open('files/'+hashlib.sha1(str(size)).hexdigest()+'.txt','w')

	# buf.close()
	fileContent.close()
	fileWriter.close()
if __name__=='__main__':
	MaxSize = 1
	size = random.randint(100,10240)
	print size
	Make_File('./files/test.txt',size)
	qianpian('./files/test.txt',size,MaxSize)