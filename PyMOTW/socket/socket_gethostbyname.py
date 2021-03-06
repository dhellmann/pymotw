#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Convert hostname to IP address.
"""
#end_pymotw_header

import socket

for host in [ 'homer', 'www', 'www.python.org', 'nosuchname' ]:
    try:
        print '%15s : %s' % (host, socket.gethostbyname(host))
    except socket.error, msg:
        print '%15s : ERROR: %s' % (host, msg)
