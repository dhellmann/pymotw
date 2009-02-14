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

gid = os.getgid()
group_info = grp.getgrgid(gid)
print 'Currently running with GID=%s name=%s' % (gid, group_info.gr_name)
