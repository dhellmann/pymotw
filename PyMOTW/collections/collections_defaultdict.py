#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Initializing a defaultdict.
"""

__version__ = "$Id$"

import collections

def default_factory():
    return 'default value'

d = collections.defaultdict(default_factory, foo='bar')
print d
print d['foo']
print d['bar']
