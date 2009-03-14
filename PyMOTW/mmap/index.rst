==================================================================
mmap -- Memory-map files instead of reading the contents directly.
==================================================================

.. module:: mmap
    :synopsis: Memory-map files instead of reading the contents directly.

:Purpose: Memory-map files instead of reading the contents directly.
:Python Version: 2.1 and later

Use the ``mmap()`` function to create a memory-mapped file. There are differences
in the arguments and behaviors for ``mmap()`` between Unix and Windows, which are
not discussed below. For more details, refer to the library documentation.

The first argument is a fileno, either from the ``fileno()`` method of a file
object or from ``os.open()``. Since you have opened the file before calling
``mmap()``, you are responsible for closing it.

The second argument to ``mmap()`` is a size in bytes for the portion of the file
to map. If the value is 0, the entire file is mapped. You cannot create a
zero-length mapping under Windows. If the size is larger than the current size
of the file, the file is extended.

An optional keyword argument, access, is supported by both platforms. Use
ACCESS_READ for read-only access, ACCESS_WRITE for write-through (assignments
to the memory go directly to the file), or ACCESS_COPY for copy-on-write
(assignments to memory are not written to the file).

File and String API
===================

Memory-mapped files can be treated as mutable strings or file-like objects,
depending on your need. A mapped file supports the expected file API methods,
such as close(), flush(), read(), readline(), seek(), tell(), and write(). It
also supports the string API, with features such as slicing and methods like
find().

Sample Data
===========

All of the examples use the text file lorem.txt, containing a bit of Lorem
Ipsum. For reference, the text of the file is:

.. include:: lorem.txt
    :literal:

Reading
=======

To map a file for read-only access, make sure to pass ``access=mmap.ACCESS_READ``:

.. include:: mmap_read.py
    :literal:
    :start-after: #end_pymotw_header

In this example, even though the call to ``read()`` advances the file pointer, the
slice operation still gives us the same first 10 bytes because the file
pointer is reset. The file pointer tracks the last access, so after using the
slice operation to give us the first 10 bytes for the second time, calling
read gives the next 10 bytes in the file.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'mmap_read.py'))
.. }}}
.. {{{end}}}

Writing
=======

If you need to write to the memory mapped file, start by opening it for
reading and appending (not with 'w', but 'r+') before mapping it. Then use any
of the API method which change the data (write(), assignment to a slice,
etc.).

Here's an example using the default access mode of ACCESS_WRITE and assigning
to a slice to modify part of a line in place:

.. include:: mmap_write_slice.py
    :literal:
    :start-after: #end_pymotw_header

As you can see here, the word shown in bold is replaced in the middle of the
first line:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'mmap_write_slice.py'))
.. }}}
.. {{{end}}}

ACCESS_COPY Mode
================

Using the ACCESS_COPY mode does not write changes to the file on disk. 

.. include:: mmap_write_copy.py
    :literal:
    :start-after: #end_pymotw_header

Note, in this example, that it was necessary to rewind the file handle
separately from the mmap handle.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'mmap_write_copy.py'))
.. }}}
.. {{{end}}}

Regular Expressions
===================

Since a memory mapped file can act like a string, you can use it with other
modules that operate on strings, such as regular expressions. This example
finds all of the sentences with "nulla" in them.

.. include:: mmap_regex.py
    :literal:
    :start-after: #end_pymotw_header


Since the pattern includes two groups, the return value from findall() is a
sequence of tuples. The print statement pulls out the sentence match and
replaces newlines with spaces so the result prints on a single line.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'mmap_regex.py'))
.. }}}
.. {{{end}}}


.. seealso::

    `mmap <http://docs.python.org/lib/module-mmap.html>`_
        Standard library documentation for this module.

    :mod:`os`
        The os module.
