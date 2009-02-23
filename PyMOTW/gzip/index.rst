====================================
gzip -- Read and write GNU zip files
====================================

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

.. {{{cog
.. cog.out(run_script(cog.inFile, 'gzip_write.py'))
.. }}}

::

	$ python gzip_write.py
	application/x-gzip
	example.txt.gz contains 68 bytes of compressed data

.. {{{end}}}

Different compression levels can be used by passing a *compresslevel* argument.  Valid values range from 1 to 9, inclusive.  Lower values are faster and result in less compression.  Higher values are slower and compress more, up to a point.

.. include:: gzip_compresslevel.py
    :literal:
    :start-after: #end_pymotw_header

The center column of numbers in the output of the script is the size in bytes of the files produced.  As you see, for this input data, the higher compression values do not necessarily pay off in decreased storage space.  Results will vary, depending on the input data.

.. Cannot cog this because the file contains data that changes for some reason (update timestamp?)

::

	$ python gzip_compresslevel.py
	Level  Size        Checksum
	-----  ----------  ---------------------------------
	data       754688  e4c0f9433723971563f08a458715119c
	    1        9839  c4088de2afeb9d4be8dd0ecc95a419c7
	    2        8260  621e3b156084161ccc48599218617cd8
	    3        8221  e59f000f53b82c0243026d85c7c13a6f
	    4        4160  f3af98abbbc554fe829d75ff97321d4a
	    5        4160  3d81fbcb438ee96688e599783877599b
	    6        4160  ebfbb8101820abdc4b3e59f1642e8f25
	    7        4160  93b62c79406e44fcb8d2d2de27c50663
	    8        4160  a115438bd119453c1908e826b47fc092
	    9        4160  95fc9dca4ee590c6d85c1e4048ea84cb


A GzipFile instance also includes a ``writelines()`` method that can be used to write a sequence of strings.

.. include:: gzip_writelines.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'gzip_writelines.py'))
.. }}}

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

.. {{{end}}}


Reading Compressed Data
=======================

To read data back from previously compressed files, simply open the file with mode ``'r'``.

.. include:: gzip_read.py
    :literal:
    :start-after: #end_pymotw_header

This example reads the file written by ``gzip_write.py`` from the previous section.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'gzip_read.py'))
.. }}}

::

	$ python gzip_read.py
	Contents of the example file go here.
	

.. {{{end}}}
    
While reading a file, it is also possible to seek and read only part of the data.

.. include:: gzip_seek.py
    :literal:
    :start-after: #end_pymotw_header

The ``seek()`` position is relative to the *uncompressed* data, so the caller does not even need to know that the data file is compressed.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'gzip_seek.py'))
.. }}}

::

	$ python gzip_seek.py
	Entire file:
	Contents of the example file go here.
	
	Starting at position 5 for 10 bytes:
	nts of the
	
	True

.. {{{end}}}


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

.. {{{cog
.. cog.out(run_script(cog.inFile, 'gzip_StringIO.py'))
.. }}}

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
	1f8b0800b5e9a14902ff0ac94855284ecc4d55c8c9cc4bd551c82f4b2d5248cc4b0133f4b8424665916401000000ffff
	
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
