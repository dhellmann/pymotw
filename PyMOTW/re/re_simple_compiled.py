#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Simple pattern examples.
"""
#end_pymotw_header

import re

# Pre-compile the patterns
regexes = [ re.compile(p) for p in [ 'this',
                                     'that',
                                     ]
            ]
text = 'Does this text match the pattern?'

for regex in regexes:
    print 'Looking for "%s" in "%s" ->' % (regex.pattern, text),

    if regex.search(text):
        print 'found a match!'
    else:
        print 'no match'
