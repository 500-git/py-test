#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  class Hello(object):
    #  def inside(self,name = "World"):
        #  print("Hello {0}".format(name))
#
#  h = Hello()
#  h.inside
#
#  print("type(Hello): ",type(Hello))
#  print("type(h): ",type(h)))

#  def fn(self,name = "World"):
    #  print("Hello {0}".format(name))
#
#  Hello = type("Hello",(object,),dict(hello = fn))
#  h = Hello()
#  h.hello
#  print(type(Hello))
#  print(type(h))

#  class ListMetaclass(type):
    #  def __new__(cls,name,bases,attrs):
        #  attrs["add"] = lambda self,value:self.append(value)
        #  return type.__new__(cls,name,bases,attrs)
#
#  class MyList(list, metaclass = ListMetaclass):
    #  pass
#
#  lst = MyList()
#  lst.add("test1")
#  print(lst[0])

class User(Model):

    id = IntegerField("id")
    name = StringField("username")
    email = StringField("email")
    pw = StringField("password")

u = User(id = "12345",name = "Michael", email = "123@123.com",pw = "password")
u.save()

class Field(object):
    def __init__(self,name,column_type):
        self.name = name
        self.column_type = column_type

        def __str__(self):
            return("{0}:{1}".format(self.__class__.name,self.name))

class IntegerField(Field):
    def __init__(self,name):
        super(StringField,self).__init__(name,"varchar(100)")

class IntegerField(Field):
    def __init__(self,name):
        super(IntegerField,self).__init__(name,"bright")


