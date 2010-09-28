#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Iterating over an OrderedDict
"""
#end_pymotw_header

import collections

print 'Regular dictionary:',
d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'
d1['d'] = 'D'
d1['e'] = 'E'

d2 = {}
d1['e'] = 'E'
d1['d'] = 'D'
d1['c'] = 'C'
d1['b'] = 'B'
d1['a'] = 'A'

print d1 == d2

print 'OrderedDict:',

d1 = collections.OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'
d1['c'] = 'C'
d1['d'] = 'D'
d1['e'] = 'E'

d2 = collections.OrderedDict()
d1['e'] = 'E'
d1['d'] = 'D'
d1['c'] = 'C'
d1['b'] = 'B'
d1['a'] = 'A'

print d1 == d2
