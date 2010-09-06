.. _sys-interpreter:

====================
Interpreter Settings
====================

:mod:`sys` contains attributes and functions for accessing
compile-time or runtime configuration settings for the interpreter.

.. _sys-build-time-info:

Build-time Version Information
==============================

The version used to build the C interpreter is available in a few
forms.  ``sys.version`` is a human-readable string that usually
includes the full version number as well as information about the
build date, compiler, and platform.  ``sys.hexversion`` is easier to
use for checking the interpreter version since it is a simple integer.
When formatted using ``hex()``, it is clear that parts of
``sys.hexversion`` come from the version information also visible in
the more readable ``sys.version_info`` (a 5-part tuple representing
just the version number).  More specific information about the source
that went into the build can be found in the ``sys.subversion`` tuple,
which includes the actual branch and subversion revision that was
checked out and built.  The separate C API version used by the current
interpreter is saved in ``sys.api_version``.

.. include:: sys_version_values.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_version_values.py'))
.. }}}
.. {{{end}}}

The operating system platform used to build the interpreter is saved
as ``sys.platform``.  

.. include:: sys_platform.py
    :literal:
    :start-after: #end_pymotw_header

For most Unix systems, the value comes from combining the output of
``uname -s`` with the first part of the version in ``uname -r``. For
other operating systems there is a `hard-coded table of values
<http://docs.python.org/library/sys.html#sys.platform>`_.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_platform.py'))
.. }}}
.. {{{end}}}

.. _sys-prefix:

Install Location
================

The path to the actual interpreter program is available in
``sys.executable`` on all systems for which having a path to the
interpreter makes sense.  This can be useful for ensuring that the
*correct* interpreter is being used, and also gives clues about paths
that might be set based on the interpreter location.

``sys.prefix`` refers to the parent directory of the interpreter
installation.  It usually includes ``bin`` and ``lib`` directories for
executables and installed modules, respectively.

.. include:: sys_locations.py
    :literal:
    :start-after: #end_pymotw_header

.. note:: 

  The build for PyMOTW uses a `virtualenv
  <http://pypi.python.org/pypi/virtualenv>`_, so these paths do not
  match the defaults.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_locations.py'))
.. }}}
.. {{{end}}}


Command Line Options
====================

The CPython interpreter accepts several command line options to
control its behavior.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-h'))
.. }}}
.. {{{end}}}

Some of these are available for programs to check through
``sys.flags``.

.. include:: sys_flags.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, '-3 -S -E sys_flags.py'))
.. }}}
.. {{{end}}}


.. _sys-unicode-defaults:

Unicode Defaults
================

You can ask for the default Unicode encoding being used by the
interpreter with ``getdefaultencoding()``.  The value is set during
startup by :mod:`site`, which calls ``sys.setdefaultencoding()`` and
then removes it from the namespace in :mod:`sys` to avoid having it
called again.

The internal encoding default and the filesystem encoding may be
different for some operating systems, so there is a separate way to
retrieve the filesystem setting.  ``getfilesystemencoding()`` returns
an OS-specific (*not* filesystem-specific) value.

.. include:: sys_unicode.py
    :literal:
    :start-after: #end_pymotw_header

.. note::  

  Rather than changing the global default encoding, most Unicode
  experts recommend making your application explicitly
  Unicode-aware. This gives you two benefits: It lets you handle
  different Unicode encodings for different data sources, and ensures
  there are no assumptions about encodings in your application code.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_unicode.py'))
.. }}}
.. {{{end}}}


Interactive Prompts
===================

The interactive interpreter uses two separate prompts for indicating
the default input level (``ps1``) and the "continuation" of a
multi-line statement (``ps2``).  The values are only used by the
interactive interpreter.

::

    >>> import sys
    >>> sys.ps1
    '>>> '
    >>> sys.ps2
    '... '
    >>>

Either or both prompt can be changed to a different string

::

    >>> sys.ps1 = '::: '
    ::: sys.ps2 = '~~~ '
    ::: for i in range(3):
    ~~~   print i
    ~~~ 
    0
    1
    2
    ::: 

Alternately, any object that can be converted to a string (via
``__str__``) can be used for the prompt.

.. include:: sys_ps1.py
    :literal:
    :start-after: #end_pymotw_header


::

    $ python
    Python 2.6.2 (r262:71600, Apr 16 2009, 09:17:39)
    [GCC 4.0.1 (Apple Computer, Inc. build 5250)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from PyMOTW.sys.sys_ps1 import LineCounter
    >>> import sys
    >>> sys.ps1 = LineCounter()
    (  1)>
    (  2)>
    (  3)>

Display Hook
============

``sys.displayhook`` is invoked by the interactive interpreter each
time the user enters an expression.  The *result* of the expression is
passed as the only argument to the function.  The default value (saved
in ``sys.__displayhook__``) prints the result to stdout and saves it
in ``__builtin__._`` for easy reference later.

.. include:: sys_displayhook.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python 
    Python 2.6.2 (r262:71600, Apr 16 2009, 09:17:39) 
    [GCC 4.0.1 (Apple Computer, Inc. build 5250)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import PyMOTW.sys.sys_displayhook
    installing
    >>> 1+2

      Previous: <PyMOTW.sys.sys_displayhook.ExpressionCounter object at 0x9c5f90>
      New     : 3

    3
    (  1)> 'abc'

      Previous: 3
      New     : abc

    'abc'
    (  2)> 'abc'

      Previous: abc
      New     : abc

    'abc'
    (  2)> 'abc' * 3

      Previous: abc
      New     : abcabcabc

    'abcabcabc'
    (  3)>
