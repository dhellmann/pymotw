=======================================
contextlib -- Context manager utilities
=======================================

.. module:: contextlib
    :synopsis: Utilities for creating and working with context managers.

:Purpose:
    The contextlib module contains utilities for working with context managers
    and the ``with`` statement.
:Python Version: 2.5


.. note:: 
    Context managers are tied to the ``with`` statement. Since ``with`` is officially part
    of Python 2.6, you have to import it from __future__ before using contextlib
    in Python 2.5.

From Generator to Context Manager
=================================

Creating context managers the traditional way, by writing a class with
``__enter__()`` and ``__exit__()`` methods, is not difficult. But sometimes it is more
overhead than you need just to manage a trivial bit of context. In those sorts
of situations, you can use the contextmanager() decorator to convert a
generator function into a context manager.

The generator should initialize the context, yield exactly one time, then
clean up the context. The value yielded, if any, is bound to the variable in
the as clause of the with statement. Exceptions from within the with block are
re-raised inside the generator, so you can handle them there.

.. include:: contextlib_contextmanager.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'contextlib_contextmanager.py'))
.. }}}
.. {{{end}}}


Nesting Contexts
================

At times it is necessary to manage multiple contexts simultaneously (such as
when copying data between input and output file handles, for example). It is,
of course, possible to nest with statements one inside another. If the outer
contexts do not need their own separate block, though, this adds to the
indention level without giving any real benefit. By using contextlib.nested(),
you can nest the contexts and use a single with statement.

.. include:: contextlib_nested.py
    :literal:
    :start-after: #end_pymotw_header

Notice that the contexts are exited in the reverse order in which they are
entered.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'contextlib_nested.py'))
.. }}}
.. {{{end}}}


Closing Open Handles
====================

The file() class supports the context manager API directly, but some other
objects that represent open handles do not. The example given in the standard
library documentation for contextlib is the object returned from
urllib.urlopen(), and you may have legacy classes in your own code as well. If
you want to ensure that a handle is closed, use contextlib.closing() to create
a context manager for it.

.. include:: contextlib_closing.py
    :literal:
    :start-after: #end_pymotw_header

The handle is closed whether there is an error in the with block or not.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'contextlib_closing.py'))
.. }}}
.. {{{end}}}

.. seealso::

    `contextlib <http://docs.python.org/library/contextlib.html>`_
        The standard library documentation for this module.

    `PEP 343`_
        The ``with`` statement.
        
        .. _PEP 343: http://www.python.org/peps/pep-0343.html

