#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Compute a "normalized" path.
"""

__version__ = "$Id$"

import os.path

for path in [ 'one//two//three', 
              'one/./two/./three', 
              'one/../one/two/three',
              ]:
    print path, ':', os.path.normpath(path)