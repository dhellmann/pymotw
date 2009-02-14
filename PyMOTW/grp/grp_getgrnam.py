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

name = 'admin'
info = grp.getgrnam(name)
print 'Name    :', info.gr_name
print 'GID     :', info.gr_gid
print 'Password:', info.gr_passwd
print 'Members :', ', '.join(info.gr_mem)