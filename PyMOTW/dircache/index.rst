====================================
dircache -- Cache directory listings
====================================

.. module:: dircache
    :synopsis: Cache directory listings

:Purpose: Cache directory listings, updating when the modification time of a directory changes.
:Available In: 1.4 and later

Listing Directory Contents
==========================

The main function in the :mod:`dircache` API is :func:`listdir`, a
wrapper around :func:`os.listdir` that caches the results and returns
the same :class:`list` each time it is called with a given path, unless the
modification date of the named directory changes.

.. include:: dircache_listdir.py
    :literal:
    :start-after: #end_pymotw_header

It is important to recognize that the exact same :class:`list` is
returned each time, so it should not be modified in place.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'dircache_listdir.py'))
.. }}}
.. {{{end}}}

If the contents of the directory changes, it is rescanned.

.. include:: dircache_listdir_file_added.py
    :literal:
    :start-after: #end_pymotw_header

In this case the new file causes a new :class:`list` to be
constructed.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'dircache_listdir_file_added.py'))
.. }}}
.. {{{end}}}

It is also possible to reset the entire cache, discarding its contents so that
each path will be rechecked.

.. include:: dircache_reset.py
    :literal:
    :start-after: #end_pymotw_header

After resetting, a new :class:`list` instance is returned.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'dircache_reset.py'))
.. }}}
.. {{{end}}}


Annotated Listings
==================

The other interesting function provided by the dircache module is
:func:`annotate`.  When called, :func:`annotate` modifies a
:func:`list` such as is returned by :func:`listdir`, adding a ``'/'``
to the end of the names that represent directories. 

.. include:: dircache_annotate.py
    :literal:
    :start-after: #end_pymotw_header

Unfortunately for Windows users, although :func:`annotate` uses
:func:`os.path.join` to construct names to test, it always appends a
``'/'``, not :data:`os.sep`.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'dircache_annotate.py'))
.. }}}
.. {{{end}}}

.. seealso::

    `dircache <http://docs.python.org/library/dircache.html>`_
        The standard library documentation for this module.

