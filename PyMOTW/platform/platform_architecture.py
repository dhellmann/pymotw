#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"

import platform

print 'interpreter:', platform.architecture()
print '/bin/ls    :', platform.architecture('/bin/ls')