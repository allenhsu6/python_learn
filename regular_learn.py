#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

re_email = re.compile(r'^\w+\.*\w+@\w+\.\w+$')
re_name = re.compile(r'^<?(\w+.*?\w+)>?.*?\w*?@\w+\.\w+$')
# re_email = re.compile(r'^([a-zA-Z]+)([\_\.]?)([0-9a-zA-Z]+)@(\w+)*(\.com)$')


def is_valid_email(addr):
    if re_email.match(addr):
        return 'great'
    else:
        return False

#  作业二用最小匹配？完美解决因为没有<>导致（）返回none问题
def is_valid_name(addr):
    g = re_name.match(addr)
    if g.groups():
        return g.group(1)
    else:
        return False


m = is_valid_email('bill.gates@microsoft.com')

name = is_valid_name('tom@voyager.org')
print(name)
