=======================================
contextlib -- Context manager utilities
=======================================

.. module:: contextlib
    :synopsis: Utilities for creating and working with context managers.

:Purpose: Utilities for creating and working with context managers.
:Available In: 2.5 and later

The :mod:`contextlib` module contains utilities for working with
context managers and the :command:`with` statement.

.. note:: 
    Context managers are tied to the :command:`with` statement. Since
    :command:`with` is officially part of Python 2.6, you have to import it
    from :mod:`__future__` before using contextlib in Python 2.5.

Context Manager API
===================

A *context manager* is responsible for a resource within a code block,
possibly creating it when the block is entered and then cleaning it up
after the block is exited.  For example, files support the context
manager API to make it easy to ensure they are closed after all
reading or writing is done.

.. include:: contextlib_file.py
   :literal:
   :start-after: #end_pymotw_header

A context manager is enabled by the :command:`with` statement, and the
API involves two methods.  The :func:`__enter__` method is run when
execution flow enters the code block inside the :command:`with`.  It
returns an object to be used within the context.  When execution flow
leaves the :command:`with` block, the :func:`__exit__` method of the
context manager is called to clean up any resources being used.

.. include:: contextlib_api.py
   :literal:
   :start-after: #end_pymotw_header

Combining a context manager and the :command:`with` statement is a
more compact way of writing a ``try:finally`` block, since the context
manager's :func:`__exit__` method is always called, even if an
exception is raised.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'contextlib_api.py'))
.. }}}
.. {{{end}}}

:func:`__enter__` can return any object to be associated with a name
specified in the :command:`as` clause of the :command:`with`
statement.  In this example, the :class:`Context` returns an object
that uses the open context.

.. include:: contextlib_api_other_object.py
   :literal:
   :start-after: #end_pymotw_header

It can be a little confusing, but the value associated with the
variable :data:`c` is the object returned by :func:`__enter__` and
*not* the :class:`Context` instance created in the :command:`with`
statement.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'contextlib_api_other_object.py'))
.. }}}
.. {{{end}}}

The :func:`__exit__` method receives arguments containing details of
any exception raised in the :command:`with` block.  

.. include:: contextlib_api_error.py
   :literal:
   :start-after: #end_pymotw_header

If the context manager can handle the exception, :func:`__exit__`
should return a true value to indicate that the exception does not
need to be propagated.  Returning false causes the exception to be
re-raised after :func:`__exit__` returns.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'contextlib_api_error.py', ignore_error=True))
.. }}}
.. {{{end}}}


From Generator to Context Manager
=================================

Creating context managers the traditional way, by writing a class with
:func:`__enter__()` and :func:`__exit__()` methods, is not
difficult. But sometimes it is more overhead than you need just to
manage a trivial bit of context. In those sorts of situations, you can
use the :func:`contextmanager()` decorator to convert a generator
function into a context manager.

.. include:: contextlib_contextmanager.py
    :literal:
    :start-after: #end_pymotw_header

The generator should initialize the context, yield exactly one time,
then clean up the context. The value yielded, if any, is bound to the
variable in the :command:`as` clause of the :command:`with`
statement. Exceptions from within the :command:`with` block are
re-raised inside the generator, so they can be handled there.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'contextlib_contextmanager.py', ignore_error=True))
.. }}}
.. {{{end}}}


Nesting Contexts
================

At times it is necessary to manage multiple contexts simultaneously
(such as when copying data between input and output file handles, for
example). It is possible to nest :command:`with` statements one inside
another. If the outer contexts do not need their own separate block,
though, this adds to the indention level without giving any real
benefit. Using :func:`nested()` nests the contexts using a single
:command:`with` statement.

.. include:: contextlib_nested.py
    :literal:
    :start-after: #end_pymotw_header

Notice that the contexts are exited in the reverse order in which they are
entered.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'contextlib_nested.py'))
.. }}}
.. {{{end}}}

In Python 2.7 and later, :func:`nested` is deprecated because the
:command:`with` statement supports nesting directly.

.. include:: contextlib_nested_with.py
   :literal:
   :start-after: #end_pymotw_header

Each context manager and optional :command:`as` clause are separated
by a comma (``,``).  The effect is similar to using :func:`nested`,
but avoids some of the edge-cases around error handling that
:func:`nested` could not implement correctly.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'contextlib_nested_with.py'))
.. }}}
.. {{{end}}}


Closing Open Handles
====================

The :class:`file` class supports the context manager API directly, but
some other objects that represent open handles do not. The example
given in the standard library documentation for :mod:`contextlib` is
the object returned from :func:`urllib.urlopen`.  There are other
legacy classes that use a :func:`close` method but do not support the
context manager API. To ensure that a handle is closed, use
:func:`closing()` to create a context manager for it.

.. include:: contextlib_closing.py
    :literal:
    :start-after: #end_pymotw_header

The handle is closed whether there is an error in the :command:`with`
block or not.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'contextlib_closing.py'))
.. }}}
.. {{{end}}}

.. seealso::

    `contextlib <http://docs.python.org/library/contextlib.html>`_
        The standard library documentation for this module.

    :pep:`343`
        The :command:`with` statement.

    `Context Manager Types <http://docs.python.org/library/stdtypes.html#typecontextmanager>`__
        Description of the context manager API from the standard library documentation.

    `With Statement Context Managers <http://docs.python.org/reference/datamodel.html#context-managers>`__
        Description of the context manager API from the Python Reference Guide.
