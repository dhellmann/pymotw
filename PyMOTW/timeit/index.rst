==========================================================
timeit -- Time the execution of small bits of Python code.
==========================================================

.. module:: timeit
    :synopsis: Time the execution of small bits of Python code.

:Purpose: Time the execution of small bits of Python code.
:Python Version: 2.3

The timeit module provides a simple interface for determining the execution time of small
bits of Python code. It uses a platform-specific time function to provide the most accurate
time calculation possible. It reduces the impact of startup or shutdown costs on the time
calculation by executing the code repeatedly.

Module Contents
===============

timeit defines a single public class, Timer. The constructor for Timer takes a
statement to be timed, and a setup statement (to initialize variables, for
example). The Python statements should be strings and can include embedded
newlines. 

The timeit() method runs the setup statement one time, then executes the
primary statement repeatedly and returns the amount of time which passes. The
argument to timeit() controls how many times to run the statement; the default
is 1,000,000.

Basic Example
=============

To illustrate how the various arguments to Timer are used, here is a simple
example which prints an identifying value when each statement is executed:

.. include:: timeit_example.py
    :literal:
    :start-after: #end_pymotw_header

When run, the output is:

::

    $ python timeit_example.py
    TIMEIT:
    setup
    main statement
    main statement
    0.000208854675293
    REPEAT:
    setup
    main statement
    main statement
    setup
    main statement
    main statement
    setup
    main statement
    main statement
    [0.00019812583923339844, 0.00019383430480957031, 0.00019383430480957031]

When called, timeit() runs the setup statement one time, then calls the main
statement count times. It returns a single floating point value representing
the amount of time it took to run the main statement count times.

When repeat() is used, it calls timeit() severeal times (3 in this case) and
all of the responses are returned in a list.

Storing Values in a Dictionary
==============================

For a more complex example, let's compare the amount of time it takes to
populate a dictionary with a large number of values using a variety of
methods. First, a few constants are needed to configure the Timer. We'll be
using a list of tuples containing strings and integers. The Timer will be
storing the integers in a dictionary using the strings as keys.

::

    import timeit
    import sys

    # A few constants
    range_size=1000
    count=1000
    setup_statement="l = [ (str(x), x) for x in range(%d) ]; d = {}" % range_size

Next, we can define a short utility function to print the results in a useful
format. The timeit() method returns the amount of time it takes to execute the
statement repeatedly. The output of show_results() converts that into the
amount of time it takes per iteration, and then further reduces the value to
the amount of time it takes to store one item in the dictionary (as averages,
of course).

::

    def show_results(result):
        "Print results in terms of microseconds per pass and per item."
        global count, range_size
        per_pass = 1000000 * (result / count)
        print '%.2f usec/pass' % per_pass,
        per_item = per_pass / range_size
        print '%.2f usec/item' % per_item

    print "%d items" % range_size
    print "%d iterations" % count
    print


To establish a baseline, the first configuration tested will use __setitem__.
All of the other variations avoid overwriting values already in the
dictionary, so this simple version should be the fastest.

Notice that the first argument to Timer is a multi-line string, with indention
preserved to ensure that it parses correctly when run. The second argument is
a constant established above to initialize the list of values and the
dictionary.

::

    # Using __setitem__ without checking for existing values first
    print '__setitem__:\t',
    sys.stdout.flush()
    # using setitem
    t = timeit.Timer("""
    for s, i in l:
        d[s] = i
    """, 
    setup_statement)
    show_results(t.timeit(number=count))


The next variation uses setdefault() to ensure that values already in the
dictionary are not overwritten.

::

    # Using setdefault
    print 'setdefault:\t',
    sys.stdout.flush()
    t = timeit.Timer("""
    for s, i in l:
        d.setdefault(s, i)
    """,
    setup_statement)
    show_results(t.timeit(number=count))


Another way to avoid overwriting existing values is to use has_key() to check
the contents of the dictionary explicitly.

