#!/usr/bin/env python
#
# Copyright 2007 Doug Hellmann.
#
"""Using optparse with single-letter options.
"""
#end_pymotw_header

import optparse

parser = optparse.OptionParser()
parser.add_option('-o', action="store")

parser.set_defaults(o='default value')

options, args = parser.parse_args()

print options.o
