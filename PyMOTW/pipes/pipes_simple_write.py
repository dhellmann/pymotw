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

# Pass some text through the pipeline,
# saving the output to a temporary file.
t = tempfile.NamedTemporaryFile(mode='r')
f = p.open(t.name, 'w')
try:
    f.write('Some text')
finally:
    f.close()

# Rewind and read the text written
# to the temporary file
t.seek(0)
print t.read()
t.close()
