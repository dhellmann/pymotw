#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"
#end_pymotw_header

import anydbm

db = anydbm.open('/tmp/example.db', 'w')
try:
    db[1] = 'one'
finally:
    db.close()