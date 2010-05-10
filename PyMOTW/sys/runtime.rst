.. _sys-runtime:

===================
Runtime Environment
===================

:mod:`sys` provides low-level APIs for interacting with the system outside of your application, by accepting command line arguments, accessing user input, and passing messages and status values to the user.

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

.. seealso::
    
    :mod:`getopt`, :mod:`optparse`
        Modules for parsing command line arguments.

.. _sys-input-output:

Input and Output Steams
=======================

Following the Unix paradigm, Python programs can access three file descriptors by default.  ``stdin`` is the standard way to read input, usually from a console but also from other programs via a pipeline.  ``stdout`` is the standard way to write output for a user (to the console) or to be sent to the next program in a pipeline.  ``stderr`` is intended for use with warning or error messages.

.. include:: sys_stdio.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, interpreter='cat sys_stdio.py | python', script_name='sys_stdio.py'))
.. }}}
.. {{{end}}}


.. seealso::

    :mod:`subprocess`, :mod:`pipes`
        Both subprocess and pipes have features for pipelining programs together.

Returning Status
================

To return an exit code from your program, pass an integer value to ``sys.exit()``.  A non-zero value means the program exited with an error.

.. include:: sys_exit.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_exit.py 0 ; echo "Exited $?"', trailing_newlines=False))
.. cog.out(run_script(cog.inFile, 'sys_exit.py 1 ; echo "Exited $?"', include_prefix=False, ignore_error=True))
.. }}}
.. {{{end}}}
