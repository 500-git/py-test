#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections.abc import Iterable,Iterator

print("list [] is iterable --",isinstance([],Iterable))
print("tuple {} is iterable --",isinstance({},Iterable))
print("string is iterable --",isinstance("ABC",Iterable))
print("123(int) is iterable --",isinstance(123,Iterable))

print("generator is iterator --",isinstance((x for x in range(1,11)),Iterator))
print("list [] is iterator --",isinstance([],Iterator))
print("tuple is iterator --",isinstance({},Iterator))
print("stirng is iterator --",isinstance("ABC",Iterator))

#  for x in lst_1:
    #  print(x)

iter_1 =iter([1,2,3,4])
print(isinstance(iter_1,Iterable))
print(isinstance(iter_1,Iterator))
