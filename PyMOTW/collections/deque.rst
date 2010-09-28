.. _deque:

=======
 Deque
=======

A double-ended queue, or :class:`deque`, supports adding and removing
elements from either end. The more commonly used stacks and queues are
degenerate forms of deques, where the inputs and outputs are
restricted to a single end.

.. include:: collections_deque.py
    :literal:
    :start-after: #end_pymotw_header

Since deques are a type of sequence container, they support some of
the same operations that lists support, such as examining the contents
with :func:`__getitem__`, determining length, and removing elements
from the middle by matching identity.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_deque.py'))
.. }}}
.. {{{end}}}

Populating
==========

A deque can be populated from either end, termed "left" and "right" in the
Python implementation.

.. include:: collections_deque_populating.py
    :literal:
    :start-after: #end_pymotw_header

Notice that :func:`extendleft` iterates over its input and performs
the equivalent of an :func:`appendleft` for each item. The end result
is the :class:`deque` contains the input sequence in reverse order.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_deque_populating.py'))
.. }}}
.. {{{end}}}

Consuming
=========

Similarly, the elements of the :class:`deque` can be consumed from
both or either end, depending on the algorithm being applied.

.. include:: collections_deque_consuming.py
    :literal:
    :start-after: #end_pymotw_header

Use :func:`pop` to remove an item from the "right" end of the
:class:`deque` and :func:`popleft` to take from the "left" end.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_deque_consuming.py'))
.. }}}
.. {{{end}}}


Since deques are thread-safe, the contents can even be consumed from
both ends at the same time from separate threads.

.. include:: collections_deque_both_ends.py
    :literal:
    :start-after: #end_pymotw_header

The threads in this example alternate between each end, removing items
until the :class:`deque` is empty.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_deque_both_ends.py'))
.. }}}
.. {{{end}}}

Rotating
========

Another useful capability of the :class:`deque` is to rotate it in
either direction, to skip over some items.

.. include:: collections_deque_rotate.py
    :literal:
    :start-after: #end_pymotw_header

Rotating the :class:`deque` to the right (using a positive rotation)
takes items from the right end and moves them to the left
end. Rotating to the left (with a negative value) takes items from the
left end and moves them to the right end.  It may help to visualize
the items in the deque as being engraved along the edge of a dial.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_deque_rotate.py'))
.. }}}
.. {{{end}}}

.. seealso::

    `WikiPedia: Deque <http://en.wikipedia.org/wiki/Deque>`_
        A discussion of the deque data structure.

    `Deque Recipes <http://docs.python.org/lib/deque-recipes.html>`_
        Examples of using deques in algorithms from the standard library documentation.
