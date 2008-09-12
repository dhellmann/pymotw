===================================
exceptions -- Builtin error classes
===================================

.. module:: exceptions
    :synopsis: Builtin error classes

:Purpose: The exceptions module defines the builtin errors used throughout the standard library and by the interpreter.
:Python Version: 1.5 and later


Description
===========

In the past, Python has supported simple string messages as exceptions as well as classes.  Since 1.5, all of the standard library modules use classes for exceptions.  Starting with Python 2.5, string exceptions result in a DeprecationWarning, and support for string exceptions will be removed in the future.


Base Classes
============

The exception classes are defined in a hierarchy, described in the standard library documentation.  In addition to the obvious organizational benefits, exception inheritance is useful because related exceptions can be caught by catching their base class.  In most cases, these base classes are not intended to be raised directly.

BaseException
  Base class for all exceptions.  Implements logic for creating a string representation of the exception using ``str()`` from the arguments passed to the constructor.

Exception
  Base class for exceptions that do not result in quitting the running application.  All user-defined exceptions should use Exception as a base class.

StandardError
  Base class for builtin exceptions used in the standard library.

ArithmeticError
  Base class for math-related errors.

LookupError
  Base class for errors raised when something can't be found.

EnvironmentError
  Base class for errors that come from outside of Python (the operating system, filesystem, etc.).


Raised Exceptions
=================


AssertionError
--------------

An AssertionError is raised by a failed ``assert`` statement.  

.. include:: exceptions_AssertionError_assert.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python exceptions_AssertionError_assert.py
    Traceback (most recent call last):
      File "/Users/dhellmann/Documents/PyMOTW/in_progress/exceptions/PyMOTW/exceptions/exceptions_AssertionError_assert.py", line 12, in <module>
        assert False, 'The assertion failed'
    AssertionError: The assertion failed

It is also used in the :mod:`unittest` module in methods like ``failIf()``.

.. include:: exceptions_AssertionError_unittest.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python exceptions_AssertionError_unittest.py
    F
    ======================================================================
    FAIL: test (__main__.AssertionExample)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "/Users/dhellmann/Documents/PyMOTW/in_progress/exceptions/PyMOTW/exceptions/exceptions_AssertionError_unittest.py", line 17, in test
        self.failUnless(False)
    AssertionError

    ----------------------------------------------------------------------
    Ran 1 test in 0.000s

    FAILED (failures=1)


AttributeError
--------------

When an attribute reference or assignment fails, AttributeError is raised.

For example, when trying to reference an attribute that does not exist:

.. include:: exceptions_AttributeError.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python exceptions_AttributeError.py
    Traceback (most recent call last):
      File "/Users/dhellmann/Documents/PyMOTW/in_progress/exceptions/PyMOTW/exceptions/exceptions_AttributeError.py", line 16, in <module>
        print o.attribute
    AttributeError: 'NoAttributes' object has no attribute 'attribute'

Or when trying to modify a read-only attribute:

.. include:: exceptions_AttributeError_assignment.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python exceptions_AttributeError_assignment.py
    This is the attribute value
    Traceback (most recent call last):
      File "/Users/dhellmann/Documents/PyMOTW/in_progress/exceptions/PyMOTW/exceptions/exceptions_AttributeError_assignment.py", line 20, in <module>
        o.attribute = 'New value'
    AttributeError: can't set attribute


EOFError
--------

An EOFError is raised when a builtin function like ``input()`` or ``raw_input()`` do not read any data before encountering the end of their input stream.  The file methods like ``read()`` return an empty string at the end of the file.

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

Raised by floating point operations that result in errors, when floating point exception control (fpectl) is turned on.  Enabling :mod:`fpectl` requires an interpreter compiled with the ``--with-fpectl`` flag.  Using :mod:`fpectl` is `discouraged in the stdlib docs <http://docs.python.org/lib/module-fpectl.html>`_.

.. include:: exceptions_FloatingPointError.py
    :literal:
    :start-after: #end_pymotw_header


GeneratorExit
-------------

