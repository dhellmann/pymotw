#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""
#end_pymotw_header

import abc

class Base(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractproperty
    def value(self):
        return 'Should never get here'


class Implementation(Base):
    
    @property
    def value(self):
        return 'concrete property'


try:
    b = Base()
    print 'Base.value:', b.value
except Exception, err:
    print 'ERROR:', str(err)

i = Implementation()
print 'Implementation.value:', i.value
