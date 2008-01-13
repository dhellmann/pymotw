#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Defaults for thread-local values
"""

__version__ = "$Id$"

import random
import threading

def show_value(data):
    print threading.currentThread().getName(), ': value=',
    try:
        print data.value
    except AttributeError:
        print 'No value yet'

def worker(data):
    show_value(data)
    data.value = random.randint(1, 100)
    show_value(data)

class MyLocal(threading.local):
    def __init__(self, value):
        print '(Initializing %s for %s)' % (id(self), threading.currentThread().getName()),
        self.value = value

local_data = MyLocal(1000)
show_value(local_data)

for i in range(2):
    t = threading.Thread(target=worker, args=(local_data,))
    t.start()