Raised inside a generator the generator's ``close()`` method is called.

.. include:: exceptions_GeneratorExit.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python exceptions_GeneratorExit.py
    Yielding 0
    0
    Exiting early


IOError
-------

Raised when input or output fails, for example if a disk fills up or an input file does not exist.

.. include:: exceptions_IOError.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python exceptions_IOError.py
    Traceback (most recent call last):
      File "/Users/dhellmann/Documents/PyMOTW/in_progress/exceptions/PyMOTW/exceptions/exceptions_IOError.py", line 12, in <module>
        f = open('/does/not/exist', 'r')
    IOError: [Errno 2] No such file or directory: '/does/not/exist'


ImportError
-----------

Raised when a module, or member of a module, cannot be imported.  There are a few conditions where an ImportError might be raised.

1. If a module does not exist.

.. include:: exceptions_ImportError_nomodule.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python exceptions_ImportError_nomodule.py
    Traceback (most recent call last):
      File "/Users/dhellmann/Documents/PyMOTW/in_progress/exceptions/PyMOTW/exceptions/exceptions_ImportError_nomodule.py", line 12, in <module>
        import module_does_not_exist
    ImportError: No module named module_does_not_exist

2. If ``from X import Y`` is used and Y cannot be found inside the module X, an ImportError is raised.

.. include:: exceptions_ImportError_missingname.py
    :literal:
    :start-after: #end_pymotw_header

::

        $ python exceptions_ImportError_missingname.py
        Traceback (most recent call last):
          File "/Users/dhellmann/Documents/PyMOTW/in_progress/exceptions/PyMOTW/exceptions/exceptions_ImportError_missingname.py", line 12, in <module>
            from exceptions import MadeUpName
        ImportError: cannot import name MadeUpName


IndexError
----------

An IndexError is raised when a sequence reference is out of range.

.. include:: exceptions_IndexError.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python exceptions_IndexError.py
    Traceback (most recent call last):
      File "/Users/dhellmann/Documents/PyMOTW/in_progress/exceptions/PyMOTW/exceptions/exceptions_IndexError.py", line 13, in <module>
        print my_seq[3]
    IndexError: list index out of range


KeyError
--------

Similarly, a KeyError is raised when a value is not found as a key of a dictionary.

.. include:: exceptions_KeyError.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python exceptions_KeyError.py
    Traceback (most recent call last):
      File "/Users/dhellmann/Documents/PyMOTW/in_progress/exceptions/PyMOTW/exceptions/exceptions_KeyError.py", line 13, in <module>
        print d['c']
    KeyError: 'c'


KeyboardInterrupt
-----------------

A KeyboardInterrupt occurs whenever the user presses Ctrl-C (or Delete) to stop a running program.  Unlike most of the other exceptions, KeyboardInterrupt inherits directly from BaseException to avoid being caught by global exception handlers that catch Exception.

.. include:: exceptions_KeyboardInterrupt.py
    :literal:
    :start-after: #end_pymotw_header

Pressing Ctrl-C at the prompt causes a KeyboardInterrupt exception.

::

    $ python PyMOTW/exceptions/exceptions_KeyboardInterrupt.py
    Press Return or Ctrl-C: ^CCaught KeyboardInterrupt


MemoryError
-----------

If your program runs out of memory and it is possible to recover (by deleting some objects, for example), a MemoryError is raised.

.. include:: exceptions_MemoryError.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python PyMOTW/exceptions/exceptions_MemoryError.py
    0 1
    0 2
    0 3
    python(13482) malloc: *** mmap(size=1073745920) failed (error code=12)
    *** error: can't allocate region
    *** set a breakpoint in malloc_error_break to debug
    (error, discarding existing list)
    1 1
    1 2
    1 3
    python(13482) malloc: *** mmap(size=1073745920) failed (error code=12)
    *** error: can't allocate region
    *** set a breakpoint in malloc_error_break to debug
    (error, discarding existing list)
    2 1
    2 2
    2 3
    python(13482) malloc: *** mmap(size=1073745920) failed (error code=12)
    *** error: can't allocate region
    *** set a breakpoint in malloc_error_break to debug
    (error, discarding existing list)


