#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"
#end_pymotw_header

import asyncore
import os

class FileReader(asyncore.file_dispatcher):
    
    def writable(self):
        return False
    
    def handle_read(self):
        data = self.recv(256)
        print 'READ: (%d) "%s"' % (len(data), data)
        
    def handle_expt(self):
        # Ignore events that look like out of band data
        pass
    
    def handle_close(self):
        self.close()

lorem_fd = os.open('lorem.txt', os.O_RDONLY)
reader = FileReader(lorem_fd)
asyncore.loop()
