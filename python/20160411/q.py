import urllib2

try:
    response = urllib2.Request('http://www.bilibili.com')
    print getcode(response)

except urllib2.HTTPError, e:
    print e
