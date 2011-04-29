================================
 math -- Mathematical functions
================================

.. module:: math
    :synopsis: Mathematical functions

:Purpose: Provides functions for specialized mathematical operations.
:Available In: 1.4

The :mod:`math` module implements many of the IEEE functions that would
normally be found in the native platform C libraries for complex
mathematical operations using floating point values, including
logarithms and trigonometric operations.

Special Constants
=================

Many math operations depend on special constants.  :mod:`math`
includes values for π (pi) and e.

.. include:: math_constants.py
   :literal:
   :start-after: #end_pymotw_header

Both values are limited in precision only by the platform's floating
point C library.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_constants.py'))
.. }}}
.. {{{end}}}

Testing for Exceptional Values
==============================

Floating point calculations can result in two types of exceptional
values.  ``INF`` ("infinity") appears when the *double* used to hold a
floating point value overflows from a value with a large absolute
value.

.. include:: math_isinf.py
   :literal:
   :start-after: #end_pymotw_header

When the exponent in this example grows large enough, the square of
*x* no longer fits inside a *double*, and the value is recorded as
infinite.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_isinf.py'))
.. }}}
.. {{{end}}}

Not all floating point overflows result in ``INF`` values, however.
Calculating an exponent with floating point values, in particular,
raises :ref:`OverflowError <exceptions-OverflowError>` instead of
preserving the ``INF`` result.

.. include:: math_overflow.py
   :literal:
   :start-after: #end_pymotw_header

This discrepancy is caused by an implementation difference in the
library used by C Python.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_overflow.py'))
.. }}}
.. {{{end}}}

Division operations using infinite values are undefined.  The result
of dividing a number by infinity is ``NaN`` ("not a number").

.. include:: math_isnan.py
   :literal:
   :start-after: #end_pymotw_header

``NaN`` does not compare as equal to any value, even itself, so to
check for ``NaN`` you must use :func:`isnan`.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_isnan.py'))
.. }}}
.. {{{end}}}

Converting to Integers
======================

The :mod:`math` module includes three functions for converting
floating point values to whole numbers.  Each takes a different
approach, and will be useful in different circumstances.

The simplest is :func:`trunc`, which truncates the digits following
the decimal, leaving only the significant digits making up the whole
number portion of the value.  :func:`floor` converts its input to the
largest preceding integer, and :func:`ceil` (ceiling) produces the
largest integer following sequentially after the input value.

.. include:: math_integers.py
   :literal:
   :start-after: #end_pymotw_header

:func:`trunc` is equivalent to converting to :class:`int` directly.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_integers.py'))
.. }}}
.. {{{end}}}

Alternate Representations
=========================

:func:`modf` takes a single floating point number and returns a tuple
containing the fractional and whole number parts of the input value.

.. include:: math_modf.py
   :literal:
   :start-after: #end_pymotw_header

Both numbers in the return value are floats.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_modf.py'))
.. }}}
.. {{{end}}}

:func:`frexp` returns the mantissa and exponent of a floating point
number, and can be used to create a more portable representation of
the value.

.. include:: math_frexp.py
   :literal:
   :start-after: #end_pymotw_header

:func:`frexp` uses the formula ``x = m * 2**e``, and returns the
values *m* and *e*.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_frexp.py'))
.. }}}
.. {{{end}}}

:func:`ldexp` is the inverse of :func:`frexp`.  

.. include:: math_ldexp.py
   :literal:
   :start-after: #end_pymotw_header

Using the same formula as :func:`frexp`, :func:`ldexp` takes the
mantissa and exponent values as arguments and returns a floating point
number.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_ldexp.py'))
.. }}}
.. {{{end}}}


Positive and Negative Signs
===========================

The absolute value of number is its value without a sign.  Use
:func:`fabs` to calculate the absolute value of a floating point
number.

.. include:: math_fabs.py
   :literal:
   :start-after: #end_pymotw_header

In practical terms, the absolute value of a :class:`float` is
represented as a positive value.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_fabs.py'))
.. }}}
.. {{{end}}}

To determine the sign of a value, either to give a set of values the
same sign or simply for comparison, use :func:`copysign` to set the
sign of a known good value.

.. include:: math_copysign.py
   :literal:
   :start-after: #end_pymotw_header

An extra function like :func:`copysign` is needed because comparing
NaN and -NaN directly with other values does not work.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_copysign.py'))
.. }}}
.. {{{end}}}

Commonly Used Calculations
==========================

Representing precise values in binary floating point memory is
challenging.  Some values cannot be represented exactly, and the more
often a value is manipulated through repeated calculations, the more
likely a representation error will be introduced.  :mod:`math`
includes a function for computing the sum of a series of floating
point numbers using an efficient algorithm that minimize such errors.

.. include:: math_fsum.py
   :literal:
   :start-after: #end_pymotw_header

