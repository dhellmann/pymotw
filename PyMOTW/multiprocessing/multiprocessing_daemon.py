#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Daemon vs. non-daemon processes.
"""
#end_pymotw_header

import multiprocessing
import time
import sys

def daemon():
    print 'Starting:', multiprocessing.current_process().name
    sys.stdout.flush()
    time.sleep(2)
    print 'Exiting :', multiprocessing.current_process().name
    sys.stdout.flush()

def non_daemon():
    print 'Starting:', multiprocessing.current_process().name
    sys.stdout.flush()
    print 'Exiting :', multiprocessing.current_process().name
    sys.stdout.flush()

if __name__ == '__main__':
    d = multiprocessing.Process(name='daemon', target=daemon)
    d.daemon = True

    n = multiprocessing.Process(name='non-daemon', target=non_daemon)
    n.daemon = False

    d.start()
    time.sleep(1)
    n.start()
