===================================
cgitb -- Detailed traceback reports
===================================

.. module:: cgitb
    :synopsis: Mis-named module that provides extended traceback information.

:Purpose: cgitb provides more detailed traceback information than :mod:`traceback`.
:Available In: 2.2 and later

:mod:`cgitb` was originally designed for showing errors and debugging
information in web applications.  It was later updated to include
plain-text output as well, but unfortunately wasn't renamed.  This has
led to obscurity and the module is not used as often as it should be.
Nonetheless, :mod:`cgitb` is a valuable debugging tool in the standard
library.

Standard Traceback Dumps
========================

Python's default exception handling behavior is to print a *traceback*
to standard error with the call stack leading up to the error
position.  This basic output frequently contains enough information to
understand the cause of the exception and permit a fix.

.. include:: cgitb_basic_traceback.py
   :literal:
   :start-after: #end_pymotw_header

The above sample program has a subtle error in :func:`func3()`.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'cgitb_basic_traceback.py', ignore_error=True))
.. }}}
.. {{{end}}}

Enabling Detailed Tracebacks
============================

While the basic traceback includes enough information for us to spot
the error, enabling cgitb replaces ``sys.excepthook`` with a function
that gives extended tracebacks with even more detail.

.. include:: cgitb_extended_traceback.py
   :literal:
   :start-after: #end_pymotw_header

As you can see below, the error report is much more extensive.  Each
frame of the stack is listed, along with:

* the full path to the source file, instead of just the base name
* the values of the arguments to each function in the stack
* a few lines of source context from around the line in the error path
* the values of variables in the expression causing the error

.. {{{cog
.. cog.out(run_script(cog.inFile, 'cgitb_extended_traceback.py', ignore_error=True))
.. }}}
.. {{{end}}}

The end of the output also includes the full details of the exception
object (in case it has attributes other than ``message`` that would be
useful for debugging) and the original form of a traceback dump.

Local Variables in Tracebacks
=============================

Having access to the variables involved in the error stack can help
find a logical error that occurs somewhere higher in the stack than
the line where the actual exception is generated.

.. include:: cgitb_local_vars.py
   :literal:
   :start-after: #end_pymotw_header

In the case of this code with a :ref:`ZeroDivisionError
<exceptions-ZeroDivisionError>`, we can see that the problem is
introduced in the computation of the value of ``c`` in ``func1()``,
rather than where the value is used in ``func2()``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'cgitb_local_vars.py', ignore_error=True))
.. }}}
.. {{{end}}}

The code in :mod:`cgitb` that examines the variables used in the stack
frame leading to the error is smart enough to evaluate object
attributes to display them, too.

.. include:: cgitb_with_classes.py
   :literal:
   :start-after: #end_pymotw_header

Here we see that ``self.a`` and ``self.b`` are involved in the
error-prone code.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'cgitb_with_classes.py', ignore_error=True))
.. }}}
.. {{{end}}}




Adding More Context
===================

Suppose your function includes a lot of inline comments, whitespace,
or other code that makes it very long.  Having the default of 5 lines
of context may not be enough help in that case, if the body of the
function is pushed out of the code window displayed.  Using a larger
context value when enabling cgitb gets around this.

.. include:: cgitb_more_context.py
   :literal:
   :start-after: #end_pymotw_header

You can pass *context* to :func:`enable()` to control the amount of
code displayed for each line of the traceback.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'cgitb_more_context.py 5', ignore_error=True))
.. }}}
.. {{{end}}}

Increasing the value gets us enough of the function that we can spot
the problem in the code, again.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'cgitb_more_context.py 10', ignore_error=True))
.. }}}
.. {{{end}}}


Exception Properties
====================

In addition to the local variables from each stack frame, :mod:`cgitb`
shows all properties of the exception object.  If you have a custom
exception type with extra properties, they are printed as part of the
error report.

.. include:: cgitb_exception_properties.py
   :literal:
   :start-after: #end_pymotw_header

In this example, the *bad_value* property is included along with the
standard *message* and *args* values.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'cgitb_exception_properties.py', ignore_error=True))
.. }}}
.. {{{end}}}



Logging Tracebacks
==================

For many situations, printing the traceback details to standard error
is the best resolution.  In a production system, however, logging the
errors is even better.  :func:`enable()` includes an optional
argument, *logdir*, to enable error logging.  When a directory name is
provided, each exception is logged to its own file in the given
directory.

.. include:: cgitb_log_exception.py
   :literal:
   :start-after: #end_pymotw_header

Even though the error display is suppressed, a message is printed
describing where to go to find the error log.

.. {{{cog
.. path('PyMOTW/cgitb/LOGS').rmtree()
.. sh('mkdir -p PyMOTW/cgitb/LOGS')
.. cog.out(run_script(cog.inFile, 'cgitb_log_exception.py', ignore_error=True))
.. cog.out(run_script(cog.inFile, 'ls LOGS', interpreter=None, include_prefix=False))
.. cog.out(run_script(cog.inFile, 'cat LOGS/*.txt', interpreter=None, include_prefix=False))
.. }}}
.. {{{end}}}



HTML Output
===========

Because :mod:`cgitb` was originally developed for handling exceptions
in web apps, no discussion would be complete without an example of the
HTML output it produces.

.. include:: cgitb_html_output.py
   :literal:
   :start-after: #end_pymotw_header

By leaving out the *format* argument (or specifying ``html``), the
traceback format changes to HTML output.

.. image:: html_error.png


.. seealso::

    `cgitb <http://docs.python.org/library/cgitb.html>`_
        The standard library documentation for this module.

    :mod:`traceback`
        Standard library module for working with tracebacks.

    :mod:`inspect`
        The inspect module includes more functions for examining the
        stack.

    :mod:`sys`
        The sys module provides access to the current exception value
        and the ``excepthook`` handler invoked when an exception
        occurs.

    `Improved traceback module <http://thread.gmane.org/gmane.comp.python.devel/110326>`_
        Python-dev discussion of improvements to the traceback module
        and related enhancements other developers use locally.
