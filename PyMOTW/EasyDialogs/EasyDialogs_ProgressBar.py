#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"
#end_pymotw_header

import EasyDialogs
import time

meter = EasyDialogs.ProgressBar('Making progress...',
                                maxval=10,
                                label='Starting',
                                )
for i in xrange(1, 11):
    phase = 'Phase %d' % i
    print phase
    meter.label(phase)
    meter.inc()
    time.sleep(1)
print 'Done with loop'
time.sleep(1)

del meter
print 'The dialog should be gone now'

time.sleep(1)
