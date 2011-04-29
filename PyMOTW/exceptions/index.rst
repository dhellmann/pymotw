====================================
exceptions -- Built-in error classes
====================================

.. module:: exceptions
    :synopsis: Built-in error classes

:Purpose: The exceptions module defines the built-in errors used throughout the standard library and by the interpreter.
:Available In: 1.5 and later


Description
===========

In the past, Python has supported simple string messages as exceptions as well as classes.  Since 1.5, all of the standard library modules use classes for exceptions.  Starting with Python 2.5, string exceptions result in a DeprecationWarning, and support for string exceptions will be removed in the future.


Base Classes
============

The exception classes are defined in a hierarchy, described in the standard library documentation.  In addition to the obvious organizational benefits, exception inheritance is useful because related exceptions can be caught by catching their base class.  In most cases, these base classes are not intended to be raised directly.

BaseException
-------------

Base class for all exceptions.  Implements logic for creating a string 
representation of the exception using str() from the arguments passed 
to the constructor.

Exception
---------

Base class for exceptions that do not result in quitting the running application.
All user-defined exceptions should use Exception as a base class.

StandardError
-------------

Base class for built-in exceptions used in the standard library.

ArithmeticError
---------------

Base class for math-related errors.

LookupError
-----------

Base class for errors raised when something can't be found.

EnvironmentError
----------------

Base class for errors that come from outside of Python (the operating
system, filesystem, etc.).


Raised Exceptions
=================

.. _exceptions-AssertionError:

AssertionError
--------------

An AssertionError is raised by a failed ``assert`` statement.  

.. include:: exceptions_AssertionError_assert.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_AssertionError_assert.py', ignore_error=True))
.. }}}
.. {{{end}}}

It is also used in the :mod:`unittest` module in methods like ``failIf()``.

.. include:: exceptions_AssertionError_unittest.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_AssertionError_unittest.py', ignore_error=True))
.. }}}
.. {{{end}}}

.. _exceptions-AttributeError:

AttributeError
--------------

When an attribute reference or assignment fails, AttributeError is
raised.  For example, when trying to reference an attribute that does
not exist:

.. include:: exceptions_AttributeError.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_AttributeError.py', ignore_error=True))
.. }}}
.. {{{end}}}

Or when trying to modify a read-only attribute:

.. include:: exceptions_AttributeError_assignment.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_AttributeError_assignment.py', ignore_error=True))
.. }}}
.. {{{end}}}


EOFError
--------

An EOFError is raised when a built-in function like ``input()`` or
``raw_input()`` do not read any data before encountering the end of
their input stream.  The file methods like ``read()`` return an empty
string at the end of the file.

.. include:: exceptions_EOFError.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ echo hello | python PyMOTW/exceptions/exceptions_EOFError.py
    prompt:READ: hello
    prompt:Traceback (most recent call last):
      File "PyMOTW/exceptions/exceptions_EOFError.py", line 13, in <module>
        data = raw_input('prompt:')
    EOFError: EOF when reading a line


FloatingPointError
------------------

Raised by floating point operations that result in errors, when
floating point exception control (fpectl) is turned on.  Enabling
:mod:`fpectl` requires an interpreter compiled with the
``--with-fpectl`` flag.  Using :mod:`fpectl` is `discouraged in the
stdlib docs <http://docs.python.org/lib/module-fpectl.html>`_.

.. include:: exceptions_FloatingPointError.py
    :literal:
    :start-after: #end_pymotw_header


GeneratorExit
-------------

Raised inside a generator the generator's ``close()`` method is called.

.. include:: exceptions_GeneratorExit.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_GeneratorExit.py'))
.. }}}
.. {{{end}}}

.. _exceptions-IOError:

IOError
-------

Raised when input or output fails, for example if a disk fills up or
an input file does not exist.

.. include:: exceptions_IOError.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_IOError.py', ignore_error=True))
.. }}}
.. {{{end}}}

.. _exceptions-ImportError:

ImportError
-----------

Raised when a module, or member of a module, cannot be imported.
There are a few conditions where an ImportError might be raised.

