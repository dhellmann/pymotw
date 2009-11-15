.. _sys-imports:

===================
Modules and Imports
===================

Most Python programs end up as a combination of several modules with a main application importing them. Whether
you are using the features of the standard library, or organizing your own code in separate files to make it
easier to maintain, understanding and managing the dependencies for your program is an important aspect of
development. :mod:`sys` includes information about the modules available to your application, either as built-ins
or after being imported.

Imported Modules
================

``sys.modules`` is a dictionary mapping the names of imported modules to the module object holding the code.

.. include:: sys_modules.py
    :literal:
    :start-after: #end_pymotw_header

The contents of ``sys.modules`` change as new modules are imported.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_modules.py'))
.. }}}
.. {{{end}}}


Built-in Modules
================

The Python interpreter can be compiled with some C modules built right in, so you don't need to distribute them
as separate shared libraries. These modules don't appear in the list of imported modules managed in
``sys.modules`` because they weren't technically imported. The only way to find the available built-in modules is
through ``sys.builtin_module_names``.

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

The search path for modules is managed as a Python list saved in ``sys.path``. The default contents of the path
include the directory of the script used to start the application and the current working directory.

.. include:: sys_path_show.py
    :literal:
    :start-after: #end_pymotw_header

As you can see here, the first directory in the search path is the home for the sample script itself. That is
followed by a series of platform-specific paths where compiled extension modules (written in C) might be
installed, and then the global ``site-packages`` directory is listed last.

::

	$ python sys_path_show.py
	/Users/dhellmann/Documents/PyMOTW/src/PyMOTW/sys
	/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6
	/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/plat-darwin
	/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/lib-tk
	/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/plat-mac
	/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/plat-mac/lib-scriptpackages
	/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/site-packages


The import search path list can be modified before starting the interpreter by setting the shell variable
``PYTHONPATH`` to a colon-separated list of directories.

::

	$ PYTHONPATH=/my/private/site-packages:/my/shared/site-packages python sys_path_show.py
	/Users/dhellmann/Documents/PyMOTW/src/PyMOTW/sys
	/my/private/site-packages
	/my/shared/site-packages
	/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6
	/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/plat-darwin
	/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/lib-tk
	/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/plat-mac
	/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/plat-mac/lib-scriptpackages
	/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/site-packages

A program can also modify its path by adding elements to ``sys.path`` directly.

.. include:: sys_path_modify.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_path_modify.py'))
.. }}}
.. {{{end}}}


Custom Importers
================

Modifying the search path lets you control how standard Python modules are found, but what if you need to import
code from somewhere other than the usual ``.py`` or ``.pyc`` files on the filesystem? :pep:`302` solves this
problem by introducing the idea of *import hooks* that let you trap an attempt to find a module on the search
path and take alternative measures to load the code from somewhere else or apply pre-processing to it.

Hooks
-----

Custom importers are implemented in two separate phases. The *finder* is responsible for locating a module and
providing a *loader* to manage the actual import. Adding a custom module finder is as simple as appending a
factory to the ``sys.path_hooks`` list. On import, each part of the path is given to a finder until one claims
support (by not raising ImportError). That finder is then responsible for searching data storage represented by
its path entry for named modules.

.. include:: sys_path_hooks_noisy.py
    :literal:
    :start-after: #end_pymotw_header

This example illustrates how the finders are instantiated and queried. The NoisyImportFinder raises ImportError
when instantiated with a path entry that does not match its special trigger value, which is obviously not a real
path on the filesystem. This test prevents the NoisyImportFinder from breaking imports of real modules.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_path_hooks_noisy.py'))
.. }}}
.. {{{end}}}

Importing from a Shelve
-----------------------

When the finder locates a module, it is responsible for returning a loader capable of importing that module. This
example illustrates a custom importer that saves its module contents in a database created by :mod:`shelve`.

First, a script to populate the shelf with a package containing a sub-module and sub-package.

.. include:: sys_shelve_importer_create.py
    :literal:
    :start-after: #end_pymotw_header

A real packaging script would probably read the contents from the filesystem, but using hard-coded values is
sufficient for a simple example like this.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_shelve_importer_create.py'))
.. }}}
.. {{{end}}}

Next, we need to provide finder and loader classes that know how to look in a shelf for the source of a module or
package:

.. include:: sys_shelve_importer.py
    :literal:
    :start-after: #end_pymotw_header

Finally, a short demo script to pull the pieces together and use the ``ShelveFinder`` and ``ShelveLoader`` to import code from a shelf.

.. include:: sys_shelve_importer_demo.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_shelve_importer_demo.py'))
.. }}}
.. {{{end}}}

.. todo::

    1. Expand on the prose in this section.
    2. Read docs for Py 3 importlib
    3. demonstrate features that require get_code()

Importer Cache
--------------

Searching through all of the hooks each time a module is imported can become expensive. To save time,
``sys.path_importer_cache`` is maintained as a mapping between a path entry and the loader that can use the
value to find modules.

.. include:: sys_path_importer_cache.py
    :literal:
    :start-after: #end_pymotw_header

A cache value of ``None`` means to use the default filesystem loader. Each missing directory is associated with
an ``imp.NullImporter`` instance, since modules cannot be imported from directories that do not exist. In the
example output below, several ``zipimport.zipimporter`` instances are used to manage EGG files found on the path.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_path_importer_cache.py'))
.. }}}
.. {{{end}}}


Meta Path
---------

.. todo:: write this section

.. seealso::

    :pep:`302`
        Import Hooks

    :mod:`imp`
        The imp module provides tools used by importers.
        
    :mod:`zipimport`
        Implements importing Python modules from inside ZIP archives.
        
    `The Quick Guide to Python Eggs <http://peak.telecommunity.com/DevCenter/PythonEggs>`_
        PEAK documentation for working with EGGs.
    
    `Import this, that, and the other thing: custom importers <http://us.pycon.org/2010/conference/talks/?filter=core>`_
        Brett Cannon's PyCon 2010 presentation.
        
    `Python 3 stdlib module "importlib" <http://docs.python.org/py3k/library/importlib.html>`_
        Python 3.x includes abstract base classes that makes it easier to create custom importers.
        
Prefix
======

