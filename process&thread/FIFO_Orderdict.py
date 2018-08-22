#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import base64

# 实现安全解码，把转码丢掉的=再补回来
def safe_base64_decodes(s):
    if len(s) % 4 == 0:
        return base64.b64decode(s)
    else:
        b_str = (str(s, 'utf-8'))
        b_str = b_str + '='
        return safe_base64_decodes(bytes(b_str, encoding='utf-8'))
