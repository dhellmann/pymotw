#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""
#end_pymotw_header

import gettext
import os

localedir = os.path.join(os.path.dirname(__file__), 'locale')
catalogs = gettext.find('gettext_example', localedir, all=True)
print 'Catalog files:', catalogs

t = gettext.translation('gettext_example', localedir, fallback=True)
_ = t.ugettext

print _('This message is in the script.')
