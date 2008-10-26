#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"
#end_pymotw_header

import imp

f, filename, description = imp.find_module('example')
example_package = imp.load_module('example', f, filename, description)
print 'Package:', example_package

f, filename, description = imp.find_module('submodule', 
                                           example_package.__path__)
try:
    submodule = imp.load_module('example.module', f, filename, description)
    print 'Sub-module:', submodule
finally:
    f.close()
