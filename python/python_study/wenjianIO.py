#-*- coding:utf-8 -*-
fo = open('foo.txt', 'r+')
str = fo.read(10)
print 'read string is :', str


position = fo.tell()
print 'current file position is :', position

#position = fo.seek(0, 0)
str = fo.read(10)
print 'again read string is :', str
fo.close()
