#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"

import string

for n in dir(string):
    if n.startswith('_'):
        continue
    v = getattr(string, n)
    if isinstance(v, basestring):
        print '%s=%s' % (n, repr(v))
        print