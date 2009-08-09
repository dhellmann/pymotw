# 
#  Created by Doug Hellmann on 2009-07-04.
#  Copyright 2009 Doug Hellmann. All rights reserved.
# 

# We need absolute imports because otherwise the module
# inside our package will replace the stdlib modules
# we need to do our work.
from __future__ import absolute_import

import os
import pydoc
import sys
import types
import webbrowser

DOCS_DIR = 'docs'

def get_doc_dir(module_name):
    """Return the local directory containing documentation for the module."""
    import PyMOTW
    package_path = PyMOTW.__path__[0]
    doc_dir = os.path.join(package_path, DOCS_DIR, module_name)
    return doc_dir

def show_text(module_name):
    """How help text for the named module."""
    print >>sys.stderr, 'os', os
    filename = os.path.join(get_doc_dir(module_name), 'index.txt')
    with open(filename, 'rt') as f:
        text = f.read()
    pydoc.pager(text)
    return
    
def motw(module):
    """Show the text help for the give module by name or reference."""
    if isinstance(module, types.ModuleType):
        module = module.__name__
    show_text(module)
    return
__builtins__['motw'] = motw

def show_html(module_name):
    """Show the HTML version of the help for the named module."""
    module_path = os.path.join(get_doc_dir(module_name))
    url = 'file://localhost' + module_path + '/index.html'
    webbrowser.open(url)
    return

def show_webpage(module_name):
    """Open the remote web page with help for the named module."""
    url = 'http://www.doughellmann.com/PyMOTW/' + module_name + '/'
    webbrowser.open(url)
    return
