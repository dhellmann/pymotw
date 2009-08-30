#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""
#end_pymotw_header

import decimal

context = decimal.getcontext()

ROUNDING_MODES = [ 
    'ROUND_CEILING', 
    'ROUND_DOWN',
    'ROUND_FLOOR', 
    'ROUND_HALF_DOWN', 
    'ROUND_HALF_EVEN',
    'ROUND_HALF_UP',
    'ROUND_UP',
    'ROUND_05UP',
    ]

header_fmt = '{0:20} {1:^10} {2:^10} {3:^10}'

print 'POSITIVES:'
print

print header_fmt.format(' ', '1/8 (1)', '1/8 (2)', '1/8 (3)')
print header_fmt.format(' ', '-' * 10, '-' * 10, '-' * 10)
for rounding_mode in ROUNDING_MODES:
    print '{0:20}'.format(rounding_mode),
    for precision in [ 1, 2, 3 ]:
        context.prec = precision
        context.rounding = getattr(decimal, rounding_mode)
        value = decimal.Decimal(1) / decimal.Decimal(8)
        print '{0:<10}'.format(value),
    print

print
print 'NEGATIVES:'

print header_fmt.format(' ', '-1/8 (1)', '-1/8 (2)', '-1/8 (3)')
print header_fmt.format(' ', '-' * 10, '-' * 10, '-' * 10)
for rounding_mode in ROUNDING_MODES:
    print '{0:20}'.format(rounding_mode),
    for precision in [ 1, 2, 3 ]:
        context.prec = precision
        context.rounding = getattr(decimal, rounding_mode)
        value = decimal.Decimal(-1) / decimal.Decimal(8)
        print '{0:<10}'.format(value),
    print
