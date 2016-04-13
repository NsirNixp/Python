# -*- coding:utf-8 -*-
import httplib
import urllib2
import urllib
import cookielib

Cookie = 'DedeUserID=17668003;DedeUserID__ckMd5=8aa32229517ebaac;SESSDATA=574b1bcf%2C1461131799%2C1b41b0bb;_dfcaptcha=26b96f9e4fa9969fc15e7bd78ad210b9;sid=92xvtygd;'
def get_history():
    
    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Host':'www.bilibili.com',
        'Connection':'keep-alive',
        'Accept-Language':'zh-CN,zh;q=0.8',
#        'Cookie':'DedeUserID=17668003;DedeUserID__ckMd5=8aa32229517ebaac;SESSDATA=574b1bcf%2C1461131799%2C1b41b0bb;_dfcaptcha=26b96f9e4fa9969fc15e7bd78ad210b9;sid=92xvtygd;',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'
        }
#第一种    
#    url = 'http://www.bilibili.com/account/history'
#    req = urllib2.Request(url, headers=headers)
#    html = urllib2.urlopen(req).read()
#    print html



#第二种
#    httpClient = httplib.HTTPConnection('www.bilibili.com', 80, timeout=30)
#    httpClient.request('GET','/account/history', '', headers)
#    response = httpClient.getresponse()
#    print response.status
#    print response.read()


#第三种
    url = 'http://www.bilibili.com/account/history'
    cookie = cookielib.CookieJar()
    cookie_handler = urllib2.HTTPCookieProcessor(cookie)

    data = None

    req = urllib2.Request(url, data, headers)
    opener = urllib2.build_opener(cookie_handler)
    opener.addheaders.append(('Cookie',Cookie))
    response = opener.open(req)
    page = response.read()
    print page    
        
if __name__ == '__main__':
    get_history()        
