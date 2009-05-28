#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Configuration file for Sphinx-generated documentation.
"""

import glob
import os

__version__ = "$Id$"

source_suffix = '.rst'

project = 'Python Module of the Week'
copyright = 'Doug Hellmann'

# Version information comes from the Makefile that calls sphinx-build.
version = os.environ['VERSION']
release = version

html_title = 'Python Module of the Week'
html_short_title = 'PyMOTW'
html_use_modindex = True

master_doc = 'index' #os.environ['MODULE']

templates_path = ['../../sphinx/blog',
                  ]

# Ignore some subdirectories entirely
exclude_trees = [
    ]

# Ignore README files and other files commonly used but not part of the docs
unused_docs = [ 
    ]

ignore_base_names = [ 'README' ]
for base in ignore_base_names:
    print 'IGNORING:', glob.glob('../PyMOTW/*/%s.txt' % base)
    unused_docs.extend(n[10:-4] for n in glob.glob('../PyMOTW/*/%s.txt' % base))
