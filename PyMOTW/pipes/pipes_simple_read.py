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

# Establish a very simple pipeline using stdio
p = pipes.Template()
p.append('cat -', '--')
p.debug(True)

# Establish an input file
t = tempfile.NamedTemporaryFile(mode='w')
t.write('Some text')
t.flush()

# Pass some text through the pipeline,
# saving the output to a temporary file.
f = p.open(t.name, 'r')
try:
    contents = f.read()
finally:
    f.close()

print contents
