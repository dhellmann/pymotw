#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"

import uuid

node1 = uuid.getnode()
print hex(node1), uuid.uuid1(node1)

node2 =  0x1e5274040e
print hex(node2), uuid.uuid1(node2)