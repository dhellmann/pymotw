####################################################
Communication between processes with multiprocessing
####################################################

.. _multiprocessing-queues:

Passing Messages to Processes
=============================

As with threads, a common use pattern for multiple processes is to divide a job up among several workers to run in parallel.  A simple way to do that with :mod:`multiprocessing` is to use Queues to pass messages back and forth.  Any pickle-able object can pass through a :mod:`multiprocessing` Queue.

.. include:: multiprocessing_queue.py
    :literal:
    :start-after: #end_pymotw_header

This short example only passes a single message to a single worker, then the main process waits for the worker to finish.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_queue.py'))
.. }}}
.. {{{end}}}

A more complex example shows how to manage several workers consuming data from the queue and passing results back to the parent process.  The *poison pill* technique is used to stop the workers.  After setting up the real tasks, the main program adds one "stop" value per worker to the job queue.  When a worker encounters the special value, it breaks out of its processing loop.

.. include:: multiprocessing_producer_consumer.py
    :literal:
    :start-after: #end_pymotw_header

Although the jobs enter the queue in order, since their execution is parallelized there is no guarantee about the order they will be completed.  

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_producer_consumer.py'))
.. }}}
.. {{{end}}}



Signaling between Processes with Event objects
==============================================

Events provide a simple way to communicate state information between processes.  An event can be toggled between set and unset states.  Users of the event object can wait for it to change from unset to set, using an optional timeout value.

.. include:: multiprocessing_event.py
    :literal:
    :start-after: #end_pymotw_header

When ``wait()`` times out it returns without an error.  The caller is responsible for checking the state of the event using ``is_set()``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_event.py'))
.. }}}
.. {{{end}}}

Controlling access to resources with Lock
=========================================

In situations when a single resource needs to be shared between multiple processes, a Lock can be used to avoid conflicting accesses.  

.. include:: multiprocessing_lock.py
    :literal:
    :start-after: #end_pymotw_header

In this example, the messages printed to stdout may be jumbled together if the two processes do not synchronize their access of the output stream with the lock.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_lock.py'))
.. }}}
.. {{{end}}}


Synchronizing threads with a Condition object
=============================================

Condition objects let you synchronize parts of a workflow so that some run in parallel but others run sequentially, even if they are in separate processes.  In this example, two process run stage two of a job in parallel once the first stage is done.


Controlling concurrent access to resources with a Semaphore
===========================================================

Pool.map
========

Map/Reduce
==========

Manager
=======

Namespaces
==========

Parallel Evaluation of a List Comprehension
===========================================

MORE
====
