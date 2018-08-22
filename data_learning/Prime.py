#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt
i = 2
while i <= 100:
    k = sqrt(i)
    j = 2
    while j <= k:
        if i % j == 0:
            break
        else:
            j = j + 1
    # 如果没有break执行，我们在while后悔执行else语句
    else:
        print(i, end=' ')
    i = i+1



