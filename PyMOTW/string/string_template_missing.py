#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"

import string

values = { 'var':'foo' }

t = string.Template("$var is here but $missing is not provided")

try:
    print 'TEMPLATE:', t.substitute(values)
except KeyError, err:
    print 'ERROR:', str(err)
    
print 'TEMPLATE:', t.safe_substitute(values)