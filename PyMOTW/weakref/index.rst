====================================================
weakref -- Garbage-collectable references to objects
====================================================

.. module:: weakref
    :synopsis: Refer to an "expensive" object, but allow it to be garbage collected if there are no other non-weak references.

:Purpose: Refer to an "expensive" object, but allow it to be garbage collected if there are no other non-weak references.
:Available In: Since 2.1

The :mod:`weakref` module supports weak references to objects. A
normal reference increments the reference count on the object and
prevents it from being garbage collected. This is not always
desirable, either when a circular reference might be present or when
building a cache of objects that should be deleted when memory is
needed.

References
==========

Weak references to your objects are managed through the :class:`ref`
class. To retrieve the original object, call the reference object.

.. include:: weakref_ref.py
    :literal:
    :start-after: #end_pymotw_header

In this case, since ``obj`` is deleted before the second call to the
reference, the :class:`ref` returns ``None``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'weakref_ref.py'))
.. }}}
.. {{{end}}}

Reference Callbacks
===================

The :class:`ref` constructor takes an optional second argument that
should be a callback function to invoke when the referenced object is
deleted.

.. include:: weakref_ref_callback.py
    :literal:
    :start-after: #end_pymotw_header

The callback receives the reference object as an argument, after the
reference is "dead" and no longer refers to the original object. This
lets you remove the weak reference object from a cache, for example.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'weakref_ref_callback.py'))
.. }}}
.. {{{end}}}

Proxies
=======

Instead of using :class:`ref` directly, it can be more convenient to
use a proxy.  Proxies can be used as though they were the original
object, so you do not need to call the :class:`ref` first to access
the object.

.. include:: weakref_proxy.py
    :literal:
    :start-after: #end_pymotw_header

If the proxy is access after the referent object is removed, a
:class:`ReferenceError` exception is raised.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'weakref_proxy.py', ignore_error=True))
.. }}}
.. {{{end}}}

Cyclic References
=================

One use for weak references is to allow cyclic references without preventing
garbage collection. This example illustrates the difference between using
regular objects and proxies when a graph includes a cycle.

First, we need a :class:`Graph` class that accepts any object given to
it as the "next" node in the sequence. For the sake of brevity, this
:class:`Graph` supports a single outgoing reference from each node,
which results in boring graphs but makes it easy to create cycles. The
function :func:`demo()` is a utility function to exercise the graph
class by creating a cycle and then removing various references.

.. include:: weakref_graph.py
   :literal:
   :start-after: #end_pymotw_header

Now we can set up a test program using the :mod:`gc` module to help us
debug the leak. The ``DEBUG_LEAK`` flag causes :mod:`gc` to print
information about objects that cannot be seen other than through the
reference the garbage collector has to them.

.. include:: weakref_cycle.py
   :literal:
   :start-after: #end_pymotw_header

Even after deleting the local references to the :class:`Graph`
instances in :func:`demo()`, the graphs all show up in the garbage
list and cannot be collected.  The dictionaries in the garbage list
hold the attributes of the :class:`Graph` instances. We can forcibly
delete the graphs, since we know what they are:

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u weakref_cycle.py'))
.. }}}
.. {{{end}}}


And now let's define a more intelligent :class:`WeakGraph` class that
knows not to create cycles using regular references, but to use a
:class:`ref` when a cycle is detected.

.. include:: weakref_weakgraph.py
   :literal:
   :start-after: #end_pymotw_header

Since the :class:`WeakGraph` instances use proxies to refer to objects
that have already been seen, as :func:`demo()` removes all local
references to the objects, the cycle is broken and the garbage
collector can delete the objects for us.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'weakref_weakgraph.py'))
.. }}}
.. {{{end}}}


Caching Objects
===============

The :class:`ref` and :class:`proxy` classes are considered "low
level". While they are useful for maintaining weak references to
individual objects and allowing cycles to be garbage collected, if you
need to create a cache of several objects the
:class:`WeakKeyDictionary` and :class:`WeakValueDictionary` provide a
more appropriate API.

As you might expect, the :class:`WeakValueDictionary` uses weak
references to the values it holds, allowing them to be garbage
collected when other code is not actually using them.

To illustrate the difference between memory handling with a regular
dictionary and :class:`WeakValueDictionary`, let's go experiment with
explicitly calling the garbage collector again:

.. include:: weakref_valuedict.py
    :literal:
    :start-after: #end_pymotw_header

Notice that any loop variables that refer to the values we are caching must be
cleared explicitly to decrement the reference count on the object. Otherwise
the garbage collector would not remove the objects and they would remain in
the cache. Similarly, the all_refs variable is used to hold references to
prevent them from being garbage collected prematurely.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'weakref_valuedict.py'))
.. }}}
.. {{{end}}}

The WeakKeyDictionary works similarly but uses weak references for the keys
instead of the values in the dictionary.

The library documentation for weakref contains this warning:

.. warning::

    Caution: Because a WeakValueDictionary is built on top of a Python
    dictionary, it must not change size when iterating over it. This can be
    difficult to ensure for a WeakValueDictionary because actions performed by
    the program during iteration may cause items in the dictionary to vanish
    "by magic" (as a side effect of garbage collection).

.. seealso::

    `weakref <http://docs.python.org/lib/module-weakref.html>`_
        Standard library documentation for this module.

    :mod:`gc`
        The gc module is the interface to the interpreter's garbage collector.
