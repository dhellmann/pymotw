#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann.  All rights reserved.
#
"""
"""
#end_pymotw_header

import plistlib
import os
import glob

calendar_root = os.path.expanduser('~/Library/Calendars')
calendar_directories = (
    glob.glob(os.path.join(calendar_root, '*.caldav', '*.calendar')) +
    glob.glob(os.path.join(calendar_root, '*.calendar'))
    )

for dirname in calendar_directories:
    info_filename = os.path.join(dirname, 'Info.plist')
    if os.path.isfile(info_filename):
        info = plistlib.readPlist(info_filename)
        if info.get('Checked'):
            print info['Title']
