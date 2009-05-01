######################
multiprocessing Basics
######################

Process objects
===============

The simplest way to use a sub-process is to instantiate it with a target function
and call start() to let it begin working.

.. include:: multiprocessing_simple.py
    :literal:
    :start-after: #end_pymotw_header

The output includes the word "Worker" printed five times, although it may not be entirely clean depending on the order of execution.tr

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_simple.py'))
.. }}}
.. {{{end}}}


It usually more useful to be able to spawn a process with arguments to tell it what
work to do.  Unlike with :mod:`threading`, to pass arguments to a :mod:`multiprocessing` Process the argument must be able to be pickled.  As a simple example we could pass each
worker a number so the output is a little more interesting in the second
example.

.. include:: multiprocessing_simpleargs.py
    :literal:
    :start-after: #end_pymotw_header

The integer argument is now included in the message printed by each worker:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_simpleargs.py'))
.. }}}
.. {{{end}}}

Importable Target Functions
===========================

One difference you will notice between the :mod:`threading` and :mod:`multiprocessing` examples is the extra protection for ``__main__`` used here.  Due to the way the new processes are started, the child process needs to be able to import the script containing the target function.  In these examples I accomplish that by wrapping the main part of the application so it is not run recursively in each child.  You could also import the target function from a separate script.

For example, this main program:

.. include:: multiprocessing_import_main.py
    :literal:
    :start-after: #end_pymotw_header

uses this worker function, defined in a separate module:

.. include:: multiprocessing_import_worker.py
    :literal:
    :start-after: #end_pymotw_header

and produces output like the first example above:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_import_main.py'))
.. }}}
.. {{{end}}}

Determining the Current Process
===============================

Passing arguments to identify or name the process is cumbersome, and unnecessary.
Each Process instance has a name with a default value that you can change as
the process is created. Naming processes is useful if you have a server
with multiple service children handling different operations. 

.. include:: multiprocessing_names.py
    :literal:
    :start-after: #end_pymotw_header

The debug output includes the name of the current process on each line. The
lines with "Process-3" in the name column correspond to the unnamed
process w2.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_names.py'))
.. }}}
.. {{{end}}}


Daemon Processes
================

By default the main program will not exit until all of the children have exited. There are
times when you want to start a background process and let it run without blocking the main
program from exiting. Using daemon processes like this is useful for services where there may
not be an easy way to interrupt the worker or where letting it die in the middle of its work
does not lose or corrupt data (for example, a task that generates "heart beats" for a service
monitoring tool). To mark a process as a daemon, set its ``daemon`` attribute with a boolean
value. The default is for processes to not be daemons, so passing True turns the daemon mode
on.

.. include:: multiprocessing_daemon.py
    :literal:
    :start-after: #end_pymotw_header

Notice that the output does not include the "Exiting" message from the daemon
process, since all of the non-daemon processes (including the main program) exit
before the daemon process wakes up from its 2 second sleep.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_daemon.py'))
.. }}}
.. {{{end}}}

The daemon process is terminated automatically before the main program exits, to avoid leaving orphaned processes running.  You can verify this by looking for the process id value printed when you run the program, and then checking for that process with a command like ``ps``.

Waiting for Processes
=====================

To wait until a process has completed its work and exited, use the ``join()`` method.

.. include:: multiprocessing_daemon_join.py
    :literal:
    :start-after: #end_pymotw_header

Since we wait for the daemon to exit using ``join()``, we do see its
"Exiting" message.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_daemon_join.py'))
.. }}}
.. {{{end}}}

By default, ``join()`` blocks indefinitely. It is also possible to pass a timeout
argument (a float representing the number of seconds to wait for the process to
become inactive). If the process does not complete within the timeout period,
``join()`` returns anyway.

.. include:: multiprocessing_daemon_join_timeout.py
    :literal:
    :start-after: #end_pymotw_header

Since the timeout passed is less than the amount of time the daemon
sleeps, the process is still "alive" after ``join()`` returns.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_daemon_join_timeout.py'))
.. }}}
.. {{{end}}}

Terminating Processes
=====================

Although it is better to use the *poison pill* method of signaling to a process that it should exit (see :ref:`multiprocessing-queues`), if a process appears hung or deadlocked it can be useful to be able to kill it forcibly.  Calling ``terminate()`` on a process object kills the child process.

.. include:: multiprocessing_terminate.py
    :literal:
    :start-after: #end_pymotw_header

.. note::

    It is important to ``join()`` the process after terminating it in order to give the background machinery time to update the status of the object to reflect the termination.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_terminate.py'))
.. }}}
.. {{{end}}}


Process Exit Status
===================

The status code produced when the process exits can be accessed via the ``exitcode`` attribute.

For ``exitcode`` values

* ``== 0`` -- no error was produced
* ``> 0`` -- the process had an error, and exited with that code
* ``< 0`` -- the process was killed with a signal of ``-1 * exitcode``

.. include:: multiprocessing_exitcode.py
    :literal:
    :start-after: #end_pymotw_header

Processes that raise an exception automatically get an ``exitcode`` of 1.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_exitcode.py'))
.. }}}
.. {{{end}}}


Logging
=======

When debugging concurrency issues, it can be useful to have access to the internals of the objects provided by :mod:`multiprocessing`.  There is a convenient module-level function to enable logging called :func:`log_to_stderr`.  It sets up a logger object using :mod:`logging` and adds a handler so that log messages are sent to the standard error channel.

.. include:: multiprocessing_log_to_stderr.py
    :literal:
    :start-after: #end_pymotw_header

By default the logging level is set to ``NOTSET`` so no messages are produced.  Pass a different level to initialize the logger to the level of detail you want.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_log_to_stderr.py'))
.. }}}
.. {{{end}}}

To manipulate the logger directly (change its level setting or add handlers), use :func:`get_logger`.

.. include:: multiprocessing_get_logger.py
    :literal:
    :start-after: #end_pymotw_header

The logger can also be configured through the :mod:`logging` configuration file API, using the name ``multiprocessing``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_get_logger.py'))
.. }}}
.. {{{end}}}


Subclassing Process
===================

Although the simplest way to start a job in a separate process is to use :class:`Process` and pass a target function, it is also possible to use a custom subclass.  The derived class should override :meth:`run` to do its work.

.. include:: multiprocessing_subclass.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_subclass.py'))
.. }}}
.. {{{end}}}
