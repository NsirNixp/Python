bilibili_office    MM : bilibili0516

已通过认证，ID=2245。 倪雪鹏 project ID
==================================================================================================
nsirone		17668003
王可		4780461
张巧格		15555180
nsirtwo		19865954
望帆		
视频		451242
==================================================================================================
张巧格		13162875137	521217
王可		15618698090	222222
nsirone		18516254259	111111
nsirtwo 	nsirone@outlook.com 	111111

040b3d6034981b5f26d0f1823c1b0d22  	_dfcaptcha
==================================================================================================
http://project.bilibili.co/  project管理系统

==================================================================================================
市北性能测试系统帐号（不允许压测外网）：
访问域名：http://ngrinder.bilibili.co
账号：nixuepeng
密码：G#68z8%k

代理最大值为16（如果小于16，说明机器故障），请联系我。


==================================================================================================
账号系统的相关链接
1.后台:account-mng.bilibili.co
2.授权中心:passport.bilibili.com
3.前台:account-pyf.bilibili.com
http://account-pyf.bilibili.com/site/setting


==================================================================================================
付费视频：
172.16.0.60：3306	mysql   root	Gmxdg6WpykLM
账号授权：
172.16.0.217：3307	mysql	acc		123456
房间号：
172.16.4.212：3306	mysql	bilibili	123456

==================================================================================================
DedeUserID=4780461; 
DedeUserID__ckMd5=13d78097a9671f45; 
SESSDATA=a2836ab9%2C1448509481%2C25efe99e;
_dfcaptcha=80f4f821119131079e8d059b830990ba;

sid=d5u4wahs

DedeUserID=17668003;DedeUserID__ckMd5=8aa32229517ebaac;SESSDATA=574b1bcf%2C1453343501%2C47eed9b0;_dfcaptcha=b6ce29e5e6164f99ea23015a51f63c9b;sid=8td9ye8i;
b6ce29e5e6164f99ea23015a51f63c9b

select distinct top 10  c.fundid,a.custid,a.trdpwd,a.orgid,c.secuid,c.stkcode,d.buyunit * 10 as qty,
d.stktype,e.stklevel,e.market, t.ofcode,cast((maxrisevalue+maxdownvalue)/2 as decimal(9,2)) as price 
from customer a  
inner join stkasset c on  a.custid=c.custid  
and a.status='0'   
inner join stktrd   d on  c.stkcode=d.frzstk   
inner join stock    e on  e.stkcode=c.stkcode 
inner join etfbaseinfo t on t.etfcode0 = e.stkcode 
where d.stopflag='F'  
and e.market='1' 
and d.trdid = 'C'   
and e.stktype='E' 
and c.stkavl > 2000000 
and t.market=1 
and  t.etftype=1 
and t.etfprop = 1 order by c.fundid desc,c.stkcode

==================================================================================================
linux shell：
实时监控log文件： tail -f xx.log
==================================================================================================
拜年祭设置时间接口
http://172.16.0.239:791/act/cj/date/modify/pc?type=start&value=1453370820	开始时间
http://172.16.0.239:791/act/cj/date/modify/pc?type=zero&value=1453368300  	零点时间
http://172.16.0.239:791/act/cj/date/modify/pc?type=end&value=1453374480		结束时间

==================================================================================================
微博视频缓存路径（chrome）
C:\Users\bilibili_\AppData\Local\Google\Chrome\User Data\Default\Pepper Data\Shockwave Flash
==================================================================================================
svn账号和密码：username：nixuepeng    pwd：nixuepeng
==================================================================================================
任务栏变窄：net stop uxsms     net start uxsms 
==================================================================================================
无线路由信息：
wifi热点名字	HIWIFI_Test5G  HIWIFI_test
热点密码		bilibilitest

路由后台登录密码	bilibili0516
极账号				18600733113  密码  bilibilitest		


==================================================================================================