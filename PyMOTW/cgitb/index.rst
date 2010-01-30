===================================
cgitb -- Detailed traceback reports
===================================

.. module:: cgitb
    :synopsis: Mis-named module that provides extended traceback information.

:Purpose: cgitb provides more detailed traceback information than :mod:`traceback`.
:Python Version: 2.2 and later

cgitb was originally designed for showing errors and debugging
information in web applications.  It was later updated to include
plain-text output as well, but unfortunately wasn't renamed.  This
obscurity has led to it being under used.

Standard Traceback Dumps
========================

Python's default exception handling behavior is to print a *traceback*
to standard error with the call stack leading up to the error
position.  This basic output is frequently enough information to
understand the cause of the exception and permit a fix.

.. include:: cgitb_basic_traceback.py
   :literal:
   :start-after: #end_pymotw_header

The above sample program has a subtle error in ``func3()``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'cgitb_basic_traceback.py', ignore_error=True))
.. }}}
.. {{{end}}}

Enabling Detailed Tracebacks
============================

While the basic traceback includes enough information for us to spot
the error, enabling extended tracebacks gives even more detail.

.. include:: cgitb_extended_traceback.py
   :literal:
   :start-after: #end_pymotw_header

As you can see below, the error report is much more extensive.  Each
frame of the stack is listed, along with a few lines of source context
and the values of local variables from that frame.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'cgitb_extended_traceback.py', ignore_error=True))
.. }}}
.. {{{end}}}

The end of the output also includes the full details of the exception
object (in case it has attributes other than ``message`` that would be
useful for debugging) and the old-form traceback dump.

Local Variables in Tracebacks
=============================

show how having variable values is useful (divide by zero?)


.. seealso::

    `cgitb <http://docs.python.org/library/cgitb.html>`_
        The standard library documentation for this module.

    :mod:`traceback`
        Standard library module for working with tracebacks.

    :mod:`inspect`
        The inspect module includes more functions for examining the
        stack.

    :mod:`sys`
        The sys module provides access to the current exception
        value.
