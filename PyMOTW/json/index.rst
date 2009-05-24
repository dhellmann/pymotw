=============================================
json -- JavaScript Object Notation Serializer
=============================================

.. module:: json
    :synopsis: JavaScript Object Notation Serializer

:Purpose: Encode Python objects as JSON strings, and decode JSON strings into Python objects.
:Python Version: 2.6

The :mod:`json` module provides an API similar to :mod:`pickle` for converting in-memory Python objects to a serialized representation.  Unlike pickle, JSON has the benefit of being implemented in many languages (especially JavaScript), making it suitable for inter-application communication.  JSON is probably most widely used for communicating between the web server and client in an AJAX application, but is not limited to that problem domain.

Encoding and Decoding Simple Data Types
=======================================

The encoder understands Python's native types by default (int, float, list, tuple, dict).  

.. include:: json_simple_types.py
    :literal:
    :start-after: #end_pymotw_header

Values are encoded in a manner very similar to Python's ``repr()`` output.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'json_simple_types.py'))
.. }}}
.. {{{end}}}

Encoding, then re-decoding may not give exactly the same type of object.  

.. include:: json_simple_types_decode.py
    :literal:
    :start-after: #end_pymotw_header

For example, tuples are converted to JSON lists.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'json_simple_types_decode.py'))
.. }}}
.. {{{end}}}

Human-consumable vs. Compact Output
===================================

Another benefit of JSON over pickle is that the results are human-readable.  The ``dumps()`` function accepts several arguments to make the output even nicer.  For example, ``sort_keys`` tells the encoder to output the keys of a dictionary in sorted, instead of random, order.  

.. include:: json_sort_keys.py
    :literal:
    :start-after: #end_pymotw_header

Sorting makes it easier to scan the results by eye, and also makes it possible to compare JSON output in tests.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'json_sort_keys.py'))
.. }}}
.. {{{end}}}

For highly-nested data structures, you will want to specify a value for ``indent``, so the output is formatted nicely as well.

.. include:: json_indent.py
    :literal:
    :start-after: #end_pymotw_header

When indent is a non-negative integer, the output more closely resembles that of :mod:`pprint`, with leading spaces for each level of the data structure matching the indent level.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'json_indent.py'))
.. }}}
.. {{{end}}}

Verbose output like this increases the number of bytes needed to transmit the same amount of data, however, so it isn't the sort of thing you necessarily want to use in a production environment.  In fact, you may want to adjust the settings for separating data in the encoded output to make it even more compact than the default.

.. include:: json_compact_encoding.py
    :literal:
    :start-after: #end_pymotw_header

The ``separators`` argument to ``dumps()`` should be a tuple containing the strings to separate items in a list and keys from values in a dictionary.  The default is ``(', ', ': ')``. By removing the whitespace, we can produce a more compact output.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'json_compact_encoding.py'))
.. }}}
.. {{{end}}}

Encoding Your Own Types
=======================

- skipkeys arg to dumps
- default function
- subclassing encoder

Decoding Your Own Types
=======================

Encoding from the Command Line
==============================

Working with Streams
====================

Non-ASCII Output
================

- ensure_ascii arg to dumps()


.. seealso::

    `json <http://docs.python.org/library/json.html>`_
        The standard library documentation for this module.

    http://json.org/
        JavaScript Object Notation (JSON)
