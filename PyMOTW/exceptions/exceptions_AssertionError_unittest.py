#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"
#end_pymotw_header

import unittest

class AssertionExample(unittest.TestCase):
    
    def test(self):
        self.failUnless(False)

unittest.main()
