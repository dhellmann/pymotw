===================================
dis -- Python Bytecode Disassembler
===================================

.. module:: dis
    :synopsis: Python Bytecode Disassembler

:Purpose: Convert code objects to a human-readable representation of the bytecodes for analysis.
:Available In: 1.4 and later

The :mod:`dis` module includes functions for working with Python
bytecode by "disassembling" it into a more human-readable form.
Reviewing the bytecodes being executed by the interpreter is a good
way to hand-tune tight loops and perform other kinds of optimizations.
It is also useful for finding race conditions in multi-threaded
applications, since you can estimate the point in your code where
thread control may switch.

Basic Disassembly
=================

The function ``dis.dis()`` prints the disassembled representation of a
Python code source (module, class, method, function, or code object).
We can disassemble a module such as:

.. literalinclude:: dis_simple.py
    :linenos:

by running :mod:`dis` from the command line.  The output is organized
into columns with the original source line number, the instruction
"address" within the code object, the opcode name, and any arguments
passed to the opcode.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-m dis dis_simple.py'))
.. }}}
.. {{{end}}}

In this case, the source translates to 5 different operations to
create and populate the dictionary, then save the results to a local
variable.  Since the Python interpreter is stack-based, the first
steps are to put the constants onto the stack in the correct order
with LOAD_CONST, and then use STORE_MAP to pop off the new key and
value to be added to the dictionary.  The resulting object is bound to
the name "my_dict" with STORE_NAME.


Disassembling Functions
=======================

Unfortunately, disassembling the entire module does not recurse into
functions automatically.  For example, if we start with this module:

.. literalinclude:: dis_function.py
    :linenos:

the results show loading the code object onto the stack and then
turning it into a function (LOAD_CONST, MAKE_FUNCTION), but *not* the
body of the function.

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

You can also pass classes to ``dis``, in which case all of the methods
are disassembled in turn.

.. literalinclude:: dis_class.py
    :linenos:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'dis_class.py'))
.. }}}
.. {{{end}}}


Using Disassembly to Debug
==========================

Sometimes when debugging an exception it can be useful to see which
bytecode caused a problem.  There are a couple of ways to disassemble
the code around an error.

The first is by using ``dis.dis()`` in the interactive interpreter to
report about the last exception.  If no argument is passed to ``dis``,
then it looks for an exception and shows the disassembly of the top of
the stack that caused it.

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

Notice the ``-->`` indicating the opcode that caused the error.  There
is no ``i`` variable defined, so the value associated with the name
can't be loaded onto the stack.

Within your code you can also print the information about an active
traceback by passing it to ``dis.distb()`` directly.  In this example,
there is a DivideByZero exception, but since the formula has two
divisions it isn't clear which part is zero.

.. literalinclude:: dis_traceback.py
    :linenos:

The bad value is easy to spot when it is loaded onto the stack in the
disassembled version.  The bad operation is highlighted with the
``-->``, and we just need to look up a few lines higher to find where
``i``'s ``0`` value was pushed onto the stack.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'dis_traceback.py'))
.. }}}
.. {{{end}}}


Performance Analysis of Loops
=============================

Aside from debugging errors, :mod:`dis` can also help you identify
performance issues in your code. Examining the disassembled code is
especially useful with tight loops where the number of exposed Python
instructions is low but they translate to an inefficient set of
bytecodes.  We can see how the disassembly is helpful by examining a
few different implementations of a class, ``Dictionary``, that reads a
list of words and groups them by their first letter.

First, the test driver application:

.. include:: dis_test_loop.py
    :literal:
    :start-after: #end_pymotw_header

We can use ``dis_test_loop.py`` to run each incarnation of the
``Dictionary`` class.

A straightforward implementation of ``Dictionary`` might look
something like:

.. literalinclude:: dis_slow_loop.py
    :linenos:

The output shows this version taking 0.1074 seconds to load the 234936
words in my copy of ``/usr/share/dict/words`` on OS X.  That's not too
bad, but as you can see from the disassembly below, the loop is doing
more work than it needs to.  As it enters the loop in opcode 13, it
sets up an exception context (``SETUP_EXCEPT``).  Then it takes 6
opcodes to find ``self.by_letter[word[0]]`` before appending ``word``
to the list.  If there is an exception because ``word[0]`` isn't in
the dictionary yet, the exception handler does all of the same work to
determine ``word[0]`` (3 opcodes) and sets ``self.by_letter[word[0]]``
to a new list containing the word.

