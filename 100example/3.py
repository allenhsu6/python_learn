#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
"""
from math import sqrt

for i in range(1, 168):
    if i ** 2 - 168 > 0:
        a = int(sqrt(i ** 2 - 168))
        if a ** 2 == i ** 2 - 168:
            print(i ** 2 - 268)
