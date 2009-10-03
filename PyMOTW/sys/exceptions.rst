==================
Exception Handling
==================

Unhandled Exceptions
====================

Many applications are structured with a main loop that wraps execution in a global exception handler to trap errors not handled at a lower level.  Another way to achieve the same thing is by setting the ``sys.excepthook`` to a function that takes three arguments (error type, error value, and traceback) and let it deal with unhandled errors.

.. include:: sys_excepthook.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_excepthook.py', ignore_error=True))
.. }}}
.. {{{end}}}

Current Exception
=================

.. note:: exc_info, exc_type, exc_value, exc_traceback, exc_clear

Previous Exception
==================

.. note:: 

    sys.last_type
    sys.last_value
    sys.last_traceback

.. seealso::

    :mod:`traceback`
        Module for working with tracebacks.
    