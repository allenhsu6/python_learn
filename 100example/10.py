#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
暂停一秒输出，并格式化当前时间。
"""

import time
a = time.localtime(time.time())
print(a)
print(time.asctime(a))
time.sleep(1)
print(time.asctime(time.localtime(time.time())))
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
