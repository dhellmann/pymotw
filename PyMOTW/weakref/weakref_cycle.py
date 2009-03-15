#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Using proxy to prevent cycles.
"""

# [[[section gc_setup]]]
import gc
from pprint import pprint
import weakref

gc.set_debug(gc.DEBUG_LEAK)

def collect_and_show_garbage():
    "Show what garbage is present."
    print 'Unreachable:', gc.collect()
    print 'Garbage:', 
    pprint(gc.garbage)
# [[[endsection]]]

# [[[section demo]]]
def demo(graph_factory):
    print 'Set up graph:'
    one = graph_factory('one')
    two = graph_factory('two')
    three = graph_factory('three')
    one.set_next(two)
    two.set_next(three)
    three.set_next(one)
    
    print
    print 'Graphs:'
    print str(one)
    print str(two)
    print str(three)
    collect_and_show_garbage()

    print
    three = None
    two = None
    print 'After 2 references removed:'
    print str(one)
    collect_and_show_garbage()

    print
    print 'Removing last reference:'
    one = None
    collect_and_show_garbage()
# [[[endsection]]]

# [[[section graph]]]
class Graph(object):
    def __init__(self, name):
        self.name = name
        self.other = None
    def set_next(self, other):
        print '%s.set_next(%s (%s))' % (self.name, other, type(other))
        self.other = other
    def all_nodes(self):
        "Generate the nodes in the graph sequence."
        yield self
        n = self.other
        while n and n.name != self.name:
            yield n
            n = n.other
        if n is self:
            yield n
        return
    def __str__(self):
        return '->'.join([n.name for n in self.all_nodes()])
    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, self.name)
    def __del__(self):
        print '(Deleting %s)' % self.name
        self.set_next(None)
# [[[endsection]]]

# [[[section without_proxy]]]
print 'WITHOUT PROXY'
print
demo(Graph)
# [[[endsection]]]

# [[[section break_cycle]]]
print
print 'BREAKING CYCLE AND CLEARING GARBAGE'
print
gc.garbage[0].set_next(None)
while gc.garbage:
    del gc.garbage[0]
collect_and_show_garbage()
# [[[endsection]]]

# [[[section with_proxy]]]
print
print 'WITH PROXY'
print

class WeakGraph(Graph):
    def set_next(self, other):
        if other is not None:
            # See if we should replace the reference
            # to other with a weakref.
            if self in other.all_nodes():
                other = weakref.proxy(other)
        super(WeakGraph, self).set_next(other)
        return
                
demo(WeakGraph)
# [[[endsection]]]