.. timing values are sensitive to other operations, so don't cog

::

	$ python dis_test_loop.py dis_slow_loop
	 11           0 SETUP_LOOP              84 (to 87)
	              3 LOAD_FAST                1 (words)
	              6 GET_ITER            
	        >>    7 FOR_ITER                76 (to 86)
	             10 STORE_FAST               2 (word)
	
	 12          13 SETUP_EXCEPT            28 (to 44)
	
	 13          16 LOAD_FAST                0 (self)
	             19 LOAD_ATTR                0 (by_letter)
	             22 LOAD_FAST                2 (word)
	             25 LOAD_CONST               1 (0)
	             28 BINARY_SUBSCR       
	             29 BINARY_SUBSCR       
	             30 LOAD_ATTR                1 (append)
	             33 LOAD_FAST                2 (word)
	             36 CALL_FUNCTION            1
	             39 POP_TOP             
	             40 POP_BLOCK           
	             41 JUMP_ABSOLUTE            7
	
	 14     >>   44 DUP_TOP             
	             45 LOAD_GLOBAL              2 (KeyError)
	             48 COMPARE_OP              10 (exception match)
	             51 JUMP_IF_FALSE           27 (to 81)
	             54 POP_TOP             
	             55 POP_TOP             
	             56 POP_TOP             
	             57 POP_TOP             
	
	 15          58 LOAD_FAST                2 (word)
	             61 BUILD_LIST               1
	             64 LOAD_FAST                0 (self)
	             67 LOAD_ATTR                0 (by_letter)
	             70 LOAD_FAST                2 (word)
	             73 LOAD_CONST               1 (0)
	             76 BINARY_SUBSCR       
	             77 STORE_SUBSCR        
	             78 JUMP_ABSOLUTE            7
	        >>   81 POP_TOP             
	             82 END_FINALLY         
	             83 JUMP_ABSOLUTE            7
	        >>   86 POP_BLOCK           
	        >>   87 LOAD_CONST               0 (None)
	             90 RETURN_VALUE        
	
	TIME: 0.1074

One technique to eliminate the exception setup is to pre-populate
``self.by_letter`` with one list for each letter of the alphabet.
That means we should always find the list we want for the new word,
and can just do the lookup and save the value.


.. literalinclude:: dis_faster_loop.py
    :linenos:

The change cuts the number of opcodes in half, but only shaves the
time down to 0.0984 seconds.  Obviously the exception handling had
some overhead, but not a huge amount.

.. timing values are sensitive to other operations, so don't cog

::

	$ python dis_test_loop.py dis_faster_loop
	 14           0 SETUP_LOOP              38 (to 41)
	              3 LOAD_FAST                1 (words)
	              6 GET_ITER            
	        >>    7 FOR_ITER                30 (to 40)
	             10 STORE_FAST               2 (word)
	
	 15          13 LOAD_FAST                0 (self)
	             16 LOAD_ATTR                0 (by_letter)
	             19 LOAD_FAST                2 (word)
	             22 LOAD_CONST               1 (0)
	             25 BINARY_SUBSCR       
	             26 BINARY_SUBSCR       
	             27 LOAD_ATTR                1 (append)
	             30 LOAD_FAST                2 (word)
	             33 CALL_FUNCTION            1
	             36 POP_TOP             
	             37 JUMP_ABSOLUTE            7
	        >>   40 POP_BLOCK           
	        >>   41 LOAD_CONST               0 (None)
	             44 RETURN_VALUE        
	
	TIME: 0.0984

We can further improve the performance by moving the lookup for
``self.by_letter`` outside of the loop (the value doesn't change,
after all).

.. literalinclude:: dis_fastest_loop.py
    :linenos:

Opcodes 0-6 now find the value of ``self.by_letter`` and save it as a
local variable ``by_letter``.  Using a local variable only takes a
single opcode, instead of 2 (statement 22 uses ``LOAD_FAST`` to place
the dictionary onto the stack).  After this change, the run time is
down to 0.0842 seconds.

.. timing values are sensitive to other operations, so don't cog

