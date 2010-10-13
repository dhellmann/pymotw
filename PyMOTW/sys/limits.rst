.. _sys-limits:

============================
Memory Management and Limits
============================

:mod:`sys` includes several functions for understanding and
controlling memory usage.

Reference Counts
================

Python uses *reference counting* and *garbage collection* for
automatic memory management.  An object is automatically marked to be
collected when its reference count drops to zero.  To examine the
reference count of an existing object, use :func:`getrefcount`.

.. include:: sys_getrefcount.py
    :literal:
    :start-after: #end_pymotw_header

The count is actually one higher than expected because there is a
temporary reference to the object held by :func:`getrefcount` itself.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_getrefcount.py'))
.. }}}
.. {{{end}}}

.. seealso::

    :mod:`gc`
        Control the garbage collector via the functions exposed in :mod:`gc`.

Object Size
===========

Knowing how many references an object has may help find cycles or a
memory leak, but it isn't enough to determine what objects are
consuming the *most* memory.  That requires knowledge about how big
objects are.

.. include:: sys_getsizeof.py
    :literal:
    :start-after: #end_pymotw_header

:func:`getsizeof` reports the size in bytes.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_getsizeof.py'))
.. }}}
.. {{{end}}}

The reported size for a custom class does not include the size of the
attribute values.

.. include:: sys_getsizeof_object.py
    :literal:
    :start-after: #end_pymotw_header

This can give a false impression of the amount of memory being
consumed.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_getsizeof_object.py'))
.. }}}
.. {{{end}}}


For a more complete estimate of the space used by a class, provide a
:func:`__sizeof__` method to compute the value by aggregating the
sizes of attributes of an object.

.. include:: sys_getsizeof_custom.py
    :literal:
    :start-after: #end_pymotw_header

This version adds the base size of the object to the sizes of all of
the attributes stored in the internal :data:`__dict__`.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_getsizeof_custom.py'))
.. }}}
.. {{{end}}}

Recursion
=========

Allowing infinite recursion in a Python application may introduce a
stack overflow in the interpreter itself, leading to a crash. To
eliminate this situation, the interpreter provides a way to control
the maximum recursion depth using :func:`setrecursionlimit` and
:func:`getrecursionlimit`.

.. include:: sys_recursionlimit.py
    :literal:
    :start-after: #end_pymotw_header

Once the recursion limit is reached, the interpreter raises a
:ref:`RuntimeError <exceptions-RuntimeError>` exception so the
program has an opportunity to handle the situation.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_recursionlimit.py'))
.. }}}
.. {{{end}}}


Maximum Values
==============

Along with the runtime configurable values, :mod:`sys` includes
variables defining the maximum values for types that vary from system
to system.

.. include:: sys_maximums.py
    :literal:
    :start-after: #end_pymotw_header

:const:`maxint` is the largest representable regular integer.
:const:`maxsize` is the maximum size of a list, dictionary, string, or
other data structure dictated by the C interpreter's size type.
:const:`maxunicode` is the largest integer Unicode point supported by
the interpreter as currently configured.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_maximums.py'))
.. }}}
.. {{{end}}}

Floating Point Values
=====================

The structure :data:`float_info` contains information about the
floating point type representation used by the interpreter, based on
the underlying system's float implementation.

.. include:: sys_float_info.py
    :literal:
    :start-after: #end_pymotw_header

.. note:: 

    These values depend on the compiler and underlying system.  These
    examples were produced on OS X 10.6.4.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_float_info.py'))
.. }}}
.. {{{end}}}

.. seealso::

    The ``float.h`` C header file for the local compiler contains more
    details about these settings.

Byte Ordering
=============

:const:`byteorder` is set to the native byte order.

.. include:: sys_byteorder.py
   :literal:
   :start-after: #end_pymotw_header

The value is either ``big`` for big-endian or ``little`` for
little-endian.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_byteorder.py'))
.. }}}
.. {{{end}}}

.. seealso::

    `Wikipedia: Endianness <http://en.wikipedia.org/wiki/Byte_order>`__
        Description of big and little endian memory systems.

    :mod:`array`, :mod:`struct`
        Other modules that depend on the byte order.
