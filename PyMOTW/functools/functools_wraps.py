#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"
#end_pymotw_header

import functools

def show_details(name, f):
    """Show details of a callable object."""
    print '%s:' % name
    print '\tobject:', f
    print '\t__name__:', 
    try:
        print f.__name__
    except AttributeError:
        print '(no __name__)'
    print '\t__doc__', repr(f.__doc__)
    print
    return

def simple_decorator(f):
    @functools.wraps(f)
    def decorated(a='decorated defaults', b=1):
        print '\tdecorated:', (a, b)
        print '\t',
        f(a, b=b)
        return
    return decorated

def myfunc(a, b=2):
    print '\tmyfunc:', (a,b)
    return

show_details('myfunc', myfunc)
myfunc('unwrapped, default b')
myfunc('unwrapped, passing b', 3)
print

wrapped_myfunc = simple_decorator(myfunc)
show_details('wrapped_myfunc', wrapped_myfunc)
wrapped_myfunc()
wrapped_myfunc('args to decorated', 4)
