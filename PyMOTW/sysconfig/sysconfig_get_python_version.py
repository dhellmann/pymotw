#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""The Python interpreter version
"""
#end_pymotw_header

import sysconfig
import sys

print 'sysconfig.get_python_version() =>', sysconfig.get_python_version()
print 'sys.version_info =>', sys.version_info
