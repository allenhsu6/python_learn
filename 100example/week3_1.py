#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
主要学习字典：
创建方式：元祖中包含元组，列表中包含元组，直接创建，等号创建都可以
"""
import requests
a = {'q':'python'}
r = requests.get('https://www.google.com/search?q=python',a)
print(r.url)