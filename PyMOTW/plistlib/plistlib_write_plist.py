#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann.  All rights reserved.
#
"""
"""
#end_pymotw_header

import plistlib
import datetime
import tempfile

d = { 'an_int':2,
      'a_bool':False,
      'the_float':5.9,
      'simple_string':'This string has no special characters.',
      'xml_string':'<element attr="value">This string includes XML markup &nbsp;</element>',
      'nested_list':['a', 'b', 'c'],
      'nested_dict':{ 'key':'value' },
      'timestamp':datetime.datetime.now(),
      }

output_file = tempfile.NamedTemporaryFile()
try:
    plistlib.writePlist(d, output_file)
    output_file.seek(0)
    print output_file.read()
finally:
    output_file.close()
    
