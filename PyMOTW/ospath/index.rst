===========================================================
os.path -- Platform-independent manipulation of file names.
===========================================================

.. module:: os.path
    :synopsis: Platform-independent manipulation of file names.

:Purpose: Parse, build, test, and otherwise work on file names and paths.
:Available In: 1.4 and later

Writing code to work with files on multiple platforms is easy using
the functions included in the :mod:`os.path` module. Even programs not
intended to be ported between platforms should use :mod:`os.path` for
reliable filename parsing.

Parsing Paths
=============

The first set of functions in os.path can be used to parse strings
representing filenames into their component parts. It is important to
realize that these functions do not depend on the paths actually
existing; they operate solely on the strings.

Path parsing depends on a few variable defined in :mod:`os`:

* ``os.sep`` - The separator between portions of the path (e.g.,
  "``/``" or "``\``").

* ``os.extsep`` - The separator between a filename and the file
  "extension" (e.g., "``.``").

* ``os.pardir`` - The path component that means traverse the directory
  tree up one level (e.g., "``..``").

* ``os.curdir`` - The path component that refers to the current
  directory (e.g., "``.``").

``split()`` breaks the path into 2 separate parts and returns the
tuple. The second element is the last component of the path, and the
first element is everything that comes before it.

.. include:: ospath_split.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ospath_split.py'))
.. }}}
.. {{{end}}}

``basename()`` returns a value equivalent to the second part of the
``split()`` value.

.. include:: ospath_basename.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ospath_basename.py'))
.. }}}
.. {{{end}}}

``dirname()`` returns the first part of the split path:

.. include:: ospath_dirname.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ospath_dirname.py'))
.. }}}
.. {{{end}}}

``splitext()`` works like ``split()`` but divides the path on the
extension separator, rather than the directory separator.

.. include:: ospath_splitext.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ospath_splitext.py'))
.. }}}
.. {{{end}}}

``commonprefix()`` takes a list of paths as an argument and returns a
single string that represents a common prefix present in all of the
paths. The value may represent a path that does not actually exist,
and the path separator is not included in the consideration, so the
prefix might not stop on a separator boundary.

.. include:: ospath_commonprefix.py
    :literal:
    :start-after: #end_pymotw_header

In this example the common prefix string is ``/one/two/three``, even
though one path does not include a directory named ``three``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ospath_commonprefix.py'))
.. }}}
.. {{{end}}}

Building Paths
==============

Besides taking existing paths apart, you will frequently need to build paths
from other strings.

To combine several path components into a single value, use ``join()``:

.. include:: ospath_join.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ospath_join.py'))
.. }}}
.. {{{end}}}

It's also easy to work with paths that include "variable" components
that can be expanded automatically. For example, ``expanduser()``
converts the tilde (``~``) character to a user's home directory.

.. include:: ospath_expanduser.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ospath_expanduser.py'))
.. }}}
.. {{{end}}}

``expandvars()`` is more general, and expands any shell environment
variables present in the path.

.. include:: ospath_expandvars.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ospath_expandvars.py'))
.. }}}
.. {{{end}}}

Normalizing Paths
=================

Paths assembled from separate strings using ``join()`` or with
embedded variables might end up with extra separators or relative path
components. Use ``normpath()`` to clean them up:

.. include:: ospath_normpath.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ospath_normpath.py'))
.. }}}
.. {{{end}}}

To convert a relative path to a complete absolute filename, use
``abspath()``.

.. include:: ospath_abspath.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ospath_abspath.py'))
.. }}}
.. {{{end}}}

File Times
==========

Besides working with paths, os.path also includes some functions for
retrieving file properties, which can be more convenient than calling
``os.stat()``:

.. include:: ospath_properties.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ospath_properties.py'))
.. }}}
.. {{{end}}}

Testing Files
=============

When your program encounters a path name, it often needs to know
whether the path refers to a file or directory. If you are working on
a platform that supports it, you may need to know if the path refers
to a symbolic link or mount point. You will also want to test whether
the path exists or not.  :mod:`os.path` provides functions to test all
of these conditions.

.. include:: ospath_tests.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. run_script(cog.inFile, 'rm -f broken_link', interpreter='')
.. cog.out(run_script(cog.inFile, 'ln -s /does/not/exist broken_link', interpreter='', trailing_newlines=False))
.. cog.out(run_script(cog.inFile, 'ospath_tests.py', include_prefix=False))
.. }}}
.. {{{end}}}


Traversing a Directory Tree
===========================

``os.path.walk()`` traverses all of the directories in a tree and
calls a function you provide passing the directory name and the names
of the contents of that directory. This example produces a recursive
directory listing, ignoring ``.svn`` directories.

.. include:: ospath_walk.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. run_script(cog.inFile, 'rm -rf example', interpreter='')
.. cog.out(run_script(cog.inFile, 'ospath_walk.py'))
.. }}}
.. {{{end}}}


.. seealso::

    `os.path <http://docs.python.org/lib/module-os.path.html>`_
        Standard library documentation for this module.

    :mod:`os`
        The os module is a parent of os.path.

    :ref:`article-file-access`
        Other tools for working with files.
