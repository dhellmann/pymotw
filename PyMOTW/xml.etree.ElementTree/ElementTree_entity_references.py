#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann.  All rights reserved.
#
"""Dump the OPML in plain text
"""
#end_pymotw_header

from xml.etree import ElementTree

with open('data.xml', 'rt') as f:
    tree = ElementTree.parse(f)

node = tree.find('entity_expansion')
print 'Entity in attribute:', node.attrib['attribute']
print 'Entity in text     :', node.text
