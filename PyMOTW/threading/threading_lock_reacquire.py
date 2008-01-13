#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Normal locks cannot be acquired more than once, even by the same thread
"""

__version__ = "$Id$"

import threading

lock = threading.Lock()

def first():
    print 'First try:', lock.acquire()
    second()
    
def second():
    print 'Second try:', lock.acquire(0)

first()
