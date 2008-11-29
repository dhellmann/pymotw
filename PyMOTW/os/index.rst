============================================================
os -- Portable access to operating system specific features.
============================================================

.. module:: os
    :synopsis: Portable access to operating system specific features.

:Purpose: Portable access to operating system specific features.
:Python Version: 1.4 (or earlier)

The os module provides a wrapper for platform specific modules such as :mod:`posix`,
:mod:`nt`, and :mod:`mac`. The API for functions available on all platform should be the
same, so using the os module offers some measure of portability. Not all
functions are available on all platforms, however. Many of the process
management functions described in this summary are not available for Windows.

The Python documentation for the os module is subtitled "Miscellaneous
operating system interfaces". The module includes mostly functions for
creating and managing running processes or filesystem content (files and
directories), with a few other random bits of functionality thrown in besides.

.. note::

    Some of the example code below will only work on Unix-like operating systems.

Process Owner
=============

The first set of functions to cover are used for determining and changing
the process owner ids. These are mostly useful to authors of daemons or
special system programs which need to change permission level rather than
running as root. I won't try to explain all of the intricate details of Unix
security, process owners, etc. in this brief post. See the References list
below for more details.

Let's start with a script to show the real and effective user and group
information for a process, and then change the effective values. This is
similar to what a daemon would need to do when it starts as root during a
system boot, to lower the privilege level and run as a different user. If you
download the examples to try them out, you should change the TEST_GID and
TEST_UID values to match your user.

.. include:: os_process_user_example.py
    :literal:
    :start-after: #end_pymotw_header

When run as myself (527, 501) on OS X, I see this output:

::

    $ python os_process_user_example.py
    BEFORE CHANGE:
    Effective User  : 527
    Effective Group : 501
    Actual User      : 527 dhellmann
    Actual Group    : 501
    Actual Groups   : [501, 81, 79, 80]

    CHANGED GROUP:
    Effective User  : 527
    Effective Group : 501
    Actual User      : 527 dhellmann
    Actual Group    : 501
    Actual Groups   : [501, 81, 79, 80]

    CHANGE USER:
    Effective User  : 527
    Effective Group : 501
    Actual User      : 527 dhellmann
    Actual Group    : 501
    Actual Groups   : [501, 81, 79, 80]

Notice that the values do not change. Since I am not running as root,
processes I start cannot change their effective owner values. If I do try to
set the effective user id or group id to anything other than my own, an
OSError is raised.

Now let's look at what happens when we run the same script using ``sudo`` to start
out with root privileges:

::

    $ sudo python os_process_user_example.py
    Password:
    BEFORE CHANGE:
    Effective User  : 0
    Effective Group : 0
    Actual User      : 0 dhellmann
    Actual Group    : 0
    Actual Groups   : [0, 262, 1, 2, 3, 31, 4, 29, 5, 80, 20]

    CHANGED GROUP:
    Effective User  : 0
    Effective Group : 501
    Actual User      : 0 dhellmann
    Actual Group    : 0
    Actual Groups   : [501, 262, 1, 2, 3, 31, 4, 29, 5, 80, 20]

    CHANGE USER:
    Effective User  : 527
    Effective Group : 501
    Actual User      : 0 dhellmann
    Actual Group    : 0
    Actual Groups   : [501, 262, 1, 2, 3, 31, 4, 29, 5, 80, 20]


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

Another feature of the operating system exposed to your program though the os
module is the environment. Variables set in the environment are visible as
strings which can be read through os.environ or os.getenv(). Environment
variables are commonly used for configuration values such as search paths,
file locations, and debug flags. Let's look at an example of retrieving an
environment variable, and passing a value through to a child process.

.. include:: os_environ_example.py
    :literal:
    :start-after: #end_pymotw_header


The os.environ object follows the standard Python mapping API for retrieving
and setting values. Changes to os.environ are exported for child processes.

