====================================
gzip -- Read and write GNU zip files
====================================

.. module:: gzip
    :synopsis: Read and write gzip files

:Purpose: Read and write gzip files.
:Available In: 1.5.2 and later

The gzip module provides a file-like interface to GNU zip files, using
:mod:`zlib` to compress and uncompress the data.

Writing Compressed Files
========================

The module-level function ``open()`` creates an instance of the
file-like class GzipFile.  The usual methods for writing and reading
data are provided.  To write data into a compressed file, open the
file with mode ``'w'``.

.. include:: gzip_write.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'gzip_write.py'))
.. }}}
.. {{{end}}}

Different amounts of compression can be used by passing a
*compresslevel* argument.  Valid values range from 1 to 9, inclusive.
Lower values are faster and result in less compression.  Higher values
are slower and compress more, up to a point.

.. include:: gzip_compresslevel.py
    :literal:
    :start-after: #end_pymotw_header

The center column of numbers in the output of the script is the size
in bytes of the files produced.  As you see, for this input data, the
higher compression values do not necessarily pay off in decreased
storage space.  Results will vary, depending on the input data.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'gzip_compresslevel.py'))
.. }}}
.. {{{end}}}


A GzipFile instance also includes a ``writelines()`` method that can
be used to write a sequence of strings.

.. include:: gzip_writelines.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'gzip_writelines.py'))
.. }}}
.. {{{end}}}


Reading Compressed Data
=======================

To read data back from previously compressed files, simply open the
file with mode ``'r'``.

.. include:: gzip_read.py
    :literal:
    :start-after: #end_pymotw_header

This example reads  the file  written by  ``gzip_write.py``  from the
previous section.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'gzip_read.py'))
.. }}}
.. {{{end}}}
    
While reading a file, it is also possible to seek and read only part
of the data.

.. include:: gzip_seek.py
    :literal:
    :start-after: #end_pymotw_header

The ``seek()`` position is relative to the *uncompressed* data, so the
caller does not even need to know that the data file is compressed.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'gzip_seek.py'))
.. }}}
.. {{{end}}}


Working with Streams
====================

When working with a data stream instead of a file, use the GzipFile
class directly to compress or uncompress it.  This is useful when the
data is being transmitted over a socket or from read an existing
(already open) file handle.  A StringIO buffer can also be used.

.. include:: gzip_StringIO.py
    :literal:
    :start-after: #end_pymotw_header

.. note::

    When re-reading the previously compressed data, I pass an explicit length to
    ``read()``.  Leaving the length off resulted in a CRC error, possibly because
    StringIO returned an empty string before reporting EOF.  If you are
    working with streams of compressed data, you may want to prefix the data with
    an integer representing the actual amount of data to be read.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'gzip_StringIO.py'))
.. }}}
.. {{{end}}}


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
