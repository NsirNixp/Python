import urllib

baidu = urllib.urlopen('http://www.baidu.com')
print baidu.info()
print baidu.getcode()
print baidu.geturl()
for line in baidu:
    print line

baidu.close()
