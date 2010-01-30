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

In the case of this code with a ZeroDivisionError, we can see that the
problem is introduced in the computation of the value of ``c`` in
``func1()``, rather than where the value is used in ``func2()``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'cgitb_local_vars.py', ignore_error=True))
.. }}}
.. {{{end}}}

The code in cgitb that examines the variables used in the stack frame
leading to the error is smart enough to evaluate object attributes to
display them, too.

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

You can pass ``context`` to ``cgitb.enable()`` to control the amount
of code displayed for each line of the traceback.

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

Logging Tracebacks
==================

HTML Output
===========


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

    `Improved traceback module <http://thread.gmane.org/gmane.comp.python.devel/110326>`_
        Python-dev discussion of improvements to the traceback module
        and related enhancements other developers use locally.
