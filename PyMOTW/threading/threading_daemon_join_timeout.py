#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Timing out join() for busy daemon threads
"""

__version__ = "$Id$"

import threading
import time

def daemon():
    print 'Starting:', threading.currentThread().getName()
    time.sleep(2)
    print 'Exiting :', threading.currentThread().getName()

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print 'Starting:', threading.currentThread().getName()
    print 'Exiting :', threading.currentThread().getName()

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join(1)
print 'd.isAlive()', d.isAlive()
t.join()
