#!/usr/bin/python
def func(x):
        if not isinstance (x,int):
                raise ValueError('Must be int')
        a=str(x)
        my_long=len(a)
        print 'Your input numbers is %s digits' % my_long
        while x%10==0:
                x=x/10
#               print x         
        b=str(x)
        c=b[::-1]
        print 'And Palindrome string is: %s'% c
        return True


# func(1234567890)
# func("fsfsafaf")
# func(True)
# d = 2312.332
# func(2312.332)
print type(d)