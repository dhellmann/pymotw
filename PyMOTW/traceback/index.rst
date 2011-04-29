====================================================================
traceback -- Extract, format, and print exceptions and stack traces.
====================================================================

.. module:: traceback
    :synopsis: Extract, format, and print exceptions and stack traces.

:Purpose: Extract, format, and print exceptions and stack traces.
:Available In: 1.4 and later, with modifications over time

The :mod:`traceback` module works with the call stack to produce error
messages. A traceback is a stack trace from the point of an exception
handler down the call chain to the point where the exception was
raised. You can also work with the current call stack up from the
point of a call (and without the context of an error), which is useful
for finding out the paths being followed into a function.

The functions in :mod:`traceback` fall into several common categories.
There are functions for extracting raw tracebacks from the current
runtime environment (either an exception handler for a traceback, or
the regular stack). The extracted stack trace is a sequence of tuples
containing the filename, line number, function name, and text of the
source line.

Once extracted, the stack trace can be formatted using functions like
:func:`format_exception()`, :func:`format_stack()`, etc. The format
functions return a list of strings with messages formatted to be
printed. There are shorthand functions for printing the formatted
values, as well.

Although the functions in :mod:`traceback` mimic the behavior of the
interactive interpreter by default, they also are useful for handling
exceptions in situations where dumping the full stack trace to stderr
is not desirable. For example, a web application may need to format
the traceback so it looks good in HTML. An IDE may convert the
elements of the stack trace into a clickable list that lets the user
browse the source.

Supporting Functions
====================

The examples below use the module traceback_example.py (provided in
the source package for PyMOTW). The contents are:

.. include:: traceback_example.py
    :literal:
    :start-after: #end_pymotw_header


Working With Exceptions
=======================

The simplest way to handle exception reporting is with
:func:`print_exc()`. It uses :func:`sys.exc_info()` to obtain the
exception information for the current thread, formats the results, and
prints the text to a file handle (``sys.stderr``, by default).

.. include:: traceback_print_exc.py
    :literal:
    :start-after: #end_pymotw_header


In this example, the file handle for ``sys.stdout`` is substituted so
the informational and traceback messages are mingled correctly:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'traceback_print_exc.py'))
.. }}}
.. {{{end}}}

``print_exc()`` is just a shortcut for :func:`print_exception()`,
which requires explicit arguments:

.. include:: traceback_print_exception.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'traceback_print_exception.py'))
.. }}}
.. {{{end}}}


And :func:`print_exception()` uses :func:`format_exception()`:

.. include:: traceback_format_exception.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'traceback_format_exception.py'))
.. }}}
.. {{{end}}}


Working With the Stack
======================

There are a similar set of functions for performing the same operations with
the current call stack instead of a traceback. 

print_stack()
-------------

.. include:: traceback_print_stack.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'traceback_print_stack.py'))
.. }}}
.. {{{end}}}

format_stack()
--------------

.. include:: traceback_format_stack.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'traceback_format_stack.py'))
.. }}}
.. {{{end}}}

extract_stack()
---------------

.. include:: traceback_extract_stack.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'traceback_extract_stack.py'))
.. }}}
.. {{{end}}}

.. seealso::

    `traceback <http://docs.python.org/lib/module-traceback.html>`_
        Standard library documentation for this module.

    :mod:`sys`
        The sys module includes singletons that hold the current exception.

    :mod:`inspect`
        The inspect module includes other functions for probing the frames on the stack.

    :mod:`cgitb`
        Another module for formatting tracebacks nicely.
