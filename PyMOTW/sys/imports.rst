===================
Modules and Imports
===================

Most Python programs end up as a combination of several modules with a main application importing them.  Whether you are using the features of the standard library, or organizing your own code in separate files to make it easier to maintain, understanding and managing the dependencies for your program is an important aspect of development.  :mod:`sys` includes information about the modules available to your application, either as built-ins or after being imported.

Imported Modules
================


``sys.modules`` is a dictionary mapping the names of imported modules to the module object holding the code.

.. include:: sys_modules.py
    :literal:
    :start-after: #end_pymotw_header


.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_modules.py'))
.. }}}
.. {{{end}}}

.. seealso::

    :mod:`textwrap`
        Pretty-printing for plain text.

.. todo:: modules

Built-in Modules
================

The Python interpreter can be compiled with some C modules built right in, so you don't need to distribute them as separate shared libraries.  These modules don't appear in the list of imported modules managed in ``sys.modules`` because they weren't technically imported.  The only way to find the available built-in modules is through ``sys.builtin_module_names``.

.. include:: sys_builtins.py
    :literal:
    :start-after: #end_pymotw_header

.. note::

    Your results may vary, especially if you have built a custom version of the interpreter.
    This script was run using a copy of the interpreter installed from the standard python.org
    installer for the platform.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_builtins.py'))
.. }}}
.. {{{end}}}


.. seealso::

    `Build instructions <http://svn.python.org/view/python/trunk/README?view=markup>`_
        Instructions for building Python, from the README distributed with the source.

Import Path
===========

The search path for modules is managed as a Python list saved in ``sys.path``.  The default contents of the path include the directory of the script used to start the application and the current working directory.  

.. include:: sys_path_default.py
    :literal:
    :start-after: #end_pymotw_header

As you can see here, the first directory in the search path is the home for the sample script itself.  That is followed by a series of platform-specific paths where ``.so`` extension modules might be installed, and then the global ``site-packages`` directory is listed last.

::

	$ python sys_path_default.py
	/Users/dhellmann/Documents/PyMOTW/src/PyMOTW/sys
    /Library/Frameworks/Python.framework/Versions/2.6/lib/python26.zip
    /Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6
    /Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/plat-darwin
    /Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/plat-mac
    /Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/plat-mac/lib-scriptpackages
    /Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/lib-tk
    /Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/lib-old
    /Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/lib-dynload
    /Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/site-packages


The import search path list can be modified before starting the interpreter by setting ``PYTHONPATH``, or during program execution by manipulating the list directly.



Path Hooks
==========

Importer Cache
==============

Prefix
======