1. If a module does not exist.

.. include:: exceptions_ImportError_nomodule.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_ImportError_nomodule.py', ignore_error=True))
.. }}}
.. {{{end}}}

2. If ``from X import Y`` is used and Y cannot be found inside the
module X, an ImportError is raised.

.. include:: exceptions_ImportError_missingname.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_ImportError_missingname.py', ignore_error=True))
.. }}}
.. {{{end}}}


IndexError
----------

An IndexError is raised when a sequence reference is out of range.

.. include:: exceptions_IndexError.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_IndexError.py', ignore_error=True))
.. }}}
.. {{{end}}}

.. _exceptions-KeyError:

KeyError
--------

Similarly, a KeyError is raised when a value is not found as a key of a dictionary.

.. include:: exceptions_KeyError.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_KeyError.py', ignore_error=True))
.. }}}
.. {{{end}}}

.. _exceptions-KeyboardInterrupt:

KeyboardInterrupt
-----------------

A KeyboardInterrupt occurs whenever the user presses Ctrl-C (or
Delete) to stop a running program.  Unlike most of the other
exceptions, KeyboardInterrupt inherits directly from BaseException to
avoid being caught by global exception handlers that catch Exception.

.. include:: exceptions_KeyboardInterrupt.py
    :literal:
    :start-after: #end_pymotw_header

Pressing Ctrl-C at the prompt causes a KeyboardInterrupt exception.

::

    $ python exceptions_KeyboardInterrupt.py
    Press Return or Ctrl-C: ^CCaught KeyboardInterrupt


MemoryError
-----------

If your program runs out of memory and it is possible to recover (by
deleting some objects, for example), a MemoryError is raised.

.. include:: exceptions_MemoryError.py
    :literal:
    :start-after: #end_pymotw_header

.. This takes a while to run, so don't bother with cog.

::

	$ python exceptions_MemoryError.py
	python(49670) malloc: *** mmap(size=1073745920) failed (error code=12)
	*** error: can't allocate region
	*** set a breakpoint in malloc_error_break to debug
	python(49670) malloc: *** mmap(size=1073745920) failed (error code=12)
	*** error: can't allocate region
	*** set a breakpoint in malloc_error_break to debug
	python(49670) malloc: *** mmap(size=1073745920) failed (error code=12)
	*** error: can't allocate region
	*** set a breakpoint in malloc_error_break to debug
	0 1
	0 2
	0 3
	(error, discarding existing list)
	1 1
	1 2
	1 3
	(error, discarding existing list)
	2 1
	2 2
	2 3
	(error, discarding existing list)


NameError
---------

NameErrors are raised when your code refers to a name that does not
exist in the current scope.  For example, an unqualified variable
name.

.. include:: exceptions_NameError.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_NameError.py', ignore_error=True))
.. }}}
.. {{{end}}}

.. _exceptions-NotImplementedError:

NotImplementedError
-------------------

User-defined base classes can raise NotImplementedError to indicate
that a method or behavior needs to be defined by a subclass,
simulating an *interface*.

.. include:: exceptions_NotImplementedError.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_NotImplementedError.py', ignore_error=True))
.. }}}
.. {{{end}}}

.. seealso::

   :mod:`abc` - Abstract base classes

OSError
-------

OSError serves as the error class for the :mod:`os` module, and is
raised when an error comes back from an os-specific function.

.. include:: exceptions_OSError.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_OSError.py', ignore_error=True))
.. }}}
.. {{{end}}}


.. _exceptions-OverflowError:

OverflowError
-------------

When an arithmetic operation exceeds the limits of the variable type,
an OverflowError is raise.  Long integers allocate more space as
values grow, so they end up raising MemoryError.  Floating point
exception handling is not standardized, so floats are not checked.
Regular integers are converted to long values as needed.

.. include:: exceptions_OverflowError.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_OverflowError.py', ignore_error=True))
.. }}}
.. {{{end}}}


ReferenceError
--------------

When a :mod:`weakref` proxy is used to access an object that has
already been garbage collected, a ReferenceError occurs.

