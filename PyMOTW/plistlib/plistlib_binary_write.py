#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann.  All rights reserved.
#
"""
"""
#end_pymotw_header

import plistlib

d = { 'binary_data':plistlib.Data('This data has an embedded null. \0'),
      }

print plistlib.writePlistToString(d)
