#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Case-insensitive matches
"""
#end_pymotw_header

import re

text = 'This is some text -- with punctuation.'
pattern = r'\bT\w+'
with_case = re.compile(pattern)
without_case = re.compile(pattern, re.IGNORECASE)

print 'Text            :', text
print 'Pattern         :', pattern
print 'Case-sensitive  :', with_case.findall(text)
print 'Case-insensitive:', without_case.findall(text)

