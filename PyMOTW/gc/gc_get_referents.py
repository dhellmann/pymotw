#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Show the objects with references to a given object.
"""
#end_pymotw_header

import gc
import pprint

class Graph(object):
    def __init__(self, name):
        self.name = name
        self.next = None
    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, self.name)

one = Graph('one')
two = Graph('two')
three = Graph('three')
one.next = two
two.next = three
three.next = one

for r in gc.get_referents(three):
    pprint.pprint(r)
