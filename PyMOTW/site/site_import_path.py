#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""The default import path from site
"""
#end_pymotw_header

import sys
import os
import platform

if 'Windows' in platform.platform():
    SUFFIXES = [
        '',
        'lib/site-packages',
        ]
else:
    SUFFIXES = [
        'lib/python2.6/site-packages',
        'lib/site-python',
        ]

print 'Path prefixes:'
print '   sys.prefix     :', sys.prefix
print '   sys.exec_prefix:', sys.exec_prefix

for prefix in sorted(set([ sys.prefix, sys.exec_prefix ])):
    print
    for suffix in SUFFIXES:
        path = os.path.join(prefix, suffix).rstrip(os.sep)
        print path
        print '   exists:', os.path.exists(path)
        print '  in path:', path in sys.path
