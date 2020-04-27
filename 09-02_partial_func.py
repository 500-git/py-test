#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools

def test(x,y=1):
    return x + y

print(4)

test2 = functools.partial(test,y = 2)
print(test2(6))
print(test2(2, y = 3))
