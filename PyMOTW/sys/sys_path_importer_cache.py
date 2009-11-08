#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""
#end_pymotw_header

import sys
import pprint

print 'PATH:',
pprint.pprint(sys.path)
print
print 'IMPORTERS:'
pprint.pprint(sys.path_importer_cache)