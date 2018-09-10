#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
用字典创建一个平台的用户信息（包含用户名和密码）管理系统，
新用户可以用与现有系统帐号不冲突的用户名创建帐号，已存在的老用户则可以用用户名和密码登陆重返系统
"""

system = {}
def register(name, password):
    if name in system.keys():
        print('账号名重复，请重新输入')
        begin()
    else:
        system[name] = password
        print("注册成功")
        begin()

def login(name, password):
    if name in system.keys():
        if password == system.get(name):
            print("登录成功")
    else:print("账户名或密码错误，登录失败")
    begin()

def begin():
    a = int(input())

    if a == 1:
        b = input()
        c = input()
        register(b,c)

    if a == 2:
        b = input()
        c = input()
        login(b,c)

    if a == 3:
        return




if __name__ == '__main__':
    begin()
    print(system)