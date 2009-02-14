#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"
#end_pymotw_header

import grp
import os
import sys

filename = 'grp_getgrgid_fileowner.py'
stat_info = os.stat(filename)
owner = grp.getgrgid(stat_info.st_gid).gr_name

print '%s is owned by %s (%s)' % (filename, owner, stat_info.st_gid)