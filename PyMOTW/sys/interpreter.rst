.. _sys-interpreter:

============================
Runtime Interpreter Settings
============================

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


Executable and DLL References
=============================

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

Command Line Options
====================

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
