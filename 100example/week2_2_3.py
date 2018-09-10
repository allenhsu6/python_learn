#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2) 在文件头部插入歌名“Blowin’ in the wind”

(3) 在歌名后插入歌手名“Bob Dylan”

(4) 在文件末尾加上字符串“1962 by Warner Bros. Inc.”

(5) 在屏幕上打印文件内容
"""
def insert_lines(lines):
    lines.insert(0, "Blowin' in the wind\n")
    lines.insert(1, "Bob Dylan\n")
    lines.append("\n1962 by Warner Bros. Inc.")
    return lines
with open('/Users/allenhsu/Desktop/Blowin in the wind', 'r+') as f:
    lines = f.readlines()
    insert_lines(lines)
    s = ''.join(lines)
    print(s)
