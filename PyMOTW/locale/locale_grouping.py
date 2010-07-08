#!/usr/bin/env python

import locale

sample_locales = [ ('USA', 'en_US'),
                   ('France', 'fr_FR'),
                   ('Spain', 'es_ES'),
                   ('Portugal', 'pt_PT'),
                   ('Poland', 'pl_PL'),
                   ]

for name, loc in sample_locales:
    locale.setlocale(locale.LC_ALL, loc)

    print '%20s:' % name,
    print locale.format('%15d', 1234567,    grouping=True),
    print locale.format('%20.2f', 1234567.89, grouping=True)
