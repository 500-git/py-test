#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum,unique

#  week = Enum("Weekday",("Mon","Tue","Wed","Thu","Fri","Sat","Sun"))
#  day1 = week.Mon
#  print(day1)
#
#  for name,member in week.__members__.items():
    #  print(name,member,member.value)

#  @unique
#  class week_2(Enum):
    #  Sun = 0
    #  Mon = 1
    #  Tue = 2
    #  Wed = 3
    #  Thu = 4
    #  Fri = 5
    #  Sat = 6
#
#  day1 = week_2.Mon
#  print(day1)
#  print(week_2.Tue)
#  print(week_2.Fri.value)
#  print(day1 == week_2.Mon)
#  print(day1 == week_2(1))
#
#  for name,member in week_2.__members__.items():
    #  print(name,member,member.value)

class Gender(Enum):
    Male = 0
    Female = 1

class student(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

bart = student("Bart",Gender.Male)
print(bart.gender == Gender.Male)
