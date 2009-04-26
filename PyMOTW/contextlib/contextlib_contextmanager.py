#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
$Id$
"""
#end_pymotw_header
import contextlib

@contextlib.contextmanager
def make_context():
    print '  entering'
    try:
        yield {}
    except RuntimeError, err:
        print '  ERROR:', err
    finally:
        print '  exiting'

print 'Normal:'
with make_context() as value:
    print '  inside with statement:', value

print
print 'Handled error:'
with make_context() as value:
    raise RuntimeError('showing example of handling an error')

print
print 'Unhandled error:'
with make_context() as value:
    raise ValueError('this exception is not handled')
