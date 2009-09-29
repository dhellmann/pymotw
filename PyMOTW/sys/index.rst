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

Runtime Interpreter Settings
============================

Executable and DLL References
-----------------------------

Under Windows, ``sys.dllhandle`` is an integer that refers to the Python DLL loaded by the system.

The path to the actual interpreter program is available in ``sys.executable`` on all systems for which having a path to the interpreter makes sense.

.. include:: sys_executable.py
    :literal:
    :start-after: #end_pymotw_header

This can be useful for ensuring that the *right* interpreter is being used, and also gives clues about paths that might be set based on the interpreter location.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_executable.py'))
.. }}}
.. {{{end}}}


type cache, frames, get/set checkinterval, getdefaultencoding, getfilesystemencoding, getwindowsversion, platform,

Interactive Interpreter Prompts
-------------------------------

The interpreter uses two separate prompts for indicating the default input level (``ps1``) and the "continuation" of a multi-line statement (``ps2``).  The values are only used by the interactive interpreter.

::

    >>> import sys
    >>> print repr(sys.ps1)
    '>>> '
    >>> print repr(sys.ps2)
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

Alternately, any object that can be converted to a string (via ``__str__``) can be used for the prompt.

.. include:: sys_ps1.py
    :literal:
    :start-after: #end_pymotw_header

For another example of how to set up fancy prompts, see :ref:`sys-displayhook`

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

Interpreter Command Line Options
--------------------------------

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

Runtime Environment
===================

Arguments to Your Program
-------------------------

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

Following the Unix paradigm, Python programs can access three file descriptors by default.  ``stdin`` is the standard way to read input, usually from a console but also from other programs via a pipeline.  ``stdout`` is the standard way to write output for a user (to the console) or to be sent to the next program in a pipeline.  ``stderr`` is intended for use with warning or error messages.

.. include:: sys_stdio.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, interpreter='cat sys_stdio.py | python', script_name='sys_stdio.py'))
.. }}}
.. {{{end}}}


Returning Values
----------------

To return an exit code from your program, pass an integer value to ``sys.exit()``.  A non-zero value means the program exited with an error.

.. include:: sys_exit.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_exit.py 0 ; echo "Exited $?"', trailing_newlines=False))
.. cog.out(run_script(cog.inFile, 'sys_exit.py 1 ; echo "Exited $?"', include_prefix=False, ignore_error=True))
.. }}}
.. {{{end}}}



Hooks
=====

.. _sys-displayhook:

Display Hook
------------

``sys.displayhook`` is invoked by the interactive interpreter each time the user enters an expression.  The *result* of the expression is passed as the only argument to the function.  The default value (available in ``sys.__displayhook__``) prints the result to stdout and saves it in ``__builtin__._`` for easy reference later.

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

Exception Handling
------------------

Many applications are structured with a main loop that wraps execution in a global exception handler to trap errors not handled at a lower level.  Another way to achieve the same thing is by setting the ``sys.excepthook`` to a function that takes three arguments (error type, error value, and traceback) and let it deal with unhandled errors.

.. include:: sys_excepthook.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_excepthook.py', ignore_error=True))
.. }}}
.. {{{end}}}


Profile Hook
------------

get / set

Trace Hook
----------

get / set

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