NameError
---------

NameErrors are raised when your code refers to a name that does not exist in the current scope.  For example, an unqualified variable name.

.. include:: exceptions_NameError.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python exceptions_NameError.py
    Traceback (most recent call last):
      File "/Users/dhellmann/Documents/PyMOTW/in_progress/exceptions/PyMOTW/exceptions/exceptions_NameError.py", line 15, in <module>
        func()
      File "/Users/dhellmann/Documents/PyMOTW/in_progress/exceptions/PyMOTW/exceptions/exceptions_NameError.py", line 13, in func
        print unknown_name
    NameError: global name 'unknown_name' is not defined


NotImplementedError
-------------------

User-defined base classes can raise NotImplementedError to indicate that a method or behavior needs to be defined by a subclass, simulating an *interface*.

.. include:: exceptions_NotImplementedError.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python exceptions_NotImplementedError.py
    SubClass doing something!
    Traceback (most recent call last):
      File "/Users/dhellmann/Documents/PyMOTW/in_progress/exceptions/PyMOTW/exceptions/exceptions_NotImplementedError.py", line 27, in <module>
        BaseClass().do_something()
      File "/Users/dhellmann/Documents/PyMOTW/in_progress/exceptions/PyMOTW/exceptions/exceptions_NotImplementedError.py", line 18, in do_something
        raise NotImplementedError(self.__class__.__name__ + '.do_something')
    NotImplementedError: BaseClass.do_something


OSError
-------

OSError serves as the error class for the :mod:`os` module, and is raised when an error comes back from an os-specific function.

.. include:: exceptions_OSError.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python exceptions_OSError.py
    0
    Traceback (most recent call last):
      File "/Users/dhellmann/Documents/PyMOTW/in_progress/exceptions/PyMOTW/exceptions/exceptions_OSError.py", line 15, in <module>
        print i, os.ttyname(i)
    OSError: [Errno 25] Inappropriate ioctl for device


OverflowError
-------------

When an arithmetic operation exceeds the limits of the variable type, an OverflowError is raise.  Long integers allocate more space as values grow, so they end up raising MemoryError.  Floating point exception handling is not standardized, so floats are not checked.  Regular integers are converted to long values as needed.

.. include:: exceptions_OverflowError.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python exceptions_OverflowError.py
    Regular integer: (maxint=2147483647)
    No overflow for  <type 'long'> i = 6442450941

    Long integer:
     0 1
    10 1024
    20 1048576
    30 1073741824
    40 1099511627776
    50 1125899906842624
    60 1152921504606846976
    70 1180591620717411303424
    80 1208925819614629174706176
    90 1237940039285380274899124224

    Floating point values:
    0 1.23794003929e+27
    1 1.53249554087e+54
    2 2.34854258277e+108
    3 5.5156522631e+216
    Overflowed after  5.5156522631e+216 (34, 'Result too large')


ReferenceError
--------------

When a :mod:`weakref` proxy is used to access an object that has already been garbage collected, a ReferenceError occurs.

.. include:: exceptions_ReferenceError.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python exceptions_ReferenceError.py
    BEFORE: obj
    (Deleting <__main__.ExpensiveObject object at 0x844f0>)
    AFTER:
    Traceback (most recent call last):
      File "/Users/dhellmann/Documents/PyMOTW/in_progress/exceptions/PyMOTW/exceptions/exceptions_ReferenceError.py", line 26, in <module>
        print 'AFTER:', p.name
    ReferenceError: weakly-referenced object no longer exists


RuntimeError
------------

A RuntimeError exception is used when no other more specific exception applies.  The interpreter does not raise this exception itself very often, but some user code does.


StopIteration
-------------

When an iterator is done, it's ``next()`` method raises StopIteration.  This exception is not considered an error.

