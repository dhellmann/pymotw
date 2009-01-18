=======================================
anydbm -- Access to DBM-style databases
=======================================

.. module:: anydbm
    :synopsis: anydbm provides a generic dictionary-like interface to DBM-style, string-keyed databases

:Purpose: anydbm provides a generic dictionary-like interface to DBM-style, string-keyed databases
:Python Version: 1.4 and later

anydbm is a front-end for DBM-style databases that use simple string values as keys to access records containing strings.  It uses the :mod:`whichdb` module to identify :mod:`dbhash`, :mod:`gdbm`, and :mod:`dbm` databases, then opens them with the appropriate module.  It is used as a backend for :mod:`shelve`, which knows how to store objects using :mod:`pickle`.

Creating a New Database
=======================

The storage format for new databases is selected by looking for each of these modules in order:

- :mod:`dbhash`
- :mod:`gdbm`
- :mod:`dbm`
- :mod:`dumbdbm`

The ``open()`` function takes *flags* to control how the database file is managed.  To create a new database when necessary, use ``'c'``.  To always create a new database, use ``'n'``.

.. include:: anydbm_new.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. from paver.path import path
.. from paver.runtime import sh
.. workdir = path(cog.inFile).dirname()
.. sh("cd %s; rm -f /tmp/example.db" % workdir)
.. cog.out(run_script(cog.inFile, 'anydbm_new.py'))
.. }}}

::

	$ python anydbm_new.py
	

.. {{{end}}}


In this example, the file is always re-initialized.  To see what type of database was created, we can use :mod:`whichdb`.

.. include:: anydbm_whichdb.py
    :literal:
    :start-after: #end_pymotw_header

Your results may vary, depending on what modules are installed on your system.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'anydbm_whichdb.py'))
.. }}}

::

	$ python anydbm_whichdb.py
	dbhash

.. {{{end}}}


Opening an Existing Database
============================

To open an existing database, use *flags* of either ``'r'`` (for read-only) or ``'w'`` (for read-write).  You don't need to worry about the format, because existing databases are automatically given to :mod:`whichdb` to identify.  If a file can be identified, the appropriate module is used to open it.

.. include:: anydbm_existing.py
    :literal:
    :start-after: #end_pymotw_header

Once open, ``db`` is a dictionary-like object, with support for the usual methods:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'anydbm_existing.py'))
.. }}}

::

	$ python anydbm_existing.py
	keys(): ['key', 'today', 'author']
	iterating: key value
	iterating: today Sunday
	iterating: author Doug
	db["author"] = Doug

.. {{{end}}}

Error Cases
===========

The keys of the database need to be strings.

.. include:: anydbm_intkeys.py
    :literal:
    :start-after: #end_pymotw_header

Passing another type results in a TypeError.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'anydbm_intkeys.py'))
.. }}}

::

	$ python anydbm_intkeys.py
	Traceback (most recent call last):
	  File "anydbm_intkeys.py", line 16, in <module>
	    db[1] = 'one'
	  File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/bsddb/__init__.py", line 230, in __setitem__
	    _DeadlockWrap(wrapF)  # self.db[key] = value
	  File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/bsddb/dbutils.py", line 62, in DeadlockWrap
	    return function(*_args, **_kwargs)
	  File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/bsddb/__init__.py", line 229, in wrapF
	    self.db[key] = value
	TypeError: Integer keys only allowed for Recno and Queue DB's

.. {{{end}}}

Values must be strings or ``None``.

.. include:: anydbm_intvalue.py
    :literal:
    :start-after: #end_pymotw_header

A similar TypeError is raised if a value is not a string.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'anydbm_intvalue.py'))
.. }}}

::

	$ python anydbm_intvalue.py
	Traceback (most recent call last):
	  File "anydbm_intvalue.py", line 16, in <module>
	    db['one'] = 1
	  File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/bsddb/__init__.py", line 230, in __setitem__
	    _DeadlockWrap(wrapF)  # self.db[key] = value
	  File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/bsddb/dbutils.py", line 62, in DeadlockWrap
	    return function(*_args, **_kwargs)
	  File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/bsddb/__init__.py", line 229, in wrapF
	    self.db[key] = value
	TypeError: Data values must be of type string or None.

.. {{{end}}}

.. seealso::

    Module :mod:`shelve`
        Examples for the :mod:`shelve` module, which uses :mod:`anydbm` to store data.

    `anydbm <http://docs.python.org/library/anydbm.html>`_
        The standard library documentation for this module.
