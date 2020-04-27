#!/usr/bin/env python
# -*- coding: utf-8 -*-

##cut list/tuple==

#ex_1:
#  lst1 = []
#  n = 97
#  while n <= 103:
    #  lst1.append(chr(n))
    #  n += 1
#
#  print(lst1)
#  print(lst1[0])
#
#  print("No.0-No.2 {0}".format(lst1[0:3]))
#  print("0-5{0}".format(lst1[:5]))
#  print("last 5{0}".format(lst1[-5:]))
#  print("No.4-last{0}".format(lst1[3:]))
#  print("0-5,2 space{0}".format(lst1[0:5:2]))
#  print("0-second last{0}".format(lst1[0:-1]))

##ex_2:
#  def trim(lst):
    #  if lst[0] == " ":
        #  newlst = lst[1:]
        #  return trim(newlst)
    #  elif lst[-1] == " ":
        #  newlst = lst[:-1]
        #  return trim(newlst)
    #  else:
        #  newlst = lst
        #  print("".join(newlst))
#
#  str_1 = input("input string:")
#  trim(str_1)

##iter==
def min_max(lst):
    if lst != []:
        min = lst[0]
        max = lst[0] 
        for x in lst:
            if x < min:
                min = x
            elif x > max:
                max = x
        return(min,max)
    else:
        return(None,None)
a = [7,1,3,9,5,11,-1]
print(min_max(a))
b = []
print(min_max(b))