.. include:: exceptions_StopIteration.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python exceptions_StopIteration.py
    <listiterator object at 0x808b0>
    0
    1
    2
    Traceback (most recent call last):
      File "/Users/dhellmann/Documents/PyMOTW/in_progress/exceptions/PyMOTW/exceptions/exceptions_StopIteration.py", line 19, in <module>
        print i.next()
    StopIteration


SyntaxError
-----------

A SyntaxError occurs any time the parser finds source code it does not understand.  This can be while importing a module, invoking exec, or calling eval().  Attributes of the exception can be used to find exactly what part of the input text caused the exception.

.. include:: exceptions_SyntaxError.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python exceptions_SyntaxError.py
    Syntax error <string> (1-10): five times three
    invalid syntax (<string>, line 1)


SystemError
-----------

When an error occurs in the interpreter itself and there is some chance of continuing to run successfully, it raises a SystemError.  SystemErrors probably indicate a bug in the interpreter and should be reported to the maintainer.


SystemExit
----------

When sys.exit() is called, it raises SystemExit instead of exiting immediately.  This allows cleanup code in ``try:finally`` blocks to run and callers (like debuggers and test frameworks) to catch the exception and avoid exiting.


TypeError
---------

TypeErrors are caused by combining the wrong type of objects, or calling a function with the wrong type of object.

.. include:: exceptions_TypeError.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python exceptions_TypeError.py
    Traceback (most recent call last):
      File "/Users/dhellmann/Documents/PyMOTW/in_progress/exceptions/PyMOTW/exceptions/exceptions_TypeError.py", line 12, in <module>
        result = ('tuple',) + 'string'
    TypeError: can only concatenate tuple (not "str") to tuple


UnboundLocalError
-------------------

An UnboundLocalError is a type of NameError specific to local variable names.

.. include:: exceptions_UnboundLocalError.py
    :literal:
    :start-after: #end_pymotw_header

The difference between the global NameError and the UnboundLocal is the way the name is used.  Because the name "local_val" appears on the left side of an expression, it is interpreted as a local variable name.

::

    $ python exceptions_UnboundLocalError.py
    Global name error: global name 'unknown_global_name' is not defined
    Local name error: local variable 'local_val' referenced before assignment


UnicodeError
------------

UnicodeError is a subclass of ValueError and is raised when a Unicode problem occurs.  There are separate subclasses for UnicodeEncodeError, UnicodeDecodeError, and UnicodeTranslateError.


ValueError
----------

A ValueError is used when a function receives a value that has the right type but an invalid value.

.. include:: exceptions_ValueError.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python exceptions_ValueError.py
    Traceback (most recent call last):
      File "/Users/dhellmann/Documents/PyMOTW/in_progress/exceptions/PyMOTW/exceptions/exceptions_ValueError.py", line 12, in <module>
        print chr(1024)
    ValueError: chr() arg not in range(256)


ZeroDivisionError
-----------------

When zero shows up in the denominator of a division operation, a ZeroDivisionError is raised.

.. include:: exceptions_ZeroDivisionError.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python exceptions_ZeroDivisionError.py
    Traceback (most recent call last):
      File "/Users/dhellmann/Documents/PyMOTW/in_progress/exceptions/PyMOTW/exceptions/exceptions_ZeroDivisionError.py", line 12, in <module>
        print 1/0
    ZeroDivisionError: integer division or modulo by zero


Warning Categories
==================

There are also several exceptions defined for use with the :mod:`warnings` module.

Warning
  The base class for all warnings.

UserWarning
  Base class for warnings coming from user code.

DeprecationWarning
  Used for features no longer being maintained.

PendingDeprecationWarning
  Used for features that are soon going to be deprecated.

SyntaxWarning
  Used for questionable syntax.

RuntimeWarning
  Used for events that happen at runtime that might cause problems.

FutureWarning
  Warning about changes to the language or library that are coming at a later time.

ImportWarning
  Warn about problems importing a module.

UnicodeWarning
  Warn about problems with unicode text.


References
==========

Standard library documentation: `exceptions <http://docs.python.org/lib/module-exceptions.html>`_
