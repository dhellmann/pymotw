=======================================================
atexit -- Call functions when a program is closing down
=======================================================

.. module:: atexit
    :synopsis: Register function(s) to be called when a program is closing down.

:Purpose: Register function(s) to be called when a program is closing down.
:Python Version: 2.1.3 and later

Description
===========

The atexit module provides a simple interface to register functions to be
called when a program closes down normally. The sys module also provides a
hook, sys.exitfunc, but only one function can be registered there. The atexit
registry can be used by multiple modules and libraries simultaneously.

Examples
========

A simple example of registering a function via atexit.register() looks like:

::

    import atexit

    def all_done():
       print 'all_done()'

    print 'Registering'
    atexit.register(all_done)
    print 'Registered'

Since the program doesn't do anything else, all_done() is called right away:

::

    $ python atexit_simple.py
    Registering
    Registered
    all_done()

It is also possible to register more than one function, and to pass arguments.
That can be useful to cleanly disconnect from databases, remove temporary
files, etc. Since it is possible to pass arguments to the registered
functions, we don't even need to keep a separate list of things to clean up --
we can just register a clean up function more than once.

::

    def my_cleanup(name):
       print 'my_cleanup(%s)' % name

    atexit.register(my_cleanup, 'first')
    atexit.register(my_cleanup, 'second')
    atexit.register(my_cleanup, 'third')

Notice that order in which the exit functions are called is not the reverse of
the order they are registered. This allows modules to be cleaned up in the
reverse order from which they are imported (and therefore register their
atexit functions), which should reduce dependencies.

::

    $ python atexit_multiple.py
    my_cleanup(third)
    my_cleanup(second)
    my_cleanup(first)

When are atexit functions not called?
=====================================

The callbacks registered with atexit are not invoked if:

* the program dies because of a signal

* os._exit() is invoked directly

* a Python fatal error is detected (in the interpreter)

To illustrate a program being killed via a signal, we can modify one of the
examples from the subprocess summary last week. There are 2 files involved,
the parent and the child programs. The parent starts the child, pauses, then
kills it:

::

    import os
    import signal
    import subprocess
    import time

    proc = subprocess.Popen('atexit_signal_child.py')
    print 'PARENT: Pausing before sending signal...'
    time.sleep(1)
    print 'PARENT: Signaling %s' % proc.pid
    os.kill(proc.pid, signal.SIGTERM)

The child sets up an atexit callback, to prove that it is not called.

::

    import atexit
    import time

    def not_called():
       print 'CHILD: atexit handler should not have been called'

    print 'CHILD: Registering atexit handler'
    atexit.register(not_called)

    print 'CHILD: Pausing to wait for signal'
    time.sleep(5)

When run, the output should look something like this:

::

    $ python atexit_signal_parent.py
    CHILD: Registering atexit handler
    CHILD: Pausing to wait for signal
    PARENT: Pausing before sending signal...
    PARENT: Signaling 2038

Note that the child does not print the message embedded in not_called().

Similarly, if a program bypasses the normal exit path it can avoid having the
atexit callbacks invoked.

::

    import atexit
    import os

    def not_called():
       print 'This should not be called'

    print 'Registering'
    atexit.register(not_called)
    print 'Registered'

    print 'Exiting...'
    os._exit(0)

Since we call os._exit() instead of exiting normally, the callback is not
invoked. 

::

    $ python atexit_os_exit.py
    Registering
    Registered
    Exiting...

If we had instead used sys.exit(), the callbacks would still have been called.

::

    import atexit
    import sys

    def all_done():
       print 'all_done()'

    print 'Registering'
    atexit.register(all_done)
    print 'Registered'

    print 'Exiting...'
    sys.exit()

::

    $ python atexit_sys_exit.py
    Registering
    Registered
    Exiting...
    all_done()

Simulating a fatal error in the Python interpreter is left as an exercise to
the reader. :-)

Exceptions in atexit Callbacks
==============================

Tracebacks for exceptions raised in atexit callbacks are printed to the
console and the last exception raised is re-raised to be the final error
message of the program.

::

    def exit_with_exception(message):
       raise RuntimeError(message)

    atexit.register(exit_with_exception, 'Registered first')
    atexit.register(exit_with_exception, 'Registered second')

Notice again that the registration order controls the execution order. If an
error in one callback introduces an error in another (registered earlier, but
called later), the final error message might not be the most useful error
message to show the user.

::

    $ python atexit_exception.py
    Error in atexit._run_exitfuncs:
    Traceback (most recent call last):
     File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/atexit.py", line 24, in _run_exitfuncs
       func(*targs, **kargs)
     File "atexit_exception.py", line 36, in exit_with_exception
       raise RuntimeError(message)
    RuntimeError: Registered second
    Error in atexit._run_exitfuncs:
    Traceback (most recent call last):
     File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/atexit.py", line 24, in _run_exitfuncs
       func(*targs, **kargs)
     File "atexit_exception.py", line 36, in exit_with_exception
       raise RuntimeError(message)
    RuntimeError: Registered first
    Error in sys.exitfunc:
    Traceback (most recent call last):
     File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/atexit.py", line 24, in _run_exitfuncs
       func(*targs, **kargs)
     File "atexit_exception.py", line 36, in exit_with_exception
       raise RuntimeError(message)
    RuntimeError: Registered first

In general you will probably want to handle and quietly log all exceptions in
your cleanup functions, since it is messy to have a program dump errors on
exit.

.. seealso::

    `atexit <http://docs.python.org/library/atexit.html>`_
        The standard library documentation for this module.

