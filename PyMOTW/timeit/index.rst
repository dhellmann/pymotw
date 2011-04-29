==========================================================
timeit -- Time the execution of small bits of Python code.
==========================================================

.. module:: timeit
    :synopsis: Time the execution of small bits of Python code.

:Purpose: Time the execution of small bits of Python code.
:Available In: 2.3

The :mod:`timeit` module provides a simple interface for determining
the execution time of small bits of Python code. It uses a
platform-specific time function to provide the most accurate time
calculation possible. It reduces the impact of startup or shutdown
costs on the time calculation by executing the code repeatedly.

Module Contents
===============

:mod:`timeit` defines a single public class, :class:`Timer`. The
constructor for :class:`Timer` takes a statement to be timed, and a
setup statement (to initialize variables, for example). The Python
statements should be strings and can include embedded newlines.

The :func:`timeit()` method runs the setup statement one time, then
executes the primary statement repeatedly and returns the amount of
time which passes. The argument to timeit() controls how many times to
run the statement; the default is 1,000,000.

Basic Example
=============

To illustrate how the various arguments to :class:`Timer` are used,
here is a simple example which prints an identifying value when each
statement is executed:

.. include:: timeit_example.py
    :literal:
    :start-after: #end_pymotw_header

When run, the output is:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'timeit_example.py'))
.. }}}
.. {{{end}}}

When called, :func:`timeit()` runs the setup statement one time, then
calls the main statement count times. It returns a single floating
point value representing the amount of time it took to run the main
statement count times.

When :func:`repeat()` is used, it calls :func:`timeit()` severeal
times (3 in this case) and all of the responses are returned in a
list.

Storing Values in a Dictionary
==============================

For a more complex example, let's compare the amount of time it takes
to populate a dictionary with a large number of values using a variety
of methods. First, a few constants are needed to configure the
:class:`Timer`. We'll be using a list of tuples containing strings and
integers. The :class:`Timer` will be storing the integers in a
dictionary using the strings as keys.

::

    # {{{cog include('timeit/timeit_dictionary.py', 'header')}}}
    # {{{end}}}

Next, we can define a short utility function to print the results in a
useful format. The :func:`timeit()` method returns the amount of time
it takes to execute the statement repeatedly. The output of
:func:`show_results()` converts that into the amount of time it takes
per iteration, and then further reduces the value to the amount of
time it takes to store one item in the dictionary (as averages, of
course).

::

    # {{{cog include('timeit/timeit_dictionary.py', 'show_results')}}}
    # {{{end}}}

To establish a baseline, the first configuration tested will use
:func:`__setitem__`.  All of the other variations avoid overwriting
values already in the dictionary, so this simple version should be the
fastest.

Notice that the first argument to :class:`Timer` is a multi-line
string, with indention preserved to ensure that it parses correctly
when run. The second argument is a constant established above to
initialize the list of values and the dictionary.

::

    # {{{cog include('timeit/timeit_dictionary.py', 'setitem')}}}
    # {{{end}}}

The next variation uses :func:`setdefault()` to ensure that values
already in the dictionary are not overwritten.

::

    # {{{cog include('timeit/timeit_dictionary.py', 'setdefault')}}}
    # {{{end}}}

Another way to avoid overwriting existing values is to use
:func:`has_key()` to check the contents of the dictionary explicitly.

::

    # {{{cog include('timeit/timeit_dictionary.py', 'has_key')}}}
    # {{{end}}}

Or by adding the value only if we receive a :ref:`KeyError
<exceptions-KeyError>` exception when looking for the existing value.

::

    # {{{cog include('timeit/timeit_dictionary.py', 'exception')}}}
    # {{{end}}}

And the last method we will test is the (relatively) new form using
"``in``" to determine if a dictionary has a particular key.

::

    # {{{cog include('timeit/timeit_dictionary.py', 'in')}}}
    # {{{end}}}


When run, the script produces output similar to this:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'timeit_dictionary.py'))
.. }}}
.. {{{end}}}

Those times are for a MacBook Pro running Python 2.6. Your times will
be different. Experiment with the *range_size* and *count* variables,
since different combinations will produce different results.

From the Command Line
=====================

In addition to the programmatic interface, timeit provides a command
line interface for testing modules without instrumentation.

To run the module, use the new :option:`-m` option to find the module and
treat it as the main program:

::

    $ python -m timeit

For example, to get help:

.. {{{cog
.. cog.out(run_script(cog.inFile, '-m timeit -h', ignore_error=True))
.. }}}
.. {{{end}}}

The statement argument works a little differently than the argument to
:class:`Timer`.  Instead of one long string, you pass each line of the
instructions as a separate command line argument. To indent lines
(such as inside a loop), embed spaces in the string by enclosing the
whole thing in quotes. For example:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'python -m timeit -s "d={}" "for i in range(1000):" "  d[str(i)] = i"', interpreter=None))
.. }}}
.. {{{end}}}

It is also possible to define a function with more complex code, then
import the module and call the function from the command line:

.. include:: timeit_setitem.py
    :literal:
    :start-after: #end_pymotw_header

Then to run the test:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'python -m timeit "import timeit_setitem; timeit_setitem.test_setitem()"', interpreter=None))
.. }}}
.. {{{end}}}


.. seealso::

    `timeit <http://docs.python.org/lib/module-timeit.html>`_
        Standard library documentation for this module.

    :mod:`profile`
        The profile module is also useful for performance analysis.
