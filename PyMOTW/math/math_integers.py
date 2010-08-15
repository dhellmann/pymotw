#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Converting floats to ints.
"""
#end_pymotw_header

import math

print '{:^5}  {:^5}  {:^5}  {:^5}  {:^5}'.format('i', 'int', 'trunk', 'floor', 'ceil')
print '{:-^5}  {:-^5}  {:-^5}  {:-^5}  {:-^5}'.format('', '', '', '', '')

fmt = '  '.join(['{:5.1f}'] * 5)

for i in [ -1.5, -0.8, -0.5, -0.2, 0, 0.2, 0.5, 0.8, 1 ]:
    print fmt.format(i, int(i), math.trunc(i), math.floor(i), math.ceil(i))
    
