#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"
#end_pymotw_header

import string

class MyTemplate(string.Template):
    delimiter = '%'
    idpattern = '[a-z]+_[a-z]+'

t = MyTemplate('%% %with_underscore %notunderscored')
d = { 'with_underscore':'replaced', 
      'notunderscored':'not replaced',
      }

print t.safe_substitute(d)