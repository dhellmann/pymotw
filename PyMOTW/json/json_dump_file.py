#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""
#end_pymotw_header

import json
import tempfile

data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]

f = tempfile.NamedTemporaryFile(mode='w+')
json.dump(data, f)
f.flush()

print open(f.name, 'r').read()