::

    $ python os_environ_example.py
    Initial value: None
    Child process:


    Changed value: THIS VALUE WAS CHANGED
    Child process:
    THIS VALUE WAS CHANGED

    Removed value: None
    Child process:


Process Working Directory
=========================

A concept from operating systems with hierarchical filesystems is the notion
of the "current working directory". This is the directory on the filesystem
the process uses as the default location when files are accessed with relative
paths.

.. include:: os_cwd_example.py
    :literal:
    :start-after: #end_pymotw_header

Note the use of os.curdir and os.pardir to refer to the current and parent
directories in a portable manner. The output should not be surprising:

::

    $ python os_cwd_example.py
    Starting: /Users/dhellmann/Documents/PyMOTW/PyMOTW/os
    ['.svn', '__init__.py', 'os_cwd_example.py', 'os_environ_example.py',
    'os_process_id_example.py', 'os_process_user_example.py']
    Moving up one: ..
    After move: /Users/dhellmann/Documents/PyMOTW/PyMOTW
    ['.svn', '__init__.py', 'bisect', 'ConfigParser', 'fileinput', 'linecache',
    'locale', 'logging', 'os', 'Queue', 'StringIO', 'textwrap']


Pipes
=====

The os module provides several functions for managing the I/O of child
processes using *pipes*. The functions all work essentially the same way, but
return different file handles depending on the type of input or output
desired. For the most part, these functions are made obsolete by the new-ish
:mod:`subprocess` module (added in 2.4), but there is a good chance you will
encounter them if you are maintaining existing code.

The most commonly used pipe function is popen(). It creates a new process
running the command given and attaches a single stream to the input or output
of that process, depending on the mode argument. While popen functions work on
Windows, some of these examples assume some sort of Unix-like shell. The
descriptions of the streams also assume Unix-like terminology:

* stdin - The "standard input" stream for a process (file descriptor 0) is
  readable by the process. This is usually where terminal input goes.

* stdout - The "standard output" stream for a process (file descriptor 1) is
  writable by the process, and is used for displaying non-error information to
  the user.

* stderr - The "standard error" stream for a process (file descriptor 2) is
  writable by the process, and is used for conveying error messages.

.. include:: os_popen.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python os_popen.py 
    popen, read:
            stdout: 'to stdout\n'

    popen, write:
            stdin: to stdin

The caller can only read from OR write to the streams associated with the
child process, which limits the usefulness. The other popen variants provide
additional streams so it is possible to work with stdin, stdout, and stderr as
needed.

For example, popen2() returns a write-only stream attached to stdin of the
child process, and a read-only stream attached to its stdout.

.. include:: os_popen2.py
    :literal:
    :start-after: #end_pymotw_header


This simplistic example illustrates bi-directional communication. The value
written to stdin is read by ``cat`` (because of the '-' argument), then written
back to stdout. Obviously a more complicated process could pass other types of
messages back and forth through the pipe; even serialized objects.

::

    $ python os_popen2.py 
    popen2:
            pass through: 'through stdin to stdout'

In most cases, it is desirable to have access to both stdout and stderr. The
stdout stream is used for message passing and the stderr stream is used for
errors, so reading from it separately reduces the complexity for parsing any
error messages. The popen3() function returns 3 open streams tied to stdin,
stdout, and stderr of the new process.

.. include:: os_popen3.py
    :literal:
    :start-after: #end_pymotw_header

Notice that we have to read from and close both streams *separately*. There are
some related to flow control and sequencing when dealing with I/O for multiple
processes. The I/O is buffered, and if the caller expects to be able to read
all of the data from a stream then the child process must close that stream to
indicate the end-of-file. For more information on these issues, refer to the
Flow Control Issues section of the Python library documentation.

::

    $ python os_popen3.py 
    popen3:
            pass through: 'through stdin to stdout'
            stderr: ';to stderr\n'

And finally, popen4() returns 2 streams, stdin and a merged stdout/stderr.
This is useful when the results of the command need to be logged, but not
parsed directly.

