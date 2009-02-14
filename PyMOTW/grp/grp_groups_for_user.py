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

username = 'dhellmann'
groups = [g.gr_name for g in grp.getgrall() if username in g.gr_mem]
print username, 'belongs to:', ', '.join(groups)
