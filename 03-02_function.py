#!/usr/bin/env python
# -*- coding: utf-8 -*-

print(abs(-1))
print(bool(0))


def sum_diff(x1,x2):
    if not isinstance(x1,(int,float))&isinstance(x2,(int,float)):
        raise TypeError("wrong type")
    # print(x1+x2)
    return x1+x2,x1-x2


a = input("x1:")
b = input("x2:")

#add(int(a),int(b))

c = sum_diff(int(a),int(b))

print(c)
print("c is {0} {1}".format(c,c))

#def empty_fuc():
#    pass
