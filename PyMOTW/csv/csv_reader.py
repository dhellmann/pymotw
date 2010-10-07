#!/usr/bin/env python
#
# Copyright 2007 Doug Hellmann.
#
"""Example of reading a comma separated value file.
"""

__module_id__ = "$Id$"
#end_pymotw_header

import csv
import sys

f = open(sys.argv[1], 'rt')
try:
    reader = csv.reader(f)
    for row in reader:
        print row
finally:
    f.close()
