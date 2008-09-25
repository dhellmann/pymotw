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

response = EasyDialogs.AskPassword('Password:', default='s3cr3t')
print 'Shh!:', response