.. include:: os_popen4.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python os_popen4.py 
    popen4:
            combined output: 'through stdin to stdout;to stderr\n'

Besides accepting a single string command to be given to the shell for
parsing, popen2(), popen3(), and popen4() also accept a sequence of strings
(command, followed by arguments). In this case, the arguments are not
processed by the shell.

.. include:: os_popen2_seq.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python os_popen2_seq.py 
    popen2, cmd as sequence:
            pass through: 'through stdin to stdout'


File Descriptors
================

The os module includes the standard set of functions for working with low-level *file descriptors* (integers
representing open files owned by the current process). This is a lower-level API than is provided by
file() objects. I am going to skip over describing them here, since it is generally easier to work
directly with file() objects. Refer to the library documentation for details if you do need to use file
descriptors.

Filesystem Permissions
======================

The function os.access() can be used to test the access rights a process has
for a file.

.. include:: os_access.py
    :literal:
    :start-after: #end_pymotw_header

Your results will vary depending on how you install the example code, but it
should look something like this:

::

    $ python os_access.py
    Testing: os_access.py
    Exists: True
    Readable: True
    Writable: True
    Executable: False


The library documentation for os.access() includes 2 special warnings. First,
there isn't much sense in calling os.access() to test whether a file can be
opened before actually calling open() on it. There is a small, but real,
window between the 2 calls during which the permissions on the file could
change. The other warning applies mostly to networked filesystems which extend
the POSIX permission semantics. Some filesystem types may respond to the POSIX
call that a process has permission to access a file, then report a failure
when the attempt is made using open() for some reason not tested via the POSIX
call. All in all, it is better to call open() with the required mode and catch
the IOError raised if there is a problem.

More detailed information about the file can be accessed using os.stat() or
os.lstat() (if you want the status of something that might be a symbolic
link).

.. include:: os_stat.py
    :literal:
    :start-after: #end_pymotw_header

Once again, your results will vary depending on how the example code was
installed. Try passing different filenames on the command line to os_stat.py.

::

    $ python os_stat.py
    os.stat(os_stat.py):
          Size: 1547
          Permissions: 0100644
          Owner: 527
          Device: 234881026
          Last modified: Sun Jun 10 08:13:26 2007


On Unix-like systems, file permissions can be changed using os.chmod(),
passing the mode as an integer. Mode values can be constructed using constants
defined in the stat module. Here is an example which toggles the user's
execute permission bit:

.. include:: os_stat_chmod.py
    :literal:
    :start-after: #end_pymotw_header


The script assumes you have the right permissions to modify the mode of the
file to begin with:

::

    $ python os_stat_chmod.py
    Adding execute permission
    $ python os_stat_chmod.py
    Removing execute permission

Directories
===========

There are several functions for working with directories on the filesystem,
including creating, listing contents, and removing them.

.. include:: os_directories.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python os_directories.py
    Creating os_directories_example
    Creating os_directories_example/example.txt
    Listing os_directories_example
    ['example.txt']
    Cleaning up


There are 2 sets of functions for creating and deleting directories. When
creating a new directory with os.mkdir(), all of the parent directories must
already exist. When removing a directory with os.rmdir(), only the leaf
directory (the last part of the path) is actually removed. In contrast,
os.makedirs() and os.removedirs() operate on all of the nodes in the path.
os.makedirs() will create any parts of the path which do not exist, and
os.removedirs() will remove all of the parent directories (assuming it can).

Symbolic Links
==============

For platforms and filesystems which support them, there are several functions
for working with symlinks.

.. include:: os_symlinks.py
    :literal:
    :start-after: #end_pymotw_header


Notice that although os includes os.tempnam() for creating temporary
filenames, it is not as secure as the tempfile module and produces a
RuntimeWarning message when it is used. In general it is better to use the
tempfile module.

::

    $ python os_symlinks.py
    Creating link /tmp/tmpRxRiHn->os_symlinks.py
    Permissions: 0120755
    Points to: os_symlinks.py


