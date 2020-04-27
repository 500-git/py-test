#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

import os

lst1 = [pow(x,2) for x in range(1,11)]
print(lst1)

lst2 = [pow(x,2) for x in range(1,11) if x % 2 == 0]
print(lst2)

lst3 = [m + n for m in "ABC" for n in "123"]
print(lst3)

lstd = [d for d in os.listdir('.')]
print(lstd)

#  os.chmod('./01-01.py',777)

dict1 = {"A":"a","B":"b","C":"c"}
print(dict1)

lst4 = [key + "--" + value for key,value in dict1.items()]
print(lst4)

L1 = ["Hello","World",18,"Apple",None]

L2 = [x.lower() for x in L1 if isinstance(x,str)]
print(L2)
