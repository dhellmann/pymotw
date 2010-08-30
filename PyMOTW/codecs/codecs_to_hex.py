#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Format a string of bytes for output.
"""
#end_pymotw_header

import binascii

def to_hex(t, nbytes):
    "Format text t as a sequence of nbyte long values separated by spaces."
    chars_per_item = nbytes * 2
    hex_version = binascii.hexlify(t)
    num_chunks = len(hex_version) / chars_per_item
    def chunkify():
        for start in xrange(0, len(hex_version), chars_per_item):
            yield hex_version[start:start + chars_per_item]
    return ' '.join(chunkify())

if __name__ == '__main__':
    print to_hex('abcdef', 1)
    print to_hex('abcdef', 2)
    
