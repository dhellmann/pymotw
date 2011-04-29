========================================================
zlib -- Low-level access to GNU zlib compression library
========================================================

.. module:: zlib
    :synopsis: Low-level access to GNU zlib compression library

:Purpose: Low-level access to GNU zlib compression library
:Available In: 2.5 and later

The :mod:`zlib` module provides a lower-level interface to many of the
functions in the :mod:`zlib` compression library from GNU.

Working with Data in Memory
===========================

The simplest way to work with :mod:`zlib` requires holding all of the
data to be compressed or decompressed in memory, and then using
:func:`compress()` and :func:`decompress()`.

.. include:: zlib_memory.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'zlib_memory.py'))
.. }}}
.. {{{end}}}

Notice that for short text, the compressed version can be longer.
While the actual results depend on the input data, for short bits of
text it is interesting to observe the compression overhead.

.. include:: zlib_lengths.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'zlib_lengths.py'))
.. }}}
.. {{{end}}}

Working with Streams
====================

The in-memory approach has obvious drawbacks that make it impractical
for real-world use cases.  The alternative is to use :class:`Compress`
and :class:`Decompress` objects to manipulate streams of data, so that
the entire data set does not have to fit into memory.

The simple server below responds to requests consisting of filenames
by writing a compressed version of the file to the socket used to
communicate with the client.  It has some artificial chunking in place
to illustrate the buffering behavior that happens when the data passed
to :func:`compress()` or :func:`decompress()` doesn't result in a
complete block of compressed or uncompressed output.

.. warning::

    This server has obvious security implications.  Do not run it on a
    system on the open internet or in any environment where security
    might be an issue.

.. include:: zlib_server.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'zlib_server.py'))
.. }}}
.. {{{end}}}

Mixed Content Streams
=====================

The :class:`Decompress` class returned by :func:`decompressobj()` can
also be used in situations where compressed and uncompressed data is
mixed together.  After decompressing all of the data, the
*unused_data* attribute contains any data not used.

.. include:: zlib_mixed.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'zlib_mixed.py'))
.. }}}
.. {{{end}}}


Checksums
=========

In addition to compression and decompression functions, :mod:`zlib`
includes two functions for computing checksums of data,
:func:`adler32()` and :func:`crc32()`.  Neither checksum is billed as
cryptographically secure, and they are only intended for use for data
integrity verification.

Both functions take the same arguments, a string of data and an
optional value to be used as a starting point for the checksum.  They
return a 32-bit signed integer value which can also be passed back on
subsequent calls as a new starting point argument to produce a
*running* checksum.

.. include:: zlib_checksums.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'zlib_checksums.py'))
.. }}}
.. {{{end}}}


The Adler32 algorithm is said to be faster than a standard CRC, but I
found it to be slower in my own tests.

.. include:: zlib_checksum_tests.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'zlib_checksum_tests.py'))
.. }}}
.. {{{end}}}

.. seealso::

    `zlib <http://docs.python.org/library/zlib.html>`_
        The standard library documentation for this module.

    :mod:`gzip`
        The gzip module includes a higher level (file-based) interface to the zlib library.

    http://www.zlib.net/
        Home page for zlib library.

    http://www.zlib.net/manual.html
        Complete zlib documentation.

    :mod:`bz2`
        The bz2 module provides a similar interface to the bzip2 compression library.
