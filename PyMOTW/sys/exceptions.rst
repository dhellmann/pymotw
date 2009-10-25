.. _sys-exceptions:

==================
Exception Handling
==================

:mod:`sys` includes features for trapping and working with exceptions.

Unhandled Exceptions
====================

Many applications are structured with a main loop that wraps execution in a global exception handler to trap errors not handled at a lower level.  Another way to achieve the same thing is by setting the ``sys.excepthook`` to a function that takes three arguments (error type, error value, and traceback) and let it deal with unhandled errors.

.. include:: sys_excepthook.py
    :literal:
    :start-after: #end_pymotw_header

Since there is no try:except block around the line where the exception is raised the following print statement is not run, even though the except hook is set.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_excepthook.py', ignore_error=True))
.. }}}
.. {{{end}}}

Current Exception
=================

There are times when an explicit exception handler is preferred, either for code clarity or to avoid conflicts with libraries that try to install their own excepthook.  In these cases you may want to write a common handler function, but avoid passing the exception object to it explicitly.  You can get the current exception for a thread by calling ``exc_info()``.  

The return value of ``exc_info()`` is a three member tuple containing the exception class, an exception instance, and a traceback.  Using ``exc_info()`` is preferred over the old form (with ``exc_type``, ``exc_value``, and ``exc_traceback``) because it is thread-safe.

.. include:: sys_exc_info.py
    :literal:
    :start-after: #end_pymotw_header

.. note:: This example avoids introducing a circular reference between the traceback and a local variable in the current frame by ignoring that part of the return value from ``exc_info()``.  If you do need the traceback for some reason (such as to log it), you should explicitly delete the local variable when you're done (using ``del``) to avoid cycles.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_exc_info.py'))
.. }}}
.. {{{end}}}

Previous Interactive Exception
==============================

In the interactive interpreter, there is only one thread of interaction.  Unhandled exceptions in that thread are saved to three variables in :mod:`sys` (``last_type``, ``last_value``, and ``last_traceback``) to make it easy to retrieve them for debugging.  With the post-mortem debugger in :mod:`pdb` you don't have to use the values directly.

::

    $ python
    Python 2.6.2 (r262:71600, Apr 16 2009, 09:17:39) 
    [GCC 4.0.1 (Apple Computer, Inc. build 5250)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> def cause_exception():
    ...   raise RuntimeError('This is the error message')
    ... 
    >>> cause_exception()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 2, in cause_exception
    RuntimeError: This is the error message
    >>> import pdb
    >>> pdb.pm()
    > <stdin>(2)cause_exception()
    (Pdb) where
      <stdin>(1)<module>()
    > <stdin>(2)cause_exception()
    (Pdb) 


.. seealso::
    
    :mod:`exceptions`
        Built-in errors

    :mod:`pdb`
        Python debugger

    :mod:`traceback`
        Module for working with tracebacks.
