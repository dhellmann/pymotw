========================================
bisect -- Maintain lists in sorted order
========================================

.. module:: bisect
    :synopsis: Maintains a list in sorted order without having to call sort each time an item is added to the list.

:Purpose: Maintains a list in sorted order without having to call sort each time an item is added to the list.
:Available In: 1.4

The bisect module implements an algorithm for inserting elements into a list
while maintaining the list in sorted order. This can be much more efficient
than repeatedly sorting a list, or explicitly sorting a large list after it is
constructed.

Example
=======

Let's look at a simple example using bisect.insort(), which inserts items into
a list in sorted order.

.. include:: bisect_example.py
    :literal:
    :start-after: #end_pymotw_header

The output for that script is:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'bisect_example.py'))
.. }}}
.. {{{end}}}

The first column shows the new random number. The second column shows the
position where the number will be inserted into the list. The remainder of
each line is the current sorted list.

This is a simple example, and for the amount of data we are manipulating it
might be faster to simply build the list and then sort it once. But for long
lists, significant time and memory savings can be achieved using an insertion
sort algorithm such as this.

You probably noticed that the result set above includes a few repeated values
(45 and 77). The bisect module provides 2 ways to handle repeats. New values
can be inserted to the left of existing values, or to the right. The insort()
function is actually an alias for insort_right(), which inserts after the
existing value. The corresponding function insort_left() inserts before the
existing value.

If we manipulate the same data using bisect_left() and insort_left(), we end
up with the same sorted list but notice that the insert positions are
different for the duplicate values.

.. include:: bisect_example2.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'bisect_example2.py'))
.. }}}
.. {{{end}}}


In addition to the Python implementation, there is a faster C implementation
available. If the C version is present, that implementation overrides the pure
Python implementation automatically when you import the bisect module.


.. seealso::

    `bisect <http://docs.python.org/library/bisect.html>`_
        The standard library documentation for this module.

    `WikiPedia: Insertion Sort <http://en.wikipedia.org/wiki/Insertion_sort>`_
        A description of the insertion sort algorithm.

    :ref:`article-data-structures`
