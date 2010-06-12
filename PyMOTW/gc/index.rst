=======================
gc -- Garbage Collector
=======================

.. module:: gc
    :synopsis: Garbage Collector

:Purpose: Manages memory used by Python objects
:Python Version: 2.1+

:mod:`gc` exposes the underlying memory management mechanism of
Python, the automatic garbage collector.  The module includes
functions for controlling how the collector operates and to examine
the objects known to the system, either pending collection or stuck in
reference cycles and unable to be freed.

Tracing References
==================

You can use the incoming and outgoing references between objects to
find cycles in complex data structures.  If you know the data
structure with the cycle, you can construct custom code to examine its
properties.  If not, you can the :func:`get_referents()` and
:func:`get_referrers()` functions to build generic debugging tools.

For example, :func:`get_referents()` shows the objects *referred to*
by the input arguments.

.. include:: gc_get_referents.py
   :literal:
   :start-after: #end_pymotw_header

In this case, the :class:`Graph` instance ``three`` holds references
to its instance dictionary (in the ``__dict__`` attribute) and its
class.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'gc_get_referents.py'))
.. }}}
.. {{{end}}}

We can use a :mod:`Queue` to perform a breadth-first traversal of all
of the object references and look for cycles.  The elements of the
queue are the reference chain so far, and the next object to examine.
We start with ``three``, and look at everything it refers to.
Skipping classes lets us avoid looking at methods, modules, etc.

.. include:: gc_get_referents_cycles.py
   :literal:
   :start-after: #end_pymotw_header

The cycle in the nodes is easily found by scanning in this way.  The
dictionaries in the chain hold the instance attributes of the Graph
objects.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'gc_get_referents_cycles.py'))
.. }}}
.. {{{end}}}



.. include:: gc_get_referrers.py
   :literal:
   :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'gc_get_referrers.py'))
.. }}}
.. {{{end}}}




.. seealso::

    `gc <http://docs.python.org/library/gc.html>`_
        The standard library documentation for this module.

    :mod:`weakref`
        The :mod:`weakref` module gives you references to objects
        without increasing their reference count, so they can still be
        garbage collected.
