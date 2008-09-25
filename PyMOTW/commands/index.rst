=======================================
commands -- Run external shell commands
=======================================

.. module:: commands
    :synopsis: Run external shell commands and capture the status code and output.

:Purpose: The commands module contains utility functions for working with shell command output under Unix.
:Python Version: 1.4


.. warning::
    This module is made obsolete by the :mod:`subprocess` module.

There are 3 functions in the commands module for working with external
commands. The functions are shell-aware and return the output or status code
from the command. 

getstatusoutput()
=================

The function getstatusoutput() runs a command via the shell and returns the
exit code and the text output (stdout and stderr combined). The exit codes are
the same as for the C function wait() or os.wait(). The code is a 16-bit
number. The low byte contains the signal number that killed the process. When
the signal is zero, the high byte is the exit status of the program. If a core
file was produced, the high bit of the low byte is set.

.. include:: commands_getstatusoutput.py
    :literal:
    :start-after: #end_pymotw_header

This example runs 2 commands which exit normally, and a third which blocks
waiting to be killed from another shell. (Don't simply use Ctrl-C as the
interpreter will intercept that signal. Use ps and grep in another window to
find the read process and send it a signal with kill.)

::

    $ python commands_getstatusoutput.py
    Running: "ls -l *.py"
    Signal: 0
    Exit  : 0
    Core? : False
    Output:
    -rw-r--r--   1 dhellman  dhellman  1191 Oct 21 09:41 __init__.py
    -rw-r--r--   1 dhellman  dhellman  1321 Oct 21 09:48 commands_getoutput.py
    -rw-r--r--   1 dhellman  dhellman  1265 Oct 21 09:50 commands_getstatus.py
    -rw-r--r--   1 dhellman  dhellman  1626 Oct 21 10:10 commands_getstatusoutput.py

    Running: "ls -l *.notthere"
    Signal: 0
    Exit  : 1
    Core? : False
    Output:
    ls: *.notthere: No such file or directory

    Running: "echo "WAITING TO BE KILLED"; read input"
    Signal: 1
    Exit  : 0
    Core? : False
    Output:
    WAITING TO BE KILLED

In this example, I used ``kill -HUP $PID`` to kill the read process.

getoutput()
===========

If the exit code is not useful for your application, you can use getoutput()
to receive only the text output from the command.

.. include:: commands_getoutput.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python commands_getoutput.py
    ls -l *.py:
    -rw-r--r--   1 dhellman  dhellman  1191 Oct 21 09:41 __init__.py
    -rw-r--r--   1 dhellman  dhellman  1321 Oct 21 09:48 commands_getoutput.py
    -rw-r--r--   1 dhellman  dhellman  1265 Oct 21 09:50 commands_getstatus.py
    -rw-r--r--   1 dhellman  dhellman  1626 Oct 21 10:10 commands_getstatusoutput.py

    ls -l *.py:
    ls: *.notthere: No such file or directory


getstatus()
===========

Contrary to what you might expect, getstatus() does not run a command and
return the status code. Instead, it's argument is a filename which is combined
with "ls -ld" to build a command to be run by getoutput(). The text output of
the command is returned.

.. include:: commands_getstatus.py
    :literal:
    :start-after: #end_pymotw_header

As you notice from the output, the $ character in the argument to the last
call is escaped so the environment variable name is not expanded.

::

    $ python commands_getstatus.py
    commands_getstatus.py: -rw-r--r--   1 dhellman  dhellman  1387 Oct 21 10:19 commands_getstatus.py
    notthere.py: ls: notthere.py: No such file or directory
    $filename: ls: $filename: No such file or directory

References
==========

Standard library documentation: `commands <http://docs.python.org/lib/module-commands.html>`_
