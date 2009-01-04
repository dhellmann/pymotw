#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"
#end_pymotw_header

import bz2

input_file = bz2.BZ2File('example.txt.bz2', 'rb')
try:
    print input_file.read()
finally:
    input_file.close()
