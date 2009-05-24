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

- show sorting keys and indenting output vs. tight output used for RPC
- separators

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
