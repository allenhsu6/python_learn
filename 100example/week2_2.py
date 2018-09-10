#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
1.定义函数countchar()按字母表顺序统计字符串中26个字母出现的次数（不区分大小写）。例如字符串“Hope is a good thing.”的统计结果为：
[1, 0, 0, 1, 1, 0, 2, 2, 2, 0, 0, 0, 0, 1, 3, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0]

"""

# def countchar(s):
#     lst = [0] * 26
#     for i in range(len(s)):
#         if 'a' <= s[i] <= 'z':
#             lst[ord(s[i])- ord('a')] += 1
#     print(lst)
#
# # 测试函数的入口
# if __name__ == "__main__":
#     s = "Hope is a good thing."
#     s = s.lower()
#     countchar(s)


def countchar(s):
    s = s.lower()
    lst = [0]*26
    for i in range(len(s)):
        if 'a' <= s[i] <= 'z':
            lst[ord(s[i]) - ord('a')] += 1
    print(lst)

if __name__ ==  "__main__":
    s = input()
    countchar(s)


