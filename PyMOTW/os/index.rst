============================================================
os -- Portable access to operating system specific features.
============================================================

.. module:: os
    :synopsis: Portable access to operating system specific features.

:Purpose: Portable access to operating system specific features.
:Python Version: 1.4 (or earlier)

The :mod:`os` module provides a wrapper for platform specific modules
such as :mod:`posix`, :mod:`nt`, and :mod:`mac`. The API for functions
available on all platform should be the same, so using the os module
offers some measure of portability. Not all functions are available on
all platforms, however. Many of the process management functions
described in this summary are not available for Windows.

The Python documentation for the os module is subtitled "Miscellaneous
operating system interfaces". The module includes mostly functions for
creating and managing running processes or filesystem content (files
and directories), with a few other random bits of functionality thrown
in besides.

.. note::

    Some of the example code below will only work on Unix-like
    operating systems.

Process Owner
=============

The first set of functions to cover are used for determining and
changing the process owner ids. These are mostly useful to authors of
daemons or special system programs which need to change permission
level rather than running as ``root``. I won't try to explain all of
the intricate details of Unix security, process owners, etc. in this
brief post. See the References list below for more details.

Let's start with a script to show the real and effective user and
group information for a process, and then change the effective
values. This is similar to what a daemon would need to do when it
starts as root during a system boot, to lower the privilege level and
run as a different user. If you download the examples to try them out,
you should change the ``TEST_GID`` and ``TEST_UID`` values to match
your user.

.. include:: os_process_user_example.py
    :literal:
    :start-after: #end_pymotw_header

When run as myself (527, 501) on OS X, I see this output:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'os_process_user_example.py'))
.. }}}
.. {{{end}}}

Notice that the values do not change. Since I am not running as root,
processes I start cannot change their effective owner values. If I do try to
set the effective user id or group id to anything other than my own, an
OSError is raised.

Now let's look at what happens when we run the same script using
``sudo`` to start out with root privileges:

.. Don't use cog here because sudo sometimes asks for a password.

::

	$ sudo python os_process_user_example.py
	BEFORE CHANGE:
	Effective User  : 0
	Effective Group : 0
	Actual User	 : 0 dhellmann
	Actual Group	: 0
	Actual Groups   : [0, 1, 2, 8, 29, 3, 9, 4, 5, 80, 20]
	
	CHANGED GROUP:
	Effective User  : 0
	Effective Group : 501
	Actual User	 : 0 dhellmann
	Actual Group	: 0
	Actual Groups   : [501, 1, 2, 8, 29, 3, 9, 4, 5, 80, 20]
	
	CHANGE USER:
	Effective User  : 527
	Effective Group : 501
	Actual User	 : 0 dhellmann
	Actual Group	: 0
	Actual Groups   : [501, 1, 2, 8, 29, 3, 9, 4, 5, 80, 20]
	

In this case, since we start as root, we can change the effective user and
group for the process. Once we change the effective UID, the process is
limited to the permissions of that user. Since non-root users cannot change
their effective group, we need to change the group first then the user.

Besides finding and changing the process owner, there are functions for
determining the current and parent process id, finding and changing the
process group and session ids, as well as finding the controlling terminal id.
These can be useful for sending signals between processes or for complex
applications such as writing your own command line shell.

Process Environment
===================

Another feature of the operating system exposed to your program though
the os module is the environment. Variables set in the environment are
visible as strings that can be read through ``os.environ`` or
:func:`os.getenv()`. Environment variables are commonly used for
configuration values such as search paths, file locations, and debug
flags. Let's look at an example of retrieving an environment variable,
and passing a value through to a child process.

.. include:: os_environ_example.py
    :literal:
    :start-after: #end_pymotw_header


The ``os.environ`` object follows the standard Python mapping API for
retrieving and setting values. Changes to ``os.environ`` are exported
for child processes.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u os_environ_example.py'))
.. }}}
.. {{{end}}}


Process Working Directory
=========================

The notion of the "current working directory" for a process is a
concept from operating systems with hierarchical filesystems.  This is
the directory on the filesystem the process uses as the starting
location when files are accessed with relative paths.

.. include:: os_cwd_example.py
    :literal:
    :start-after: #end_pymotw_header

Note the use of ``os.curdir`` and ``os.pardir`` to refer to the
current and parent directories in a portable manner. The output should
not be surprising:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'os_cwd_example.py'))
.. }}}
.. {{{end}}}


Pipes
=====

