========================================================
 operator -- Functional interface to built-in operators
========================================================

.. module:: operator
    :synopsis: Functional interface to built-in operators

:Purpose: Functional interface to built-in operators.
:Available In: 1.4 and later

Functional programming using iterators occasionally requires creating
small functions for simple expressions. Sometimes these can be
expressed as lambda functions, but some operations do not need to be
implemented with custom functions at all. The :mod:`operator` module
defines functions that correspond to built-in operations for
arithmetic and comparison, as well as sequence and dictionary
operations.

Logical Operations
==================

There are functions for determining the boolean equivalent for a
value, negating that to create the opposite boolean value, and
comparing objects to see if they are identical.

.. include:: operator_boolean.py
    :literal:
    :start-after: #end_pymotw_header

:func:`not_` includes the trailing underscore because :command:`not`
is a Python keyword.  :func:`truth` applies the same logic used when
testing an expression in an :command:`if` statement.  :func:`is_`
implements the same check used by the :command:`is` keyword, and
:func:`is_not` does the same test and returns the opposite answer.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'operator_boolean.py'))
.. }}}
.. {{{end}}}


Comparison Operators
====================

All of the rich comparison operators are supported.

.. include:: operator_comparisons.py
    :literal:
    :start-after: #end_pymotw_header

The functions are equivalent to the expression syntax using ``<``,
``<=``, ``==``, ``>=``, and ``>``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'operator_comparisons.py'))
.. }}}
.. {{{end}}}


Arithmetic Operators
====================

The arithmetic operators for manipulating numerical values are also supported.

.. include:: operator_math.py
    :literal:
    :start-after: #end_pymotw_header

.. note::

  There are two separate division operators: :func:`floordiv` (integer
  division as implemented in Python before version 3.0) and
  :func:`truediv` (floating point division).

.. {{{cog
.. cog.out(run_script(cog.inFile, 'operator_math.py'))
.. }}}
.. {{{end}}}



Sequence Operators
==================

The operators for working with sequences can be divided into four
groups for building up sequences, searching for items, accessing
contents, and removing items from sequences.

.. include:: operator_sequences.py
    :literal:
    :start-after: #end_pymotw_header

Some of these operations, such as :func:`setitem` and :func:`delitem`,
modify the sequence in place and do not return a value.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'operator_sequences.py'))
.. }}}
.. {{{end}}}



In-place Operators
==================

In addition to the standard operators, many types of objects support
"in-place" modification through special operators such as ``+=``. There are
equivalent functions for in-place modifications, too:

.. include:: operator_inplace.py
    :literal:
    :start-after: #end_pymotw_header

These examples only demonstrate a few of the functions. Refer to the stdlib
documentation for complete details.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'operator_inplace.py'))
.. }}}
.. {{{end}}}


Attribute and Item "Getters"
============================

One of the most unusual features of the :mod:`operator` module is the
concept of *getters*. These are callable objects constructed at
runtime to retrieve attributes of objects or contents from
sequences. Getters are especially useful when working with iterators
or generator sequences, where they are intended to incur less overhead
than a lambda or Python function.

.. include:: operator_attrgetter.py
    :literal:
    :start-after: #end_pymotw_header

Attribute getters work like ``lambda x, n='attrname': getattr(x, n)``:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'operator_attrgetter.py'))
.. }}}
.. {{{end}}}

While item getters work like ``lambda x, y=5: x[y]``:

.. include:: operator_itemgetter.py
    :literal:
    :start-after: #end_pymotw_header

Item getters work with mappings as well as sequences.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'operator_itemgetter.py'))
.. }}}
.. {{{end}}}



Combining Operators and Custom Classes
======================================

The functions in the :mod:`operator` module work via the standard
Python interfaces for their operations, so they work with user-defined
classes as well as the built-in types.

.. include:: operator_classes.py
    :literal:
    :start-after: #end_pymotw_header

Refer to the Python reference guide for a complete list of the special
methods used by each operator.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'operator_classes.py'))
.. }}}
.. {{{end}}}



Type Checking
=============

Besides the actual operators, there are functions for testing API
compliance for mapping, number, and sequence types. 

.. include:: operator_typechecking.py
    :literal:
    :start-after: #end_pymotw_header

The tests are not perfect, since the interfaces are not strictly
defined, but they do provide some idea of what is supported.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'operator_typechecking.py'))
.. }}}
.. {{{end}}}

:mod:`abc` includes :ref:`abstract base classes
<abc-collection-types>` that define the APIs for collection types.


.. seealso::

    `operator <http://docs.python.org/lib/module-operator.html>`_
        Standard library documentation for this module.

    :mod:`functools`
        Functional programming tools, including the
        :func:`total_ordering` decorator for adding rich comparison
        methods to a class.

    :mod:`itertools`
        Iterator operations.
