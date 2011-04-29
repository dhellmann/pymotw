======================================
resource -- System resource management
======================================

.. module:: resource
    :synopsis: System resource management

:Purpose: Manage the system resource limits for a Unix program.
:Available In: 1.5.2

The functions in :mod:`resource` probe the current system resources
consumed by a process, and place limits on them to control how much
load a program can impose on a system.

Current Usage
=============

Use :func:`getrusage()` to probe the resources used by the current
process and/or its children.  The return value is a data structure
containing several resource metrics based on the current state of the
system.

.. note::  

  Not all of the resource values gathered are displayed here.  Refer
  to the `stdlib docs
  <http://docs.python.org/library/resource.html#resource.getrusage>`_
  for a more complete list.

.. include:: resource_getrusage.py
    :literal:
    :start-after: #end_pymotw_header

Because the test program is extremely simple, it does not use very
many resources:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'resource_getrusage.py'))
.. }}}
.. {{{end}}}

Resource Limits
===============

Separate from the current actual usage, it is possible to check the
*limits* imposed on the application, and then change them.

.. include:: resource_getrlimit.py
    :literal:
    :start-after: #end_pymotw_header

The return value for each limit is a tuple containing the *soft* limit
imposed by the current configuration and the *hard* limit imposed by
the operating system.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'resource_getrlimit.py'))
.. }}}
.. {{{end}}}

The limits can be changed with :func:`setrlimit()`.  For example, to
control the number of files a process can open the :const:`RLIMIT_NOFILE`
value can be set to use a smaller soft limit value.

.. include:: resource_setrlimit_nofile.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'resource_setrlimit_nofile.py'))
.. }}}
.. {{{end}}}

It can also be useful to limit the amount of CPU time a process should
consume, to avoid eating up too much time.  When the process runs past
the allotted amount of time, it it sent a :const:`SIGXCPU` signal.

.. include:: resource_setrlimit_cpu.py
    :literal:
    :start-after: #end_pymotw_header

Normally the signal handler should flush all open files and close
them, but in this case it just prints a message and exits.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'resource_setrlimit_cpu.py', ignore_error=True))
.. }}}
.. {{{end}}}


.. seealso::

    `resource <http://docs.python.org/library/resource.html>`_
        The standard library documentation for this module.

    :mod:`signal`
        For details on registering signal handlers.
