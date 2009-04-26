#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Multiple concurrent access to a resource
"""
#end_pymotw_header
import logging
import random
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s (%(threadName)-2s) %(message)s',
                    )

class ActivePool(object):
    def __init__(self):
        super(ActivePool, self).__init__()
        self.active = []
        self.lock = threading.Lock()
    def makeActive(self, name):
        with self.lock:
            self.active.append(name)
    def makeInactive(self, name):
        with self.lock:
            self.active.remove(name)
    def __str__(self):
        with self.lock:
            return str(self.active)

def worker(s, pool):
    with s:
        name = threading.currentThread().getName()
        pool.makeActive(name)
        logging.debug('Running: %s', str(pool))
        time.sleep(random.random())
        pool.makeInactive(name)

pool = ActivePool()
s = threading.Semaphore(5)
for i in range(20):
    t = threading.Thread(target=worker, name=str(i), args=(s, pool))
    t.start()