Walking a Directory Tree
========================

The function os.walk() traverses a directory recursively and for each
directory generates a tuple containing the directory path, any immediate
sub-directories of that path, and the names of any files in that directory.
This example shows a simplistic recursive directory listing.

.. include:: os_walk.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python os_walk.py

    /tmp
          .KerberosLogin-0--1074266944 (inited,root,local)/
          .KerberosLogin-527-4839472 (inited,gui,tty,local)/
          527/
          cs_cache_lock_527
          cs_cache_lock_92
          emacs527/
          fry.log
          hsperfdata_dhellmann/
          objc_sharing_ppc_4294967294
          objc_sharing_ppc_527
          objc_sharing_ppc_92
          svn.arg.1835l59
          var_backups/

    /tmp/.KerberosLogin-527-4839472 (inited,gui,tty,local)
          KLLCCache.lock

    /tmp/527

    /tmp/emacs527
          server

    /tmp/hsperfdata_dhellmann
          976

    /tmp/var_backups
          infodir.bak
          local.nidump


Running External Command
========================

.. warning::

    Many of these functions for working with processes have limited portability. For a more 
    consistent way to work with processes in a platform independent manner, see the :mod:`subprocess`
    module instead.

The simplest way to run a separate command, without interacting with it at
all, is os.system(). It takes a single string which is the command line to be
executed by a sub-process running a shell.

.. include:: os_system_example.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python os_system_example.py
    total 168
    -rw-r--r--   1 dhellman  dhellman     0 May 27 06:58 __init__.py
    -rw-r--r--   1 dhellman  dhellman  1391 Jun 10 09:36 os_access.py
    -rw-r--r--   1 dhellman  dhellman  1383 May 27 09:23 os_cwd_example.py
    -rw-r--r--   1 dhellman  dhellman  1535 Jun 10 09:36 os_directories.py
    -rw-r--r--   1 dhellman  dhellman  1613 May 27 09:23 os_environ_example.py
    -rw-r--r--   1 dhellman  dhellman  2816 Jun  3 08:34 os_popen_examples.py
    -rw-r--r--   1 dhellman  dhellman  1438 May 27 09:23 os_process_id_example.py
    -rw-r--r--   1 dhellman  dhellman  1887 May 27 09:23 os_process_user_example.py
    -rw-r--r--   1 dhellman  dhellman  1545 Jun 10 09:36 os_stat.py
    -rw-r--r--   1 dhellman  dhellman  1638 Jun 10 09:36 os_stat_chmod.py
    -rw-r--r--   1 dhellman  dhellman  1452 Jun 10 09:36 os_symlinks.py
    -rw-r--r--   1 dhellman  dhellman  1279 Jun 17 12:17 os_system_example.py
    -rw-r--r--   1 dhellman  dhellman  1672 Jun 10 09:36 os_walk.py


Since the command is passed directly to the shell for processing, it can even
include shell syntax such as globbing or environment variables:

.. include:: os_system_shell.py
    :literal:
    :start-after: #end_pymotw_header

::

    total 40
    -rwx------    1 dhellman  dhellman  1328 Dec 13  2005 %backup%~
    drwx------   11 dhellman  dhellman   374 Jun 17 12:11 Desktop
    drwxr-xr-x   15 dhellman  dhellman   510 May 27 07:50 Devel
    drwx------   29 dhellman  dhellman   986 May 31 17:01 Documents
    drwxr-xr-x   45 dhellman  dhellman  1530 Jun 17 12:12 DownloadedApps
    drwx------   55 dhellman  dhellman  1870 May 22 14:53 Library
    drwx------    8 dhellman  dhellman   272 Mar  4  2006 Movies
    drwx------   10 dhellman  dhellman   340 Feb 14 10:54 Music
    drwx------   12 dhellman  dhellman   408 Jun 17 01:00 Pictures
    drwxr-xr-x    5 dhellman  dhellman   170 Oct  1  2006 Public
    drwxr-xr-x   15 dhellman  dhellman   510 May 12 15:19 Sites
    drwxr-xr-x    4 dhellman  dhellman   136 Jan 23  2006 iPod
    -rw-r--r--    1 dhellman  dhellman   105 Mar  7 11:48 pgadmin.log
    drwxr-xr-x    3 dhellman  dhellman   102 Apr 29 16:32 tmp


