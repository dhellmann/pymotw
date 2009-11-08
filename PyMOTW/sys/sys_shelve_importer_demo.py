#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""
#end_pymotw_header

import sys
import sys_shelve_importer

filename = '/tmp/pymotw_import_example.shelve'
sys.path_hooks.append(sys_shelve_importer.ShelveFinder)
sys.path.insert(0, filename)

print 'First import of "package":'
import package

print
print 'Examine package contents:'
print 'package.message:', package.message
print 'package.__name__:', package.__name__
print 'package.__file__:', package.__file__
print 'package.__path__:', package.__path__
print 'package.__loader__:', package.__loader__

print
print 'Global settings:'
print 'sys.modules entry:', sys.modules['package']

print
print 'Reloading "package":'
reload(package)

print
print 'First import of "package.module1":'
import package.module1
print 'package.module1.message:', package.module1.message

print
print 'Trying to import a module that does not exist:'
try:
    import package.module3
except ImportError, e:
    print 'Failed to import:', e