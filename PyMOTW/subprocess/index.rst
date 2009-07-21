==============================================================
subprocess -- Spawn and communicate with additional processes.
==============================================================

.. module:: subprocess
    :synopsis: Spawn and communicate with additional processes.

:Purpose: Spawn and communicate with additional processes.
:Python Version: New in 2.4

The subprocess module provides a consistent interface to creating and working
with additional processes. It offers a higher-level interface than some of the
other available modules, and is intended to replace functions such as
os.system, os.spawn*, os.popen*, popen2.* and commands.*. To make it easier to
compare subprocess with those other modules, I will re-create
the previous examples using the functions being replaced.

The subprocess module defines one class, Popen() and a few wrapper functions
which use that class. Popen() takes several arguments to make it easier to set
up the new process, and then communicate with it via pipes. I will concentrate
on example code here; for a complete description of the arguments, refer to
section 17.1.1 of the library documentation.

.. note::

    The API is roughly the same, but the underlying implementation is slightly
    different between Unix and Windows. All of the examples shown here were tested
    on Mac OS X. Your mileage on a non-Unix OS will vary.

Running External Command
========================

To run an external command without interacting with it, such as one would do
with os.system(), Use the call() function.

.. include:: subprocess_os_system.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'subprocess_os_system.py'))
.. }}}
.. {{{end}}}

And since we set ``shell=True``, shell variables in the command string are
expanded:

.. include:: subprocess_shell_variables.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'subprocess_shell_variables.py'))
.. }}}
.. {{{end}}}

Working with Pipes
==================

By passing different arguments for stdin, stdout, and stderr it is possible to
mimic the variations of os.popen().

popen
-----

Reading from the output of a pipe:

.. include:: subprocess_popen_read.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'subprocess_popen_read.py'))
.. }}}
.. {{{end}}}


Writing to the input of a pipe:

.. include:: subprocess_popen_write.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'subprocess_popen_write.py'))
.. }}}
.. {{{end}}}

popen2
------

Reading and writing, as with popen2:

.. include:: subprocess_popen2.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'subprocess_popen2.py'))
.. }}}
.. {{{end}}}

popen3
------

Separate streams for stdout and stderr, as with popen3:

.. include:: subprocess_popen3.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'subprocess_popen3.py'))
.. }}}
.. {{{end}}}

popen4
------

Merged stdout and stderr, as with popen4:

.. include:: subprocess_popen4.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'subprocess_popen4.py'))
.. }}}
.. {{{end}}}


Interacting with Another Command
================================

All of the above examples assume a limited amount of interaction. The
communicate() method reads all of the output and waits for child process to
exit before returning. It is also possible to write to and read from the
individual pipe handles used by the Popen instance. To illustrate this, I will
use this simple echo program which reads its standard input and writes it back
to standard output:

.. include:: repeater.py
    :literal:
    :start-after: #end_pymotw_header

Make note of the fact that repeater.py writes to stdout when it starts and
stops. We can use that to show the lifetime of the subprocess in the next
example. The following interaction example uses the stdin and stdout file
handles owned by the Popen instance in different ways. In the first example, a
sequence of 10 numbers are written to stdin of the process, and after each
write the next line of output is read back. In the second example, the same 10
numbers are written but the output is read all at once using communicate().

.. include:: interaction.py
    :literal:
    :start-after: #end_pymotw_header


Notice where the "repeater.py: exiting" lines fall in the output for each
loop:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'interaction.py'))
.. }}}
.. {{{end}}}


Signaling Between Processes
===========================

In the article on :mod:`os`, I included an example of signaling between processes using
os.fork() and os.kill(). Since each Popen instance provides a pid attribute with the process
id of the child process, it is possible to do something similar with subprocess. For this
example, I will again set up a separate script for the child process to be executed by the
parent process.

.. include:: signal_child.py
    :literal:
    :start-after: #end_pymotw_header


And now the parent process:

.. include:: signal_parent.py
    :literal:
    :start-after: #end_pymotw_header

And the output should look something like this:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'signal_parent.py'))
.. }}}
.. {{{end}}}

.. _subprocess-process-groups:

Process Groups / Sessions
-------------------------

Because of the way the process tree works under Unix, if the process created by Popen spawns sub-processes, those children will not receive any signals sent to the parent.  That means, for example, that it will be difficult to cause them to terminate by sending SIGINT or SIGTERM.

.. include:: subprocess_signal_parent_shell.py
    :literal:
    :start-after: #end_pymotw_header

Notice that the pid used to send the signal is different from the pid of the child of the shell script waiting for the signal because in this example, there are three separate processes interacting:

1. subprocess_signal_parent_shell.py
2. a Unix shell process running the script created by the main python program
3. signal_child.py

.. {{{cog
.. cog.out(run_script(cog.inFile, 'subprocess_signal_parent_shell.py'))
.. }}}
.. {{{end}}}

The solution to this problem is to use a *process group* to associate the children so they can be signaled together.  The process group is created with ``os.setsid()``, setting the "session id" to the process id of the current process.  All child processes inherit the session id, and since we only want it set in the shell created by Popen and its descendants we don't call it in the parent process.  Instead, we pass it to Popen as the *preexec_fn* argument so it is run inside the new process before it calls ``exec()``.

.. include:: subprocess_signal_setsid.py
    :literal:
    :start-after: #end_pymotw_header

To signal the entire process group, we use ``os.killpg()`` with the pid value from our Popen instance.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'subprocess_signal_setsid.py'))
.. }}}
.. {{{end}}}


Conclusions
===========

As you can see, subprocess can be much easier to work with than fork, exec,
and pipes on their own. It provides all of the functionality of the other
modules and functions it replaces, and more. The API is consistent for all
uses and many of the extra steps of overhead needed (such as closing extra
file descriptors, ensuring the pipes are closed, etc.) are "built in" instead
of being handled by your code separately.


.. seealso::

    `subprocess <http://docs.python.org/lib/module-subprocess.html>`_
        Standard library documentation for this module.

    :mod:`os`
        Although many are deprecated, the functions for working with processes
        found in the os module are still widely used in existing code.

    `UNIX SIgnals and Process Groups <http://www.frostbytes.com/~jimf/papers/signals/signals.html>`_
        A good description of UNIX signaling and how process groups work.


    `Advanced Programming in the UNIX(R) Environment <http://www.amazon.com/Programming-Environment-Addison-Wesley-Professional-Computing/dp/0201433079/ref=pd_bbs_3/002-2842372-4768037?ie=UTF8&s=books&amp;qid=1182098757&sr=8-3>`_
        Covers working with multiple processes, such as handling signals, closing duplicated
        file descriptors, etc.