Unless you explicitly run the command in the background, the call to
os.system() blocks until it is complete. Standard input, output, and error
from the child process are tied to the appropriate streams owned by the caller
by default, but can be redirected using shell syntax.

.. include:: os_system_background.py
    :literal:
    :start-after: #end_pymotw_header


This is getting into shell trickery, though, and there are better ways to
accomplish the same thing.

::

    $ python os_system_background.py
    Calling...
    Sun Jun 17 12:27:20 EDT 2007
    Sleeping...
    Sun Jun 17 12:27:23 EDT 2007

.. _creating-processes-with-os-fork:

Creating Processes with os.fork()
=================================

The POSIX functions fork() and exec*() (available under Mac OS X, Linux, and
other UNIX variants) are available through the os module. Entire books have
been written about reliably using these functions, so check your library or
bookstore for more details than I will present here.

To create a new process as a clone of the current process, use os.fork():

.. include:: os_fork_example.py
    :literal:
    :start-after: #end_pymotw_header

Your output will vary based on the state of your system each time you run the
example, but it should look something like:

::

    $ python os_fork_example.py
    Child process id: 5883
    I am the child

After the fork, you end up with 2 processes running the same code. To tell
which one you are in, check the return value. If it is 0, you are inside the
child process. If it is not 0, you are in the parent process and the return
value is the process id of the child process.

From the parent process, it is possible to send the child signals. This is a
bit more complicated to set up, and uses the :mod:`signal` module, so let's walk
through the code. First we can define a signal handler to be invoked when the
signal is received.

::

    import os
    import signal
    import time

    def signal_usr1(signum, frame):
       pid = os.getpid()
       print 'Received USR1 in process %s' % pid

Then we fork, and in the parent pause a short amount of time before sending a
USR1 signal using os.kill(). The short pause gives the child process time to
set up the signal handler.

::

    print 'Forking...'
    child_pid = os.fork()
    if child_pid:
       print 'PARENT: Pausing before sending signal...'
       time.sleep(1)
       print 'PARENT: Signaling %s' % child_pid
       os.kill(child_pid, signal.SIGUSR1)

In the child, we set up the signal handler and go to sleep for a while to give
the parent time to send us the signal:

::

    else:
       print 'CHILD: Setting up signal handler'
       signal.signal(signal.SIGUSR1, signal_usr1)
       print 'CHILD: Pausing to wait for signal'
       time.sleep(5)


In a real app, you probably wouldn't need to (or want to) call sleep, of
course.

::

    $ python os_kill_example.py
    Forking...
    PARENT: Pausing before sending signal...
    CHILD: Setting up signal handler
    CHILD: Pausing to wait for signal
    PARENT: Signaling 6053
    Received USR1 in process 6053


As you see, a simple way to handle separate behavior in the child process is
to check the return value of fork() and branch. For more complex behavior, you
may want more code separation than a simple branch. In other cases, you may
have an existing program you have to wrap. For both of these situations, you
can use the os.exec*() series of functions to run another program. When you
"exec" a program, the code from that program replaces the code from your
existing process.

.. include:: os_exec_example.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python os_exec_example.py       
    total 40
    drwxr-xr-x   2 dhellman  wheel      68 Jun 17 14:35 527
    prw-------   1 root      wheel       0 Jun 15 19:24 afpserver_PIPE
    drwx------   3 dhellman  wheel     102 Jun 17 12:13 emacs527
    drwxr-xr-x   2 dhellman  wheel      68 Jun 16 05:01 hsperfdata_dhellmann
    -rw-------   1 nobody    wheel      12 Jun 17 13:55 objc_sharing_ppc_4294967294
    -rw-------   1 dhellman  wheel     144 Jun 17 14:32 objc_sharing_ppc_527
    -rw-------   1 security  wheel      24 Jun 17 07:09 objc_sharing_ppc_92
    drwxr-xr-x   4 dhellman  dhellman  136 Jun  8 03:16 var_backups


