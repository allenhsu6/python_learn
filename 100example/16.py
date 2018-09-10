#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = input('请输入一个字符串:\n')
letters = 0
space = 0
digit = 0
others = 0
i = 0
while i < len(s):
    a = s[i]
    i += 1
    if a.isalpha():
        letters += 1
    elif a.isspace():
        space += 1
    elif a.isdigit():
        digit += 1
    else:
        others += 1
print('letter = %d, \t space = %d digit = %d, others = %d' %(letters,space,digit,others))