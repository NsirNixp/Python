#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: Nsirone
#contact: nsirone@outlook.com
#software: PyCharm Community Edition
#file: shoufayoujian.py
#time: 16/4/16 下午5:28
import sys
import time
import smtplib
import poplib

# 邮件发送函数
def send_mail():
    try:
        handle = smtplib.SMTP('smtp.163.com', 25)
        handle.login('18516254259@163.com', '8491398girl')
        msg = 'TO: 237654354@qq.com\r\nFrom:18516254259@163.com\r\nSubject:hello\r\n'
        handle.sendmail('18516254259@163.com', '237654354@qq.com')
        handle.close()
        return 1
    except:
        return 0

# 邮件接收函数
def accept_mail():
	try:
		p = poplib.POP3('pop.163.com')
		p.user('18516254259@163.com')
		p.pass_('8491398girl')
		ret = p.stat() #返回一个元组：(邮件数，邮件尺寸)
		# p.retr('邮件号码')方法返回一个元组：(状态信息，邮件，邮件尺寸)
	except poplib.error_proto, e:
		print 'Login failed: ', e
		sys.exit(1)

# 运行当前文件时，执行sendmail函数和accept_mail函数
if __name__ == '__main__':
	send_mail()
	accept_mail()