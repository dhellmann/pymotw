#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""
#end_pymotw_header

import contextlib
import imp
import os
import shelve
import sys

@contextlib.contextmanager
def shelve_context(filename, flag='r'):
    db = shelve.open(filename, flag)
    try:
        yield db
    finally:
        db.close()


class ShelveFinder(object):
    """Find modules collected in a shelve archive."""
    
    def __init__(self, path_entry):
        if not os.path.exists(path_entry):
            raise ImportError()
        try:
            # Test the path_entry to see if it is a valid shelve file
            with shelve_context(path_entry):
                pass
        except Exception, e:
            raise ImportError(str(e))
        else:
            print 'new shelve added to import path:', path_entry
            self.path_entry = path_entry
        return
        
    def __str__(self):
        return '<%s for "%s">' % (self.__class__.__name__, self.path_entry)
        
    def find_module(self, fullname, path=None):
        print 'looking for "%s" in %s ...' % (fullname, self.path_entry),
        with shelve_context(self.path_entry) as db:
            if fullname in db:
                print 'found it'
                return ShelveLoader(self.path_entry)
        print 'not found'
        return None


class ShelveLoader(object):
    """Load source for modules from shelve databases."""
    
    def __init__(self, path_entry):
        self.path_entry = path_entry
        return
        
    def _get_filename(self, fullname):
        return '<%s "%s"[%s]>' % (self.__class__.__name__, self.path_entry, fullname)
        
    def get_source(self, fullname):
        print 'loading source for "%s" from shelve file' % fullname
        try:
            with shelve_context(self.path_entry) as db:
                return db[fullname]
        except Exception, e:
            print 'could not load source:', e
            raise ImportError(str(e))
            
    def get_code(self, fullname):
        print 'compiling code for "%s"' % fullname
        source = self.get_source(fullname)
        return compile(source, self._get_filename(fullname), 'exec', dont_inherit=True)
            
    def is_package(self, fullname):
        # This trivial example does not support nested packages.
        return '.' not in fullname

    def load_module(self, fullname):
        source = self.get_source(fullname)

        if fullname in sys.modules:
            print 'reusing existing module from previous import of "%s"' % fullname
            mod = sys.modules[fullname]
        else:
            print 'creating a new module object for "%s"' % fullname
            mod = sys.modules.setdefault(fullname, imp.new_module(fullname))

        # Set a few properties required by PEP 302
        mod.__file__ = self._get_filename(fullname)
        mod.__name__ = fullname
        mod.__path__ = self.path_entry
        mod.__loader__ = self
        mod.__package__ = '.'.join(fullname.split('.')[:-1])
        
        if self.is_package(fullname):
            # Set __path__ for packages
            # so we can find the sub-modules.
            mod.__path__ = [self.path_entry]
        
        print 'execing source...'
        exec source in mod.__dict__
        print 'done'
        return mod
        