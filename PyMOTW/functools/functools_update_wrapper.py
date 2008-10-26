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

def myfunc(a, b=2):
    """Docstring for myfunc()."""
    print '\tcalled myfunc with:', (a, b)
    return

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

show_details('myfunc', myfunc)

p1 = functools.partial(myfunc, b=4)
show_details('raw wrapper', p1)

print 'Updating wrapper:'
print '\tassign:', functools.WRAPPER_ASSIGNMENTS
print '\tupdate:', functools.WRAPPER_UPDATES
print

functools.update_wrapper(p1, myfunc)
show_details('updated wrapper', p1)
