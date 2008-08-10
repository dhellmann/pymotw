===============
dircache
===============
.. module:: dircache
    :synopsis: Cache directory listings, updating when the modification time of a directory changes.

:Module: dircache
:Purpose: Cache directory listings, updating when the modification time of a directory changes.
:Python Version: 1.4 and later
:Abstract:

    The dircache module includes a function for caching directory listings.

Listing Directory Contents
==========================

The main function in the dircache API is listdir(), a wrapper around
os.listdir() that caches the results and returns the same list each time it is
called with the a path unless the modification date of the named directory
changes.

::

    import dircache

    path = '.'
    first = dircache.listdir(path)
    second = dircache.listdir(path)

    print 'Contents :', first
    print 'Identical:', first is second
    print 'Equal    :', first == second

It is important to recognize that the exact same list is returned each time,
so it should not be modified in place.

::

    $ python dircache_listdir.py
    Contents : ['.svn', '__init__.py', 'dircache_annotate.py', 'dircache_listdir.py', 
    'dircache_listdir_file_added.py', 'dircache_reset.py']
    Identical: True
    Equal    : True

Of course, if the contents of the directory changes it is rescanned.

::

    import dircache
    import os

    path = '/tmp'
    file_to_create = os.path.join(path, 'pymotw_tmp.txt')

    # Look at the directory contents
    first = dircache.listdir(path)

    # Create the new file
    open(file_to_create, 'wt').close()

    # Rescan the directory
    second = dircache.listdir(path)

    # Remove the file we created
    os.unlink(file_to_create)

    print 'Identical :', first is second
    print 'Equal     :', first == second
    print 'Difference:', list(set(second) - set(first))

In this case the new file causes a new list to be constructed.

::

    $ python dircache_listdir_file_added.py
    Identical : False
    Equal     : False
    Difference: ['pymotw_tmp.txt']

It is also possible to reset the entire cache, discarding its contents so that
each path will be rechecked.

::

    import dircache

    path = '/tmp'
    first = dircache.listdir(path)
    dircache.reset()
    second = dircache.listdir(path)

    print 'Identical :', first is second
    print 'Equal     :', first == second
    print 'Difference:', list(set(second) - set(first))

::

    $ python dircache_reset.py
    Identical : False
    Equal     : True
    Difference: []


Annotated Listings
==================

The other interesting function provided by the dircache module is annotate().
When called, annotate() modifies a list such as is returned by listdir(),
adding a '/' to the end of the names that represent directories. (Sorry
Windows users, although it uses os.path.join() to construct names to test, it
always appends a '/', not os.sep.)

::

    import dircache
    from pprint import pprint

    path = '../../trunk'

    contents = dircache.listdir(path)

    annotated = contents[:]
    dircache.annotate(path, annotated)

    fmt = '%20s\t%20s'

    print fmt % ('ORIGINAL', 'ANNOTATED')
    print fmt % (('-' * 20,)*2)

    for o, a in zip(contents, annotated):
        print fmt % (o, a)

::

    $ python dircache_annotate.py
                ORIGINAL               ANNOTATED
    --------------------    --------------------
               .DS_Store               .DS_Store
                    .svn                   .svn/
               ChangeLog               ChangeLog
             LICENSE.txt             LICENSE.txt
                MANIFEST                MANIFEST
             MANIFEST.in             MANIFEST.in
          MANIFEST.in.in          MANIFEST.in.in
                Makefile                Makefile
                  PyMOTW                 PyMOTW/
              README.txt              README.txt
             setup.py.in             setup.py.in
          static_content         static_content/
           template.html           template.html


