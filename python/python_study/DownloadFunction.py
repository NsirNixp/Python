
import urllib

def cbk(a, b, c):
	per = 100.0 * a * b / c
	if per>100:
		per = 100

	print '%.2f%%' % per

url = 'http://www.google.com'
local = 'D://google.html'
urllib.urlretrieve(url, local, cbk)