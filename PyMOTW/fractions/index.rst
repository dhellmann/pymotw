=============================
fractions -- Rational Numbers
=============================

.. module:: fractions
    :synopsis: Implements a class for working with rational numbers.

:Purpose: Implements a class for working with rational numbers.
:Available In: 2.6 and later

The Fraction class implements numerical operations for rational numbers based on the API defined by :class:`Rational` in :mod:`numbers`.

Creating Fraction Instances
===========================

As with :mod:`decimal`, new values can be created in several ways.  One easy way is to create them from separate numerator and denominator values:

.. include:: fractions_create_integers.py
    :literal:
    :start-after: #end_pymotw_header

The lowest common denominator is maintained as new values are computed.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'fractions_create_integers.py'))
.. }}}
.. {{{end}}}

Another way to create a Fraction is using a string representation of ``<numerator> / <denominator>``:

.. include:: fractions_create_strings.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'fractions_create_strings.py'))
.. }}}
.. {{{end}}}

Strings can also use the more usual decimal or floating point notation of ``[<digits>].[<digits>]``.

.. include:: fractions_create_strings_floats.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'fractions_create_strings_floats.py'))
.. }}}
.. {{{end}}}

There are class methods for creating Fraction instances directly from other representations of rational values such as float or :mod:`decimal`.

.. include:: fractions_from_float.py
    :literal:
    :start-after: #end_pymotw_header

Notice that for floating point values that cannot be expressed exactly the rational representation may yield unexpected results.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'fractions_from_float.py'))
.. }}}
.. {{{end}}}

Using :mod:`decimal` representations of the values gives the expected results.

.. include:: fractions_from_decimal.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'fractions_from_decimal.py'))
.. }}}
.. {{{end}}}



Arithmetic
==========

Once the fractions are instantiated, they can be used in mathematical expressions as you would expect.

.. include:: fractions_arithmetic.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'fractions_arithmetic.py'))
.. }}}
.. {{{end}}}

Approximating Values
====================

A useful feature of Fraction is the ability to convert a floating point number to an approximate rational value by limiting the size of the denominator.

.. include:: fractions_limit_denominator.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'fractions_limit_denominator.py'))
.. }}}
.. {{{end}}}


.. seealso::

    `fractions <http://docs.python.org/library/fractions.html>`_
        The standard library documentation for this module.

    :mod:`decimal`
        The decimal module provides an API for fixed and floating point math.

    :mod:`numbers`
        Numeric abstract base classes.
