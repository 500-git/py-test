#!/usr/bin/env python
# -*- coding: utf-8 -*-

list1=['first','second','third']

print(len(list1))

list1.append("forth")

list1.insert(1,"1.5")

print(list1)

list1.pop(1)

print(list1)

list1[3]=("last")

print(list1,list1[-1])

list2=["a","b"]

list1[3]=list2

print(list1[3][1],list1,len(list1))

print(list1[-1][0])

# num=input('list num:')
