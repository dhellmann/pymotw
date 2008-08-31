.. $Id$

=============
profile
=============
.. module:: profile
    :synopsis: Performance analysis of Python programs.

:Purpose: Performance analysis of Python programs.
:Python Version: 1.4 and later, these examples are for Python 2.5

Description
===========

The profile and cProfile modules provide APIs for collecting and analyzing statistics about how Python source consumes processor resources.

run()
=====

The most basic starting point in the profile module is ``run()``.  It takes a string statement as argument, and creates a report of the time spent executing different lines of code while running the statement.

.. include:: profile_fibonacci_raw.py
   :literal:
   :start-after: import profile

This recursive version of a fibonacci sequence calculator is especially useful for demonstrating the profile because we can improve the performance so much.  The standard report format looks like::

    $ python profile_fibonacci_raw.py
    RAW
    ================================================================================
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]

             57356 function calls (66 primitive calls) in 0.746 CPU seconds

       Ordered by: standard name

       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
           21    0.000    0.000    0.000    0.000 :0(append)
           20    0.000    0.000    0.000    0.000 :0(extend)
            1    0.001    0.001    0.001    0.001 :0(setprofile)
            1    0.000    0.000    0.745    0.745 &lt;string&gt;:1(&lt;module&gt;)
            1    0.000    0.000    0.746    0.746 profile:0(print fib_seq(20); print)
            0    0.000             0.000          profile:0(profiler)
     57291/21    0.744    0.000    0.744    0.035 profile_fibonacci_raw.py:13(fib)
         21/1    0.001    0.000    0.745    0.745 profile_fibonacci_raw.py:22(fib_seq)


As you can see, it takes 57356 separate function calls and 3/4 of a second to run.  Since there are only 66 *primitive* calls, we know that the vast majority of those 57k calls were recursive.  The details about where time was spent are broken out by function in the listing showing the number of calls, total time spent in the function, time per call (tottime/ncalls), cumulative time spent in a function, and the ratio of cumulative time to primitive calls.  

Not surprisingly, most of the time here is spent calling ``fib()`` repeatedly.  We can add a memoize decorator to reduce the number of recursive calls and have a big impact on the performance of this function.

.. include:: profile_fibonacci_memoized.py
    :literal:
    :start-after: import profile

By remembering the Fibonacci value at each level we can avoid most of the recursion and drop down to 145 calls that only take 0.003 seconds.  Also notice that the ncalls count for ``fib()`` shows that it *never* recurses.

::

    $ python profile_fibonacci_memoized.py
    MEMOIZED
    ================================================================================
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]

             145 function calls (87 primitive calls) in 0.003 CPU seconds

       Ordered by: standard name

       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
           21    0.000    0.000    0.000    0.000 :0(append)
           20    0.000    0.000    0.000    0.000 :0(extend)
            1    0.001    0.001    0.001    0.001 :0(setprofile)
            1    0.000    0.000    0.002    0.002 &lt;string&gt;:1(&lt;module&gt;)
            1    0.000    0.000    0.003    0.003 profile:0(print fib_seq(20); print)
            0    0.000             0.000          profile:0(profiler)
        59/21    0.001    0.000    0.001    0.000 profile_fibonacci_memoized.py:19(__call__)
           21    0.000    0.000    0.001    0.000 profile_fibonacci_memoized.py:26(fib)
         21/1    0.001    0.000    0.002    0.002 profile_fibonacci_memoized.py:36(fib_seq)


References
==========

The Fibonacci example implementation came from `Fibonacci numbers (Python) - LiteratePrograms <http://en.literateprograms.org/Fibonacci_numbers_(Python)>`_.

The memoize decorator came from `Python Decorators: Syntactic Sugar | avinash.vora <http://avinashv.net/2008/04/python-decorators-syntactic-sugar/>`_.

