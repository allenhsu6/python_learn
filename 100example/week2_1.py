#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
从豆瓣上截取一部分短评，并统计有用总数
我清楚的意识到下一步就是数据可视化
"""
import requests
from bs4 import BeautifulSoup
import re

sum = 0   # star总数
command_num = 0
count = 0
i = 0
while count < 50:
    r = requests.get('https://book.douban.com/subject/30259720/comments/hot?p=' + str(i + 1))  # 短评页面
    soup = BeautifulSoup(r.text, 'html.parser')  # soup解析
    pattern = soup.find_all('span', 'short')
    for item in pattern:
        print(item.string)
        count += 1
    pattern_s = re.compile('<span class="user-stars allstar(.*?) rating"')
    p = re.findall(pattern_s, r.text)
    for star in p:
        sum += int(star)
        command_num += 1
print(sum)
print(command_num)

print('评论数：'+str(count))
print(sum/command_num)