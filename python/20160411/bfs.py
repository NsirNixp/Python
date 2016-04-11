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
from os.path import join,getsize
import thread
from poster.encode import multipart_encode
from time import sleep, ctime 
import gevent
import gevent.monkey
gevent.monkey.patch_all()


BFS_IP = "172.16.0.141"
BFS_PORT = 2232
#BFS_IP = "172.16.13.90"
#BFS_PORT = 2232
#BFS_IP = "bfs.bilibili.co"
#BFS_PORT = 80

#BUCKET_NAME = "drawyoo"
#FILE_NAME = ""
#ACCESS_KEY = "2eebaf8d99e316da"
#ACCESS_SECRET = "1f7e1c4e5c8c1cc47cde6cd5818ae4"

BUCKET_NAME = "test"
FILE_NAME = "ccc/bbb/ccc/ddd/eee/fff/ggg/hhh/iii/"
ACCESS_KEY = "221bce6492eba70f"
ACCESS_SECRET = "6eb80603e85842542f9736eb13b7e3"

def get_sha1(src):
    mySha1 = hashlib.sha1()
    mySha1.update(src)
    mySha1_Digest = mySha1.hexdigest()
    return mySha1_Digest


def Make_File(path,size):
    fileWriter = open(path,'w')
    fileWriter.seek(size)
    Comment = random.randint(1,10)
    for x in xrange(1,10):
        fileWriter.write("abcdefghijklmnopqrstuvwxyz"*Comment)
    fileWriter.close()

def create_authorization(METHOD,FILE_NAME):
    now = int(time.time())
    h = hmac.new(ACCESS_SECRET,METHOD+"\n"+BUCKET_NAME+"\n"+FILE_NAME + "\n" + str(now) + "\n", sha)
    signature = base64.b64encode(h.digest())
    authorization = ACCESS_KEY + ":" + signature + ":" + str(now)
    return authorization

def Upload(params):
    METHOD = "PUT"

    uri = "/%s/%s" % (BUCKET_NAME, FILE_NAME)
    httpClient = None
    size = os.path.getsize(params)
    try:
        body = open(params).read()
        headers = {"Content-type": "image/jpg","Authorization": create_authorization(METHOD,FILE_NAME)}
        httpClient = httplib.HTTPConnection(BFS_IP, BFS_PORT, timeout=30)
        print uri
        httpClient.request(METHOD, uri,body,headers)
        response = httpClient.getresponse()
        print response.status
        print response.reason
        print response.read()
	fd = open('location_error.txt','a')
        header = response.getheaders()
        for h in header:
            if h[0] == 'location':
                location = h[1]
	    elif h[0] == 'code':
		code = int(h[1])
	    elif h[0] == 'etag':
		etag = h[1]
		print etag
	if code != 200:
	    fd.write('返回码是：===========================================  %d  文件大小为：%d \n' %(code,size))
	    return
	else:
	    fd.write(location + ' Success,code：=  %d files: %d \n' %(code,size))

    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()


def DownLoad(params):
    METHOD = "GET"
    FILE_NAME = params
    uri = "/bfs/%s/%s" % (BUCKET_NAME, FILE_NAME)
    httpClient = None
	
    try:
	headers = {"Content-type": "image/jpeg","Authorization": create_authorization(METHOD,params)}
	httpClient = httplib.HTTPConnection(BFS_IP, BFS_PORT, timeout=30)
	httpClient.request(METHOD, uri,"",headers)
	response = httpClient.getresponse()
	print "status:",response.status
	print "reason:",response.reason

	body = response.read()
	etag = get_sha1(body)
	return etag
    except Exception, e:
	print e
    finally:
	if httpClient:
	    httpClient.close()


def Delete(params):
    METHOD = "DELETE"
    FILE_NAME = params
    print params
    uri = "/%s/%s" % (BUCKET_NAME, FILE_NAME)
    httpClient = None
    try:
        headers = {"Content-type": "image/jpg","Authorization": create_authorization(METHOD,params)}
        httpClient = httplib.HTTPConnection(BFS_IP, BFS_PORT, timeout=30)
        httpClient.request(METHOD, uri,"",headers)
        response = httpClient.getresponse()
        print "status:",response.status
        print "reason:",response.reason
        f = open('delete_error.txt', 'a')
	if response.status != 200:
	    f.write(params+'有异常,返回码是：================%d\n' %(response.status))
	else:
	    f.write('此次成功\n')
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()

def Task(index):
    for x in xrange(0, 200000):
    	time.sleep(1)
        size = random.randint(index,index+1000000)
        #size = random.randint(index,index+1)
        params = 'test'+hashlib.sha1(str(size)).hexdigest()+'.txt'
        Make_File(params,size)
        time1 = time.time()
        Upload(params)
        time2 = time.time()
        print time2-time1
        if os.path.isfile(params):
            os.remove(params)

def Task_dl():
    name = ''
    etag = ''
    f = open("location_error.txt","r")
    fd = open("get_error.txt","a")
    lines = f.readlines()
    for x in xrange(0,len(lines)):
    	time.sleep(0.01)
        if lines[x].find(FILE_NAME) > 0:
            name = lines[x][lines[x].index(FILE_NAME)+len(FILE_NAME):].strip('\n').split('.')[0]
            time1 = time.time()
	    etag = DownLoad(FILE_NAME+lines[x][lines[x].index(FILE_NAME)+len(FILE_NAME):].strip('\n').split(' ')[0])
            time2 = time.time()
            timex = time2 - time1
        else:
            name = lines[x].split('/')[5].strip('\n').split('.')[0]
            time1 = time.time()
            etag = DownLoad(lines[x].split('/')[5].strip('\n').split(' ')[0])
            time2 = time.time()
            timex = time2 - time1
	if etag == name:
            fd.write("对比成功     time:%s\n" %(timex))
	else:
	    fd.write(lines[x].strip('\n').split(' ')[0] + "   ================================有异常\n")
    fd.close()
    f.close()

def Task_d():
    f = open("location_error.txt","r")
    lines = f.readlines()
    for x in xrange(0,len(lines)):
    	time.sleep(0.01)
        if lines[x].find(FILE_NAME) > 0:
            print lines[x][lines[x].index(FILE_NAME)+len(FILE_NAME):].strip('\n').split(' ')[0]
            time1 = time.time()
            Delete(FILE_NAME+lines[x][lines[x].index(FILE_NAME)+len(FILE_NAME):].strip('\n').split(' ')[0])
            time2 = time.time()
            print time2 - time1
        else:
	    print lines[x].split('/')[5].strip('\n').split(' ')[0]
            time1 = time.time()
	    Delete(lines[x].split('/')[5].strip('\n').split(' ')[0])
            time2 = time.time()
            print time2 - time1
    f = open("location.txt","w")
    f.writelines(lines)
    f.close()

def MT_Thread():
    tasks = []
    for i in range(0,2):
        tasks.append(gevent.spawn(Task, i*1000000))
    gevent.joinall(tasks)

if __name__ == '__main__':
    #MT_Thread()
    #for x in xrange(1,1000):
    #Make_File("test.txt",32252)
    #Upload("2.jpg")
    #Task(1)
    Task_dl()
    #Task_d()
    # main() 





 
