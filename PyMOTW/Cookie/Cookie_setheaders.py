#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"

import Cookie

c = Cookie.SimpleCookie()
c['mycookie'] = 'cookie_value'
print c
