# -*- coding: utf-8 -*-

import difflib
import sys

a = open('a.txt', 'a')
a.write("1234567890")
a.close()


b = open('b.txt', 'a')
b.write("1234567890")
b.close()

a = open('a.txt', 'U')
b = open('b.txt', 'U')


diff = difflib.ndiff(a, b)
sys.stdout.writelines(diff)