#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5
"""
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
i = 2
a = int(input())
while isprime(a) == 0:
    while a % i == 0:
        print(i)
        a = a / i
    i += 1
if a != 1:
    print(a)

