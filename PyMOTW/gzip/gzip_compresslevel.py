#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"
#end_pymotw_header

import gzip
import os
import hashlib

data = open('lorem.txt', 'r').read() * 1024
print 'Input contains %d bytes' % len(data)
print

print 'Level  Size        Checksum'
print '-----  ----------  ---------------------------------'

for i in xrange(1, 10):
    filename = 'compress-level-%s.gz' % i
    output = gzip.open(filename, 'wb', compresslevel=i)
    try:
        output.write(data)
    finally:
        output.close()
    size = os.stat(filename).st_size
    cksum = hashlib.md5(open(filename, 'rb').read()).hexdigest()
    print '%5d  %10d  %s' % (i, size, cksum)
