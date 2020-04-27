#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import reduce
#  def ho_func(x,y,f):
    #  return f(x) + f(y)
#
#  print(ho_func(-1,-5,abs))

#map==
#  map(function,Interable factor) map(abs,[-1,-2,-3,-4]

#  test = input("input string:")
#
#  def str2int(in_str):
    #  d = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
    #  def up_digi(x,y):
        #  return x * 10 + y
#
    #  def cha2num(n):
        #  return d[n]
#
    #  return reduce(up_digi, map(cha2num, in_str))
#
#  print(str2int(test)*10)

#A1:
name_list = ["adam","LISA","barT"]

def normalize(name):
    def rename (n):
        return (n.lower()).capitalize()
    return map(rename,name)

print(list(normalize(name_list)))

#A2:
test_list = [3,5,7,9]

def prod(num_list):
    def times(x,y):
        return x * y
    return reduce(times,num_list)

print(prod(test_list))

#A3:
test_list2 = "123.456"

def str2float(origin):
    def char2num(n):
        if n == ".":
            return n
        else:
            return int(n)

    def calc(x,y):
        if y == ".":
            return x
        else:
            return x * 10 + y
    
    dot_pos = origin.find(".")
    return reduce(calc,map(char2num,origin))*pow(10,-(dot_pos))

print(str2float(test_list2))