Given a sequence of ten values each equal to ``0.1``, the expected
value for the sum of the sequence is ``1.0``.  Since ``0.1`` cannot be
represented exactly as a floating point value, however, errors are
introduced into the sum unless it is calculated with :func:`fsum`.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_fsum.py'))
.. }}}
.. {{{end}}}

:func:`factorial` is commonly used to calculate the number of
permutations and combinations of a series of objects.  The factorial
of a positive integer *n*, expressed ``n!``, is defined recursively as
``(n-1)! * n`` and stops with ``0! == 1``.

.. include:: math_factorial.py
   :literal:
   :start-after: #end_pymotw_header

:func:`factorial` only works with whole numbers, but does accept
:class:`float` arguments as long as they can be converted to an
integer without losing value.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_factorial.py'))
.. }}}
.. {{{end}}}

:func:`gamma` is like :func:`factorial`, except it works with real
numbers and the value is shifted down one (gamma is equal to ``(n -
1)!``).

.. include:: math_gamma.py
   :literal:
   :start-after: #end_pymotw_header

Since zero causes the start value to be negative, it is not allowed.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_gamma.py'))
.. }}}
.. {{{end}}}

:func:`lgamma` returns the natural logarithm of the absolute value of
Gamma for the input value.

.. include:: math_lgamma.py
   :literal:
   :start-after: #end_pymotw_header

Using :func:`lgamma` retains more precision than calculating the
logarithm separately using the results of :func:`gamma`.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_lgamma.py'))
.. }}}
.. {{{end}}}

The modulo operator (``%``) computes the remainder of a division
expression (i.e., ``5 % 2 = 1``).  The operator built into the
language works well with integers but, as with so many other floating
point operations, intermediate calculations cause representational
issues that result in a loss of data.  :func:`fmod` provides a more
accurate implementation for floating point values.

.. include:: math_fmod.py
   :literal:
   :start-after: #end_pymotw_header

A potentially more frequent source of confusion is the fact that the
algorithm used by :mod:`fmod` for computing modulo is also different
from that used by ``%``, so the sign of the result is different.
mixed-sign inputs.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_fmod.py'))
.. }}}
.. {{{end}}}

Exponents and Logarithms
========================

Exponential growth curves appear in economics, physics, and other
sciences.  Python has a built-in exponentiation operator ("``**``"),
but :func:`pow` can be useful when you need to pass a callable
function as an argument.

.. include:: math_pow.py
   :literal:
   :start-after: #end_pymotw_header

Raising ``1`` to any power always returns ``1.0``, as does raising any
value to a power of ``0.0``.  Most operations on the not-a-number
value ``nan`` return ``nan``.  If the exponent is less than ``1``,
:func:`pow` computes a root.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_pow.py'))
.. }}}
.. {{{end}}}

Since square roots (exponent of ``1/2``) are used so frequently, there
is a separate function for computing them.

.. include:: math_sqrt.py
   :literal:
   :start-after: #end_pymotw_header

Computing the square roots of negative numbers requires *complex
numbers*, which are not handled by :mod:`math`.  Any attempt to
calculate a square root of a negative value results in a
:ref:`ValueError <exceptions-ValueError>`.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_sqrt.py'))
.. }}}
.. {{{end}}}

The logarithm function finds *y* where ``x = b ** y``.  By default,
:func:`log` computes the natural logarithm (the base is *e*).  If a
second argument is provided, that value is used as the base.

.. include:: math_log.py
   :literal:
   :start-after: #end_pymotw_header

Logarithms where *x* is less than one yield negative results.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_log.py'))
.. }}}
.. {{{end}}}

There are two variations of :func:`log`.  Given floating point
representation and rounding errors the computed value produced by
``log(x, b)`` has limited accuracy, especially for some bases.
:func:`log10` computes ``log(x, 10)``, using a more accurate algorithm
than :func:`log`.

.. include:: math_log10.py
   :literal:
   :start-after: #end_pymotw_header

The lines in the output with trailing ``*`` highlight the inaccurate
values.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_log10.py'))
.. }}}
.. {{{end}}}

:func:`log1p` calculates the Newton-Mercator series (the natural
logarithm of ``1+x``).

.. include:: math_log1p.py
   :literal:
   :start-after: #end_pymotw_header

:func:`log1p` is more accurate for values of *x* very close to zero
because it uses an algorithm that compensates for round-off errors
from the initial addition.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_log1p.py'))
.. }}}
.. {{{end}}}

:func:`exp` computes the exponential function (``e**x``).  

.. include:: math_exp.py
   :literal:
   :start-after: #end_pymotw_header

As with other special-case functions, it uses an algorithm that
produces more accurate results than the general-purpose equivalent
``math.pow(math.e, x)``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_exp.py'))
.. }}}
.. {{{end}}}

:func:`expm1` is the inverse of :func:`log1p`, and calculates ``e**x -
1``.

