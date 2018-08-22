#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time, queue
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

print('connect to server')
m = QueueManager(address=('127.0.0.1', 5000), authkey=b'qwe')

m.connect()

task = m.get_task_queue()
result = m.get_result_queue()

for i in range(10):
    try:
        n = task.get(timeout=1)
        print('task is %d * %d' % (n, n))
        r = 'result is %d' % n * n
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task is empty')

print('worker exit')


