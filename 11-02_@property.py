#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  class student(object):
    #  def __init__(self,name):
        #  self.__name = name
#
    #  def set_score(self,value):
        #  if not isinstance(value,int):
            #  raise ValueError("ERROR")
        #  if value < 0 or value > 100:
            #  raise ValueError("out of range")
        #  self.__score = value
#
    #  def get_score(self):
        #  return self.__score
#
#  jack = student("Jack")
#  jack.set_score(99)
#  print(jack.get_score())

#  class student(object):
#
    #  @property
    #  def birth(self):
        #  return self._birth
#
    #  @birth.setter
    #  def birth(self,value):
        #  self._birth = value
#
    #  @property
    #  def age(self):
        #  return 2020 - self._birth
#
#  james = student()
#  james.birth = 1994
#  print(james.age)

#ex

class screen(object):
    
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self,value_w):
        self.__width = value_w

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self,value_h):
        self.__height = value_h

    @property
    def resolution(self):
        return self.__width * self.__height


a = screen()
a.width = 1024
a.height = 768
print(a.resolution)
