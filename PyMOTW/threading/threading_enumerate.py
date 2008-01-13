#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Using enumerate() to find the active threads.
"""

__version__ = "$Id$"

import random
import threading
import time

def worker():
    """thread worker function"""
    t = threading.currentThread()
    pause = random.randint(1,5)
    print 'Starting:', t.getName(), 'sleeping', pause
    time.sleep(pause)
    print 'Ending  :', t.getName()
    return

for i in range(3):
    t = threading.Thread(target=worker)
    t.setDaemon(True)
    t.start()

main_thread = threading.currentThread()
for t in threading.enumerate():
    if t is main_thread:
        continue
    print 'Joining :', t.getName()
    t.join()
