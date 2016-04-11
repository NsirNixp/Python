#!/usr/bin/env python
# -*- coding: utf-8 -*-
import httplib
import urllib

def upload(body):
    httpClient = None
    try:
        method = "PUT"
        uri = "/%s/%s" % (BUCKET_NAME, FILE_NAME)
        # body = open("333.jpg").read()
        # sha1sum = get_sha1(body)
        headers = {"Content-type": "image/jpg"
                        , "Authorization": authorization}
        httpClient = httplib.HTTPConnection(BFS_IP, BFS_PORT, timeout=30)
        httpClient.request(method, uri, body, headers)

        response = httpClient.getresponse()
        if response.status != 200:
            sendsms()
            return
        header = response.getheaders() #获取头信息
        for h in header:
            if h[0] == 'code':
                code = int(h[1])
            elif h[0] == 'etag':
                etag = h[1]
            elif h[0] == 'location':
                location = h[1]
        if code != 200 or sha1sum != etag:
            sendsms()
            return
        return etag
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()

if __name__ == '__main__':
    body = open("2.jpg".read())
    upload(body)