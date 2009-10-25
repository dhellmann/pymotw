.. _sys-tracing:

===============================
Tracing Your Program As It Runs
===============================

There are two ways to inject code to watch your program run: tracing and profiling.  They are similar, but intended for different purposes and so have different constraints.  The easiest, but least efficient, way to monitor your program is through a *trace hook*, which can be used for writing a debugger, code coverage monitoring, or many other purposes.

The trace hook is modified by passing a callback function to ``sys.settrace()``.  The callback is passed three arguments, frame (the stack frame from the code being run), event (a string naming the type of notification), and arg (an event-specific value).  There are 7 event types for different levels of information that occur as your program is being executed.

+-------------------+-------------------------------------+------------------------------------------+
| Event             | When                                | arg value                                |
+===================+=====================================+==========================================+
| ``'call'``        | Before a function is executed.      | ``None``                                 |
+-------------------+-------------------------------------+------------------------------------------+
| ``'line'``        | Before a line is executed.          | ``None``                                 |
+-------------------+-------------------------------------+------------------------------------------+
| ``'return'``      | Before a function returns.          | The value being returned.                |
+-------------------+-------------------------------------+------------------------------------------+
| ``'exception'``   | After an exception occurs.          | The (exception, value, traceback) tuple. |
+-------------------+-------------------------------------+------------------------------------------+
| ``'c_call'``      | Before a C function is called.      | The C function object.                   |
+-------------------+-------------------------------------+------------------------------------------+
| ``'c_return'``    | After a C function returns.         | ``None``                                 |
+-------------------+-------------------------------------+------------------------------------------+
| ``'c_exception'`` | After a C function throws an error. | ``None``                                 |
+-------------------+-------------------------------------+------------------------------------------+

Tracing Function Calls
======================

A call event is generated before every function call.  The frame passed to the callback can be used to find out which function is being called and from where.

.. literalinclude:: sys_settrace_call.py
    :linenos:

This example ignores calls to ``write()``, as used by ``print`` to write to sys.stdout.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_settrace_call.py'))
.. }}}
.. {{{end}}}

Tracing Inside Functions
========================

The trace hook can return a new hook to be used inside the new scope (the *local* trace function). It is possible, for instance, to control tracing to only run line-by-line within certain modules or functions.

.. literalinclude:: sys_settrace_line.py
    :linenos:

Here the global list of functions is kept in the variable ``TRACE_INTO``, so when ``trace_calls()`` runs it can return ``trace_lines()`` to enable tracing inside of ``b()``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_settrace_line.py'))
.. }}}
.. {{{end}}}


Watching the Stack
==================

Another useful way to use the hooks is to keep up with which functions are being called, and what their return values are.  To monitor return values, watch for the ``return`` event.

.. literalinclude:: sys_settrace_return.py
    :linenos:

The local trace function is used for watching returns, so we need to return ``trace_calls_and_returns`` when a function is called.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_settrace_return.py'))
.. }}}
.. {{{end}}}


Exception Propagation
=====================

Exceptions can be monitored by looking for the ``exception`` event in a local trace function.  When an exception occurs, the trace hook is called with the ``(type, instance, traceback)`` triple passed as ``arg``.

.. literalinclude:: sys_settrace_exception.py
    :linenos:

Take care to limit where the local function is applied because some of the internals of
formatting error messages generate, and ignore, their own exceptions.  **Every** exception is
seen by the trace hook, whether the caller catches and ignores it or not.


.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_settrace_exception.py'))
.. }}}
.. {{{end}}}


.. seealso::

    :mod:`profile`
        The profile module documentation shows how to use a ready-made profiler.

    `Types and Members <http://docs.python.org/library/inspect.html#types-and-members>`_
        The descriptions of frame and code objects and their attributes.

    `Tracing python code <http://www.dalkescientific.com/writings/diary/archive/2005/04/20/tracing_python_code.html>`_
        Another ``settrace()`` tutorial.