::

    # Using has_key
    print 'has_key:\t',
    sys.stdout.flush()
    # using setitem
    t = timeit.Timer("""
    for s, i in l:
        if not d.has_key(s):
            d[s] = i
    """, 
    setup_statement)
    show_results(t.timeit(number=count))

Or by adding the value only if we receive a KeyError exception when looking
for the existing value.

::

    # Using exceptions
    print 'KeyError:\t',
    sys.stdout.flush()
    # using setitem
    t = timeit.Timer("""
    for s, i in l:
        try:
            existing = d[s]
        except KeyError:
            d[s] = i
    """, 
    setup_statement)
    show_results(t.timeit(number=count))

And the last method we will test is the (relatively) new form using "in" to
determine if a dictionary has a particular key.

::

    # Using "not in"
    print '"in":\t',
    sys.stdout.flush()
    # using setitem
    t = timeit.Timer("""
    for s, i in l:
        if s not in d:
            d[s] = i
    """, 
    setup_statement)
    show_results(t.timeit(number=count))


When run, the script produces output similar to this:

::

    $ python timeit_dictionary.py 
    1000 items
    1000 iterations

    __setitem__:    848.35 usec/pass 0.85 usec/item
    setdefault:     2050.21 usec/pass 2.05 usec/item
    has_key:        1554.51 usec/pass 1.55 usec/item
    KeyError:       1040.11 usec/pass 1.04 usec/item
    "not in":       707.38 usec/pass 0.71 usec/item

Those times are for a G4 PowerBook running Python 2.5. Your times will be
different. Experiment with the range_size and count variables, since different
combinations will produce different results. For example:

::

    $ python timeit_dictionary.py 
    10000 items
    1000 iterations

    __setitem__:    11227.27 usec/pass 1.12 usec/item
    setdefault:     24125.01 usec/pass 2.41 usec/item
    has_key:        19145.40 usec/pass 1.91 usec/item
    KeyError:       24127.39 usec/pass 2.41 usec/item
    "not in":       16064.97 usec/pass 1.61 usec/item

From the Command Line
=====================

In addition to the programmatic interface, timeit provides a command line
interface for testing modules without instrumentation. 

To run the module, use the new -m option to find the module and treat it as
main:

::

    $ python -m timeit

For example, to get help:

::

    $ python -m timeit -h
    Tool for measuring execution time of small code snippets.

    This module avoids a number of common traps for measuring execution times.
    See also Tim Peters' introduction to the Algorithms chapter in the Python
    Cookbook, published by O'Reilly.

    Library usage: see the Timer class.

    Command line usage:
        python timeit.py [-n N] [-r N] [-s S] [-t] [-c] [-h] [statement]

    Options:
      -n/--number N: how many times to execute 'statement' (default: see below)
      -r/--repeat N: how many times to repeat the timer (default 3)
      -s/--setup S: statement to be executed once initially (default 'pass')
      -t/--time: use time.time() (default on Unix)
      -c/--clock: use time.clock() (default on Windows)
      -v/--verbose: print raw timing results; repeat for more digits precision
      -h/--help: print this usage message and exit
      statement: statement to be timed (default 'pass')

The statement argument works a little differently than the argument to Timer.
Instead of one long string, you pass each line of the instructions as a
separate command line argument. To indent lines (such as inside a loop), embed
spaces in the string by enclosing the whole thing in quotes. For example:

::

    $ python -m timeit -s "d={}" "for i in range(1000):" "  d[str(i)] = i"
    10 loops, best of 3: 16.7 msec per loop

It is also possible to define a function with more complex code, then import
the module and call the function from the command line:

::

    def test_setitem(range_size=1000):
        l = [ (str(x), x) for x in range(range_size) ]
        d = {}
        for s, i in l:
            d[s] = i

Then to run the test::

    $ python -m timeit "import timeit_setitem; timeit_setitem.test_setitem()"
    100 loops, best of 3: 3.56 msec per loop


.. seealso::

    `timeit <http://docs.python.org/lib/module-timeit.html>`_
        Standard library documentation for this module.
