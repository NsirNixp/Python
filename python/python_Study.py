#!/usr/bin/env python
# -*- coding: utf-8 -*-
#以linux环境下运行情况为准
import base64
import hmac
import random
import hashlib
import sha
import httplib
import urllib
import time
import os
import thread
import sys
from poster.encode import multipart_encode
from time import sleep, ctime 

#连接服务器配置

# 随机创建文件
def Make_File(path,size):
    #首先以路径path新建一个文件，并设置模式为写
    fileWriter = open(path,'w')
    #根据文件大小，偏移文件读取位置
    fileWriter.seek(size)
    #然后在当前位置写入任何内容，必须要写入，不然文件不会那么大
    # file.write('\x00')
    k = "abcdefghijklmnopqrstuvwxyz123456789l0"
    Comment = random.randint(1,100)*k
    for x in xrange(1,10):
        Sum = 0
        fileWriter.write(Comment)
        Sum = Sum+sys.getsizeof(Comment)

    
    fileWriter.close()
    return  Sum
# 上传
def Upload(params):
    BFS_IP = "bfs.bilibili.co"
    BFS_PORT = 80
    #指定bucket名称
    BUCKET_NAME = "test"
    #文件名，不指定文件名的时候为空
    FILE_NAME = ""
    #测试需要的 accessKey&Secret
    ACCESS_KEY = "221bce6492eba70f"
    ACCESS_SECRET = "6eb80603e85842542f9736eb13b7e3"
    #几点说明
    #1.上传-METHOD = "PUT"        指定url：/{$BUCKET_NAME}/{$FILE_NAME}
    #   不需要bfs路径，指定文件名即可
    #2.删除-METHOD = "DELETE"     指定url：/{$BUCKET_NAME}/{$FILE_NAME}
    #   不需要bfs领，指定文件名即可
    #3.下载-METHOD = "GET"        指定url：/bfs/{$BUCKET_NAME}/{$FILE_NAME}
    #   需要指定文件的路径，发送请求时可以不需要body内容，或者指定body为空
    #4.HEAD-METHOD = "HEAD"       指定url：/bfs/{$BUCKET_NAME}/{$FILE_NAME}
    #   需要指定文件的路径，发送请求时可以不需要body内容，或者指定body为空
    # 上传文件不同的时候，PUT提示数据的方式需要修改,测试时去掉了文件类型的校验，上传任何类型的文件，image/jpeg格式均能校验通过
    METHOD = "PUT"

    now = int(time.time())
    h = hmac.new(ACCESS_SECRET,METHOD+"\n"+BUCKET_NAME+"\n"+FILE_NAME + "\n" + str(now) + "\n", sha)
    #算sha1，文件加密
    signature = base64.b64encode(h.digest())
    #token
    authorization = ACCESS_KEY + ":" + signature + ":" + str(now)
    uri = "/%s/%s" % (BUCKET_NAME, FILE_NAME)
    httpClient = None
    try:
        body = open(params).read()
    #   上传文件为图片
        headers = {"Content-type": "image/jpeg","Authorization": authorization}
    #   上传文件为其他
    #   headers = {"Content-type": "multipart/form-data","Authorization": authorization}  
        httpClient = httplib.HTTPConnection(BFS_IP, BFS_PORT, timeout=30)
        print uri
        httpClient.request(METHOD, uri,body,headers)
        response = httpClient.getresponse()
        print response.status
        print response.reason
        print response.read()
        # print response.getheaders()

        if response.status != 200:
                # sendsms()
                return
        header = response.getheaders() #获取头信息
        for h in header:
            if h[0] == 'location':
                location = h[1]
                f = open('1.txt', 'a')
                f.write(location+'\n')
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()
# 需要的任务
def Task(index):
    for x in xrange(0, 4):
        size = random.randint(index,index+1000000)
        params = 'test'+hashlib.sha1(str(size)).hexdigest()+'.txt'
        Sum = Make_File(params,size)
        Upload(params)
        if os.path.isfile(params):
            os.remove(params)
        return Sum+size
if __name__ == '__main__':
    print Task(1)
#   20971520