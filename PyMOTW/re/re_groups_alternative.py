#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Matching alternative groups
"""
#end_pymotw_header

from re_test_patterns_groups import test_patterns

test_patterns('abbaaabbbbaaaaa',
              [r'a((a+)|(b+))', # 'a' followed by a sequence of 'a' or sequence of 'b'
               r'a((a|b)+)',    # 'a' followed by a sequence of 'a' or 'b'
               ])
