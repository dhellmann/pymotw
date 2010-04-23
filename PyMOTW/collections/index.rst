===================================
collections -- Container data types
===================================

.. module:: collections
    :synopsis: Container data types.

:Purpose: Container data types.
:Python Version: 2.4 and later

The collections module includes container data types beyond the
built-in types list and dict.

Deque
=====

A double-ended queue, or "deque", supports adding and removing elements from
either end. The more commonly used stacks and queues are degenerate forms of
deques, where the inputs and outputs are restricted to a single end.

Since deques are a type of sequence container, they support some of the same
operations that lists support, such as examining the contents with
__getitem__(), determining length, and removing elements from the middle by
matching identity.

.. include:: collections_deque.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python collections_deque.py
    Deque: deque(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    Length: 7
    Left end: a
    Right end: g
    remove(c): deque(['a', 'b', 'd', 'e', 'f', 'g'])


A deque can be populated from either end, termed "left" and "right" in the
Python implementation.

.. include:: collections_deque_populating.py
    :literal:
    :start-after: #end_pymotw_header

Notice that extendleft() iterates over its input and performs the equivalent
of an appendleft() for each item. The end result is the deque contains the
input sequence in reverse order.

::

    $ python collections_deque_populating.py
    extend    : deque(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    append    : deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
    extendleft: deque(['g', 'f', 'e', 'd', 'c', 'b', 'a'])
    appendleft: deque(['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a'])

Similarly, the elements of the deque can be consumed from both or either end,
depending on the algorithm you're applying.

.. include:: collections_deque_consuming.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python collections_deque_consuming.py
    From the right:
    g
    f
    e
    d
    c
    b
    a
    From the left:
    a
    b
    c
    d
    e
    f
    g


Since deques are thread-safe, you can even consume the contents from both ends
at the same time in separate threads.

.. include:: collections_deque_both_ends.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python collections_deque_both_ends.py
        Left: 0
       Right: 10
        Left: 1
       Right: 9
        Left: 2
       Right: 8
        Left: 3
       Right: 7
        Left: 4
       Right: 6
        Left: 5
       Right done
        Left done


Another useful capability of the deque is to rotate it in either direction, to
skip over some item(s).

.. include:: collections_deque_rotate.py
    :literal:
    :start-after: #end_pymotw_header

Rotating the deque to the right (using a positive rotation) takes items from
the right end and moves them to the left end. Rotating to the left (with a
negative value) takes items from the left end and moves them to the right end.
It may help to visualize the items in the deque as being engraved along the
edge of a dial.

::

    $ python collections_deque_rotate.py
    Normal        : deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    Right rotation: deque([8, 9, 0, 1, 2, 3, 4, 5, 6, 7])
    Left rotation : deque([2, 3, 4, 5, 6, 7, 8, 9, 0, 1])


defaultdict
===========

The standard dictionary includes the method setdefault() for retrieving a
value and establishing a default if the value does not exist. By contrast,
defaultdict lets you specify the default up front when it is initialized.

.. include:: collections_defaultdict.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python collections_defaultdict.py
    defaultdict(<function default_factory at 0x7ca70>, {'foo': 'bar'})
    bar
    default value


This works well as long as it is appropriate for all keys to use that same
default. It can be especially useful if the default is a type used for
aggregating or accumulating values, such as a list, set, or even integer. The
standard library documentation includes several examples of using defaultdict
this way.

namedtuple
==========

The standard tuple class uses numerical indexes to access its members.

.. include:: collections_tuple.py
   :literal:
   :start-after: #end_pymotw_header

This makes tuples convenient containers for simple uses.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_tuple.py'))
.. }}}
.. {{{end}}}

On the other hand, remembering which index should be used for each
value can be error prone, especially if the tuple has a lot of fields
and is constructed far from where it is used.  A :class:`namedtuple`
lets you assign names to each member as well, so users of the tuples
can refer to values by name instead of a numerical index.

Namedtuple instances are just as memory efficient as regular tuples
because they do not have per-instance dictionaries.  Each kind of
namedtuple you want to create is represented by its own class, created
by using the ``namedtuple()`` factory function.  The arguments are the
name of the new class and a string containing the names of the
elements.

.. include:: collections_namedtuple_person.py
    :literal:
    :start-after: #end_pymotw_header

As the example illustrates, it is possible to access the fields of the
namedtuple by name using dotted notation (obj.attr) as well as using
the positional indexes of standard tuples.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_namedtuple_person.py'))
.. }}}
.. {{{end}}}


.. seealso::

    `collections <http://docs.python.org/library/collections.html>`_
        The standard library documentation for this module.

    `WikiPedia: Deque <http://en.wikipedia.org/wiki/Deque>`_
        A discussion of the deque data structure.

    `Deque Recipes <http://docs.python.org/lib/deque-recipes.html>`_
        Examples of using deques in algorithms from the standard library documentation.

    `defaultdict examples <http://docs.python.org/lib/defaultdict-examples.html>`_
        Examples of using defaultdict from the standard library documentation.

    `James Tauber: Evolution of Default Dictionaries in Python <http://jtauber.com/blog/2008/02/27/evolution_of_default_dictionaries_in_python/>`_
        Discussion of how defaultdict relates to other means of initializing dictionaries.

    :ref:`article-data-structures`
