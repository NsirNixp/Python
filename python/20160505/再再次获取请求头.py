import chardet
import urllib
data = urllib.urlopen('http://www.pythontab.com').read()
chardit = chardet.detect(data)
data1 = urllib.urlopen('http://www.baidu.com').read()
chardit1 = chardet.detect(data1)
print chardit['encoding']
print chardit1['encoding']