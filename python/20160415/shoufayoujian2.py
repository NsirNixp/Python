#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: Nsirone
#contact: nsirone@outlook.com
#software: PyCharm Community Edition
#file: shoufayoujian.py
#time: 16/4/16 下午5:28

import smtplib
from email.mime.text import MIMEText

mailto_list = ['237654354@qq.com']
mail_host = 'smtp.163.com'
mail_user = '18516254259'
mail_pass = '8491398girl'
mail_postfix = '163.com'

def send_mail(to_list, sub, content):
	me = 'Hugo' + '<' + mail_user + '@' +mail_postfix + '>'
	msg = MIMEText(content, _subtype='plain')
	msg['Subject'] = sub
	msg['From'] = me
	msg['To'] = ';'.join(to_list)
	try:
		server = smtplib.SMTP()
		server.connect(mail_host)
		server.login(mail_user, mail_pass)
		server.sendmail(me, to_list, msg.as_string())
		server.close()
		return True
	except Exception, e:
		print str(e)
		return False

if __name__ == '__main__':
	send_mail(mailto_list, '主题1', '发送的内容1')
