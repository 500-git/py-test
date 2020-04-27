#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  gene = (pow(x,2) for x in range(1,11))
#
#  for n in gene:
    #  print(n)

#  n = int(input("n:"))
#
#  def fib (n):
    #  a,b = 1,1
    #  x = 0
    #  while x < n:
         #  yield(a)
         #  a,b =  b,a + b
         #  x += 1
    #  return "END"

#print(fib(n))
#  fib_gen = fib(n)

#  for i in fib(n):
    #  print(next(fib_gen))

#  while 1:
    #  try:
        #  print(next(fib_gen))
    #  except StopIteration as err:
        #  print(err.value)
        #  break

 #testl = [1,2,3,4]

def tri(n):
    lst = [1]
    while n >= 1:
        yield(lst)
        lst = [1] + [lst[i] + lst[i + 1] for i in range(len(lst)-1)] + [1]
        n -= 1  

tri_gen = tri(5)
for x in tri(5):
    print(next(tri_gen))

