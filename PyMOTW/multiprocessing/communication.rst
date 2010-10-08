###############################
Communication Between Processes
###############################

As with threads, a common use pattern for multiple processes is to
divide a job up among several workers to run in parallel.  Effective
use of multiple processes usually requires some communication between
them, so that work can be divided and results can be aggregated.

.. _multiprocessing-queues:

Passing Messages to Processes
=============================

A simple way to communicate between process with
:mod:`multiprocessing` is to use a :class:`Queue` to pass messages
back and forth.  Any pickle-able object can pass through a
:class:`Queue`.

.. include:: multiprocessing_queue.py
    :literal:
    :start-after: #end_pymotw_header

This short example only passes a single message to a single worker,
then the main process waits for the worker to finish.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_queue.py'))
.. }}}
.. {{{end}}}

A more complex example shows how to manage several workers consuming
data from a :class:`JoinableQueue` and passing results back to the
parent process.  The *poison pill* technique is used to stop the
workers.  After setting up the real tasks, the main program adds one
"stop" value per worker to the job queue.  When a worker encounters
the special value, it breaks out of its processing loop.  The main
process uses the task queue's :func:`join` method to wait for all of
the tasks to finish before processin the results.

.. include:: multiprocessing_producer_consumer.py
    :literal:
    :start-after: #end_pymotw_header

Although the jobs enter the queue in order, since their execution is
parallelized there is no guarantee about the order they will be
completed.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u multiprocessing_producer_consumer.py'))
.. }}}
.. {{{end}}}



Signaling between Processes
===========================

The :class:`Event` class provides a simple way to communicate state
information between processes.  An event can be toggled between set
and unset states.  Users of the event object can wait for it to change
from unset to set, using an optional timeout value.

.. include:: multiprocessing_event.py
    :literal:
    :start-after: #end_pymotw_header

When :func:`wait` times out it returns without an error.  The caller
is responsible for checking the state of the event using
:func:`is_set`.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u multiprocessing_event.py'))
.. }}}
.. {{{end}}}

Controlling Access to Resources
===============================

In situations when a single resource needs to be shared between
multiple processes, a :class:`Lock` can be used to avoid conflicting
accesses.

.. include:: multiprocessing_lock.py
    :literal:
    :start-after: #end_pymotw_header

In this example, the messages printed to the console may be jumbled
together if the two processes do not synchronize their access of the
output stream with the lock.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_lock.py'))
.. }}}
.. {{{end}}}


Synchronizing Operations
========================

:class:`Condition` objects can be used to synchronize parts of a
workflow so that some run in parallel but others run sequentially,
even if they are in separate processes.

.. include:: multiprocessing_condition.py
    :literal:
    :start-after: #end_pymotw_header

In this example, two process run the second stage of a job in
parallel, but only after the first stage is done.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_condition.py'))
.. }}}
.. {{{end}}}


Controlling Concurrent Access to Resources
==========================================

Sometimes it is useful to allow more than one worker access to a
resource at a time, while still limiting the overall number. For
example, a connection pool might support a fixed number of
simultaneous connections, or a network application might support a
fixed number of concurrent downloads. A :class:`Semaphore` is one way
to manage those connections.

.. include:: multiprocessing_semaphore.py
    :literal:
    :start-after: #end_pymotw_header

In this example, the :class:`ActivePool` class simply serves as a
convenient way to track which processes are running at a given
moment. A real resource pool would probably allocate a connection or
some other value to the newly active process, and reclaim the value
when the task is done. Here, the pool is just used to hold the names
of the active processes to show that only three are running
concurrently.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_semaphore.py'))
.. }}}
.. {{{end}}}

Managing Shared State
=====================

In the previous example, the list of active processes is maintained
centrally in the :class:`ActivePool` instance via a special type of
list object created by a :class:`Manager`.  The :class:`Manager` is
responsible for coordinating shared information state between all of
its users.  

.. include:: multiprocessing_manager_dict.py
    :literal:
    :start-after: #end_pymotw_header

By creating the list through the manager, it is shared and updates are
seen in all processes.  Dictionaries are also supported.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_manager_dict.py'))
.. }}}
.. {{{end}}}

Shared Namespaces
=================

In addition to dictionaries and lists, a :class:`Manager` can create a
shared :class:`Namespace`.  

.. include:: multiprocessing_namespaces.py
    :literal:
    :start-after: #end_pymotw_header

Any named value added to the :class:`Namespace` is visible to all of
the clients that receive the :class:`Namespace` instance.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_namespaces.py'))
.. }}}
.. {{{end}}}

It is important to know that *updates* to the contents of mutable
values in the namespace are *not* propagated automatically.

.. include:: multiprocessing_namespaces_mutable.py
    :literal:
    :start-after: #end_pymotw_header

To update the list, attach it to the namespace object again.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_namespaces_mutable.py'))
.. }}}
.. {{{end}}}


Process Pools
=============

The :class:`Pool` class can be used to manage a fixed number of
workers for simple cases where the work to be done can be broken up
and distributed between workers independently.  The return values from
the jobs are collected and returned as a list.  The pool arguments
include the number of processes and a function to run when starting
the task process (invoked once per child).

.. include:: multiprocessing_pool.py
    :literal:
    :start-after: #end_pymotw_header

The result of the :func:`map` method is functionally equivalent to the
built-in :func:`map`, except that individual tasks run in parallel.
Since the pool is processing its inputs in parallel, :func:`close` and
:func:`join` can be used to synchronize the main process with the task
processes to ensure proper cleanup.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_pool.py'))
.. }}}
.. {{{end}}}

By default :class:`Pool` creates a fixed number of worker processes
and passes jobs to them until there are no more jobs.  Setting the
*maxtasksperchild* parameter tells the pool to restart a worker
process after it has finished a few tasks.  This can be used to avoid
having long-running workers consume ever more system resources.

.. include:: multiprocessing_pool_maxtasksperchild.py
   :literal:
   :start-after: #end_pymotw_header

The pool restarts the workers when they have completed their allotted
tasks, even if there is no more work.  In this output, eight workers
are created, even though there are only 10 tasks, and each worker can
complete two of them at a time.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_pool_maxtasksperchild.py'))
.. }}}
.. {{{end}}}

