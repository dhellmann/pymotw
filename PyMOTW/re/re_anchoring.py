#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Anchoring the search
"""
#end_pymotw_header

from re_test_patterns import test_patterns

test_patterns('This is some text -- with punctuation.',
              [ r'^\w+',     # word at start of string
                r'\A\w+',    # word at start of string
                r'\w+\S*$',  # word at end of string, with optional punctuation
                r'\w+\S*\Z', # word at end of string, with optional punctuation
                r'\w*t\w*',  # word containing 't'
                r'\bt\w+',   # 't' at start of word
                r'\w+t\b',   # 't' at end of word
                r'\Bt\B',    # 't', not start or end of word
                ])
