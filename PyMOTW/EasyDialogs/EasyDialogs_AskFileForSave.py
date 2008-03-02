#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"

import EasyDialogs
import os

filename = EasyDialogs.AskFileForSave(
    message='Name the destination',
    defaultLocation=os.getcwd(),
    wanted=unicode,
    )

print 'Selected:', filename