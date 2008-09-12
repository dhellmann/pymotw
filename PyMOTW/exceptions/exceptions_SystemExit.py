#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"
#end_pymotw_header

import sys

try:
    sys.exit(1)
except SystemExit, err:
    print 'Tried to exit with code', err.code
