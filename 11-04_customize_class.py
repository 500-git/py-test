#!/usr/bin/env python
# -*- coding: utf-8 -*-

class student(object):
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return ("student type (name:{0})".format(self.name))

    __repr__ = __str__

mike = student("Mike")
print(mike)

#  class fib(object):
    #  def __init__(self):
        #  self.a, self.b = 0, 1
#
    #  def __iter__(self):
        #  return self
#
    #  def __next__(self):
        #  self.a, self.b = self.b, self.a + self.b
        #  if self.a > 20:
            #  raise StopIteration()
        #  return self.a
    #  def __getitem__(self):
#
#  for n in fib():
    #  print(n)

#  class chain_path(object):
    #  def __init__(self,path="~"):
        #  self.__path = path
#
    #  def __getattr__(self,path):
        #  return chain_path("{0}/{1}".format(self.__path,path))
#
    #  def __str__(self):
        #  return self.__path
#
#  print(chain_path().user.test.test1)

class chain_user(object):
    def __init__(self,path=""):
        self.__path = path

    def user(self,username):
        return chain_user("/user:{0}".format(username))

    def __getattr__(self,path):
            return chain_user("{0}/{1}".format(self.__path,path))
    
    def __str__(self):
        return self.__path
    def __call__(self):
        print("This is a __call__ test")

print(chain_user().user("michael").repos.test)
print(callable(chain_user))
