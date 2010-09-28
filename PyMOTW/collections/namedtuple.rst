.. _collections-namedtuple:

============
 namedtuple
============

The standard :class:`tuple` uses numerical indexes to access its
members.

.. include:: collections_tuple.py
   :literal:
   :start-after: #end_pymotw_header

This makes tuples convenient containers for simple uses.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_tuple.py'))
.. }}}
.. {{{end}}}

On the other hand, remembering which index should be used for each
value can lead to errors, especially if the :class:`tuple` has a lot
of fields and is constructed far from where it is used.  A
:class:`namedtuple` assigns names, as well as the numerical index, to
each member.

:class:`namedtuple` instances are just as memory efficient as regular
tuples because they do not have per-instance dictionaries.  Each kind
of :class:`namedtuple` is represented by its own class, created by
using the :func:`namedtuple` factory function.  The arguments are the
name of the new class and a string containing the names of the
elements.

.. include:: collections_namedtuple_person.py
    :literal:
    :start-after: #end_pymotw_header

As the example illustrates, it is possible to access the fields of the
:class:`namedtuple` by name using dotted notation (``obj.attr``) as
well as using the positional indexes of standard tuples.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'collections_namedtuple_person.py'))
.. }}}
.. {{{end}}}
