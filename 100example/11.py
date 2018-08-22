#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，
因为153=1的三次方＋5的三次方＋3的三次方。

"""

for i in range(100,1000):
    a = i // 100
    b = (i - a * 100) // 10
    c = i - a * 100 - b * 10
    d = a**3 + b**3 + c**3
    if d == i:
        print(i)