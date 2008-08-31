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
html_additional_pages = {
    'index':'index.html',
    }
html_use_modindex = True

# The TEMPLATES variable is set by the Makefile before sphinx-build is called.
templates_path = ['../sphinx/templates/%s' % os.environ['TEMPLATES']]

# Ignore some subdirectories entirely
exclude_trees = [
    'glob/dir',
    'zipimport/example_package',
    ]

# Ignore README files and other files commonly used but not part of the docs
unused_docs = [ 
    'cmd/cmd_file',
    'mmap/lorem', 
    'mmap/lorem_copy', 
    'shlex/apostrophe', 
    'shlex/comments',
    'shlex/quotes',
    'weakref/trace',
    ]
ignore_base_names = [ 'README' ]
for base in ignore_base_names:
    print 'IGNORING:', glob.glob('../PyMOTW/*/%s.txt' % base)
    unused_docs.extend(n[10:-4] for n in glob.glob('../PyMOTW/*/%s.txt' % base))
