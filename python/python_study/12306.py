# _*_ coding: utf-8 _*_
import json, urllib
from urllib import urlencode

def main():
	appkey = "8ec922a215b8272c779303fd8f0c8a6d"
	request(appkey, "GET")


def request(appkey, m="GET"):
	url = "http://apis.juhe.cn/train/s"
	params ={
		"name" : "G4",
		"key" : appkey,
		"dtype" : ""
	}
	params = urlencode(params)
	print params
	if m == "GET":
		print "%s?%s" %(url,params)
		f = urllib.urlopen("%s?%s" %(url, params))
	else:
		f = urllib.urlopen(url, params)

	content = f.read()
	res = json.loads(content)
	print res
	if res:
		error_code = res['error_code']
		if error_code == 0:
			print res['error_code']
		else:
			print "%s:%s" %(res["error_code"], res["reason"])
	else:
		print "request is fail"

if __name__ == '__main__':
	main()