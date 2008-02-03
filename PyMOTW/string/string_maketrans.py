#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"

import string

leet = string.maketrans('abegiloprstz', '463611092572')

s = 'The quick brown fox jumped over the lazy dog.'

print s
print s.translate(leet)