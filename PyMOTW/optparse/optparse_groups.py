#!/usr/bin/env python
#
# Copyright 2007 Doug Hellmann.
"""Using optparse with single-letter options.
"""
#end_pymotw_header

import optparse

parser = optparse.OptionParser()

parser.add_option('-q', action='store_const', const='query', dest='mode',
                  help='Query')
parser.add_option('-i', action='store_const', const='install', dest='mode',
                  help='Install')

query_opts = optparse.OptionGroup(
    parser, 'Query Options',
    'These options control the query mode.',
    )
query_opts.add_option('-l', action='store_const', const='list', dest='query_mode',
                      help='List contents')
query_opts.add_option('-f', action='store_const', const='file', dest='query_mode',
                      help='Show owner of file')
query_opts.add_option('-a', action='store_const', const='all', dest='query_mode',
                      help='Show all packages')
parser.add_option_group(query_opts)

install_opts = optparse.OptionGroup(
    parser, 'Installation Options',
    'These options control installation.',
    )
install_opts.add_option('--hash', action='store_true', default=False,
                        help='Show hash marks as progress indication')
install_opts.add_option('--force', dest='install_force', action='store_true', default=False,
                        help='Install, regardless of depdencies or existing version')
parser.add_option_group(install_opts)

print parser.parse_args()
