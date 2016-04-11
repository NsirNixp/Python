# -*- coding:utf-8 -*-
import httplib
import urllib2
import urllib
# httplib实现了HTTP和HTTPS的客户端协议，一般不直接使用，在python更高层的封装模块中
# （urllib，urllib2）使用了它的http实现

conn = httplib.HTTPConnection('www.google.com', 80, False)
conn.request('get', '/', headers={'Host':'www.google.com',
									'User-Agent':'Mozila/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5',
									'Accept':'text/plain'})
res = conn.getresponse()
print 'version：', res.version
print 'reason：', res.reason
print 'status：', res.status
print 'msg：', res.msg
print 'headers：', res.getheaders()
conn.close()

# urllib2:
req = urllib2.Request('http://www.pythontab.com')
response = urllib2.urlopen(req)
the_page = response.read()
print the_page


url = 'http://www.pythontab.com'
response = urllib2.urlopen(url)
html = response.read() #读取网页信息 html
print html
print response.geturl() #返回真正的url
print '============================'
print response.info() #获取返回头信息

# 有时候会发送一些数据到URL
# post 方法：
url = 'http://www.baidu.com'
values = {'body':'test short talk', 'via':'xxxx'}
data = urllib.urlencode(values)
req = urllib2.Request(url, data)

# 使用Basic HTTP Authentication:

# urllib：比较简单，功能相对也比较弱，可以从指定的URL下载文件，或是对一些字符串进行编码解码以使他们成为特定的 URL串。
# urllib2：它有各种各样的Handler啊，Processor啊可以处理更复杂的问 题，比如网络认证，使用代理服务器，使用cookie等等。
# HTTP是基于请求和应答机制的--客户端提出请求，服务端提供应答。urllib2用一个Request对象来映射你提出的HTTP请求,在它最简单的使用形式中你将用你要请求的地址创建一个Request对象，通过调用urlopen并传入Request对象，将返回一个相关请求response对象，这个应答对象如同一个文件对象，所以你可以在Response中调用.read()。

# urllib 和urllib2(python3已经合并成一个了)都是接受URL请求的相关模块，但是提供了不同的功能。（老外写的）
# 1、urllib2可以接受一个Request类的实例来设置URL请求的headers，urllib仅可以接受URL:这意味着你不可以伪装你的User Agent字符串等。
# 2、urllib提供urlencode方法用来GET查询字符串的产生，而urllib2没有。这是为何urllib常和urllib2一起使用的原因。Data同样可以通过在Get请求的URL本身上面编码来传送。urllib.urlencode(data) 

auth_handler = urllib2.HTTPBasicAuthHandler()
auth_handler.add_password(realm='PDQ Application',
							uri='https://pythoneye,com.vecrty.py',
							user='user',
							passwd='pass')
opener = urllib2.build_opener(auth_handler)
urllib2.install_opener(opener)
urllib2.urlopen('http://www.pythoneye.com/app.html')
