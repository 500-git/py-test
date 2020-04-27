#!/usr/bin/env python
# -*- coding: utf-8 -*-
#factorial==
def fact(n,sum_n=1):
    res = sum_n
    while n > 1:
        res *= n
        n -=1
    return n,res

a = input("fact num:")
result = fact(int(a))
print(result[-1])

#hanoi==

def hanoi(n,fm,bf,to):
    if n == 1:
        print("move No.{0} {1} ==> {2}".format(1,fm,to))
    else:
        hanoi(n - 1,fm,to,bf)
       # hanoi(1,fm,bf,to)
        print("move No.{0} {1} ==> {2}".format(n,fm,to))
        hanoi(n - 1,bf,fm,to)

num = input("input layer:")
hanoi(int(num),"a","b","c")
