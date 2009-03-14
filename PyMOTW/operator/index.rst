=======================================================
operator -- Functional interface to built-in operators.
=======================================================

.. module:: operator
    :synopsis: Functional interface to built-in operators.

:Purpose: Functional interface to built-in operators.
:Python Version: 1.4 and later

Functional programming using iterators occasionally requires you to create
small functions for simple expressions. Sometimes these can be expressed as
lambda functions. But for some operations, you don't need to define your own
function at all. The operator module defines functions that correspond to
built-in operations for arithmetic, and comparison as well as sequence and
dictionary operations.

Logical Operations
==================

There are logical operations for determining the boolean equivalent for a
value, negating that to create the opposite boolean value, and comparing
objects to see if they are identical.

.. include:: operator_boolean.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'operator_boolean.py'))
.. }}}
.. {{{end}}}


Comparison Operators
====================

All of the rich comparison operators are supported:

.. include:: operator_comparisons.py
    :literal:
    :start-after: #end_pymotw_header

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

  There are separate two division operators: ``floordiv`` (pre-3.0 integer division) 
  and ``truediv`` (floating point division).

.. {{{cog
.. cog.out(run_script(cog.inFile, 'operator_math.py'))
.. }}}
.. {{{end}}}



Sequence Operators
==================

The operators for working with sequences can be divided into roughly 4 groups
for building up sequences, searching, working with items, and removing items
from sequences.

.. include:: operator_sequences.py
    :literal:
    :start-after: #end_pymotw_header

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

These examples only demonstrate a couple of the functions. Refer to the stdlib
documentation for complete details.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'operator_inplace.py'))
.. }}}
.. {{{end}}}


Attribute and Item "Getters"
============================

One of the most unusual features of the operator module is the notion of
*getters*. These are callable objects constructed at runtime to retrieve
attributes of items from objects or sequences. Getters are especially useful
when working with iterators or generator sequences, where they are intended to
incur less overhead than a lambda or Python function.

Attribute getters work like ``lambda x, n='attrname': getattr(x, n)``:

.. include:: operator_attrgetter.py
    :literal:
    :start-after: #end_pymotw_header

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



Working With Your Own Classes
=============================

The functions in the operator module work via the standard Python interfaces
for their operations, so they work with your classes as well as the built-in
types.

.. include:: operator_classes.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'operator_classes.py'))
.. }}}
.. {{{end}}}



Type Checking
=============

Besides the actual operators, there are functions for testing API compliance
for mapping, number, and sequence types. The tests are not perfect, since the
interfaces are not strictly defined, but they do give you some idea of what is
supported.

.. include:: operator_typechecking.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'operator_typechecking.py'))
.. }}}
.. {{{end}}}



.. seealso::

    `operator <http://docs.python.org/lib/module-operator.html>`_
        Standard library documentation for this module.
