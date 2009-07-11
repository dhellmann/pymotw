==================================
struct -- Working with Binary Data
==================================

.. module:: struct
    :synopsis: Convert between strings and binary data.

:Purpose: Convert between strings and binary data.
:Python Version: 1.4 and later

The :mod:`struct` module includes functions for converting between strings of bytes and native Python data types such as numbers and strings.

Functions vs. Struct Class
==========================

There are a set of module-level functions for working with structured values, and there is also the Struct class (new in Python 2.5).  Format specifiers are converted from their string format to a compiled representation, similar to the way regular expressions are.  The conversion takes some resources, so it is typically more efficient to do it once when creating a Struct instance and call methods on the instance instead of using the module-level functions.  All of the examples below use the Struct class.

Packing and Unpacking
=====================

Structs support *packing* data into strings, and *unpacking* data from strings using format specifiers made up of characters representing the type of the data and optional count and endian-ness indicators.  For complete details, refer to `the standard library documentation <http://docs.python.org/library/struct.html>`_.

In this example, the format specifier calls for an integer or long value, a 2 character string, and a floating point number.  The spaces between the format specifiers are included here for clarity, and are ignored when the format is compiled.

.. include:: struct_pack.py
    :literal:
    :start-after: #end_pymotw_header

The packed value is converted to a sequence of hex bytes for printing, since some of the characters are nulls.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'struct_pack.py'))
.. }}}
.. {{{end}}}

If we pass the packed value to :func:`unpack`, we get basically the same values back (note the discrepancy in the floating point value).

.. include:: struct_unpack.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'struct_unpack.py'))
.. }}}
.. {{{end}}}


Endianness
==========

By default values are encoded using the native C library notion of "endianness".  It is easy to override that choice by providing an explicit endianness directive in the format string.

.. include:: struct_endianness.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'struct_endianness.py'))
.. }}}
.. {{{end}}}

Buffers
=======

Working with binary packed data is typically reserved for highly performance sensitive situations or passing data into and out of extension modules.  One way to optimize is to avoid allocating a new buffer for each packed structure.  The :meth:`pack_into` and :meth:`unpack_from` methods support writing to pre-allocated buffers directly.

.. include:: struct_buffers.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'struct_buffers.py'))
.. }}}
.. {{{end}}}


.. seealso::

    `struct <http://docs.python.org/library/struct.html>`_
        The standard library documentation for this module.

    :mod:`array`
        The array module, for working with sequences of fixed-type values.

    :mod:`binascii`
        The binascii module, for producing ASCII representations of binary data.

    `WikiPedia: Endianness <http://en.wikipedia.org/wiki/Endianness>`_
        Explanation of byte order and endianness in encoding.

    :ref:`article-data-structures`
