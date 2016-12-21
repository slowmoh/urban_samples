# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 11:53:13 2016

@author: Ben
"""

import threading
from queue import Queue
import time

# locker
print_lock = threading.Lock()

# defining a job for the thread
def exampleJob(worker):
    time.sleep(0.5)
    with print_lock:
        print(threading.current_thread().name,worker)

# thread things
def threader():
    while True:
        worker = q.get()
        exampleJob(worker)
        q.task_done()
    

q = Queue()
# create 10 threads
for x in range(10):
    t = threading.Thread(target = threader)
    t.daemon = True
    t.start()
    
start = time.time()
# 20 jobs/task
for worker in range(20):
    q.put(worker)    
q.join()

print('Entire job took:', time.time()-start)


    