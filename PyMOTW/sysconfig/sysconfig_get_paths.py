#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""The paths for a scheme.
"""
#end_pymotw_header

import sysconfig
import pprint

for scheme in ['posix_prefix', 'posix_user']:
    print scheme
    print '=' * len(scheme)
    pprint.pprint(sysconfig.get_paths(scheme=scheme))
    print 
