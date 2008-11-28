#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Expand tilde in filenames.
"""

__version__ = "$Id$"
#end_pymotw_header

import os.path

for user in [ '', 'dhellmann', 'postgres' ]:
    lookup = '~' + user
    print lookup, ':', os.path.expanduser(lookup)