The :mod:`os` module provides several functions for managing the I/O
of child processes using *pipes*. The functions all work essentially
the same way, but return different file handles depending on the type
of input or output desired. For the most part, these functions are
made obsolete by the :mod:`subprocess` module (added in Python 2.4),
but there is a good chance you will encounter them if you are
maintaining legacy code.

The most commonly used pipe function is :func:`popen()`. It creates a
new process running the command given and attaches a single stream to
the input or output of that process, depending on the mode
argument. While :func:`popen` functions work on Windows, some of these
examples assume some sort of Unix-like shell. The descriptions of the
streams also assume Unix-like terminology:

* stdin - The "standard input" stream for a process (file descriptor 0) is
  readable by the process. This is usually where terminal input goes.

* stdout - The "standard output" stream for a process (file descriptor
  1) is writable by the process, and is used for displaying regular
  output to the user.

* stderr - The "standard error" stream for a process (file descriptor 2) is
  writable by the process, and is used for conveying error messages.

.. include:: os_popen.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u os_popen.py'))
.. }}}
.. {{{end}}}

The caller can only read from or write to the streams associated with
the child process, which limits the usefulness. The other
:func:`popen` variants provide additional streams so it is possible to
work with stdin, stdout, and stderr as needed.

For example, :func:`popen2()` returns a write-only stream attached to
stdin of the child process, and a read-only stream attached to its
stdout.

.. include:: os_popen2.py
    :literal:
    :start-after: #end_pymotw_header


This simplistic example illustrates bi-directional communication. The
value written to stdin is read by ``cat`` (because of the ``'-'``
argument), then written back to stdout. Obviously a more complicated
process could pass other types of messages back and forth through the
pipe; even serialized objects.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u os_popen2.py'))
.. }}}
.. {{{end}}}

In most cases, it is desirable to have access to both stdout and
stderr. The stdout stream is used for message passing and the stderr
stream is used for errors, so reading from it separately reduces the
complexity for parsing any error messages. The :func:`popen3()`
function returns 3 open streams tied to stdin, stdout, and stderr of
the new process.

.. include:: os_popen3.py
    :literal:
    :start-after: #end_pymotw_header

Notice that we have to read from and close both stdout and stderr
*separately*. There are some related to flow control and sequencing
when dealing with I/O for multiple processes. The I/O is buffered, and
if the caller expects to be able to read all of the data from a stream
then the child process must close that stream to indicate the
end-of-file. For more information on these issues, refer to the `Flow
Control Issues
<http://docs.python.org/library/popen2.html#popen2-flow-control>`__
section of the Python library documentation.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u os_popen3.py'))
.. }}}
.. {{{end}}}

And finally, :func:`popen4()` returns 2 streams, stdin and a merged
stdout/stderr.  This is useful when the results of the command need to
be logged, but not parsed directly.

.. include:: os_popen4.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u os_popen4.py'))
.. }}}
.. {{{end}}}

Besides accepting a single string command to be given to the shell for
parsing, :func:`popen2()`, :func:`popen3()`, and :func:`popen4()` also
accept a sequence of strings (command, followed by arguments). In this
case, the arguments are not processed by the shell.

.. include:: os_popen2_seq.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u os_popen2_seq.py'))
.. }}}
.. {{{end}}}


File Descriptors
================

:mod:`os` includes the standard set of functions for working with
low-level *file descriptors* (integers representing open files owned
by the current process). This is a lower-level API than is provided by
:class:`file` objects. I am going to skip over describing them here,
since it is generally easier to work directly with :class:`file`
objects. Refer to the library documentation for details if you do need
to use file descriptors.

Filesystem Permissions
======================

The function :func:`os.access()` can be used to test the access rights a
process has for a file.

.. include:: os_access.py
    :literal:
    :start-after: #end_pymotw_header

Your results will vary depending on how you install the example code, but it
should look something like this:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'os_access.py'))
.. }}}
.. {{{end}}}


The library documentation for :func:`os.access()` includes two special
warnings. First, there isn't much sense in calling :func:`os.access()`
to test whether a file can be opened before actually calling
:func:`open()` on it. There is a small, but real, window of time
between the two calls during which the permissions on the file could
change. The other warning applies mostly to networked filesystems that
extend the POSIX permission semantics. Some filesystem types may
respond to the POSIX call that a process has permission to access a
file, then report a failure when the attempt is made using
:func:`open()` for some reason not tested via the POSIX call. All in
all, it is better to call :func:`open()` with the required mode and
catch the :ref:`IOError <exceptions-IOError>` raised if there is a
problem.

