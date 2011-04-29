=======================
gc -- Garbage Collector
=======================

.. module:: gc
    :synopsis: Garbage Collector

:Purpose: Manages memory used by Python objects
:Available In: 2.1+

:mod:`gc` exposes the underlying memory management mechanism of
Python, the automatic garbage collector.  The module includes
functions for controlling how the collector operates and to examine
the objects known to the system, either pending collection or stuck in
reference cycles and unable to be freed.

Tracing References
==================

With :mod:`gc` you can use the incoming and outgoing references
between objects to find cycles in complex data structures.  If you
know the data structure with the cycle, you can construct custom code
to examine its properties.  If not, you can the
:func:`get_referents()` and :func:`get_referrers()` functions to build
generic debugging tools.

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

The garbage collector maintains three lists of objects it sees as it
runs, one for each "generation" tracked by the collector.  As objects
are examined in each generation, they are either collected or they age
into subsequent generations until they finally reach the stage where
they are kept permanently.

The collector routines can be tuned to occur at different frequencies
based on the difference between the number of object allocations and
deallocations between runs.  When the number of allocations minus the
number of deallocations is greater than the threshold for the
generation, the garbage collector is run.  The current thresholds can
be examined with :func:`get_threshold()`.

.. include:: gc_get_threshold.py
   :literal:
   :start-after: #end_pymotw_header

The return value is a tuple with the threshold for each generation.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'gc_get_threshold.py'))
.. }}}
.. {{{end}}}

The thresholds can be changed with :func:`set_threshold()`.  This
example program reads the threshold for generation ``0`` from the
command line, adjusts the :mod:`gc` settings, then allocates a series
of objects.

.. include:: gc_threshold.py
   :literal:
   :start-after: #end_pymotw_header

Different threshold values introduce the garbage collection sweeps at
different times, shown here because debugging is enabled.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u gc_threshold.py 5'))
.. }}}
.. {{{end}}}

A smaller threshold causes the sweeps to run more frequently.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u gc_threshold.py 2'))
.. }}}
.. {{{end}}}



Debugging
=========

Debugging memory leaks can be challenging.  :mod:`gc` includes several
options to expose the inner workings to make the job easier.  The
options are bit-flags meant to be combined and passed to
:func:`set_debug()` to configure the garbage collector while your
program is running.  Debugging information is printed to :ref:`stderr
<sys-input-output>`.

The :const:`DEBUG_STATS` flag turns on statistics reporting, causing
the garbage collector to report when it is running, the number of
objects tracked for each generation, and the amount of time it took to
perform the sweep.

.. include:: gc_debug_stats.py
   :literal:
   :start-after: #end_pymotw_header

This example output shows two separate runs of the collector because
it runs once when it is invoked explicitly, and a second time when the
interpreter exits.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'gc_debug_stats.py'))
.. }}}
.. {{{end}}}

Enabling :const:`DEBUG_COLLECTABLE` and :const:`DEBUG_UNCOLLECTABLE`
causes the collector to report on whether each object it examines can
or cannot be collected.  You need to combine these flags need with
:const:`DEBUG_OBJECTS` so :mod:`gc` will print information about
the objects being held.

.. include:: gc_debug_collectable_objects.py
   :literal:
   :start-after: #end_pymotw_header

The two classes :class:`Graph` and :class:`CleanupGraph` are
constructed so it is possible to create structures that are
automatically collectable and structures where cycles need to be
explicitly broken by the user.

The output shows that the :class:`Graph` instances :obj:`one` and
:obj:`two` create a cycle, but are still collectable because they do
not have a finalizer and their only incoming references are from other
objects that can be collected.  Although :class:`CleanupGraph` has a
finalizer, :obj:`three` is reclaimed as soon as its reference count
goes to zero. In contrast, :obj:`four` and :obj:`five` create a cycle
and cannot be freed.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u gc_debug_collectable_objects.py'))
.. }}}
.. {{{end}}}

The flag :const:`DEBUG_INSTANCES` works much the same way for
instances of old-style classes (not derived from :class:`object`.

.. include:: gc_debug_collectable_instances.py
   :literal:
   :start-after: #end_pymotw_header

In this case, however, the :class:`dict` objects holding the instance
attributes are not included in the output.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u gc_debug_collectable_instances.py'))
.. }}}
.. {{{end}}}

If seeing the uncollectable objects is not enough information to
understand where data is being retained, you can enable
:const:`DEBUG_SAVEALL` to cause :mod:`gc` to preserve all objects it
finds without any references in the :obj:`garbage` list, so you can
examine them.  This is helpful if, for example, you don't have access
to the constructor to print the object id when each object is created.

.. include:: gc_debug_saveall.py
   :literal:
   :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u gc_debug_saveall.py'))
.. }}}
.. {{{end}}}

For simplicity, :const:`DEBUG_LEAK` is defined as a combination of all
of the other options.

.. include:: gc_debug_leak.py
   :literal:
   :start-after: #end_pymotw_header

Keep in mind that because :const:`DEBUG_SAVEALL` is enabled by
:const:`DEBUG_LEAK`, even the unreferenced objects that would normally
have been collected and deleted are retained.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u gc_debug_leak.py'))
.. }}}
.. {{{end}}}


.. seealso::

    `gc <http://docs.python.org/library/gc.html>`_
        The standard library documentation for this module.

    :mod:`weakref`
        The :mod:`weakref` module gives you references to objects
        without increasing their reference count, so they can still be
        garbage collected.

    `Supporting Cyclic Garbage Collection <http://docs.python.org/c-api/gcsupport.html>`__
        Background material from Python's C API documentation.

    `How does Python manage memory? <http://effbot.org/pyfaq/how-does-python-manage-memory.htm>`__
        An article on Python memory management by Fredrik Lundh.
