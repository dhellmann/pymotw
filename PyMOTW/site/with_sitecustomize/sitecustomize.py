#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Example sitecustomize.py
"""
#end_pymotw_header

print 'Loading sitecustomize.py'

import site
import platform

path = '/opt/local/' + platform.platform()
print 'Adding new path', path
                    
site.addsitedir(path)
    
