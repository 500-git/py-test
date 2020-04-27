#!/usr/bin/env python
# -*- coding: utf-8 -*-

def is_palindrome(n):
    n_str = list(str(n))
    n_str.reverse()
    return n_str == list(str(n))

print(list(filter(is_palindrome,list(range(1,1000)))))

