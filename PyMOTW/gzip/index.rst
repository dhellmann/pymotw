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

.. {{{cog
.. cog.out(run_script(cog.inFile, 'gzip_compresslevel.py'))
.. }}}

::

	$ python gzip_compresslevel.py
	Input contains 754688 bytes
	
	Level  Size        Checksum
	-----  ----------  ---------------------------------
	    1        9839  c8846d31ca545a7a0e8fdd949c54c45a
	    2        8260  27e5aae3ba8bd0d3b198b0a5ffc00596
	    3        8221  3945c1528f3021121a15be354dd5486c
	    4        4160  a0337f59f61cb6cba74e109010f67816
	    5        4160  a2ecdfbf94475207363c110f45ea88f8
	    6        4160  e49bb2a8c96e07d1330bc0d17627b9c5
	    7        4160  11af8a85058684d8434baf0c4fbcab78
	    8        4160  ada8a279ccb0d83061eccc3899dcf2c9
	    9        4160  0ad228f1007db41284284ba702009f3a

.. {{{end}}}

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
	1f8b080084e3a14902ff0ac94855284ecc4d55c8c9cc4bd551c82f4b2d5248cc4b0133f4b8424665916401000000ffff
	
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