::

	$ python dis_test_loop.py dis_fastest_loop
	 13           0 LOAD_FAST                0 (self)
	              3 LOAD_ATTR                0 (by_letter)
	              6 STORE_FAST               2 (by_letter)
	
	 14           9 SETUP_LOOP              35 (to 47)
	             12 LOAD_FAST                1 (words)
	             15 GET_ITER            
	        >>   16 FOR_ITER                27 (to 46)
	             19 STORE_FAST               3 (word)
	
	 15          22 LOAD_FAST                2 (by_letter)
	             25 LOAD_FAST                3 (word)
	             28 LOAD_CONST               1 (0)
	             31 BINARY_SUBSCR       
	             32 BINARY_SUBSCR       
	             33 LOAD_ATTR                1 (append)
	             36 LOAD_FAST                3 (word)
	             39 CALL_FUNCTION            1
	             42 POP_TOP             
	             43 JUMP_ABSOLUTE           16
	        >>   46 POP_BLOCK           
	        >>   47 LOAD_CONST               0 (None)
	             50 RETURN_VALUE        
	
	TIME: 0.0842

A further optimization, suggested by Brandon Rhodes, is to eliminate
the Python version of the ``for`` loop entirely. If we use
:ref:`itertools.groupby() <itertools-groupby>` to arrange the input,
the iteration is moved to C.  We can do this safely because we know
the inputs are already sorted.  If you didn't know they were sorted
you would need to sort them first.

.. literalinclude:: dis_eliminate_loop.py
    :linenos:

The :mod:`itertools` version takes only 0.0543 seconds to run, just
over half of the original time.

.. timing values are sensitive to other operations, so don't cog

::

	$ python dis_test_loop.py dis_eliminate_loop
	 15           0 LOAD_GLOBAL              0 (itertools)
	              3 LOAD_ATTR                1 (groupby)
	              6 LOAD_FAST                1 (words)
	              9 LOAD_CONST               1 ('key')
	             12 LOAD_GLOBAL              2 (operator)
	             15 LOAD_ATTR                3 (itemgetter)
	             18 LOAD_CONST               2 (0)
	             21 CALL_FUNCTION            1
	             24 CALL_FUNCTION          257
	             27 STORE_FAST               2 (grouped)
	
	 17          30 LOAD_GLOBAL              4 (dict)
	             33 LOAD_CONST               3 (<code object <genexpr> at 0x7e7b8, file "/Users/dhellmann/Documents/PyMOTW/dis/PyMOTW/dis/dis_eliminate_loop.py", line 17>)
	             36 MAKE_FUNCTION            0
	             39 LOAD_FAST                2 (grouped)
	             42 GET_ITER            
	             43 CALL_FUNCTION            1
	             46 CALL_FUNCTION            1
	             49 LOAD_FAST                0 (self)
	             52 STORE_ATTR               5 (by_letter)
	             55 LOAD_CONST               0 (None)
	             58 RETURN_VALUE        
	
	TIME: 0.0543


Compiler Optimizations
======================

Disassembling compiled source also exposes some of the optimizations
made by the compiler.  For example, literal expressions are folded
during compilation, when possible.

.. literalinclude:: dis_constant_folding.py
    :linenos:

The expressions on lines 5-7 can be computed at compilation time and
collapsed into single LOAD_CONST instructions because nothing in the
expression can change the way the operation is performed.  That isn't
true about lines 10-12. Because a variable is involved in those
expressions, and the variable might refer to an object that overloads
the operator involved, the evaluation has to be delayed to runtime.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-m dis dis_constant_folding.py'))
.. }}}
.. {{{end}}}


.. seealso::

    `dis <http://docs.python.org/library/dis.html>`_
        The standard library documentation for this module, including
        the list of `bytecode instructions
        <http://docs.python.org/library/dis.html#python-bytecode-instructions>`_.

    *Python Essential Reference*, 4th Edition, David M. Beazley
        http://www.informit.com/store/product.aspx?isbn=0672329786

    `thomas.apestaart.org "Python Disassembly" <http://thomas.apestaart.org/log/?p=927>`_
        A short discussion of the difference between storing values in
        a dictionary between Python 2.5 and 2.6.

    `Why is looping over range() in Python faster than using a while loop? <http://stackoverflow.com/questions/869229/why-is-looping-over-range-in-python-faster-than-using-a-while-loop>`_
        A discussion on StackOverflow.com comparing 2 looping examples
        via their disassembled bytecodes.

    `Decorator for binding constants at compile time <http://code.activestate.com/recipes/277940/>`_
        Python Cookbook recipe by Raymond Hettinger and Skip Montanaro
        with a function decorator that re-writes the bytecodes for a
        function to insert global constants to avoid runtime name
        lookups.
