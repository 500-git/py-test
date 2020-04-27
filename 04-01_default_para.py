#!/usr/bin/env python
# -*- coding: utf-8 -*-

#default parameter

def para(x,y,z=1):
    if not isinstance(x,(int,float))&isinstance(y,(int,float)):
        raise TypeError("ERROR TYPE")
    a = x+y+z
    b = x-y+z
    print("x{0} y{1} z{2} a{3} b{4}".format(x,y,z,a,b))

c = para(1,2)
c = para(1,2,3)

def add_end(L=None):
    if L==None:
        L.append("END")
    elif L==["END"]:
        pass
    else:
        L.append("END")

    print(L)

lst1=[1,2,3]
print(lst1)
add_end(lst1)
lst2=["END"]
add_end(lst2)
lst3=[]
add_end(lst3)

#print(lst1[-1])


