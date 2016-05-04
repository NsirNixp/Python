#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: Nsirone
#contact: nsirone@outlook.com
#software: PyCharm Community Edition
#file: two.py
#time: 4/28/16 12:44 PM

def cheeseshop(kind, *arguments, **keywords):
	print '-- Do you have any', kind, '?'
	print '--I\'m sorry, we\'re all out of',kind
	for arg in arguments:
		print arg
	print '-' * 40
	keys = sorted(keywords.keys())
	for kw in keys:
		print kw, ':', keywords[kw]


if __name__ == '__main__':
	cheeseshop('Limberger', 'It\'s very runny, sir.',
				'It\'s really very ,VERY runny, sir.',
				shopkeeper='Micheal Palin',
				client='John Clesse',
				sketch='Cheese Shop Sketch')