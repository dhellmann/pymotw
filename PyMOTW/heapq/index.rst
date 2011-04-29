=====================================
heapq -- In-place heap sort algorithm
=====================================

.. module:: heapq
    :synopsis: In-place heap sort algorithm

:Purpose:
    The heapq implements a min-heap sort algorithm suitable for use with
    Python's lists.
:Available In: New in 2.3 with additions in 2.5

A *heap* is a tree-like data structure where the child nodes have a
sort-order relationship with the parents. *Binary heaps* can be
represented using a list or array organized so that the children of
element N are at positions 2*N+1 and 2*N+2 (for zero-based
indexes). This layout makes it possible to rearrange heaps in place,
so it is not necessary to reallocate as much memory when adding or
removing items.

A max-heap ensures that the parent is larger than or equal to both of
its children. A min-heap requires that the parent be less than or
equal to its children. Python's heapq module implements a min-heap.

Example Data
============

The examples below use this sample data:

.. include:: heapq_heapdata.py
    :literal:
    :start-after: #end_pymotw_header

The heap output is printed using ``heapq_showtree.py``:

.. include:: heapq_showtree.py
   :literal:
   :start-after: #end_pymotw_header



Creating a Heap
===============

There are 2 basic ways to create a heap, ``heappush()`` and
``heapify()``.

Using ``heappush()``, the heap sort order of the elements is
maintained as new items are added from a data source.

.. include:: heapq_heappush.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'heapq_heappush.py'))
.. }}}
.. {{{end}}}


If the data is already in memory, it is more efficient to use
``heapify()`` to rearrange the items of the list in place.

.. include:: heapq_heapify.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'heapq_heapify.py'))
.. }}}
.. {{{end}}}


Accessing Contents of a Heap
============================

Once the heap is organized correctly, use ``heappop()`` to remove the
element with the lowest value. In this example, adapted from the
stdlib documentation, ``heapify()`` and ``heappop()`` are used to sort
a list of numbers.

.. include:: heapq_heappop.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'heapq_heappop.py'))
.. }}}
.. {{{end}}}


To remove existing elements and replace them with new values in a
single operation, use ``heapreplace()``.

.. include:: heapq_heapreplace.py
    :literal:
    :start-after: #end_pymotw_header

Replacing elements in place lets you maintain a fixed size heap, such
as a queue of jobs ordered by priority.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'heapq_heapreplace.py'))
.. }}}
.. {{{end}}}

Data Extremes
=============

:mod:`heapq` also includes 2 functions to examine an iterable to find
a range of the largest or smallest values it contains. Using
``nlargest()`` and ``nsmallest()`` are really only efficient for
relatively small values of n > 1, but can still come in handy in a few
cases.

.. include:: heapq_extremes.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'heapq_extremes.py'))
.. }}}
.. {{{end}}}

.. seealso::

    `heapq <http://docs.python.org/library/heapq.html>`_
        The standard library documentation for this module.

    `WikiPedia: Heap (data structure) <http://en.wikipedia.org/wiki/Heap_(data_structure)>`_
        A general description of heap data structures.

    :ref:`article-data-structures`
        Other Python data structures.

    :ref:`Queue-PriorityQueue`
        A priority queue implementation from :mod:`Queue` in the
        standard library.
