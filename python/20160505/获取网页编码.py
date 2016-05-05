# -*- coding:utf-8 -*-
import urllib
url1 = 'http://www.baidu.com'
url2 = 'http://www.pythontab.com'
fopen1 = urllib.urlopen(url1).info()
fopen2 = urllib.urlopen(url2).info()



print fopen1.getparam('charset') #baidu
print fopen2.getparam('charset') #python tab