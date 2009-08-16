===================================
dis -- Python Bytecode Disassembler
===================================

.. module:: dis
    :synopsis: Python Bytecode Disassembler

:Purpose: Convert code objects to a human-readable representation of the bytecodes for analysis.
:Python Version: 1.4 and later

The :mod:`dis` module includes functions for working with Python bytecode by "disassembling" it into a more human-readable form.  Reviewing the bytecodes being executed by the interpreter is a good way to hand-tune tight loops and perform other kinds of optimizations.  It is also useful for finding race conditions in multi-threaded applications, since you can estimate where in your code thread control may switch.

Basic Disassembly
=================

The function ``dis.dis()`` prints the disassembled representation of a Python code source (module, class, method, function, or code object).  We can disassemble a module such as:

.. literalinclude:: dis_simple.py
    :linenos:

by running dis from the command line.  The output is organized into columns with the original source line number, the instruction "address" within the code object, the opcode name, and any arguments passed to the opcode.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-m dis dis_simple.py'))
.. }}}
.. {{{end}}}

In this case, the source translates to 5 different operations to create and populate the dictionary, then save the results to a local variable.  Since the Python interpreter is stack-based, the first steps are to put the constants onto the stack in the correct order with LOAD_CONST, and then use STORE_MAP to pop off the new key and value to be added to the dictionary.  The resulting object is bound to the name "my_dict" with STORE_NAME.


Disassembling Functions
=======================

Unfortunately, disassembling the entire module does not recurse into functions automatically.  For example, if we disassemble this module:

.. literalinclude:: dis_function.py
    :linenos:

the results show loading the code object onto the stack and then turning it into a function (LOAD_CONST, MAKE_FUNCTION), but *not* the body of the function.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-m dis dis_function.py'))
.. }}}
.. {{{end}}}

To see inside the function, we need to pass it to ``dis.dis()``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'dis_function.py'))
.. }}}
.. {{{end}}}


Classes
=======

You can also pass classes to ``dis``, in which case all of the methods are disassembled in turn.

.. literalinclude:: dis_class.py
    :linenos:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'dis_class.py'))
.. }}}
.. {{{end}}}


Exception Handling
==================

Sometimes when debugging an exception it can be useful to see which bytecode caused a problem.  There are a couple of ways to disassemble the code around an error.  

The first is by using ``dis.dis()`` in the interactive interpreter to report about the last exception.  If no argument is passed to ``dis``, then it looks for an exception and shows the disassembly of the most top of the stack that caused it.

::

    $ python
    Python 2.6.2 (r262:71600, Apr 16 2009, 09:17:39) 
    [GCC 4.0.1 (Apple Computer, Inc. build 5250)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import dis
    >>> j = 4
    >>> i = i + 4
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'i' is not defined
    >>> dis.distb()
      1 -->       0 LOAD_NAME                0 (i)
                  3 LOAD_CONST               0 (4)
                  6 BINARY_ADD          
                  7 STORE_NAME               0 (i)
                 10 LOAD_CONST               1 (None)
                 13 RETURN_VALUE        
    >>>

Notice the ``-->`` indicating the opcode that caused the error.  There is no "i" variable defined, so the value associated with the name can't be loaded onto the stack.

Within your code you can also print the information about an active traceback by passing it to ``dis.distb()`` directly.  In this example, there is a DivideByZero exception, but since the formula has two divisions it isn't clear which part is zero.  

.. literalinclude:: dis_traceback.py
    :linenos:

The bad value is easy to spot when it is loaded onto the stack in the disassembled version.  The bad operation is highlighted with the ``-->``, and we just need to look up a few lines higher to find where ``i``'s ``0`` value was pushed onto the stack.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'dis_traceback.py'))
.. }}}
.. {{{end}}}


Loop Analysis
=============

.. literalinclude:: dis_slow_loop.py
    :linenos:

.. {{{cog
.. cog.out(run_script(cog.inFile, '-m dis dis_slow_loop.py'))
.. }}}
.. {{{end}}}


Compiler Optimizations
======================

literal constant expression folding (d = {'a':1+2})

.. seealso::

    `dis <http://docs.python.org/library/dis.html>`_
        The standard library documentation for this module, including the list of `bytecode instructions <http://docs.python.org/library/dis.html#python-bytecode-instructions>`_.

    *Python Essential Reference*, 4th Edition, David M. Beazley
        http://www.informit.com/store/product.aspx?isbn=0672329786

    `thomas.apestaart.org "Python Disassembly" <http://thomas.apestaart.org/log/?p=927>`_
        A short discussion of the difference between storing values in a dictionary between Python 2.5 and 2.6.

    `Why is looping over range() in Python faster than using a while loop? <http://stackoverflow.com/questions/869229/why-is-looping-over-range-in-python-faster-than-using-a-while-loop>`_
        A discussion on StackOverflow.com comparing 2 looping examples via their disassembled bytecodes.

    `Decorator for binding constants at compile time <http://code.activestate.com/recipes/277940/>`_
        Python Cookbook recipe by Raymond Hettinger and Skip Montanaro with a function decorator that re-writes the bytecodes for a function to insert global constants to avoid runtime name lookups.
