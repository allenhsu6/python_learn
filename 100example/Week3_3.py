#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
"""
词频统计
"""

# 第一种方法ß
import collections
import copy
s = "我 是 一个 测试 句子 ， 大家 赶快 来 统计 我 吧 ， 大家 赶快 来 统计 我 吧，大家 赶快 来 统计 我 吧 ， 重要 事情 说 三遍 ！"
s_split = s.split(' ')
s_split_backup = copy.deepcopy(s_split)
[s_split.remove(item) for item in s_split if item in '， 。! “ ”']
print('第一种方法：%s'  %(collections.Counter(s_split)))

# 用字典实现第二种方法
s_dict = {}
for item in s_split:
    if item not in '， 。! “ ”':
        if item not in s_dict:
            s_dict[item] = 1
        else: s_dict[item] += 1

print('第二种方法：%s'  % sorted(s_dict.items(), key=lambda item:item[1],reverse=True))
