#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"
#end_pymotw_header

import tarfile

print 'creating archive'
out = tarfile.open('tarfile_append.tar', mode='w')
try:
    out.add('README.txt')
finally:
    out.close()

print 'contents:', [m.name 
                    for m in tarfile.open('tarfile_append.tar', 'r').getmembers()]

print 'adding index.rst'
out = tarfile.open('tarfile_append.tar', mode='a')
try:
    out.add('index.rst')
finally:
    out.close()

print 'contents:', [m.name 
                    for m in tarfile.open('tarfile_append.tar', 'r').getmembers()]
