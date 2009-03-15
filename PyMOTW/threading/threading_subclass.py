#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Subclassing Thread to create your own thread types.
"""
#end_pymotw_header

import threading

class MyThread(threading.Thread):

    def run(self):
        print 'MyThread:', self.getName()
        return

for i in range(5):
    t = MyThread()
    t.start()
