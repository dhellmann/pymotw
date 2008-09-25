#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"
#end_pymotw_header

import EasyDialogs
import string

default = string.ascii_letters * 10
print 'len(default)=', len(default)
response = EasyDialogs.AskString('Enter a long string', default=default)
print 'len(response)=', len(response)
