#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  def creatCounter():
    #  def num():
        #  n = 0
        #  while 1:
            #  n += 1
            #  yield n
    #  nextnum = num()
    #  def counter():
        #  return next(nextnum)
    #  return counter

#  def creatCounter():
    #  x = [0]
    #  def counter():
        #  x[0] += 1
        #  return x[0]
    #  return counter

def creatCounter():
    x = 0
    def counter():
        nonlocal x
        x +=1
        return x
    return counter





ct = creatCounter()

print(ct())
print(ct())
print(ct())
print(ct())
