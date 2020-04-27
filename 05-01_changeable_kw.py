#!/usr/bin/env python
# -*- coding: utf-8 -*-

#changeable_para==
def sqr_sum(*num):
    sum = 0
    for x in num:
        sum += pow(x,2)
    return sum

print(sqr_sum(1,2,3,4))
tuple1 = (1,2,3,4)
print(sqr_sum(*tuple1))
print(sqr_sum())

#keyword_para==
def kw_para(name,age,**kw):
    print("name:{0} age:{1} ext:{2}".format(name,age,kw))

kw_para("a",1,**{"add":"qwer","code":123})

