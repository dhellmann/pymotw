=====================================================
itertools -- Iterator functions for efficient looping
=====================================================

.. module:: itertools
    :synopsis: Iterator functions for efficient looping

:Purpose:
    The itertools module includes a set of functions for working with iterable
    (sequence-like) data sets. 
:Available In: 2.3

The functions provided are inspired by similar features of the "lazy
functional programming language" Haskell and SML. They are intended to
be fast and use memory efficiently, but also to be hooked together to
express more complicated iteration-based algorithms.

Iterator-based code may be preferred over code which uses lists for
several reasons. Since data is not produced from the iterator until it
is needed, all of the data is not stored in memory at the same
time. Reducing memory usage can reduce swapping and other side-effects
of large data sets, increasing performance.

Merging and Splitting Iterators
===============================

The ``chain()`` function takes several iterators as arguments and
returns a single iterator that produces the contents of all of them as
though they came from a single sequence.

.. include:: itertools_chain.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'itertools_chain.py'))
.. }}}
.. {{{end}}}

``izip()`` returns an iterator that combines the elements of several
iterators into tuples. It works like the built-in function ``zip()``,
except that it returns an iterator instead of a list.

.. include:: itertools_izip.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'itertools_izip.py'))
.. }}}
.. {{{end}}}

The ``islice()`` function returns an iterator which returns selected
items from the input iterator, by index. It takes the same arguments
as the slice operator for lists: start, stop, and step. The start and
step arguments are optional.

.. include:: itertools_islice.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'itertools_islice.py'))
.. }}}
.. {{{end}}}

The ``tee()`` function returns several independent iterators (defaults
to 2) based on a single original input. It has semantics similar to
the Unix `tee <http://unixhelp.ed.ac.uk/CGI/man-cgi?tee>`__ utility,
which repeats the values it reads from its input and writes them to a
named file and standard output.

.. include:: itertools_tee.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'itertools_tee.py'))
.. }}}
.. {{{end}}}

Since the new iterators created by ``tee()`` share the input, you
should not use the original iterator any more. If you do consume
values from the original input, the new iterators will not produce
those values:

.. include:: itertools_tee_error.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'itertools_tee_error.py'))
.. }}}
.. {{{end}}}

Converting Inputs
=================

The ``imap()`` function returns an iterator that calls a function on
the values in the input iterators, and returns the results. It works
like the built-in ``map()``, except that it stops when any input
iterator is exhausted (instead of inserting ``None`` values to
completely consume all of the inputs).

In the first example, the lambda function multiplies the input values
by 2. In a second example, the lambda function multiplies 2 arguments,
taken from separate iterators, and returns a tuple with the original
arguments and the computed value.

.. include:: itertools_imap.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'itertools_imap.py'))
.. }}}
.. {{{end}}}


The ``starmap()`` function is similar to ``imap()``, but instead of
constructing a tuple from multiple iterators it splits up the items in
a single iterator as arguments to the mapping function using the ``*``
syntax. Where the mapping function to imap() is called f(i1, i2), the
mapping function to starmap() is called ``f(*i)``.

.. include:: itertools_starmap.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'itertools_starmap.py'))
.. }}}
.. {{{end}}}

Producing New Values
====================

The ``count()`` function returns an interator that produces
consecutive integers, indefinitely. The first number can be passed as
an argument, the default is zero. There is no upper bound argument
(see the built-in ``xrange()`` for more control over the result
set). In this example, the iteration stops because the list argument
is consumed.

.. include:: itertools_count.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'itertools_count.py'))
.. }}}
.. {{{end}}}

The ``cycle()`` function returns an iterator that repeats the contents
of the arguments it is given indefinitely. Since it has to remember
the entire contents of the input iterator, it may consume quite a bit
of memory if the iterator is long. In this example, a counter variable
is used to break out of the loop after a few cycles.

.. include:: itertools_cycle.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'itertools_cycle.py'))
.. }}}
.. {{{end}}}

The ``repeat()`` function returns an iterator that produces the same
value each time it is accessed. It keeps going forever, unless the
optional times argument is provided to limit it.

.. include:: itertools_repeat.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'itertools_repeat.py'))
.. }}}
.. {{{end}}}

It is useful to combine ``repeat()`` with ``izip()`` or ``imap()``
when invariant values need to be included with the values from the
other iterators.

.. include:: itertools_repeat_izip.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'itertools_repeat_izip.py'))
.. }}}
.. {{{end}}}

.. include:: itertools_repeat_imap.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'itertools_repeat_imap.py'))
.. }}}
.. {{{end}}}


Filtering
=========

The ``dropwhile()`` function returns an iterator that returns elements
of the input iterator after a condition becomes false for the first
time. It does not filter every item of the input; after the condition
is false the first time, all of the remaining items in the input are
returned.

.. include:: itertools_dropwhile.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'itertools_dropwhile.py'))
.. }}}
.. {{{end}}}


The opposite of ``dropwhile()``, ``takewhile()`` returns an iterator
that returns items from the input iterator as long as the test
function returns true.

.. include:: itertools_takewhile.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'itertools_takewhile.py'))
.. }}}
.. {{{end}}}


``ifilter()`` returns an iterator that works like the built-in
``filter()`` does for lists, including only items for which the test
function returns true. It is different from ``dropwhile()`` in that
every item is tested before it is returned.

.. include:: itertools_ifilter.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'itertools_ifilter.py'))
.. }}}
.. {{{end}}}


The opposite of ``ifilter()``, ``ifilterfalse()`` returns an iterator
that includes only items where the test function returns false.

.. include:: itertools_ifilterfalse.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'itertools_ifilterfalse.py'))
.. }}}
.. {{{end}}}

.. _itertools-groupby:

Grouping Data
=============

The ``groupby()`` function returns an iterator that produces sets of
values grouped by a common key.

This example from the standard library documentation shows how to group keys
in a dictionary which have the same value:

.. include:: itertools_groupby.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'itertools_groupby.py'))
.. }}}
.. {{{end}}}


This more complicated example illustrates grouping related values based on
some attribute. Notice that the input sequence needs to be sorted on the key
in order for the groupings to work out as expected.

.. include:: itertools_groupby_seq.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'itertools_groupby_seq.py'))
.. }}}
.. {{{end}}}



.. seealso::

    `itertools <http://docs.python.org/library/itertools.html>`_
        The standard library documentation for this module.

    `The Standard ML Basis Library <http://www.standardml.org/Basis/>`_
        The library for SML.

    `Definition of Haskell and the Standard Libraries <http://www.haskell.org/definition/>`_
        Standard library specification for the functional language Haskell.
