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

response = EasyDialogs.AskString('What is your favorite color?', default='blue')
print 'RESPONSE:', response