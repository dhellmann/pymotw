#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""
#end_pymotw_header

import pickle

class Node(object):
    """A simple digraph where each node knows about the other nodes
    it leads to.
    """
    def __init__(self, name):
        self.name = name
        self.connections = []
        return

    def add_edge(self, node):
        "Create an edge between this node and the other."
        self.connections.append(node)
        return

    def __iter__(self):
        return iter(self.connections)

def preorder_traversal(root, seen=None, parent=None):
    """Generator function to yield the edges via a preorder traversal."""
    if seen is None:
        seen = set()
    yield (parent, root)
    if root in seen:
        return
    seen.add(root)
    for node in root:
        for (parent, subnode) in preorder_traversal(node, seen, root):
            yield (parent, subnode)
    return
    
def show_edges(root):
    "Print all of the edges in the graph."
    for parent, child in preorder_traversal(root):
        if not parent:
            continue
        print '%5s -> %2s (%s)' % (parent.name, child.name, id(child))

# Set up the nodes.
root = Node('root')
a = Node('a')
b = Node('b')
c = Node('c')

# Add edges between them.
root.add_edge(a)
root.add_edge(b)
a.add_edge(b)
b.add_edge(a)
b.add_edge(c)
a.add_edge(a)

print 'ORIGINAL GRAPH:'
show_edges(root)

# Pickle and unpickle the graph to create
# a new set of nodes.
dumped = pickle.dumps(root)
reloaded = pickle.loads(dumped)

print
print 'RELOADED GRAPH:'
show_edges(reloaded)