#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""
#end_pymotw_header

import csv
from StringIO import StringIO
import textwrap

csv.register_dialect('escaped', escapechar='\\', doublequote=False, quoting=csv.QUOTE_NONE)
csv.register_dialect('singlequote', quotechar="'", quoting=csv.QUOTE_ALL)

# Generate sample data for all known dialects

samples = []

for name in sorted(csv.list_dialects()):
    buffer = StringIO()
    dialect = csv.get_dialect(name)
    writer = csv.writer(buffer, dialect=dialect)
    for i in xrange(3):
        writer.writerow(
            ('col1', i, '10/%02d/2010' % i,
             'Contains special chars: " \' %s to be parsed' % dialect.delimiter)
            )
    samples.append( (name, dialect, buffer.getvalue()) )

# Guess the dialect for a given sample, then use the results to parse
# the data.
 
sniffer = csv.Sniffer()

for name, expected, sample in samples:
    print '\nDialect: "%s"\n' % name

    dialect = sniffer.sniff(sample, delimiters=',\t')

    reader = csv.reader(StringIO(sample), dialect=dialect)
    for row in reader:
        print row
