#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"
#end_pymotw_header

import filecmp

dc = filecmp.dircmp('example/dir1', 'example/dir2')
print 'Common     :', dc.common
print 'Directories:', dc.common_dirs
print 'Files      :', dc.common_files
print 'Funny      :', dc.common_funny