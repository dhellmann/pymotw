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
    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, self.name)

one = Graph('one')
two = Graph('two')
three = Graph('three')
one.next = two
two.next = three
three.next = one

seen = set()
to_process = Queue.Queue()

# Start with an empty object chain and Graph three.
to_process.put( ([], three) )

# Look for cycles, building the object chain for each object we find
# in the queue so we can print the full cycle when we're done.
while not to_process.empty():
    chain, next = to_process.get()
    chain = chain[:]
    chain.append(next)
    print 'Examining:', repr(next)
    seen.add(id(next))
    for r in gc.get_referents(next):
        if isinstance(r, basestring) or isinstance(r, type):
            # Ignore strings and classes
            pass
        elif id(r) in seen:
            print 'Found a cycle to %s:' % r
            for i, link in enumerate(chain):
                print '  %d: ' % i,
                pprint.pprint(link)
        else:
            to_process.put( (chain, r) )
            
