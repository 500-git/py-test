#!/usr/bin/env python
# -*- coding: utf-8 -*-

class student(object):
    count = 0
    def __init__(self,name):
        self.name = name
        student.count += 1


jack = student("Jack")
print(student.count)
bart = student("Bart")
print(student.count)
linda = student("Linda")
print(student.count)
