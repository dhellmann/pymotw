#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"
#end_pymotw_header

import gzip

input = gzip.open('example.txt.gz', 'rb')
try:
    print input.read()
finally:
    input.close()
