# -*- coding:utf-8 -*-
class tClass():
	"""测试用的"""
	def __init__(self, orig=0):
		self.storedValue = orig
	def read(self):
		return self.storedValue
	def write(self, x):
		self.storedValue = x

class Test():
	a = tClass()
	print 'a: ' + str(a.read())
	a.write(10)
	print 'a: ' + str(a.read())
	b = tClass(100)
	print 'b: ' + str(b.read())

if __name__ == '__main__':
	Test()