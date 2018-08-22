#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
print(s.recv(1024))
for data in [b'xuzhi', b'allen', b'hsu']:
    s.send(data)
    print(s.recv(1024))
s.send(b'exit')
s.close()
