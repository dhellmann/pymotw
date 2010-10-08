#!/usr/bin/env python
#
# Copyright 2007 Doug Hellmann.
"""Explicit usage message
"""
#end_pymotw_header

import optparse

parser = optparse.OptionParser(usage='%prog [options] <arg1> <arg2> [<arg3>...]',
                               version='1.0',
                               )

parser.parse_args()
