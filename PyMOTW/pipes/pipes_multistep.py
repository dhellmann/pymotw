#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""
#end_pymotw_header

import pipes
import pprint
import tempfile

p = pipes.Template()
p.append('cd "$WORKON_HOME"; for f in */bin/activate; do echo $f; done', '--')
p.append(r"sed 's|^\./||'", '--')
p.append("sed 's|/bin/activate||'", '--')
p.append('sort', '--')

t = tempfile.NamedTemporaryFile('r')

f = p.open(t.name, 'r')
try:
    sandboxes = [ l.strip() for l in f.readlines() ]
finally:
    f.close()

print 'SANDBOXES:'
pprint.pprint(sandboxes)
