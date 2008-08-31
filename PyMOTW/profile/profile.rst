=============
profile
=============
.. module:: profile
    :synopsis: Performance analysis of Python programs.

:Purpose: Performance analysis of Python programs.
:Python Version: 1.4 and later, these examples are for Python 2.5

Description
===========

The :module:`profile` and cProfile modules provide APIs for collecting and analyzing statistics about how Python source consumes processor resources.

Examples
========

The most basic starting point in the profile module is ``run()``.  It takes a string statement as argument, and creates a report of the time spent executing different lines of code while running the statement.

.. include:: profile_fibonacci_raw.py
   :literal:
   :start-after: import profile

References
==========

