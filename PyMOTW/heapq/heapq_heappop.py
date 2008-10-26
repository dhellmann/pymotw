#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"
#end_pymotw_header

import heapq
from heapq_showtree import show_tree
from heapq_heapdata import data

print 'random    :', data
heapq.heapify(data)
print 'heapified :'
show_tree(data)
print

inorder = []
while data:
    smallest = heapq.heappop(data)
    print 'pop    %3d:' % smallest
    show_tree(data)
    inorder.append(smallest)
print 'inorder   :', inorder