More detailed information about the file can be accessed using
:func:`os.stat()` or :func:`os.lstat()` (if you want the status of
something that might be a symbolic link).

.. include:: os_stat.py
    :literal:
    :start-after: #end_pymotw_header

Once again, your results will vary depending on how the example code
was installed. Try passing different filenames on the command line to
``os_stat.py``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'os_stat.py'))
.. }}}
.. {{{end}}}


On Unix-like systems, file permissions can be changed using
:func:`os.chmod()`, passing the mode as an integer. Mode values can be
constructed using constants defined in the :mod:`stat` module. Here is
an example which toggles the user's execute permission bit:

.. include:: os_stat_chmod.py
    :literal:
    :start-after: #end_pymotw_header


The script assumes you have the permissions necessary to modify the
mode of the file to begin with:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'os_stat_chmod.py'))
.. }}}
.. {{{end}}}

.. _os-directories:

Directories
===========

There are several functions for working with directories on the filesystem,
including creating, listing contents, and removing them.

.. include:: os_directories.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'os_directories.py'))
.. }}}
.. {{{end}}}


There are two sets of functions for creating and deleting
directories. When creating a new directory with :func:`os.mkdir()`,
all of the parent directories must already exist. When removing a
directory with :func:`os.rmdir()`, only the leaf directory (the last
part of the path) is actually removed. In contrast,
:func:`os.makedirs()` and :func:`os.removedirs()` operate on all of
the nodes in the path.  :func:`os.makedirs()` will create any parts of
the path which do not exist, and :func:`os.removedirs()` will remove
all of the parent directories (assuming it can).

Symbolic Links
==============

For platforms and filesystems which support them, there are functions
for working with symlinks.

.. include:: os_symlinks.py
    :literal:
    :start-after: #end_pymotw_header


Although :mod:`os` includes :func:`os.tempnam()` for creating
temporary filenames, it is not as secure as the :mod:`tempfile` module
and produces a :ref:`RuntimeWarning <exceptions-RuntimeWarning>`
message when it is used. In general it is better to use
:mod:`tempfile`, as in this example.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'os_symlinks.py'))
.. }}}
.. {{{end}}}


Walking a Directory Tree
========================

The function :func:`os.walk()` traverses a directory recursively and
for each directory generates a tuple containing the directory path,
any immediate sub-directories of that path, and the names of any files
in that directory.  This example shows a simplistic recursive
directory listing.

.. include:: os_walk.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'os_walk.py'))
.. }}}
.. {{{end}}}

.. _os-system:

Running External Commands
=========================

.. warning::

    Many of these functions for working with processes have limited
    portability. For a more consistent way to work with processes in a
    platform independent manner, see the :mod:`subprocess` module
    instead.

The simplest way to run a separate command, without interacting with
it at all, is :func:`os.system()`. It takes a single string which is
the command line to be executed by a sub-process running a shell.

.. include:: os_system_example.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u os_system_example.py'))
.. }}}
.. {{{end}}}


Since the command is passed directly to the shell for processing, it can even
include shell syntax such as globbing or environment variables:

.. include:: os_system_shell.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u os_system_shell.py'))
.. }}}
.. {{{end}}}


Unless you explicitly run the command in the background, the call to
:func:`os.system()` blocks until it is complete. Standard input,
output, and error from the child process are tied to the appropriate
streams owned by the caller by default, but can be redirected using
shell syntax.

.. include:: os_system_background.py
    :literal:
    :start-after: #end_pymotw_header


This is getting into shell trickery, though, and there are better ways to
accomplish the same thing.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u os_system_background.py'))
.. }}}
.. {{{end}}}

.. _creating-processes-with-os-fork:

Creating Processes with os.fork()
=================================

The POSIX functions :func:`fork()` and :func:`exec*()` (available
under Mac OS X, Linux, and other UNIX variants) are exposed via the
:mod:`os` module. Entire books have been written about reliably using
these functions, so check your library or bookstore for more details
than I will present here.

To create a new process as a clone of the current process, use
:func:`os.fork()`:

.. include:: os_fork_example.py
    :literal:
    :start-after: #end_pymotw_header

Your output will vary based on the state of your system each time you run the
example, but it should look something like:

.. {{{cog
.. cog.out(run_script(cog.inFile, '-u os_fork_example.py'))
.. }}}
.. {{{end}}}

After the fork, you end up with two processes running the same
code. To tell which one you are in, check the return value of
:func:`fork()`. If it is ``0``, you are inside the child process. If
it is not ``0``, you are in the parent process and the return value is
the process id of the child process.

