================================
Interactive Interpreter Settings
================================

Prompts
=======

The interpreter uses two separate prompts for indicating the default input level (``ps1``) and the "continuation" of a multi-line statement (``ps2``).  The values are only used by the interactive interpreter.

::

    >>> import sys
    >>> print repr(sys.ps1)
    '>>> '
    >>> print repr(sys.ps2)
    '... '
    >>>

Either or both prompt can be changed to a different string

::

    >>> sys.ps1 = '::: '
    ::: sys.ps2 = '~~~ '
    ::: for i in range(3):
    ~~~   print i
    ~~~ 
    0
    1
    2
    :::

Alternately, any object that can be converted to a string (via ``__str__``) can be used for the prompt.

.. include:: sys_ps1.py
    :literal:
    :start-after: #end_pymotw_header


::

    $ python
    Python 2.6.2 (r262:71600, Apr 16 2009, 09:17:39)
    [GCC 4.0.1 (Apple Computer, Inc. build 5250)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from PyMOTW.sys.sys_ps1 import LineCounter
    >>> import sys
    >>> sys.ps1 = LineCounter()
    (  1)>
    (  2)>
    (  3)>

Display Hook
============

``sys.displayhook`` is invoked by the interactive interpreter each time the user enters an expression.  The *result* of the expression is passed as the only argument to the function.  The default value (available in ``sys.__displayhook__``) prints the result to stdout and saves it in ``__builtin__._`` for easy reference later.

.. include:: sys_displayhook.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python 
    Python 2.6.2 (r262:71600, Apr 16 2009, 09:17:39) 
    [GCC 4.0.1 (Apple Computer, Inc. build 5250)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import PyMOTW.sys.sys_displayhook
    installing
    >>> 1+2

      Previous: <PyMOTW.sys.sys_displayhook.ExpressionCounter object at 0x9c5f90>
      New     : 3

    3
    (  1)> 'abc'

      Previous: 3
      New     : abc

    'abc'
    (  2)> 'abc'

      Previous: abc
      New     : abc

    'abc'
    (  2)> 'abc' * 3

      Previous: abc
      New     : abcabcabc

    'abcabcabc'
    (  3)>
