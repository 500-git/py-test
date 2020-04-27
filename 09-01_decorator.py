#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools
import time
#  def log(text):
    #  def decorator(func):
       #  @functools.wraps(func)
       #  def show():
            #  print("call {0}==={1}".format(text,func.__name__))
            #  return func()
       #  return show
    #  return decorator
#
#
#  @log("something before func name")
#  def now():
    #  print("2020-04")
#
#  now()
#  print(now.__name__)

#  def  metric(fn):
    #  def inside(*args,**kw):
        #  start = time.time()
        #  x = fn(*args,**kw)
        #  end = time.time()
        #  print("{0} executed in {1} ms".format(fn.__name__,end-start))
        #  return x
    #  return inside
#
#  @metric
#  def fast(x, y):
    #  time.sleep(0.0012)
    #  return x + y;
#
#  @metric
#  def slow(x, y, z):
    #  time.sleep(0.1234)
    #  return x * y * z;
#
#  f = fast(11, 22)
#  s = slow(11, 22, 33)

#  def call_dec(func):
    #  def inside(*args,**kw):
        #  print("begin call {0}".format(func.__name__))
        #  print(func(*args,**kw))
        #  print("end call {0}".format(func.__name__))
    #  return inside
#
#  @call_dec
#  def test(x,y):
    #  return x + y
#
#  test(1,19)

def log(*args):
    def inside(func):
        if args != ():
            print("call {0} {1}".format(args[0],func.__name__))
        else:
            print("call {0}".format(func.__name__))
    return inside

@log()
def f():
    pass
