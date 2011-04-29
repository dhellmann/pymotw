========================================
decimal -- Fixed and floating point math
========================================

.. module:: decimal
    :synopsis: Fixed and floating point math

:Purpose: Decimal arithmetic using fixed and floating point numbers
:Available In: 2.4 and later

The :mod:`decimal` module implements fixed and floating point
arithmetic using the model familiar to most people, rather than the
IEEE floating point version implemented by most computer hardware.  A
Decimal instance can represent any number exactly, round up or down,
and apply a limit to the number of significant digits.

Decimal
=======

Decimal values are represented as instances of the :class:`Decimal`
class.  The constructor takes as argument an integer, or a string.
Floating point numbers must be converted to a string before being used
to create a :class:`Decimal`, letting the caller explicitly deal with
the number of digits for values that cannot be expressed exactly using
hardware floating point representations.

.. include:: decimal_create.py
    :literal:
    :start-after: #end_pymotw_header

Notice that the floating point value of ``0.1`` is not represented as
an exact value, so the representation as a float is different from the
Decimal value.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'decimal_create.py'))
.. }}}
.. {{{end}}}

Less conveniently, Decimals can also be created from tuples containing
a sign flag (``0`` for positive, ``1`` for negative), a tuple of
digits, and an integer exponent.

.. include:: decimal_tuple.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'decimal_tuple.py'))
.. }}}
.. {{{end}}}


Arithmetic
==========

Decimal overloads the simple arithmetic operators so once you have a
value you can manipulate it in much the same way as the built-in
numeric types.

.. include:: decimal_operators.py
    :literal:
    :start-after: #end_pymotw_header

Decimal operators also accept integer arguments, but floating point
values must be converted to Decimal instances.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'decimal_operators.py'))
.. }}}
.. {{{end}}}


Logarithms
==========

Beyond basic arithmetic, Decimal includes methods to find the base 10
and natural logarithms.

.. include:: decimal_log.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'decimal_log.py'))
.. }}}
.. {{{end}}}



Special Values
==============

In addition to the expected numerical values, :class:`Decimal` can
represent several special values, including positive and negative
values for infinity, "not a number", and zero.

.. include:: decimal_special.py
    :literal:
    :start-after: #end_pymotw_header

Adding to infinite values returns another infinite value.  Comparing
for equality with NaN always returns False and comparing for
inequality always returns true.  Comparing for sort order against NaN
is undefined and results in an error.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'decimal_special.py'))
.. }}}
.. {{{end}}}


Context
=======

So far all of the examples have used the default behaviors of the
decimal module. It is possible to override settings such as the
precision maintained, how rounding is performed, error handling,
etc. All of these settings are maintained via a *context*.  Contexts
can be applied for all Decimal instances in a thread or locally within
a small code region.

Current Context
---------------

To retrieve the current global context, use ``getcontext()``.

.. include:: decimal_getcontext.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'decimal_getcontext.py'))
.. }}}
.. {{{end}}}


Precision
---------

The *prec* attribute of the context controls the precision maintained
for new values created as a result of arithmetic.  Literal values are
maintained as described.

.. include:: decimal_precision.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'decimal_precision.py'))
.. }}}
.. {{{end}}}


Rounding
--------

There are several options for rounding to keep values within the
desired precision.

ROUND_CEILING
  Always round upwards towards infinity.

ROUND_DOWN
  Always round toward zero.

ROUND_FLOOR
  Always round down towards negative infinity.

ROUND_HALF_DOWN
  Rounds away from zero if the last significant digit is greater than
  or equal to 5, otherwise toward zero.

ROUND_HALF_EVEN
  Like ROUND_HALF_DOWN except that if the value is 5 then the
  preceding digit is examined.  Even values cause the result to be
  rounded down and odd digits cause the result to be rounded up.

ROUND_HALF_UP
  Like ROUND_HALF_DOWN except if the last significant digit is 5 the
  value is rounded away from zero.

ROUND_UP
  Round away from zero.

ROUND_05UP
  Round away from zero if the last digit is ``0`` or ``5``, otherwise
  towards zero.

.. include:: decimal_rounding.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'decimal_rounding.py'))
.. }}}
.. {{{end}}}

Local Context
-------------

Using Python 2.5 or later you can also apply the context to a subset
of your code using the ``with`` statement and a context manager.

.. include:: decimal_context_manager.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'decimal_context_manager.py'))
.. }}}
.. {{{end}}}

Per-Instance Context
--------------------

Contexts can be used to construct Decimal instances, applying the precision and rounding arguments to the conversion from the input type.  This lets your application select the precision of constant values separately from the precision of user data.

.. include:: decimal_instance_context.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'decimal_instance_context.py'))
.. }}}
.. {{{end}}}


Threads
-------

The "global" context is actually thread-local, so each thread can potentially be configured using different values.

.. include:: decimal_thread_context.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'decimal_thread_context.py'))
.. }}}
.. {{{end}}}


.. seealso::

    `decimal <http://docs.python.org/library/decimal.html>`_
        The standard library documentation for this module.

    `Wikipedia: Floating Point <http://en.wikipedia.org/wiki/Floating_point>`_
        Article on floating point representations and arithmetic.
