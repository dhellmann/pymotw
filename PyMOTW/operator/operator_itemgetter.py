#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"
#end_pymotw_header

from operator import *

print 'Dictionaries:'
l = [ dict(val=i) for i in xrange(5) ]
print l
g = itemgetter('val')
vals = [ g(i) for i in l ]
print vals

print
print 'Tuples:'
l = [ (i, i*2) for i in xrange(5) ]
print l
g = itemgetter(1)
vals = [ g(i) for i in l ]
print vals
