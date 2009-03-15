#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Simple example with urllib.urlopen().
"""
#end_pymotw_header

import urllib

response = urllib.urlopen('http://localhost:8080/')
for line in response:
    print line.rstrip()
