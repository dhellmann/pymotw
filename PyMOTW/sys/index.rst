====================================
sys -- System-specific Configuration
====================================

.. module:: sys
    :synopsis: System-specific configuration

:Purpose: Provides system-specific configuration and operations.
:Python Version: 1.4 and later

The :mod:`sys` module includes a collection of services for probing and changing the configuration of the interpreter at runtime.

Version Information
===================

The version used to build the C interpreter is available in a few forms.  ``sys.version`` is a human-readable string that usually includes the full version number as well as information about the build date, compiler, and platform.  ``sys.hexversion`` is easier to use for checking the interpreter version since it is a simple integer.  When formatted using ``hex()``, it is clear that parts of ``sys.hexversion`` come from the version information also visible in the more readable ``sys.version_info`` (a 5-part tuple representing just the version number).  More specific information about the source that went into the build can be found in the ``sys.subversion`` tuple, which includes the actual branch and subversion revision that was checked out and built.  The separate C API version used by the current interpreter is saved in ``sys.api_version``.

.. include:: sys_version_values.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_version_values.py'))
.. }}}
.. {{{end}}}

Interpreter Command Line Options
================================

The CPython interpreter accepts several command line options to control its behavior.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-h'))
.. }}}
.. {{{end}}}

Some of these are available for programs to check through ``sys.flags``.

.. include:: sys_flags.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, '-3 -S -E sys_flags.py'))
.. }}}
.. {{{end}}}

Arguments to Your Program
=========================

The arguments captured by the interpreter are processed there and not passed along to your program directly.  Any remaining options and arguments, including the name of the script itself, are saved to ``sys.argv`` in case your program does need to use them.

.. include:: sys_argv.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_argv.py', trailing_newlines=False))
.. cog.out(run_script(cog.inFile, 'sys_argv.py -v foo blah', include_prefix=False))
.. }}}
.. {{{end}}}


Input and Output
----------------

stdin, stdout, stderr, 


exit, 

Runtime Interpreter Settings
============================

type cache, frames, dllhandle, executable, get/set checkinterval, getdefaultencoding, getfilesystemencoding, getwindowsversion, platform,

Interactive Interpreter Settings
================================

ps1, ps2, 

Hooks
=====

display, exception, profile, trace, 

Exception Handling
==================

..., last_*, 

Memory and Stack
================

getrefcount, getrecursionlimit, getsizeof, _getframe, 

Limits
======

maxint, maxsize, maxunicode, tracebacklimit, float_info

Modules / Imports
=================

builtin modules, modules, path, path_hooks, path_importer_cache, prefix, 


.. seealso::

    `sys <http://docs.python.org/library/sys.html>`_
        The standard library documentation for this module.

    :mod:`getopt`, :mod:`optparse`
        Modules for parsing command line arguments.
    
    :mod:`traceback`
        Module for working with tracebacks.
