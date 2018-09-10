#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
'Upgrade-Insecure-Requests': '1',
'Referer': 'http://www.weather.com.cn/textFC/db.shtml',
'Host': 'www.weather.com.cn',
}
r = requests.get('http://www.weather.com.cn/textFC/hb.shtml',headers=headers)
r.encoding='utf-8' #显式地指定网页编码，一般情况可以不用
print(r.content)
