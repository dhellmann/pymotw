====================================
array -- Sequence of fixed-type data
====================================

.. module:: array
    :synopsis: Manage sequences of fixed-type numerical data efficiently.

:Purpose: Manage sequences of fixed-type numerical data efficiently.
:Available In: 1.4 and later

The :mod:`array` module defines a sequence data structure that looks
very much like a :class:`list` except that all of the members have to
be of the same type.  The types supported are all numeric or other
fixed-size primitive types such as bytes.

+------------+-------------------+--------------------------+
| Code       | Type              | Minimum size (bytes)     |
+============+===================+==========================+
| ``c``      | character         | 1                        |
+------------+-------------------+--------------------------+
| ``b``      | int               | 1                        |
+------------+-------------------+--------------------------+
| ``B``      | int               | 1                        |
+------------+-------------------+--------------------------+
| ``u``      | Unicode character | 2 or 4 (build-dependent) |
+------------+-------------------+--------------------------+
| ``h``      | int               | 2                        |
+------------+-------------------+--------------------------+
| ``H``      | int               | 2                        |
+------------+-------------------+--------------------------+
| ``i``      | int               | 2                        |
+------------+-------------------+--------------------------+
| ``I``      | long              | 2                        |
+------------+-------------------+--------------------------+
| ``l``      | int               | 4                        |
+------------+-------------------+--------------------------+
| ``L``      | long              | 4                        |
+------------+-------------------+--------------------------+
| ``f``      | float             | 4                        |
+------------+-------------------+--------------------------+
| ``d``      | float             | 8                        |
+------------+-------------------+--------------------------+


array Initialization
====================

An :class:`array` is instantiated with an argument describing the type
of data to be allowed, and possibly an initial sequence of data to
store in the array.

.. include:: array_string.py
    :literal:
    :start-after: #end_pymotw_header

In this example, the array is configured to hold a sequence of bytes
and is initialized with a simple string.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'array_string.py'))
.. }}}
.. {{{end}}}


Manipulating Arrays
===================

An :class:`array` can be extended and otherwise manipulated in the
same ways as other Python sequences.

.. include:: array_sequence.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'array_sequence.py'))
.. }}}
.. {{{end}}}


Arrays and Files
================

The contents of an array can be written to and read from files using
built-in methods coded efficiently for that purpose.

.. include:: array_file.py
    :literal:
    :start-after: #end_pymotw_header

This example illustrates reading the data "raw", directly from the
binary file, versus reading it into a new array and converting the
bytes to the appropriate types.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'array_file.py'))
.. }}}
.. {{{end}}}


Alternate Byte Ordering
=======================

If the data in the array is not in the native byte order, or needs to
be swapped before being written to a file intended for a system with a
different byte order, it is easy to convert the entire array without
iterating over the elements from Python.

.. include:: array_byteswap.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'array_byteswap.py'))
.. }}}
.. {{{end}}}


.. seealso::

    `array <http://docs.python.org/library/array.html>`_
        The standard library documentation for this module.

    :mod:`struct`
        The struct module.

    `Numerical Python <http://www.scipy.org>`_
        NumPy is a Python library for working with large datasets efficiently.

    :ref:`article-data-structures`
