#!/usr/bin/env python
#
# Copyright 2007 Doug Hellmann.
#
"""Printing help with optparse.  

Call this script with --help on the command line.

"""
#end_pymotw_header

import optparse

parser = optparse.OptionParser()
parser.add_option('--no-foo', action="store_true", 
                  default=False, 
                  dest="foo",
                  help="Turn off foo",
                  )
parser.add_option('--with', action="store", help="Include optional feature",
                  metavar='feature_NAME')

parser.parse_args()
