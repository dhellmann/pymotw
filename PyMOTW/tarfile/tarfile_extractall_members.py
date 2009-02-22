#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"
#end_pymotw_header

import tarfile
import os

os.mkdir('outdir')
t = tarfile.open('example.tar', 'r')
t.extractall('outdir', members=[t.getmember('README.txt')])
print os.listdir('outdir')