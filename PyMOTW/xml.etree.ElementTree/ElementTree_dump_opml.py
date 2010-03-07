#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann.  All rights reserved.
#
"""Dump the OPML in plain text
"""
#end_pymotw_header

try:
    from xml.etree import cElementTree as ElementTree
except:
    from xml.etree import ElementTree

with open('podcasts.opml', 'rt') as f:
    tree = ElementTree.parse(f)

for node in tree.getiterator():
    print node.tag, node.attrib



