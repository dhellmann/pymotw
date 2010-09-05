#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Repetition of patterns
"""
#end_pymotw_header

from re_test_patterns import test_patterns

test_patterns('abbaaabbbbaaaaa',
              [ '[ab]',    # either a or b
                'a[ab]+',  # a followed by one or more a or b
                'a[ab]+?', # a followed by one or more a or b, not greedy
                ])
