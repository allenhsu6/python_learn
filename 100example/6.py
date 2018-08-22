#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
斐波那契数列
分析： 递归中核心是出口，出口一定要定义明白
"""


def fibonacci(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibonacci(n-1) + fibonacci(n - 2)

print(fibonacci(3))
