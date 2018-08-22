
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import queue, random
from multiprocessing.managers import BaseManager
#   启动queue
task_queue = queue.Queue()
result_queue = queue.Queue()


#   注册网络
class QueueManager(BaseManager):
    pass


# 把两个queue都注册到网络
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口，设置验证码
manager = QueueManager(address=('', 5000), authkey=b'qwe')
manager.start()

task = manager.get_task_queue()
result = manager.get_result_queue()
for i in range(10):
    n = random.randint(0, 10000)
    print('task %s is put' % n)
    task.put(n)
print('try to get the result...')
for i in range(10):
    r = result.get(timeout=10)
    print('result %s...' % r)

manager.shutdown()
print('master exit')
