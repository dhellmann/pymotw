#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Looking at groups on a match object
"""
#end_pymotw_header

import re

text = 'This is some text -- with punctuation.'

print text
print

for pattern in [ r'^(\w+)',           # word at start of string
                 r'(\w+)\S*$',        # word at end of string, with optional punctuation
                 r'(\bt\w+)\W+(\w+)', # word starting with 't' then another word
                 r'(\w+t)\b',         # word ending with 't'
                 ]:
    regex = re.compile(pattern)
    match = regex.search(text)
    print 'Matching "%s"' % pattern
    print '  ', match.groups()
    print

