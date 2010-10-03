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
html_static_path = ['images']
if os.environ['TEMPLATES'] == 'pkg':
    html_theme = 'sphinxdoc'
else:
    html_theme = 'default'

# The TEMPLATES variable is set by the Makefile before sphinx-build is called.
templates_path = ['../sphinx/templates/%s' % os.environ['TEMPLATES'],
                  ]

latex_documents = [
    ('pdf_contents', 'PyMOTW-%s.tex' % version, 
     'Python Module of the Week', 'Doug Hellmann', 'manual', False),
    ]

#latex_use_parts = True

#latex_preamble = r'''
#'''

#latex_show_pagerefs = True
latex_show_urls = True

latex_elements = {
    'preamble':'''
\DeclareUnicodeCharacter{FFFD}{\includegraphics{replacement-character.png}}
''',
    }

latex_additional_files = [
    'images/replacement-character.png',
    ]

extensions = [ 'sphinx.ext.todo',
               'sphinx.ext.graphviz',
               ]

unused_docs = [ 'copyright', 'doctest/doctest_in_help' ]

