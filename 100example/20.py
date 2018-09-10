#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
从第二次开始是两个路程
"""

h = 100
total = 0
i = 0
while i < 10:
    i += 1
    if i == 1:
        total = h + total
    else:
        total = total + 2*h
    h = h/2
print(total, h)
