#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"
#end_pymotw_header

import pwd
import operator

# Load all of the user data, sorted by username
all_user_data = pwd.getpwall()
interesting_users = sorted((u 
                            for u in all_user_data 
                            if not u.pw_name.startswith('_')),
                            key=operator.attrgetter('pw_name'))

# Find the longest lengths for a few fields
username_length = max(len(u.pw_name) for u in interesting_users) + 1
home_length = max(len(u.pw_dir) for u in interesting_users) + 1

# Print report headers
fmt = '%-*s %4s %-*s %s'
print fmt % (username_length, 'User', 
             'UID', 
             home_length, 'Home Dir', 
             'Description')
print '-' * username_length, '----', '-' * home_length, '-' * 30

# Print the data
for u in interesting_users:
    print fmt % (username_length, u.pw_name, 
                 u.pw_uid, 
                 home_length, u.pw_dir, 
                 u.pw_gecos)