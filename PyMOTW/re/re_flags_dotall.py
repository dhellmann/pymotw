#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Matching newlines in multiline input
"""
#end_pymotw_header

import re

text = 'This is some text -- with punctuation.\nAnd a second line.'
pattern = r'.+'
no_newlines = re.compile(pattern)
dotall = re.compile(pattern, re.DOTALL)

print 'Text        :', repr(text)
print 'Pattern     :', pattern
print 'No newlines :', no_newlines.findall(text)
print 'Dotall      :', dotall.findall(text)

