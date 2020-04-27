#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  class person(object):
    #  def __init__(self,name,tel,score):
        #  self.name = name
        #  self.tel = tel
        #  self.score = score
#
    #  def show(self):
        #  print("name:{0}\ntel:{1}\nscore:{2}".format(self.name,self.tel,self.score))
#
    #  def grade(self):
        #  if self.score >= 90:
            #  return "A+"
        #  elif self.score >=80:
            #  return "A"
        #  else:
            #  return "B"
#
#
#  john = person("john smith",12345,60)
#  linda = person("linda smith",789456,90)
#
#  john.show()
#  print(linda.grade()

#private test
#  class private(object):
    #  def __init__(self,name,tel,score):
        #  self.__name = name
        #  self.__tel = tel
        #  self.__score = score
#
    #  def show(self):
        #  print("name:{0}\ntel:{1}\nscore:{2}".format(self.__name,self.__tel,self.__score))
#
#
#  tom = private("tom harris",345678,55)
#
#  tom.show()
#  tom.score = 99
#  tom.show()

#ex
class Student(object):
    def __init__(self,name,gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self,gender):
        self.__gender = gender

lily = Student("lily","male")

print(lily.get_gender())

lily.set_gender("female")
print(lily.get_gender())

