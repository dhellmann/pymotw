===========================
grp -- Unix Group Database
===========================

.. module:: grp
    :synopsis: Unix Group Database

:Purpose: Read group data from Unix group database.
:Available In: 1.4 and later

The grp module can be used to read information about Unix groups from
the group database (usually ``/etc/group``).  The read-only interface
returns tuple-like objects with named attributes for the standard
fields of a group record.

===== ========= =======
Index Attribute Meaning
===== ========= =======
 0    gr_name   Name
 1    gr_passwd Password, if any (encrypted)
 2    gr_gid    Numerical id (integer)
 3    gr_mem    Names of group members
===== ========= =======

The name and password values are both strings, the GID is an integer,
and the members are reported as a list of strings.

Querying All Groups
===================

Suppose you need to print a report of all of the "real" groups on a
system, including their members (for our purposes, "real" is defined
as having a name not starting with "``_``").  To load the entire
password database, you would use ``getgrall()``.  The return value is
a list with an undefined order, so you probably want to sort it before
printing the report.

.. include:: grp_getgrall.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'grp_getgrall.py'))
.. }}}
.. {{{end}}}

Group Memberships for a User
============================

Another common task might be to print a list of all the groups for a
given user:

.. include:: grp_groups_for_user.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'grp_groups_for_user.py'))
.. }}}
.. {{{end}}}

Finding a Group By Name
=======================

As with :mod:`pwd`, it is also possible to query for information about
a specific group, either by name or numeric id.

.. include:: grp_getgrnam.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'grp_getgrnam.py'))
.. }}}
.. {{{end}}}

Finding a Group by ID
=====================

To identify the group running the current process, combine
``getgrgid()`` with ``os.getgid()``.

.. include:: grp_getgrgid_process.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'grp_getgrgid_process.py'))
.. }}}
.. {{{end}}}

And to get the group name based on the permissions on a file, look up
the group returned by ``os.stat()``.

.. include:: grp_getgrgid_fileowner.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'grp_getgrgid_fileowner.py'))
.. }}}
.. {{{end}}}


.. seealso::

    `grp <http://docs.python.org/library/grp.html>`_
        The standard library documentation for this module.

    :mod:`pwd`
        Read user data from the password database.

    :mod:`spwd`
        Read user data from the shadow password database.
