#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import smtplib
# # 第一步 通过email模块构建text
# from email.mime.text import MIMEText
# msg = MIMEText('hello, send by Python', 'plain', 'utf-8')
#
# from_addr = input('From: ')
# password = input('Passward: ')
# to_addr = input('To: ')
# smtp_server = input('SMTP server: ')
#
# server = smtplib.SMTP(smtp_server, 25)
# server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
from email.mime.text import MIMEText

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

from_addr = input('From: ')
password = input('Password: ')
# 输入收件人地址:
to_addr = input('To: ')
# 输入SMTP服务器地址:
smtp_server = input('SMTP server: ')

import smtplib
server = smtplib.SMTP(smtp_server, 587) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
