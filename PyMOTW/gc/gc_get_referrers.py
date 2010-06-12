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
import Queue

class Graph(object):
    def __init__(self, name):
        self.name = name
        self.next = None
    def set_next(self, next):
        print '%s.next = %s' % (self, next)
        self.next = next
    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, self.name)
    def __del__(self):
        print '%s.__del__()' % self

# Construct two graph cycles
one = Graph('one')
two = Graph('two')
three = Graph('three')
one.set_next(two)
two.set_next(three)
three.set_next(one)

# Remove references to the graph nodes in this module's namespace
one = two = three = None

# Collecting now keeps the objects as uncollectable
print
print 'Collecting...'
n = gc.collect()
print 'Unreachable objects:', n
print 'Remaining Garbage:', 
pprint.pprint(gc.garbage)
print

REFERRERS_TO_IGNORE = [ locals(), globals(), gc.garbage ]

def find_referring_graphs(node):
    referrers = [r for r in gc.get_referrers(node)
                 if r not in REFERRERS_TO_IGNORE]
    for ref in referrers:
        if isinstance(ref, Graph):
            yield ref
        elif isinstance(ref, dict):
            for parent in find_referring_graphs(ref):
                yield parent

# Look for objects that refer to the objects that remain in
# gc.garbage.
for obj in gc.garbage:
    for ref in find_referring_graphs(obj):
        ref.set_next(None)

# Clear references held by gc.garbage
del gc.garbage[:]
        
# Everything should be freed this time
print
print 'Collecting...'
n = gc.collect()
print 'Unreachable objects:', n
print 'Remaining Garbage:', 
pprint.pprint(gc.garbage)
