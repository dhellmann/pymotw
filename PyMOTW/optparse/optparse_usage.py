#!/usr/bin/env python
#
# Copyright 2007 Doug Hellmann.
"""Explicit usage message
"""
#end_pymotw_header

import optparse

parser = optparse.OptionParser(usage='%prog [options] <arg1> <arg2> [<arg3>...]')
parser.add_option('-a', action="store_true", default=False)
parser.add_option('-b', action="store", dest="b")
parser.add_option('-c', action="store", dest="c", type="int")

parser.parse_args()
