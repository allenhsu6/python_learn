#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
local_school = threading.local()

def get_student():
    std = local_school.student
    print('%s in %s' % (std, threading.current_thread().name))

def process_thread(name):
    local_school.student = name
    get_student()

t1 = threading.Thread(target=process_thread, args=('hsu',), name='怀仁一中' )
t3 = threading.Thread(target=process_thread, args=('hsu',), name='怀仁一中' )

t2 = threading.Thread(target=process_thread, args=('allen',), name='卡内基梅隆')
t1.start()
t2.start()
t3.start()
t3.join()
t1.join()
t2.join()
