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
from cStringIO import StringIO

data = 'This is the data to write to the archive.'

out = tarfile.open('tarfile_addfile_string.tar', mode='w')
try:
    info = tarfile.TarInfo('made_up_file.txt')
    info.size = len(data)
    out.addfile(info, StringIO(data))
finally:
    out.close()

print
print 'Contents:'
t = tarfile.open('tarfile_addfile_string.tar', 'r')
for member_info in t.getmembers():
    print member_info.name
    f = t.extractfile(member_info)
    print f.read()
