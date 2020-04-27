#!/usr/bin/env python
# -*- coding: utf-8 -*-

#dict==
dict1 = {"1st":1,"2nd":2,"3rd":3}
print(dict1["1st"])

dict1["1st"] = 0
print(dict1["1st"])

print("4th" in dict1)

print(dict1.get("2nd"))

dict1.pop("3rd")
print(dict1)

#set==

set1=set([1,2,3])
print(set1)
set2=set1

set1.add("this")
print(set1)

set2.add("that")
print(set2)


set2.remove(3)
print(set1,set2)

set3 = set([2,3,4])
print(set3)

print(set1&set3)
print(set1|set3)
