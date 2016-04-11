import requests
import re


re1='(<)'	# Any Single Character 1
re2='(body)'	# Word 1
re3='( )'	# White Space 1
re4='(data)'	# Word 2
re5='(-)'	# Any Single Character 2
re6='(abtest)'	# Word 3
re7='(=)'	# Any Single Character 3
re8='(".*?")'	# Double Quote String 1
re9='(>)'	# Any Single Character 4




num_a = 0
num_b = 0
num_notgated = 0    

for i in range(0,250):
#     r = requests.get('http://172.16.4.217/all?keyword=a&order=totalrank&page=1')
#     rg = re.compile(re1+re2+re3+re4+re5+re6+re7+re8+re9,re.IGNORECASE|re.DOTALL)
#     m = rg.search(r.text)
#     print m.group(8)

#     if m.group(8) == r'"notgated"':
#         num_notgated = num_notgated + 1
#     elif m.group(8) == r'"a"':
#         num_a = num_a + 1
#     elif m.group(8) == r'"b"':
#         num_b = num_b + 1


    r = requests.get('http://search.bilibili.com/all?keyword=fate')
    cookiea = r.cookies['abtest_search']    
    if cookiea == "notgated":
        num_notgated = num_notgated + 1
    elif cookiea == "a":
        num_a = num_a + 1
    elif cookiea =="b":
        num_b = num_b + 1
    else:
    	break

print 'a number is %d ' % num_a
print 'b number is %d ' % num_b
print 'notgated number is %d ' % num_notgated