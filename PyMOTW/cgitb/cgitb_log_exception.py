#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann.  All rights reserved.
#
"""Logging exceptions to a file, instead of displaying them.
"""
#end_pymotw_header

import cgitb
import os

cgitb.enable(logdir=os.path.join(os.path.dirname(__file__), 'LOGS'),
             display=False,
             format='text',
             )

def func2(a, divisor):
    return a / divisor

def func1(a, b):
    c = b - 5
    return func2(a, c)

func1(1, 5)
