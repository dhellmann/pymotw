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

::

	$ python subprocess_os_system.py
	__init__.py
	index.rst
	interaction.py
	repeater.py
	signal_child.py
	signal_parent.py
	subprocess_os_system.py
	subprocess_popen2.py
	subprocess_popen3.py
	subprocess_popen4.py
	subprocess_popen_read.py
	subprocess_popen_write.py
	subprocess_shell_variables.py

.. {{{end}}}

And since we set ``shell=True``, shell variables in the command string are
expanded:

.. include:: subprocess_shell_variables.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'subprocess_shell_variables.py'))
.. }}}

::

	$ python subprocess_shell_variables.py
	%backup%~
	Desktop
	Devel
	Documents
	DownloadedApps
	Downloads
	Library
	Logitech
	Movies
	Music
	Pictures
	Public
	Sites
	bender
	bin
	browser - logitech
	cfx
	emacs
	iPod
	nltk_data
	pgadmin.log
	public_html
	texlive
	tmp

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

::

	$ python subprocess_popen_read.py
	
	read:
		stdout: '\n'

.. {{{end}}}


Writing to the input of a pipe:

.. include:: subprocess_popen_write.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'subprocess_popen_write.py'))
.. }}}

::

	$ python subprocess_popen_write.py
		stdin: to stdin
	
	write:

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

::

	$ python subprocess_popen2.py
	
	popen2:
		pass through: 'through stdin to stdout'

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

::

	$ python subprocess_popen3.py
	
	popen3:
		pass through: 'through stdin to stdout'
		stderr: ';to stderr\n'

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

::

	$ python subprocess_popen4.py
	
	popen4:
		combined output: 'through stdin to stdout\n;to stderr\n'

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

.. {{{cog
.. cog.out(run_script(cog.inFile, 'interaction.py'))
.. }}}

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
	
	All output at once:
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
	

.. {{{end}}}


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

.. {{{cog
.. cog.out(run_script(cog.inFile, 'signal_parent.py'))
.. }}}

::

	$ python signal_parent.py
	PARENT: Pausing before sending signal...
	CHILD: Setting up signal handler
	CHILD: Pausing to wait for signal
	PARENT: Signaling 18769
	CHILD: Received USR1 in process 18769

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
        Although deprecated, the functions for working with processes
        found in the os module are still widely used in existing code.
