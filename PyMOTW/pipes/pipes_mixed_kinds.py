#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""
#end_pymotw_header

import pipes
import tempfile

p = pipes.Template()
p.append('cat $IN', 'f-')
p.append('cat - > $OUT', '-f')
p.debug(True)

t = tempfile.NamedTemporaryFile('r')
f = p.open(t.name, 'w')
try:
    f.write('Some text')
finally:
    f.close()

t.seek(0)
print t.read()
t.close()
