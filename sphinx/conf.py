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

source_suffix = '.txt'

project = 'Python Module of the Week'
copyright = 'Doug Hellmann, <a href="http://creativecommons.org/licenses/by-nc-sa/3.0/us/" rel="license">CC 3.0 (BY-NC-SA)</a>'
version = os.environ['VERSION']
release = version

html_title = 'Python Module of the Week'
html_short_title = 'PyMOTW'
html_additional_pages = {
    'index':'index.html',
    }
html_use_modindex = True

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
