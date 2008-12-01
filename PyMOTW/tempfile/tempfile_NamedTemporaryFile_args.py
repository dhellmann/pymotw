#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"
#end_pymotw_header

import tempfile

temp = tempfile.NamedTemporaryFile(suffix='_suffix', 
                                   prefix='prefix_', 
                                   dir='/tmp',
                                   )
try:
    print 'temp:', temp
    print 'temp.name:', temp.name
finally:
    temp.close()