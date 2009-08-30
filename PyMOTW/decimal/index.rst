========================================
decimal -- Fixed and floating point math
========================================

.. module:: decimal
    :synopsis: Fixed and floating point math

:Purpose: Decimal arithmetic using fixed and floating point numbers
:Python Version: 2.4 and later

The :mod:`decimal` module implements fixed and floating point arithmetic using the model familiar to most people, rather than the IEEE floating point version implemented by most computer hardware.  A Decimal instance can represent any number exactly, round up or down, and apply a limit to the number of significant digits.

Decimal
=======

Decimal values are represented as instances of the :class:`Decimal` class.  The constructor takes as argument an integer, or a string.  Floating point numbers must be converted to a string before being used to create a :class:`Decimal`, letting the caller explicitly deal with the number of digits for values that cannot be expressed exactly using hardware floating point representations.

.. include:: decimal_create.py
    :literal:
    :start-after: #end_pymotw_header

Notice that the floating point value of ``0.1`` is not represented as an exact value, so the representation as a float is different from the Decimal value.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'decimal_create.py'))
.. }}}
.. {{{end}}}

Less conveniently, Decimals can also be created from tuples containing a sign flag (``0`` for positive, ``1`` for negative), a tuple of digits, and an integer exponent.

.. include:: decimal_tuple.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'decimal_tuple.py'))
.. }}}
.. {{{end}}}


Basic Arithmetic
================

Decimal overloads the simple arithmetic operators so once you have a value you can manipulate it in much the same way as the built-in numeric types.

.. include:: decimal_operators.py
    :literal:
    :start-after: #end_pymotw_header

Decimal operators also accept integer arguments, but floating point values must be converted to Decimal instances.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'decimal_operators.py'))
.. }}}
.. {{{end}}}


Trig Methods
------------



Special Values
--------------

In addition to the expected numerical values, :class:`Decimal` can represent several special values, including positive and negative values for infinity, "not a number", and zero.

.. include:: decimal_special.py
    :literal:
    :start-after: #end_pymotw_header

Adding to infinite values returns another infinite value.  Comparing for equality with NaN always returns False and comparing for inequality always returns true.  Comparing for sort order against NaN is undefined and results in an error.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'decimal_special.py'))
.. }}}
.. {{{end}}}


Context
=======

Rounding
--------

Threads
-------

Built-in Contexts
-----------------

Signals
=======

silent errors


.. seealso::

    `decimal <http://docs.python.org/library/decimal.html>`_
        The standard library documentation for this module.

    `Wikipedia: Floating Point <http://en.wikipedia.org/wiki/Floating_point>`_
        Article on floating point representations and arithmetic.
