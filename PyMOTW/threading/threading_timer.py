#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Starting a thread after an initial delay
"""

__version__ = "$Id$"

import threading
import time

def delayed():
    print 'Worker running', threading.currentThread().getName()
    return

t1 = threading.Timer(3, delayed)
t1.setName('t1')
t2 = threading.Timer(3, delayed)
t2.setName('t2')

print 'Starting timers'
t1.start()
t2.start()

print 'Waiting before canceling', t2.getName()
time.sleep(2)
print 'Canceling', t2.getName()
t2.cancel()
print 'Main thread done'