.. include:: exceptions_ReferenceError.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_ReferenceError.py', ignore_error=True))
.. }}}
.. {{{end}}}

.. _exceptions-RuntimeError:

RuntimeError
------------

A RuntimeError exception is used when no other more specific exception
applies.  The interpreter does not raise this exception itself very
often, but some user code does.


StopIteration
-------------

When an iterator is done, it's ``next()`` method raises StopIteration.
This exception is not considered an error.

.. include:: exceptions_StopIteration.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_StopIteration.py', ignore_error=True))
.. }}}
.. {{{end}}}


SyntaxError
-----------

A SyntaxError occurs any time the parser finds source code it does not
understand.  This can be while importing a module, invoking ``exec``,
or calling ``eval()``.  Attributes of the exception can be used to
find exactly what part of the input text caused the exception.

.. include:: exceptions_SyntaxError.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_SyntaxError.py', ignore_error=True))
.. }}}
.. {{{end}}}


SystemError
-----------

When an error occurs in the interpreter itself and there is some
chance of continuing to run successfully, it raises a SystemError.
SystemErrors probably indicate a bug in the interpreter and should be
reported to the maintainer.

.. _exceptions-SystemExit:

SystemExit
----------

When ``sys.exit()`` is called, it raises SystemExit instead of exiting
immediately.  This allows cleanup code in ``try:finally`` blocks to
run and special environments (like debuggers and test frameworks) to
catch the exception and avoid exiting.

.. _exceptions-TypeError:

TypeError
---------

TypeErrors are caused by combining the wrong type of objects, or
calling a function with the wrong type of object.

.. include:: exceptions_TypeError.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_TypeError.py', ignore_error=True))
.. }}}
.. {{{end}}}


UnboundLocalError
-------------------

An UnboundLocalError is a type of NameError specific to local variable
names.

.. include:: exceptions_UnboundLocalError.py
    :literal:
    :start-after: #end_pymotw_header

The difference between the global NameError and the UnboundLocal is
the way the name is used.  Because the name "local_val" appears on the
left side of an expression, it is interpreted as a local variable
name.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_UnboundLocalError.py', ignore_error=True))
.. }}}
.. {{{end}}}

.. _exceptions-UnicodeError:

UnicodeError
------------

:class:`UnicodeError` is a subclass of :class:`ValueError` and is
raised when a Unicode problem occurs.  There are separate subclasses
for :class:`UnicodeEncodeError`, :class:`UnicodeDecodeError`, and
:class:`UnicodeTranslateError`.

.. _exceptions-ValueError:

ValueError
----------

A ValueError is used when a function receives a value that has the
right type but an invalid value.

.. include:: exceptions_ValueError.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_ValueError.py', ignore_error=True))
.. }}}
.. {{{end}}}

.. _exceptions-ZeroDivisionError:

ZeroDivisionError
-----------------

When zero shows up in the denominator of a division operation, a
ZeroDivisionError is raised.

.. include:: exceptions_ZeroDivisionError.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'exceptions_ZeroDivisionError.py', ignore_error=True))
.. }}}
.. {{{end}}}

.. _exceptions-warning:

Warning Categories
==================

There are also several exceptions defined for use with the :mod:`warnings` module.

Warning
  The base class for all warnings.

UserWarning
  Base class for warnings coming from user code.

.. _exceptions-DeprecationWarning:

DeprecationWarning
  Used for features no longer being maintained.

PendingDeprecationWarning
  Used for features that are soon going to be deprecated.

SyntaxWarning
  Used for questionable syntax.

.. _exceptions-RuntimeWarning:

RuntimeWarning
  Used for events that happen at runtime that might cause problems.

FutureWarning
  Warning about changes to the language or library that are coming at a later time.

ImportWarning
  Warn about problems importing a module.

UnicodeWarning
  Warn about problems with unicode text.


.. seealso::

    `exceptions <http://docs.python.org/library/exceptions.html>`_
        The standard library documentation for this module.

    :mod:`warnings`
        Non-error warning messages.
