#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
输入某年某月某日，判断这一天是这一年的第几天？
"""
year = int(input("请输入年："))
month = int(input("请输入月："))
day = int(input("请输入日："))

# 定义为元组，因为下面是不可变
months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0 < month <= 12:
    days = months[month-1] + day
else:
    print("错误的月份输入")
    # 下面就算是后面的判断项不加括号，依旧可行，因为从左到右判断
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    if month > 2:
        days += 1
print(days)


