#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"
#end_pymotw_header

import array

a = array.array('i', xrange(5))
print 'Initial :', a

a.extend(xrange(5))
print 'Extended:', a

print 'Slice   :', a[3:6]

print 'Iterator:', list(enumerate(a))