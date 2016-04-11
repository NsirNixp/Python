import urllib2

url = 'http://www.baidu.com'
response = urllib2.urlopen(url)
html = response.read()
print html