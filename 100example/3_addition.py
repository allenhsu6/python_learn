#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
经典程序设计问题：找第n个默尼森数。P是素数且M也是素数，并且满足等式M=2**P-1，则称M为默尼森数。
例如，P=5，M=2**P-1=31，5和31都是素数，因此31是默尼森数
求第六个莫尼森数
"""
import math
from math import sqrt


def isprime(n):
    while n > 1:
        k = int(sqrt(n))
        i = 2
        while i <= k:
            if n % i == 0:
                return 0
            i += 1
        else:
            return 1


def monisen(s):
    P = 1
    while s != 0:
        if isprime(P):
            m = math.pow(2, P) - 1
            if isprime(m):
                s -= 1
                if s == 0:
                    return m
        P += 1


print(monisen(6))