From the parent process, it is possible to send the child signals. This is a
bit more complicated to set up, and uses the :mod:`signal` module, so let's walk
through the code. First we can define a signal handler to be invoked when the
signal is received.

.. literalinclude:: os_kill_example.py
   :lines: 33-40

Then we fork, and in the parent pause a short amount of time before
sending a ``USR1`` signal using :func:`os.kill()`. The short pause
gives the child process time to set up the signal handler.

.. literalinclude:: os_kill_example.py
   :lines: 42-48

In the child, we set up the signal handler and go to sleep for a while to give
the parent time to send us the signal:

.. literalinclude:: os_kill_example.py
   :language: python
   :lines: 49-53

In a real app, you probably wouldn't need to (or want to) call
:func:`sleep()`.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'os_kill_example.py'))
.. }}}
.. {{{end}}}


As you see, a simple way to handle separate behavior in the child
process is to check the return value of :func:`fork()` and branch. For
more complex behavior, you may want more code separation than a simple
branch. In other cases, you may have an existing program you have to
wrap. For both of these situations, you can use the :func:`os.exec*()`
series of functions to run another program. When you "exec" a program,
the code from that program replaces the code from your existing
process.

.. include:: os_exec_example.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'os_exec_example.py'))
.. }}}
.. {{{end}}}


There are many variations of :func:`exec*()`, depending on what form
you might have the arguments in, whether you want the path and
environment of the parent process to be copied to the child, etc. Have
a look at the library documentation to for complete details.

For all variations, the first argument is a path or filename and the remaining
arguments control how that program runs. They are either passed as command
line arguments or override the process "environment" (see os.environ and
os.getenv).

Waiting for a Child
===================

Suppose you are using multiple processes to work around the threading
limitations of Python and the Global Interpreter Lock. If you start
several processes to run separate tasks, you will want to wait for one
or more of them to finish before starting new ones, to avoid
overloading the server. There are a few different ways to do that
using :func:`wait()` and related functions.

If you don't care, or know, which child process might exit first
:func:`os.wait()` will return as soon as any exits:

.. include:: os_wait_example.py
    :literal:
    :start-after: #end_pymotw_header


Notice that the return value from :func:`os.wait()` is a tuple
containing the process id and exit status ("a 16-bit number, whose low
byte is the signal number that killed the process, and whose high byte
is the exit status").

.. {{{cog
.. cog.out(run_script(cog.inFile, 'os_wait_example.py'))
.. }}}
.. {{{end}}}

If you want a specific process, use :func:`os.waitpid()`.

.. include:: os_waitpid_example.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'os_waitpid_example.py'))
.. }}}
.. {{{end}}}

:func:`wait3()` and :func:`wait4()` work in a similar manner, but
return more detailed information about the child process with the pid,
exit status, and resource usage.

Spawn
=====

As a convenience, the :func:`spawn*()` family of functions handles the
:func:`fork()` and :func:`exec*()` calls for you in one statement:

.. include:: os_spawn_example.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'os_spawn_example.py'))
.. }}}
.. {{{end}}}


.. seealso::

    `os <http://docs.python.org/lib/module-os.html>`_
        Standard library documentation for this module.

    :mod:`subprocess`
        The subprocess module supersedes os.popen().

    :mod:`multiprocessing` 
        The multiprocessing module makes working with extra processes
        easier than doing all of the work yourself.

    :mod:`tempfile`
        The tempfile module for working with temporary files.

    *Unix Manual Page Introduction*
        Includes definitions of real and effective ids, etc.
        
        http://www.scit.wlv.ac.uk/cgi-bin/mansec?2+intro

    *Speaking UNIX, Part 8.*
        Learn how UNIX multitasks.
        
        http://www.ibm.com/developerworks/aix/library/au-speakingunix8/index.html

    *Unix Concepts*
        For more discussion of stdin, stdout, and stderr.
        
        http://www.linuxhq.com/guides/LUG/node67.html

    *Delve into Unix Process Creation*
        Explains the life cycle of a UNIX process.
        
        http://www.ibm.com/developerworks/aix/library/au-unixprocess.html

    `Advanced Programming in the UNIX(R) Environment <http://www.amazon.com/Programming-Environment-Addison-Wesley-Professional-Computing/dp/0201433079/ref=pd_bbs_3/002-2842372-4768037?ie=UTF8&s=books&amp;qid=1182098757&sr=8-3>`_
        Covers working with multiple processes, such as handling signals, closing duplicated
        file descriptors, etc.

    :ref:`article-file-access`
