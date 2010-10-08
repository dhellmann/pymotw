#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Boolean flags.
"""
#end_pymotw_header

import optparse

parser = optparse.OptionParser()
parser.add_option('-t', action='store_true', default=False, dest='flag')
parser.add_option('-f', action='store_false', default=False, dest='flag')

options, args = parser.parse_args()

print 'Flag:', options.flag


