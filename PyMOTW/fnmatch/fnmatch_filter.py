#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Filter a list of filenames against a pattern.
"""

__version__ = "$Id$"
#end_pymotw_header

import fnmatch
import os

pattern = 'fnmatch_*.py'
print 'Pattern :', pattern

files = os.listdir('.')
print 'Files   :', files

print 'Matches :', fnmatch.filter(files, pattern)
