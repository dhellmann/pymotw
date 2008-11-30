#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"
#end_pymotw_header

import signal
import time
import threading

def signal_handler(num, stack):
    print time.ctime(), 'Alarm in', threading.currentThread()

signal.signal(signal.SIGALRM, signal_handler)

def use_alarm():
    print time.ctime(), 'Setting alarm in', threading.currentThread()
    signal.alarm(1)
    print time.ctime(), 'Sleeping in', threading.currentThread()
    time.sleep(3)
    print time.ctime(), 'Done with sleep'

# Start a thread that will not receive the signal
alarm_thread = threading.Thread(target=use_alarm, name='alarm_thread')
alarm_thread.start()
time.sleep(0.1)

# Wait for the thread to see the signal (not going to happen!)
print time.ctime(), 'Waiting for', alarm_thread
alarm_thread.join()

print time.ctime(), 'Exiting normally'