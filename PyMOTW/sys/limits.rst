============================
Memory Management and Limits
============================

:ref:`sys` includes several functions for understanding and controlling memory usage.

Reference Counts
================

Python helps you manage memory with garbage collection.  An object is automatically marked to be collected when its reference count drops to zero.  To examine the reference count of an existing object, use ``getrefcount()``.

.. include:: sys_getrefcount.py
    :literal:
    :start-after: #end_pymotw_header

Notice that the count is actually one higher than expected because there is a temporary reference to the object held by ``getrefcount()`` itself.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_getrefcount.py'))
.. }}}
.. {{{end}}}

Object Size
===========

Knowing how many references an object has may help you figure out where you have a cycle or a leak in your memory, but it isn't enough to determine what objects are consuming the *most* memory.  For that, you also need to know how big objects are.

.. include:: sys_getsizeof.py
    :literal:
    :start-after: #end_pymotw_header

The size is reported in bytes.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_getsizeof.py'))
.. }}}
.. {{{end}}}

For a more accurate estimate of the space used by a class, you can provide a ``__sizeof__()`` method to compute the value by aggregating the sizes of attributes of an object.

.. include:: sys_getsizeof_custom.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'sys_getsizeof_custom.py'))
.. }}}
.. {{{end}}}


.. note:: getrecursionlimit, ¡_getframe, 

Limits
======

.. note:: maxint, maxsize, maxunicode, tracebacklimit, float_info

.. seealso::

    :mod:`gc`
        Control the garbage collector via the functions exposed in :mod:`gc`.
