###########################################################
Communication between processes with :mod:`multiprocessing`
###########################################################

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

A more complex example uses several workers consuming data from the queue and passing results back to the parent process.

.. include:: multiprocessing_producer_consumer.py
    :literal:
    :start-after: #end_pymotw_header



Signaling between Processes with Event objects
==============================================

Controlling access to resources with Lock
=========================================

.. just use with

Synchronizing threads with a Condition object
=============================================

Controlling concurrent access to resources with a Semaphore
===========================================================

Pool.map
========

Map/Reduce
==========

Manager
=======

Parallel Evaluation of a List Comprehension
===========================================

MORE
====
