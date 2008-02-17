#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Locking via the 'with' statement
"""



from __future__ import with_statement
import threading

__version__ = "$Id$"

def worker_with(lock):
    with lock:
        print 'Lock acquired via with'
        
def worker_no_with(lock):
    lock.acquire()
    try:
        print 'Lock acquired directly'
    finally:
        lock.release()

lock = threading.Lock()
w = threading.Thread(target=worker_with, args=(lock,))
nw = threading.Thread(target=worker_no_with, args=(lock,))

w.start()
nw.start()