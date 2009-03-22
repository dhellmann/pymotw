======================================================
zipimport -- Load Python code from inside ZIP archives
======================================================

.. module:: zipimport
    :synopsis: Load Python code from inside ZIP archives.

:Purpose: Load Python code from inside ZIP archives.
:Python Version: 2.3 and later

The zipimport module implements the zipimporter class, which can be used to
find and load Python modules inside ZIP archives. The zipimporter supports the
"import hooks" API specified in :pep:`302`; this is how Python Eggs work.

You probably won't need to use the zipimport module directly, since it is
possible to import directly from a ZIP archive as long as that archive appears
in your sys.path. However, it is interesting to see the features available.

Example
=======

For the examples this week, I'll reuse some of the code from last week's
discussion of zipfile to create an example ZIP archive containing some Python
modules. If you are experimenting with the sample code on your system, run
``zipimport_make_example.py`` before any of the rest of the examples. It will
create a ZIP archive containing all of the modules in the zipimport example
directory, along with some test data needed for the code below.

.. include:: zipimport_make_example.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. (path(cog.inFile).parent / 'zipimport_example.zip').unlink()
.. cog.out(run_script(cog.inFile, 'zipimport_make_example.py'))
.. }}}
.. {{{end}}}


Finding a Module
================

Given the full name of a module, find_module() will try to locate that module
inside the ZIP archive.

.. include:: zipimport_find_module.py
    :literal:
    :start-after: #end_pymotw_header

If the module is found, the zipimporter instance is returned. Otherwise, None
is returned.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'zipimport_find_module.py'))
.. }}}
.. {{{end}}}

Accessing Code
==============

The get_code() method loads the code object for a module from the archive.

.. include:: zipimport_get_code.py
    :literal:
    :start-after: #end_pymotw_header

The code object is not the same as a module object.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'zipimport_get_code.py'))
.. }}}
.. {{{end}}}

To load the code as a usable module, use load_module() instead.

.. include:: zipimport_load_module.py
    :literal:
    :start-after: #end_pymotw_header

The result is a module object as though the code had been loaded from a
regular import:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'zipimport_load_module.py'))
.. }}}
.. {{{end}}}

Source
======

As with the inspect module, it is possible to retrieve the source code for a
module from the ZIP archive, if the archive includes the source. In the case
of the example, only zipimport_get_source.py is added to zipimport_example.zip
(the rest of the modules are just the .pyc files).

.. include:: zipimport_get_source.py
    :literal:
    :start-after: #end_pymotw_header

If the source for a module is not available, get_source() returns None.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'zipimport_get_source.py'))
.. }}}
.. {{{end}}}

Packages
========

To determine if a name refers to a package instead of a regular module, use
is_package().

.. include:: zipimport_is_package.py
    :literal:
    :start-after: #end_pymotw_header

In this case, zipimport_is_package came from a module and the example_package
is, well, a package.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'zipimport_is_package.py'))
.. }}}
.. {{{end}}}

Data
====

There are times when source modules or packages need to be distributed with
non-code data. Images, configuration files, default data, and test fixtures
are just a few examples of this. Frequently, the module __path__ is used to
find these data files relative to where the code is installed.

For example, with a normal module you might do something like:

.. include:: zipimport_get_data_nozip.py
    :literal:
    :start-after: #end_pymotw_header


The output will look something like this, with the path changed based on where
the PyMOTW sample code is on your filesystem.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'zipimport_get_data_nozip.py'))
.. }}}
.. {{{end}}}

If the example_package is imported from the ZIP archive instead of the
filesystem, that method does not work:

.. include:: zipimport_get_data_zip.py
    :literal:
    :start-after: #end_pymotw_header

The ``__file__`` of the package refers to the ZIP archive, and not a directory. So
we cannot just build up the path to the README.txt file.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'zipimport_get_data_zip.py', ignore_error=True))
.. }}}
.. {{{end}}}

Instead, we need to use the get_data() method. We can access zipimporter
instance which loaded the module through the ``__loader__`` attribute of the
imported module: 

.. include:: zipimport_get_data.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'zipimport_get_data.py'))
.. }}}
.. {{{end}}}

Although ``__loader__`` is not set for modules not imported via zipimport.

.. seealso::

    `zipimport <http://docs.python.org/lib/module-zipimport.html>`_
        Standard library documentation for this module.

    :mod:`imp`
        Other import-related functions.

    :pep:`302`
        New Import Hooks

