#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Example usercustomize.py
"""
#end_pymotw_header

print 'Loading usercustomize.py'

import site
import platform
import os

path = os.path.expanduser(os.path.join('~', 'python', platform.platform()))
print 'Adding new path', path
                    
site.addsitedir(path)
    
