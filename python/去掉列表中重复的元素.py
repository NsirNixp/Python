#!/usr/bin/env python
# -*- coding: utf-8 -*-


def func(x):
        d={}
        l=[]
        for i in x:
                d[i]='x'
        for x,y in d.iteritems():
                l.append(x)
        print l
 
x=[1,1,1,2,3,4,4]
func(x)
 
def fund(x):
          c=list(set(x))
          print c
          return True
def a():
	print "sadfasf"
fund([1, 1, 3, 4, 5, 6, 2, 2, 1, 6])

a()



