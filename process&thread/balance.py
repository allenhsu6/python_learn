#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
import time
account = 0
lock = threading.Lock()

def balance(n):
    global account
    account = account + n
    account = account - n


def run_thread(n):
    for i in range(1000000):
        lock.acquire()
        try:
            balance(n)
        finally:
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(19,))
t1.start()
t2.start()
t1.join()
t2.join()
print(account)