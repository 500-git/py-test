#!/usr/bin/env python
# -*- coding: utf-8 -*-

#module test 2

__auther__ = "500"

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print("Hello World")
    elif len(args) == 2:
        print("Hello {0}".format(args))
    else:
        print("argument error")

if __name__ == "main":
    test()
