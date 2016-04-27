#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @version: 1.0
# @author: Nsirone
# @license: Apache Licence 
# @contact: nsirone@outlook.com
# @site: http://www.google.com
# @software: PyCharm Community Edition
# @file: qiepian.py
# @time: 2016/4/27 21:14

word = ['123','123456','123456789','123456789123']
for i in word[:]:
    print word
    if len(i) > 6:
        word.insert(0, i)
# for j in word:
#     if len(j) > 6:
#         word.insert(len(word), j)
#         word.insert(0, j)
print word


def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


if __name__ == '__main__':
    print f(1)
    print f(2)