# _*_ coding:utf-8 _*_
# 此接口使用的是“聚合数据”提示的免费api服务
# 用户名：nsirone
# 密码：8491398girl
# 已经经过实名认证
# 此接口为“净值数据”  接口地址：http://japi.juhe.cn/jingzhi/query.from
# 网址：https://www.juhe.cn/docs/api/id/25

# _*_ coding:utf-8 _*_
import json, urllib
from urllib import urlencode

appkey = "c6339b77866e2b53ad823bb43409cf71"
page = '1'
pagesize = '20'
jijintype = 'zhaiquan'

params = {
	"key" : appkey,
	"page" : page,
	"pagesize" : pagesize,
	"jijintype" : jijintype
}
params = urlencode(params)
print params
def main():
	request1(params, "GET")
	# request2(appkey, "GET")
	# request3(appkey, "GET")
	# request4(appkey, "GET")
	# request5(appkey, "GET")
	# request6(appkey, "GET")
	# request7(appkey, "GET")
	# request8(appkey, "GET")
	# request9(appkey, "GET")
# 全部开放式基金
def request1(params, m="GET"):
	url = "http://japi.juhe.cn/jingzhi/query.from"
	# url = "http://web.juhe.cn:8080/fund/netdata/all"

	if m == "GET":
		print "%s?%s" % (url, params)
		f = urllib.urlopen("%s?%s" % (url, params))
	else:
		f = urllib.urlopen(url, params)

	content = f.read()
	res = json.loads(content)

	if res:
		error_code = res["error_code"]
		
		if error_code == 0:
			print res["result"]
		else:
			print "%s?%s" %(res["error_code"], res["reason"])
	else:
		print "request api error"

# 股票型基金
# def rquest2(appkey, m="GET"):

if __name__ == "__main__":
	main()