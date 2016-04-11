# _*_ coding:UTF-8 _*_
import jieba
# import sys

# reload(sys)
# sys.setdefaultencoding('utf-8')

test_str = "我来到北京清华大学"
seg_list = jieba.cut(test_str, cut_all=True)
print "Full Mode: ", "/ ".join(seg_list)