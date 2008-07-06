#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"

import xmlrpclib

server = xmlrpclib.ServerProxy('http://localhost:9000', allow_none=True)
print 'Allowed:', server.show_type(None)

server = xmlrpclib.ServerProxy('http://localhost:9000', allow_none=False)
print 'Not allowed:', server.show_type(None)
