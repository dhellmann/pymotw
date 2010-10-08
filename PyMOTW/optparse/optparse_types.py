#!/usr/bin/env python
#
# Copyright 2010 Doug Hellmann.
#
"""Type conversions
"""

__module_id__ = "$Id$"
#end_pymotw_header

import optparse

parser = optparse.OptionParser()
parser.add_option('-i', action="store", type="int")
parser.add_option('-f', action="store", type="float")
parser.add_option('-l', action="store", type="long")
parser.add_option('-c', action="store", type="complex")

options, args = parser.parse_args()

print 'int    : %-16r %s' % (type(options.i), options.i)
print 'float  : %-16r %s' % (type(options.f), options.f)
print 'long   : %-16r %s' % (type(options.l), options.l)
print 'complex: %-16r %s' % (type(options.c), options.c)
