================================
dbm -- Simple database interface
================================

.. module:: dbm
    :synopsis: Simple database interface

:Purpose: Provides an interface to the Unix (n)dbm library.
:Python Version: 1.4 and later

The :mod:`dbm` module provides an interface to one of the dbm libraries, depending on how the module was configured during compilation.

Examples
========

The ``library`` attribute identifies the library being used, by name.

.. include:: dbm_library.py
    :literal:
    :start-after: #end_pymotw_header

Of course, your results will depend on what library ``configure`` was able to find when the interpreter was built.

::

    $ python dbm_library.py
    GNU gdbm

The ``open()`` function follows the same semantics as the :mod:`anydbm` module.

.. seealso::

    `dbm <http://docs.python.org/library/dbm.html>`_
        The standard library documentation for this module.

    :mod:`anydbm`
        The :mod:`anydbm` module.
