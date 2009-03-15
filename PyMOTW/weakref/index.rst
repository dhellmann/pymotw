====================================================
weakref -- Garbage-collectable references to objects
====================================================

.. module:: weakref
    :synopsis: Refer to an "expensive" object, but allow it to be garbage collected if there are no other non-weak references.

:Purpose: Refer to an "expensive" object, but allow it to be garbage collected if there are no other non-weak references.
:Python Version: Since 2.1

The weakref module supports weak references to objects. A normal reference
increments the reference count on the object and prevents it from being
garbage collected. This is not always desirable, either when a circular
reference might be present or when building a cache of objects that should be
deleted when memory is needed.

References
==========

Weak references to your objects are managed through the ref class. To retrieve
the original object, call the reference object.

.. include:: weakref_ref.py
    :literal:
    :start-after: #end_pymotw_header

In this case, since obj is deleted before the second call to the reference,
None is returned.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'weakref_ref.py'))
.. }}}
.. {{{end}}}

Reference Callbacks
===================

The ref constructor takes an optional second argument that should be a
callback function to invoke when the referenced object is deleted.

.. include:: weakref_ref_callback.py
    :literal:
    :start-after: #end_pymotw_header

The callback receives the reference as an argument, after the reference is
"dead" and no longer refers to the original object. This lets you remove the
weak reference object from a cache, for example.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'weakref_ref_callback.py'))
.. }}}
.. {{{end}}}

Proxies
=======

Instead of using ref directly, it can be more convenient to use a proxy.
Proxies can be used as though they were the original object, so you do not
need to call the ref first to access the object.

.. include:: weakref_proxy.py
    :literal:
    :start-after: #end_pymotw_header

If the proxy is access after the referent object is removed, a ReferenceError
exception is raised.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'weakref_proxy.py', ignore_error=True))
.. }}}
.. {{{end}}}

Cyclic References
=================

One use for weak references is to allow cyclic references without preventing
garbage collection. This example illustrates the difference between using
regular objects and proxies when a graph includes a cycle.

First we set up the gc module to help us debug the leak. The DEBUG_LEAK flag
causes it to print information about objects which cannot be seen other than
through the reference the garbage collector has to them. 

::

    # {{{cog include('weakref/weakref_cycle.py', 'gc_setup')}}}
    # {{{end}}}

Next a utility function to exercise the graph class by creating a cycle and
then removing various references.

::

    # {{{cog include('weakref/weakref_cycle.py', 'demo')}}}
    # {{{end}}}

Now a naive Graph class that accepts any object given to it as the "next" node
in the sequence. For the sake of brevity, this Graph supports a single
outgoing reference from each node, which results in very boring graphs but
makes it easy to recreate cycles.

::

    # {{{cog include('weakref/weakref_cycle.py', 'graph')}}}
    # {{{end}}}

If we run the script we see:

::

    # {{{cog include('weakref/weakref_cycle.py', 'without_proxy')}}}
    # {{{end}}}

Even after deleting the local references to the Graph instances in
demo(), the graphs all show up in the garbage list and cannot be collected.
The dictionaries in the garbage list hold the attributes of the Graph
instances. We can forcibly delete the graphs, since we know what they are:

::

    # {{{cog include('weakref/weakref_cycle.py', 'break_cycle')}}}
    # {{{end}}}

And now let's define a more intelligent WeakGraph class that knows not to
create cycles using regular references, but to use a weakref.ref when a cycle
is detected.

::

    # {{{cog include('weakref/weakref_cycle.py', 'with_proxy')}}}
    # {{{end}}}


When we put it all together, we get output like:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'weakref_cycle.py'))
.. }}}
.. {{{end}}}


Caching Objects
===============

The ref and proxy classes are considered "low level". While they are useful
for maintaining weak references to individual objects and allowing cycles to
be garbage collected, if you need to create a cache of several objects the
WeakKeyDictionary and WeakValueDictionary provide a more appropriate API.

As you might expect, the WeakValueDictionary uses weak references to the
values it holds, allowing them to be garbage collected when other code is not
actually using them.

To illustrate the difference between memory handling with a regular dictionary
and WeakValueDictionary, let's go experiment with explicitly calling the
garbage collector again:

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
