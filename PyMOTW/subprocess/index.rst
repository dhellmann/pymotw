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

::

    $ python subprocess_os_system.py
    total 16
    -rw-r--r--   1 dhellman  dhellman     0 Jul  1 11:29 __init__.py
    -rw-r--r--   1 dhellman  dhellman  1316 Jul  1 11:32 replace_os_system.py
    -rw-r--r--   1 dhellman  dhellman  1167 Jul  1 11:31 replace_os_system.py~

And since we set ``shell=True``, shell variables in the command string are
expanded:

.. include:: subprocess_shell_variables.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python subprocess_shell_variables.py
    total 40
    drwx------   10 dhellman  dhellman   340 Jun 30 18:45 Desktop
    drwxr-xr-x   15 dhellman  dhellman   510 Jun 19 07:08 Devel
    drwx------   29 dhellman  dhellman   986 Jun 29 07:44 Documents
    drwxr-xr-x   44 dhellman  dhellman  1496 Jun 29 09:51 DownloadedApps
    drwx------   55 dhellman  dhellman  1870 May 22 14:53 Library
    drwx------    8 dhellman  dhellman   272 Mar  4  2006 Movies
    drwx------   11 dhellman  dhellman   374 Jun 21 07:04 Music
    drwx------   12 dhellman  dhellman   408 Jul  1 01:00 Pictures
    drwxr-xr-x    5 dhellman  dhellman   170 Oct  1  2006 Public
    drwxr-xr-x   15 dhellman  dhellman   510 May 12 15:19 Sites
    drwxr-xr-x    5 dhellman  dhellman   170 Oct  5  2005 cfx
    drwxr-xr-x    4 dhellman  dhellman   136 Jan 23  2006 iPod
    -rw-r--r--    1 dhellman  dhellman   204 Jun 18 17:07 pgadmin.log
    drwxr-xr-x    3 dhellman  dhellman   102 Apr 29 16:32 tmp

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

::

    $ python subprocess_popen_read.py
    
    read:
    	stdout: 'to stdout\n'


Writing to the input of a pipe:

.. include:: subprocess_popen_write.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python PyMOTW/subprocess/subprocess_popen_write.py 

    write:
            stdin: to stdin

popen2
------

Reading and writing, as with popen2:

.. include:: subprocess_popen2.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python PyMOTW/subprocess/subprocess_popen2.py 

    popen2:
            pass through: 'through stdin to stdout'

popen3
------

Separate streams for stdout and stderr, as with popen3:

.. include:: subprocess_popen3.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python PyMOTW/subprocess/subprocess_popen3.py 

    popen3:
            pass through: 'through stdin to stdout'
            stderr: ';to stderr\n'

popen4
------

Merged stdout and stderr, as with popen4:

.. include:: subprocess_popen4.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python PyMOTW/subprocess/subprocess_popen4.py

    popen4:
            combined output: 'through stdin to stdout\n;to stderr\n'


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

Make note of the fact that repeater.py writes to stderr when it starts and
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

::

    $ python interaction.py
    One line at a time:
    repeater.py: starting
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    repeater.py: exiting

    All output at once:
    repeater.py: starting
    repeater.py: exiting
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9


Signaling Between Processes
===========================

In part 4 of the series on the os module I included an example of signaling
between processes using os.fork() and os.kill(). Since each Popen instance
provides a pid attribute with the process id of the child process, it is
possible to do something similar with subprocess. For this example, I will
again set up a separate script for the child process to be executed by the
parent process.

.. include:: signal_child.py
    :literal:
    :start-after: #end_pymotw_header


And now the parent process:

.. include:: signal_parent.py
    :literal:
    :start-after: #end_pymotw_header

And the output should look something like this:

::

    $ python signal_parent.py
    CHILD: Setting up signal handler
    CHILD: Pausing to wait for signal
    PARENT: Pausing before sending signal...
    PARENT: Signaling 4124
    Received USR1 in process 4124


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
        Although deprecated, the functions for working with processes
        found in the os module are still widely used in existing code.
