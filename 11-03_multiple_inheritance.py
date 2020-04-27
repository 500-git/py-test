#  !/usr/bin/env python
#  -*- coding: utf-8 -*-

class animal(object):
    def eat(self):
        print("eating...")

class mammal(animal):
    def notegg(self):
        print("do not lay eggs")

class fish(animal):
    def egg(self):
        print("laying egg...")

class runable(object):
    def run(self):
        print("running...")

class swimabel(object):
    def swim(self):
        print("swimming...")

class dog(mammal,runable):
    def bark(self):
        print("bark bark...")

class whale(mammal,swimabel):
    pass

a = dog()
a.eat()
a.bark()
a.run()

b = whale()
b.swim()
b.notegg
