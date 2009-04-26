#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""
#end_pymotw_header

import multiprocessing

def do_calculation(data):
    return data * 2

if __name__ == '__main__':
    pool_size = multiprocessing.cpu_count() * 2
    pool = multiprocessing.Pool(processes=pool_size)
    
    inputs = list(range(10))
    print 'Input   :', inputs
    
    builtin_outputs = map(do_calculation, inputs)
    print 'Built-in:', builtin_outputs
    
    pool_outputs = pool.map(do_calculation, inputs)
    print 'Pool    :', pool_outputs
