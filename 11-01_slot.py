#!/usr/bin/env python
# -*- coding: utf-8 -*-

from types import MethodType

class student(object):
    __slots__ = ("name","score") #limited attribute could be import

jack = student()
jack.name = "Jack"
print(jack.name)

#  def set_age(self,age):
    #  self.age = age
#
#  jack.set_age = MethodType(set_age,jack)

#  jack.set_age(25)
#  print(jack.age)

lily = student()
lily.name = "Lily"

#  lily.set_age(24)
#  print(lily.age)

def set_score(self,score):
    self.score = score

student.set_score = set_score

lily.set_score(90)
print(lily.score)

lily.age = 24

print(lily.age)
