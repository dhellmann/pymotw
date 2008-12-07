=================================
gzip -- Read and write gzip files
=================================

.. module:: gzip
    :synopsis: Read and write gzip files

:Purpose: Read and write gzip files.
:Python Version: 1.5.2 and later

The gzip module provides a file-like interface to GNU zip files, using :mod:`zlib` to compress and uncompress the data.

Writing Compressed Files
========================

The module-level function ``open()`` creates an instance of the file-like class GzipFile.  The usual methods for writing and reading data are provided.  To write data into a compressed file, open the file with mode ``'w'``.

.. include:: gzip_write.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python gzip_write.py
    -rw-r--r--  1 dhellmann  dhellmann  68 Dec  7 10:44 example.txt.gz
    example.txt.gz: gzip compressed data, was "example.txt", last modified: Sun Dec  7 10:44:42 2008, max compression

Different compression levels can be used by passing a *compresslevel* argument.  Valid values range from 1 to 9, inclusive.  Lower values are faster and result in less compression.  Higher values are slower and compress more, up to a point.

.. include:: gzip_compresslevel.py
    :literal:
    :start-after: #end_pymotw_header

The center column of numbers in the output of the script is the size in bytes of the files produced.  As you see, for this input data, the higher compression values do not necessarily pay off in decreased storage space.  Results will vary, depending on the input data.

::

    $ python gzip_compresslevel.py
    Input contains 754688 bytes
    999397133 9839 compress-level-1.gz
    2612203818 8260 compress-level-2.gz
    3676863750 8221 compress-level-3.gz
    4292954809 4160 compress-level-4.gz
    3686111199 4160 compress-level-5.gz
    3075010677 4160 compress-level-6.gz
    2468097299 4160 compress-level-7.gz
    1221970342 4160 compress-level-8.gz
    1820398784 4160 compress-level-9.gz

A GzipFile instance also includes a ``writelines()`` method that can be used to write a sequence of strings.

.. include:: gzip_writelines.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python gzip_writelines.py
    The same line, over and over.
    The same line, over and over.
    The same line, over and over.
    The same line, over and over.
    The same line, over and over.
    The same line, over and over.
    The same line, over and over.
    The same line, over and over.
    The same line, over and over.
    The same line, over and over.


Reading Compressed Data
=======================

To read data back from previously compressed files, simply open the file with mode ``'r'``.

.. include:: gzip_read.py
    :literal:
    :start-after: #end_pymotw_header

This example reads the file written by ``gzip_write.py`` from the previous section.

::

    $ python gzip_read.py
    Contents of the example file go here.
    
While reading a file, it is also possible to seek and read only part of the data.

.. include:: gzip_seek.py
    :literal:
    :start-after: #end_pymotw_header

The ``seek()`` position is relative to the *uncompressed* data, so the caller does not even need to know that the data file is compressed.

::

    $ python gzip_seek.py
    Entire file:
    Contents of the example file go here.

    Starting at position 5 for 10 bytes:
    nts of the

    True


Working with Streams
====================

It is possible to use the GzipFile class directly to compress or uncompress a data stream, instead of an entire file.  This is useful for working with data being transmitted over a socket or from an existing (open) file handle.  A StringIO buffer can also be used.

.. include:: gzip_StringIO.py
    :literal:
    :start-after: #end_pymotw_header

.. note::

    When re-reading the previously compressed data, I pass an explicit length to
    ``read()``.  Leaving the length off resulted in a CRC error, possibly because
    StringIO returned an empty string before reporting EOF.  If you are
    working with streams of compressed data, you may want to prefix the data with
    an integer representing the actual amount of data to be read.

::

    $ python gzip_StringIO.py
    UNCOMPRESSED: 300
    The same line, over and over.
    The same line, over and over.
    The same line, over and over.
    The same line, over and over.
    The same line, over and over.
    The same line, over and over.
    The same line, over and over.
    The same line, over and over.
    The same line, over and over.
    The same line, over and over.
    
    COMPRESSED: 48
    1f8b080097fc3b4902ff0ac94855284ecc4d55c8c9cc4bd551c82f4b2d5248cc4b0133f4b8424665916401000000ffff
    
    RE-READ: 300
    The same line, over and over.
    The same line, over and over.
    The same line, over and over.
    The same line, over and over.
    The same line, over and over.
    The same line, over and over.
    The same line, over and over.
    The same line, over and over.
    The same line, over and over.
    The same line, over and over.


.. seealso::

    `gzip <http://docs.python.org/library/gzip.html>`_
        The standard library documentation for this module.

    :mod:`zlib`
        The zlib module is a lower-level interface to gzip compression.

    :mod:`zipfile`
        The zipfile module gives access to ZIP archives.

    :mod:`bz2`
        The bz2 module uses the bzip2 compression format.

    :mod:`tarfile`
        The tarfile module includes built-in support for reading compressed tar archives.
