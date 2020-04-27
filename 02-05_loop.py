#!/usr/bin/env python
# -*- coding: utf-8 -*-

list1 = ["q","w","e","r","t","y"]

for x in list1:
    print(x,end="")
n = input("\ninput n:")

sum = 0

for x in list(range(int(n) + 1)):
    sum = sum + x
print(sum)

sum = 0
n = 0

while n <= 100:
    sum = sum + n
    n = n + 1
print(sum)

sum=0
n = 0
while n <= 100:
        sum = sum + n
        n = n+1
        if n > 50:
            break
print(sum)

