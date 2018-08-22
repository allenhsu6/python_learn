#!/usr/bin/env python3
# -*- coding: utf-8 -*-
for i in range(1, 10, 2):
    if i % 5 == 0:
        print("Bingo!")
        break
else:
    print(i)