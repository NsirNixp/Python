import urllib, urllib2
import cookielib


Cookies = 'fts=1460705808; DedeUserID=17668003; DedeUserID__ckMd5=8aa32229517ebaac; SESSDATA=574b1bcf%2C1461310646%2C5ac68e5b; sid=auklngf4; LIVE_LOGIN_DATA=379e198622779cbae382a11ea7e23c4c5e25fe66; LIVE_LOGIN_DATA__ckMd5=cefb23d1af96f557; user_face=http%3A%2F%2Fi2.hdslb.com%2Fbfs%2Fface%2Fa00f3694156643ede579aed1e788d9a1843db94a.gif; LIVE_BUVID=718ea6531a53f01587e6225111e6fedf; LIVE_BUVID__ckMd5=ae33d0153bea26f7; rlc_time=1460716732542; _cnt_dyn=null; _cnt_pm=0; _cnt_notify=20; uTZ=-480; _dfcaptcha=4c646a89b298522272e9f94900d3d973; DedeID=4368788;'
headers = {
	'Accept-Encoding':'gzip, deflate',
	'Accept-Language':'zh-CN,zh;q=0.8',
	'Connection':'keep-alive',
	'Content-Length':'131',
	'Content-Type':'application/x-www-form-urlencoded',
	'Host':'interface.bilibili.com',
	'Origin':'http://static.hdslb.com',
	'Referer':'http://static.hdslb.com/play.swf',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
	'X-Requested-With':'ShockwaveFlash/21.0.0.216'
	}

url = 'http://interface.bilibili.com/dmpost?cid=7072238&aid=4368788&pid=1'
data = {
	'fontsize':25,
	'cid':'7072238',
	'pool':0,
	'mode':'1',
	'rnd':'1504465135',
	'message':'12',
	'date':'2016-04-15 21:05:46',
	'color':'16777215',
	'playTime':'857.266'
}
data = urllib.urlencode(data)
cookie = cookielib.CookieJar()
cookie_handler = urllib2.HTTPCookieProcessor(cookie)
req = urllib2.Request(url, data, headers)
opener = urllib2.build_opener(cookie_handler)
opener.addheaders.append(('Cookie',Cookies))
response = opener.open(req)