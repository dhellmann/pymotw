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

for filename in [ 'README.txt', 'example.tar', 
                  'bad_example.tar', 'notthere.tar' ]:
    try:
        print '%20s  %s' % (filename, tarfile.is_tarfile(filename))
    except IOError, err:
        print '%20s  %s' % (filename, err)