.. include:: math_expm1.py
   :literal:
   :start-after: #end_pymotw_header

As with :func:`log1p`, small values of *x* lose precision when the
subtraction is performed separately.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_expm1.py'))
.. }}}
.. {{{end}}}

Angles
======

Although degrees are more commonly used in everyday discussions of
angles, radians are the standard unit of angular measure in science
and math.  A radian is the angle created by two lines intersecting at
the center of a circle, with their ends on the circumference of the
circle spaced one radius apart.  

The circumference is calculated as ``2πr``, so there is a relationship
between radians and π, a value that shows up frequently in
trigonometric calculations.  That relationship leads to radians being
used in trigonometry and calculus, because they result in more compact
formulas.

To convert from degrees to radians, use :func:`radians`.

.. include:: math_radians.py
   :literal:
   :start-after: #end_pymotw_header

The formula for the conversion is ``rad = deg * π / 180``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_radians.py'))
.. }}}
.. {{{end}}}

To convert from radians to degrees, use :func:`degrees`.

.. include:: math_degrees.py
   :literal:
   :start-after: #end_pymotw_header

The formula is ``deg = rad * 180 / π``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_degrees.py'))
.. }}}
.. {{{end}}}


Trigonometry
============

Trigonometric functions relate angles in a triangle to the lengths of
its sides.  They show up in formulas with periodic properties such as
harmonics, circular motion, or when dealing with angles.

.. note::

  All of the trigonometric functions in the standard library take
  angles expressed as radians.

Given an angle in a right triangle, the *sine* is the ratio of the
length of the side opposite the angle to the hypotenuse (``sin A =
opposite/hypotenuse``).  The *cosine* is the ratio of the length of
the adjacent side to the hypotenuse (``cos A = adjacent/hypotenuse``).
And the *tangent* is the ratio of the opposite side to the adjacent
side (``tan A = opposite/adjacent``).

.. include:: math_trig.py
   :literal:
   :start-after: #end_pymotw_header

The tangent can also be defined as the ratio of the sine of the angle
to its cosine, and since the cosine is 0 for π/2 and 3π/2 radians, the
tangent is infinite.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_trig.py'))
.. }}}
.. {{{end}}}

Given a point (*x*, *y*), the length of the hypotenuse for the
triangle between the points [(0, 0), (*x*, 0), (*x*, *y*)] is
``(x**2 + y**2) ** 1/2``, and can be computed with :func:`hypot`.

.. include:: math_hypot.py
   :literal:
   :start-after: #end_pymotw_header

Points on the circle always have hypotenuse == ``1``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_hypot.py'))
.. }}}
.. {{{end}}}

The same function can be used to find the distance between two points.

.. include:: math_distance_2_points.py
   :literal:
   :start-after: #end_pymotw_header

Use the difference in the *x* and *y* values to move one endpoint to
the origin, and then pass the results to :func:`hypot`.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_distance_2_points.py'))
.. }}}
.. {{{end}}}

:mod:`math` also defines inverse trigonometric functions.

.. include:: math_inverse_trig.py
   :literal:
   :start-after: #end_pymotw_header

``1.57`` is roughly equal to ``π/2``, or 90 degrees, the angle at
which the sine is 1 and the cosine is 0.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_inverse_trig.py'))
.. }}}
.. {{{end}}}

.. atan2

Hyperbolic Functions
====================

Hyperbolic functions appear in linear differential equations and are
used when working with electromagnetic fields, fluid dynamics, special
relativity, and other advanced physics and mathematics.

.. include:: math_hyperbolic.py
   :literal:
   :start-after: #end_pymotw_header

Whereas the cosine and sine functions enscribe a circle, the
hyperbolic cosine and hyperbolic sine form half of a hyperbola.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_hyperbolic.py'))
.. }}}
.. {{{end}}}

Inverse hyperbolic functions :func:`acosh`, :func:`asinh`, and
:func:`atanh` are also available.

Special Functions
=================

The Gauss Error function is used in statistics.

.. include:: math_erf.py
   :literal:
   :start-after: #end_pymotw_header

Notice that ``erf(-x) == -erf(x)``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_erf.py'))
.. }}}
.. {{{end}}}

The complimentary error function is ``1 - erf(x)``.

.. include:: math_erfc.py
   :literal:
   :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'math_erfc.py'))
.. }}}
.. {{{end}}}


.. seealso::

    `math <http://docs.python.org/library/math.html>`_
        The standard library documentation for this module.

    `IEEE floating point arithmetic in Python <http://www.johndcook.com/blog/2009/07/21/ieee-arithmetic-python/>`__
        Blog post by John Cook about how special values arise and are
        dealt with when doing math in Python.

    `SciPy <http://scipy.org/>`_
        Open source libraryes for scientific and mathematical
        calculations in Python.
