#!/usr/bin/env python
# -*- coding: utf-8 -*-

class animal(object):
    def eat():
        print("animal is eating")

class dog(animal):
    def bark(self):
        print("bark bark")

class cat(animal):
    def meow(self):
        print("meow meow")

a = cat()
a.meow()
b = dog()
b.bark
#  print(dir(cat()))

print(hasattr(cat,"meow"))
print(hasattr(cat,"bark"))
#  setattr(cat,"bark","bark bark")
#  print(hasattr(cat,"bark"))
#  print(getattr(cat,"bark"))
print(getattr(cat,"shit","cat do not shit"))

setattr(b,"bark",a.meow)
b.bark()
