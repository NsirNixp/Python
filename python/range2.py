#!/usr/bin/env python
# -*- coding:utf8 -*- 
import re

p=re.compile('\n',re.S)
#读文件内容
fileContent=open('files/abc.txt','r').read()
#根据换行符对文本进行切片	
paraList=p.split(fileContent)
print paraList
#创建一个写文件的句柄
fileWriter=open('files/0.txt','w')
#遍历切片后的文本列表
for paraIndex in range(len(paraList)):
	#先将列表中第一个元素写入文件中
    fileWriter.write(paraList[paraIndex])
    #判断是否写够3个切片，如果已经够了
    if((paraIndex+1)%3==0):
    	#关闭当前句柄
        fileWriter.close()
        #重新创建一个新的句柄，等待写入下一个切片元素。注意这里文件名的处理技巧。
        fileWriter=open('files/'+str((paraIndex+1)/3)+'.txt','w')	
#关闭最后创建的那个写文件句柄
fileWriter.close()
print('finished')