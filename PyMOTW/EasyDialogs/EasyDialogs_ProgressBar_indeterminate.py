#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"

import EasyDialogs
import time

meter = EasyDialogs.ProgressBar(maxval=0)
for i in xrange(1, 1001):
    msg = 'Bytes: %d' % i
    meter.label(msg)
    meter.set(i)
