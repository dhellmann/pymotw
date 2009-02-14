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
import operator

# Load all of the user data, sorted by username
all_groups = grp.getgrall()
interesting_groups = sorted((g 
                            for g in all_groups 
                            if not g.gr_name.startswith('_')),
                            key=operator.attrgetter('gr_name'))

# Find the longest length for the name
name_length = max(len(g.gr_name) for g in interesting_groups) + 1

# Print report headers
fmt = '%-*s %4s %10s %s'
print fmt % (name_length, 'Name', 
             'GID', 
             'Password',
             'Members')
print '-' * name_length, '----', '-' * 10, '-' * 30

# Print the data
for g in interesting_groups:
    print fmt % (name_length, g.gr_name, 
                 g.gr_gid, 
                 g.gr_passwd,
                 ', '.join(g.gr_mem))