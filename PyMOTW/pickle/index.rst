=================================================
pickle and cPickle -- Python object serialization
=================================================

.. module:: pickle
    :synopsis: Python object serialization

.. module:: cPickle
    :synopsis: Python object serialization

:Purpose: Python object serialization
:Python Version: pickle at least 1.4, cPickle 1.5

The pickle module implements an algorithm for turning an arbitrary Python
object into a series of bytes ("serializing" the object). The byte stream can
then be transmitted or stored, and later reconstructed to create a new object
with the same characteristics.

The cPickle module implements the same algorithm, in C instead of Python. It
is many times faster than the Python implementation, but does not allow the
user to subclass from Pickle. If subclassing is not important for your use,
you probably want to use cPickle.

.. warning::

    The documentation for pickle makes clear that it offers no security
    guarantees. Be careful if you use pickle for inter-process communication or
    data storage and do not trust data you cannot verify as secure.

Importing
=========

It is common to first try to import cPickle, giving an alias of "pickle". If that import
fails for any reason, you can then fall back on the native Python implementation in the
pickle module. This gives you the faster implementation, if it is available,
and the portable implementation otherwise.

::

    try:
       import cPickle as pickle
    except:
       import pickle

Encoding and Decoding Data in Strings
=====================================

This first example of pickle encodes a data structure as a string, then prints the string to the console. It defines a data structure made up of entirely native types. Instances of any class can be pickled, as will be illustrated in a later example. I chose native data types to start to keep this first example simple. And now we can use pickle.dumps() to create a string representation of the value of data.

.. include:: pickle_string.py
    :literal:
    :start-after: #end_pymotw_header

By default, the pickle will use only ASCII characters. A more efficient binary
format is also available, but I will be sticking with the ASCII version for
these examples.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'pickle_string.py'))
.. }}}
.. {{{end}}}

Once the data is serialized, you can write it to a file, socket, pipe, etc.
Then later you can read the file and unpickle the data to construct a new
object with the same values.

.. include:: pickle_unpickle.py
    :literal:
    :start-after: #end_pymotw_header

As you see, the newly constructed object is the equal to but not the same
object as the original. No surprise there.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'pickle_unpickle.py'))
.. }}}
.. {{{end}}}


Working with Streams
====================

In addition to dumps() and loads(), pickle provides a couple of convenience
functions for working with file-like streams. It is possible to write multiple
objects to a stream, and then read them from the stream without knowing in
advance how many objects are written or how big they are.

.. include:: pickle_stream.py
    :literal:
    :start-after: #end_pymotw_header


The example simulates streams using StringIO buffers, so we have to play a
little trickery to establish the readable stream. A simple database format
might use pickles to store objects, too, though using the shelve module might
be easier to work with.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'pickle_stream.py'))
.. }}}
.. {{{end}}}

Besides storing data, pickles are very handy for inter-process
communication. For example, using ``os.fork()`` and ``os.pipe()``, one can establish
worker processes which read job instructions from one pipe and write the
results to another pipe. The core code for managing the worker pool and
sending jobs in and receiving responses can be reused, since the job and
response objects don't have to be of a particular class. If you are using
pipes or sockets, do not forget to flush after dumping each object, to push
the data through the connection to the other end.


Problems Reconstructing Objects
===============================

When working with your own classes, you must ensure that the class being
pickled appears in the namespace of the process reading the pickle. Only the
data for the instance is pickled, not the class definition. The class name is
used to find the constructor to create the new object when unpickling. Take
this example, which writes instances of a class to a file:

.. include:: pickle_dump_to_file_1.py
    :literal:
    :start-after: #end_pymotw_header


When I run the script, it will create a file I name as an argument on the
command line:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'pickle_dump_to_file_1.py test.dat'))
.. }}}
.. {{{end}}}

A simplistic attempt to load the resulting pickled objects might look like:

.. include:: pickle_load_from_file_1.py
    :literal:
    :start-after: #end_pymotw_header

This version fails because there is no SimpleObject class available:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'pickle_load_from_file_1.py test.dat', ignore_error=True))
.. }}}
.. {{{end}}}

A corrected version, which imports SimpleObject from the script which dumps
the data, succeeds.

Add:

::

    from pickle_dump_to_file_1 import SimpleObject

to the end of the import list, then run the script:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'pickle_load_from_file_2.py test.dat'))
.. }}}
.. {{{end}}}

There are some special considerations when pickling data types with values
that cannot be pickled (sockets, file handles, database connections, etc.).
Classes which use values which cannot be pickled can define ``__getstate__()`` and
``__setstate__()`` to return a subset of the state of the instance to be pickled.
New-style classes can also define ``__getnewargs__()``, which should return
arguments to be passed to the class memory allocator (``C.__new__()``). Use of
these features is covered in more detail in the standard library
documentation.

.. seealso::

    `pickle <http://docs.python.org/lib/module-pickle.html>`_
        Standard library documentation for this module.

    :mod:`shelve`
        The shelve module.

    *Pickle: An interesting stack language.*
        by Alexandre Vassalotti
        http://peadrop.com/blog/2007/06/18/pickle-an-interesting-stack-language/
