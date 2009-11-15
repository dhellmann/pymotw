#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""
#end_pymotw_header

import sys

class NoisyImportFinder(object):
    
    PATH_TRIGGER = 'NoisyImportFinder_PATH_TRIGGER'
    
    def __init__(self, path_entry):
        print 'Checking NoisyImportFinder support for %s' % path_entry
        if path_entry != self.PATH_TRIGGER:
            print 'NoisyImportFinder does not work for %s' % path_entry
            raise ImportError()
        return
    
    def find_module(self, fullname, path=None):
        print 'NoisyImportFinder looking for "%s"' % fullname
        return None

sys.path_hooks.append(NoisyImportFinder)

sys.path.insert(0, NoisyImportFinder.PATH_TRIGGER)

try:
    import target_module
except Exception, e:
    print 'Import failed:', e
