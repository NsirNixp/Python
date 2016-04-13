# -*-coding:utf-8 -*-
# 1.深拷贝
# 2.浅拷贝

# 将两个等长度的list合并成dict
text = 'C++ python shell ruby java javascript c'
code_num = [1,2,3,4,5,6,7]

text_list = text.split(' ')
code_dict = dict(zip(text_list,code_num))
print code_dict #{'c': 7, 'shell': 3, 'java': 5, 'python': 2, 'javascript': 6, 'C++': 1, 'ruby': 4}

#get
a = code_dict.get('fortran', None)

#update, del, copy, clear
other_code = {'php':78014, 'objective-c':34444}
code_dict.update(other_code)
del code_dict['c++']

#sort key and value 列表解析
[(k, a_copy[k]) for k in sorted(a_copy.keys())]

#Shelve库
import shelve
D = shelve.open(file)	
D['name'] = 'newtext'
D.close()
#Pickle/cPickle
import cPickle
f = open(file, mode)
cPickle.dump(obj, f)
Obj = cPickle.load(f)

# 随机函数：
import random
charactor = 'abcdefghijklmnokqrstuvwxyz1234567890'
len_char = len(charactor) - 1
#generate name
a[0]* 4
a[0] = charactor[random.randint(0, len_char)]
a[1] = charactor[random.randint(0, len_char)]
a[2] = charactor[random.randint(0, len_char)]
a[3] = charactor[random.randint(0, len_char)]

name = ''.join(a)

#generate password
a = [0]*6
a[0] = charactor[random.randint(0, len_char)]
a[1] = charactor[random.randint(0, len_char)]
a[2] = charactor[random.randint(0, len_char)]
a[3] = charactor[random.randint(0, len_char)]
a[4] = charactor[random.randint(0, len_char)]
a[5] = charactor[random.randint(0, len_char)]

password = ''.join(a)
#write file
f = open('a.txt', 'w')
f.write(name + ',' + password + '\n')
f.close()
