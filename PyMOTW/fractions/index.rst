=============================
fractions -- Rational Numbers
=============================

.. module:: fractions
    :synopsis: Implements a class for working with rational numbers.

:Purpose: Implements a class for working with rational numbers.
:Python Version: 2.6 and later

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


Rational Math
=============




.. seealso::

    `fractions <http://docs.python.org/library/fractions.html>`_
        The standard library documentation for this module.

    :mod:`decimal`
        The decimal module provides an API for fixed and floating point math.

    :mod:`numbers`
        Numeric abstract base classes.