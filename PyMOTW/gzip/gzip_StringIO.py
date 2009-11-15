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
from cStringIO import StringIO
import binascii

uncompressed_data = 'The same line, over and over.\n' * 10
print 'UNCOMPRESSED:', len(uncompressed_data)
print uncompressed_data

buf = StringIO()
f = gzip.GzipFile(mode='wb', fileobj=buf)
try:
    f.write(uncompressed_data)
finally:
    f.close()

compressed_data = buf.getvalue()
print 'COMPRESSED:', len(compressed_data)
print binascii.hexlify(compressed_data)

inbuffer = StringIO(compressed_data)
f = gzip.GzipFile(mode='rb', fileobj=inbuffer)
try:
    reread_data = f.read(len(uncompressed_data))
finally:
    f.close()

print
print 'RE-READ:', len(reread_data)
print reread_data