There are many variations of exec*(), depending on what form you might have
the arguments in, whether you want the path and environment of the parent
process to be copied to the child, etc. Have a look at the library
documentation to for details.

For all variations, the first argument is a path or filename and the remaining
arguments control how that program runs. They are either passed as command
line arguments or override the process "environment" (see os.environ and
os.getenv).

Waiting for a Child
===================

Suppose you are using multiple processes to work around the threading
limitations of Python and the Global Interpreter Lock. If you start several
processes to run separate tasks, you will want to wait for one or more of them
to finish before starting new ones, to avoid overloading the server. There are
a few different ways to do that using wait() and related functions.

If you don't care, or know, which child process might exit first os.wait()
will return as soon as any exits:

.. include:: os_wait_example.py
    :literal:
    :start-after: #end_pymotw_header


Notice that the return value from os.wait() is a tuple containing the process
id and exit status ("a 16-bit number, whose low byte is the signal number that
killed the process, and whose high byte is the exit status").

::

    $ python os_wait_example.py
    PARENT: Forking 0
    PARENT: Forking 1
    PARENT: Forking 2
    PARENT: Waiting for 0
    WORKER 0: Starting
    WORKER 1: Starting
    WORKER 2: Starting
    WORKER 0: Finishing
    PARENT: (6501, 0)
    PARENT: Waiting for 1
    WORKER 1: Finishing
    PARENT: (6502, 256)
    PARENT: Waiting for 2
    WORKER 2: Finishing
    PARENT: (6503, 512)

If you want a specific process, use os.waitpid().

.. include:: os_waitpid_example.py
    :literal:
    :start-after: #end_pymotw_header


::

    $ python os_waitpid_example.py
    PARENT: Forking 0
    WORKER 0: Starting
    PARENT: Forking 1
    WORKER 1: Starting
    PARENT: Forking 2
    WORKER 2: Starting
    PARENT: Waiting for 6547
    WORKER 0: Finishing
    PARENT: (6547, 0)
    PARENT: Waiting for 6548
    WORKER 1: Finishing
    PARENT: (6548, 256)
    PARENT: Waiting for 6549
    WORKER 2: Finishing
    PARENT: (6549, 512)

wait3() and wait4() work in a similar manner, but return more detailed
information about the child process with the pid, exit status, and resource
usage.

Spawn
=====

As a convenience, the os.spawn*() family of functions handles the fork() and
exec*() calls for you in one statement:

.. include:: os_spawn_example.py
    :literal:
    :start-after: #end_pymotw_header


::

    $ python os_spawn_example.py
    total 112
    drwx------  3 dhellmann  dhellmann   102 Nov 25 11:11 527
    -rw-------  1 _www       wheel         0 Nov 24 18:26 aprZUFiBL
    -rw-------  1 _www       wheel         0 Nov 24 18:26 aprrI2NMa
    srwxrwxrwx  1 dhellmann  wheel         0 Nov 24 18:26 com.hp.launchport
    drwx------  3 dhellmann  wheel       102 Nov 24 18:26 launchd-120.tTqeBv
    drwx------  2 dhellmann  wheel        68 Nov 25 09:06 ssh-15RWPs917O
    -rwx------  1 dhellmann  wheel       143 Nov 28 13:10 temp_textmate.PWLSvd
    drwxr-xr-x  2 dhellmann  dhellmann    68 Nov 25 03:15 var_backups


.. seealso::

    `os <http://docs.python.org/lib/module-os.html>`_
        Standard library documentation for this module.

    :mod:`subprocess`
        The subprocess module supersedes os.popen().

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
