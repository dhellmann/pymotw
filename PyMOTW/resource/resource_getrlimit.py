#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""
#end_pymotw_header

import resource

for name, desc in [
    ('RLIMIT_CORE', 'core file size'),
    ('RLIMIT_CPU',  'CPU time'),
    ('RLIMIT_FSIZE', 'file size'),
    ('RLIMIT_DATA', 'heap size'),
    ('RLIMIT_STACK', 'stack size'),
    ('RLIMIT_RSS', 'resident set size'),
    ('RLIMIT_NPROC', 'number of processes'),
    ('RLIMIT_NOFILE', 'number of open files'),
    ('RLIMIT_MEMLOCK', 'lockable memory address'),
    ]:
    limit_num = getattr(resource, name)
    soft, hard = resource.getrlimit(limit_num)
    print 'Maximum %-25s (%-15s) : %20s %20s' % (desc, name, soft, hard)
