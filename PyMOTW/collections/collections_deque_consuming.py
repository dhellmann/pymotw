#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Removing items from a deque.
"""

__version__ = "$Id$"
#end_pymotw_header

import collections

print 'From the right:'
d = collections.deque('abcdefg')
while True:
    try:
        print d.pop()
    except IndexError:
        break

print '\nFrom the left:'
d = collections.deque('abcdefg')
while True:
    try:
        print d.popleft()
    except IndexError:
        break
