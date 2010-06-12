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

This example uses a :mod:`Queue` to perform a breadth-first traversal
of all of the object references looking for cycles.  The items
inserted into the queue are tuples containing the reference chain so
far and the next object to examine.  It starts with ``three``, and
look at everything it refers to.  Skipping classes lets us avoid
looking at methods, modules, etc.

.. include:: gc_get_referents_cycles.py
   :literal:
   :start-after: #end_pymotw_header

The cycle in the nodes is easily found by watching for objects that
have already been processed.  To avoid holding references to those
objects, their :func:`id()` values are cached in a set.  The
dictionary objects found in the cycle are the ``__dict__`` values for
the :class:`Graph` instances, and hold their instance attributes.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'gc_get_referents_cycles.py'))
.. }}}
.. {{{end}}}


Forcing Garbage Collection
==========================

Although the garbage collector runs automatically as the interpreter
executes your program, you may want to trigger collection to run at a
specific time when you know there are a lot of objects to free or
there is not much work happening in your application.  Trigger
collection using :func:`collect()`.

.. include:: gc_collect.py
   :literal:
   :start-after: #end_pymotw_header

In this example, the cycle is cleared as soon as collection runs the
first time, since nothing refers to the :class:`Graph` nodes except
themselves.  :func:`collect()` returns the number of "unreachable"
objects it found.  In this case, the value is ``6`` because there are
3 objects with their instance attribute dictionaries.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'gc_collect.py'))
.. }}}
.. {{{end}}}

If :class:`Graph` has a :func:`__del__()` method, however, the garbage
collector cannot break the cycle.  

.. include:: gc_collect_with_del.py
   :literal:
   :start-after: #end_pymotw_header

Because more than one object in the cycle has a finalizer method, the
order in which the objects need to be finalized and then garbage
collected cannot be determined, so the garbage collector plays it safe
and keeps the objects.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'gc_collect_with_del.py'))
.. }}}
.. {{{end}}}

When the cycle is broken, the :class:`Graph` instances can be
collected.

.. include:: gc_collect_break_cycle.py
   :literal:
   :start-after: #end_pymotw_header

Because ``gc.garbage`` holds a reference to the objects from the
previous garbage collection run, it needs to be cleared out after the
cycle is broken to reduce the reference counts so they can be
finalized and freed.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'gc_collect_break_cycle.py'))
.. }}}
.. {{{end}}}


Finding References to Objects that Can't be Collected
=====================================================

Looking for the object holding a reference to something in the garbage
is a little trickier than seeing what an object references.  Because
the code asking about the reference needs to hold a reference itself,
some of the referrers need to be ignored.  This example creates a
graph cycle, then works through the :class:`Graph` instances in the
garbage and removes the reference in the "parent" node.

.. include:: gc_get_referrers.py
   :literal:
   :start-after: #end_pymotw_header

This sort of logic is overkill if you understand why the cycles are
being created in the first place, but if you have an unexplained cycle
in your data using :func:`get_referrers()` can expose the unexpected
relationship.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'gc_get_referrers.py'))
.. }}}
.. {{{end}}}


Collection Thresholds and Generations
=====================================



.. Debugging Flags


.. seealso::

    `gc <http://docs.python.org/library/gc.html>`_
        The standard library documentation for this module.

    :mod:`weakref`
        The :mod:`weakref` module gives you references to objects
        without increasing their reference count, so they can still be
        garbage collected.
