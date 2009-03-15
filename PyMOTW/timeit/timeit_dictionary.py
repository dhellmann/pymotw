#!/usr/bin/env python
#
# Copyright 2007 Doug Hellmann.
#
#
#                         All Rights Reserved
#
# Permission to use, copy, modify, and distribute this software and
# its documentation for any purpose and without fee is hereby
# granted, provided that the above copyright notice appear in all
# copies and that both that copyright notice and this permission
# notice appear in supporting documentation, and that the name of Doug
# Hellmann not be used in advertising or publicity pertaining to
# distribution of the software without specific, written prior
# permission.
#
# DOUG HELLMANN DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
# INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN
# NO EVENT SHALL DOUG HELLMANN BE LIABLE FOR ANY SPECIAL, INDIRECT OR
# CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS
# OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,
# NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN
# CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#

"""Example of using timeit programatically.

Time various ways to populate and check a dictionary using a long list
of strings and integers.
"""

__version__ = "$Id$"
#end_pymotw_header

# [[[section header]]]
import timeit
import sys

# A few constants
range_size=1000
count=1000
setup_statement="l = [ (str(x), x) for x in range(%d) ]; d = {}" % range_size
# [[[endsection]]]

# [[[section show_results]]]
def show_results(result):
    "Print results in terms of microseconds per pass and per item."
    global count, range_size
    per_pass = 1000000 * (result / count)
    print '%.2f usec/pass' % per_pass,
    per_item = per_pass / range_size
    print '%.2f usec/item' % per_item

print "%d items" % range_size
print "%d iterations" % count
print
# [[[endsection]]]

# [[[section setitem]]]
# Using __setitem__ without checking for existing values first
print '__setitem__:\t',
sys.stdout.flush()
# using setitem
t = timeit.Timer("""
for s, i in l:
    d[s] = i
""", 
setup_statement)
show_results(t.timeit(number=count))
# [[[endsection]]]

# [[[section setdefault]]]
# Using setdefault
print 'setdefault:\t',
sys.stdout.flush()
t = timeit.Timer("""
for s, i in l:
    d.setdefault(s, i)
""",
setup_statement)
show_results(t.timeit(number=count))
# [[[endsection]]]

# [[[section has_key]]]
# Using has_key
print 'has_key:\t',
sys.stdout.flush()
# using setitem
t = timeit.Timer("""
for s, i in l:
    if not d.has_key(s):
        d[s] = i
""", 
setup_statement)
show_results(t.timeit(number=count))
# [[[endsection]]]

# [[[section exception]]]
# Using exceptions
print 'KeyError:\t',
sys.stdout.flush()
# using setitem
t = timeit.Timer("""
for s, i in l:
    try:
        existing = d[s]
    except KeyError:
        d[s] = i
""", 
setup_statement)
show_results(t.timeit(number=count))
# [[[endsection]]]

# [[[section in]]]
# Using "in"
print '"not in":\t',
sys.stdout.flush()
# using setitem
t = timeit.Timer("""
for s, i in l:
    if s not in d:
        d[s] = i
""", 
setup_statement)
show_results(t.timeit(number=count))
# [[[endsection]]]