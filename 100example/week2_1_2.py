#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2.	在“http://money.cnn.com/data/dow30/”上抓取道指成分股数据并将30家公司的代码、公司名称和最近一次成交价放到一个列表中输出。
主要是练习正则表达式了
"""

import requests
import re

def retrieve_dji_list():
    r = requests.get('http://money.cnn.com/data/dow30/')
    search_pattern = re.compile('class="wsod_symbol">(.*?)<\/a>.*?<span.*?">(.*?)<\/span>.*?\n.*?class="wsod_stream">(.*?)<\/span>')
    dji_list_in_text = re.findall(search_pattern, r.text)
    return dji_list_in_text

dji_list = retrieve_dji_list()
print(dji_list)