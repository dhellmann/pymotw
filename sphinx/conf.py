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
html_last_updated_fmt = '%b %d, %Y'

# The TEMPLATES variable is set by the Makefile before sphinx-build is called.
templates_path = ['../sphinx/templates/%s' % os.environ['TEMPLATES'],
                  ]

latex_documents = [
    ('pdf_contents', 'PyMOTW-%s.tex' % version, 
     'Python Module of the Week', 'Doug Hellmann', 'manual', False),
    ]

#latex_preamble = r'''
#'''

extensions = [ 'sphinx.ext.todo',
               'sphinx.ext.graphviz',
               ]

unused_docs = [ 'copyright' ]

html_theme = 'sphinxdoc'
