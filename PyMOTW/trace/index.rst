======================================================
trace -- Follow Python statements as they are executed
======================================================

.. module:: trace
    :synopsis: Follow Python statements as they are executed.

:Purpose: Monitor which statements and functions are executed as a program runs to produce coverage and call-graph information.
:Python Version: 2.3 and later

The trace module helps you understand the way your program runs.  You can trace the statements executed, produce coverage reports, and investigate the relationships between functions that call each other.

Command Line Interface
======================

It is easy use trace directly from the command line.  Given the following Python scripts as input:

.. include:: trace_example/main.py
    :literal:
    :start-after: #end_pymotw_header

.. include:: trace_example/recurse.py
    :literal:
    :start-after: #end_pymotw_header

Tracing Execution
-----------------

We can see which statements are being executed as the program runs using the ``--trace`` option.

::

    $ python -m trace --trace trace_example/main.py 
     --- modulename: threading, funcname: settrace
    threading.py(70):     _trace_hook = func
     --- modulename: trace, funcname: <module>
    <string>(1):   --- modulename: trace, funcname: <module>
    main.py(7): """
    main.py(12): from recurse import recurse
     --- modulename: recurse, funcname: <module>
    recurse.py(7): """
    recurse.py(12): def recurse(level):
    main.py(14): def main():
    main.py(19): if __name__ == '__main__':
    main.py(20):     main()
     --- modulename: trace, funcname: main
    main.py(15):     print 'This is the main program.'
    This is the main program.
    main.py(16):     recurse(2)
     --- modulename: recurse, funcname: recurse
    recurse.py(13):     print 'recurse(%s)' % level
    recurse(2)
    recurse.py(14):     if level:
    recurse.py(15):         recurse(level-1)
     --- modulename: recurse, funcname: recurse
    recurse.py(13):     print 'recurse(%s)' % level
    recurse(1)
    recurse.py(14):     if level:
    recurse.py(15):         recurse(level-1)
     --- modulename: recurse, funcname: recurse
    recurse.py(13):     print 'recurse(%s)' % level
    recurse(0)
    recurse.py(14):     if level:
    recurse.py(16):     return
    recurse.py(16):     return
    recurse.py(16):     return
    main.py(17):     return

The first part of the output shows some setup operations performed by :mod:`trace`.  The rest of the output shows the entry into each function, including the module where the function is located, and then the lines of the source file as they are executed.  You can see that ``recurse()`` is entered 3 times, as you would expect from the way it is called in ``main()``.

Code Coverage
-------------

Running :mod:`trace` from the command line with the ``--count`` option will produce code coverage report information, so you can see which lines are run and which are skipped.  Since your program is usually made up of multiple files, a separate coverage report is produced for each.  By default the coverage report files are written to the same directory as the module, named after the module but with a ``.cover`` extension instead of ``.py``.  

::

    $ python -m trace --count trace_example/main.py 
    This is the main program.
    recurse(2)
    recurse(1)
    recurse(0)

And two output files, ``trace_example/main.cover``:

.. include:: trace_example/main.cover
    :literal:
    :start-after: #end_pymotw_header

and ``trace_example/recurse.cover``:

.. include:: trace_example/recurse.cover
    :literal:
    :start-after: #end_pymotw_header

.. note:: 

    Although the line ``def recurse(level):`` has a count of ``1``, that does not mean the function was only run once.  It means the function *definition* was only executed once.

It is also possible to run the program several times, perhaps with different options, to save the coverage data and produce a combined report.

::

    $ python -m trace --coverdir coverdir1 --count --file coverdir1/coverage_report.dat trace_example/main.py 
    This is the main program.
    recurse(2)
    recurse(1)
    recurse(0)
    Skipping counts file 'coverdir1/coverage_report.dat': [Errno 2] No such file or directory: 'coverdir1/coverage_report.dat'
    $ python -m trace --coverdir coverdir1 --count --file coverdir1/coverage_report.dat trace_example/main.py 
    This is the main program.
    recurse(2)
    recurse(1)
    recurse(0)
    $ python -m trace --coverdir coverdir1 --count --file coverdir1/coverage_report.dat trace_example/main.py 
    This is the main program.
    recurse(2)
    recurse(1)
    recurse(0)
    $ find coverdir1
    coverdir1
    coverdir1/coverage_report.dat

Once the coverage information is recorded to the ``.cover`` files, you can produce reports with the ``--report`` option.

::

    $ python -m trace --coverdir coverdir1 --report --summary --missing --file coverdir1/coverage_report.dat trace_example/main.py 
    lines   cov%   module   (path)
      533     0%   threading   (/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/threading.py)
        8   100%   trace_example.main   (trace_example/main.py)
        8    87%   trace_example.recurse   (trace_example/recurse.py)
    $ find coverdir1
    coverdir1
    coverdir1/coverage_report.dat
    coverdir1/threading.cover
    coverdir1/trace_example.main.cover
    coverdir1/trace_example.recurse.cover

Since the program ran three times, the coverage report shows values three times higher than the first report.  The ``--summary`` option adds the percent covered information to the output above.  The ``recurse`` module is only 87% covered.  A quick look at the cover file for recurse shows that the body of ``not_called()`` is indeed never run, indicated by the ``>>>>>>`` prefix.

.. include:: coverdir1/trace_example.recurse.cover
    :literal:
    :start-after: #end_pymotw_header

Calling Relationships
---------------------

In addition to coverage information, :mod:`trace` will collect and report on the relationships between functions that call each other.

For a simple list of the functions called, use ``--listfuncs``:

::

    $ python -m trace --listfuncs trace_example/main.py 
    This is the main program.
    recurse(2)
    recurse(1)
    recurse(0)

    functions called:
    filename: /Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/threading.py, modulename: threading, funcname: settrace
    filename: <string>, modulename: <string>, funcname: <module>
    filename: trace_example/main.py, modulename: main, funcname: <module>
    filename: trace_example/main.py, modulename: main, funcname: main
    filename: trace_example/recurse.py, modulename: recurse, funcname: <module>
    filename: trace_example/recurse.py, modulename: recurse, funcname: recurse

For more details about who is doing the calling, use ``-trackcalls``.

::

    $ python -m trace --listfuncs --trackcalls trace_example/main.py 
    This is the main program.
    recurse(2)
    recurse(1)
    recurse(0)

    calling relationships:

    *** /Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/trace.py ***
      --> /Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/threading.py
        trace.Trace.run -> threading.settrace
      --> <string>
        trace.Trace.run -> <string>.<module>

    *** <string> ***
      --> trace_example/main.py
        <string>.<module> -> main.<module>

    *** trace_example/main.py ***
        main.<module> -> main.main
      --> trace_example/recurse.py
        main.<module> -> recurse.<module>
        main.main -> recurse.recurse

    *** trace_example/recurse.py ***
        recurse.recurse -> recurse.recurse

Programming Interface
=====================

For a little more control over the trace interface, you can invoke it from within your program using a :class:`Trace` object.  :class:`Trace` lets you set up fixtures and other dependencies before running a single function or execing a Python command to be traced.

.. include:: trace_run.py
    :literal:
    :start-after: #end_pymotw_header

Since the example only traces into the ``recurse()`` function, no information from ``main.py`` is included in the output.

::

    $ python trace_run.py
     --- modulename: threading, funcname: settrace
    threading.py(70):     _trace_hook = func
     --- modulename: trace_run, funcname: <module>
    <string>(1):   --- modulename: recurse, funcname: recurse
    recurse.py(13):     print 'recurse(%s)' % level
    recurse(2)
    recurse.py(14):     if level:
    recurse.py(15):         recurse(level-1)
     --- modulename: recurse, funcname: recurse
    recurse.py(13):     print 'recurse(%s)' % level
    recurse(1)
    recurse.py(14):     if level:
    recurse.py(15):         recurse(level-1)
     --- modulename: recurse, funcname: recurse
    recurse.py(13):     print 'recurse(%s)' % level
    recurse(0)
    recurse.py(14):     if level:
    recurse.py(16):     return
    recurse.py(16):     return
    recurse.py(16):     return

That same output could have been produced with the ``runfunc()`` method, too.      ``runfunc()`` accepts arbitrary positional and keyword arguments, which are passed to the function when it is called by the tracer.

.. include:: trace_runfunc.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python trace_runfunc.py
     --- modulename: recurse, funcname: recurse
    recurse.py(13):     print 'recurse(%s)' % level
    recurse(2)
    recurse.py(14):     if level:
    recurse.py(15):         recurse(level-1)
     --- modulename: recurse, funcname: recurse
    recurse.py(13):     print 'recurse(%s)' % level
    recurse(1)
    recurse.py(14):     if level:
    recurse.py(15):         recurse(level-1)
     --- modulename: recurse, funcname: recurse
    recurse.py(13):     print 'recurse(%s)' % level
    recurse(0)
    recurse.py(14):     if level:
    recurse.py(16):     return
    recurse.py(16):     return
    recurse.py(16):     return


Saving Result Data
------------------

Counts and coverage information can be recorded as well, just as with the command line interface.  The data must be saved explicitly, using the :class:`CoverageResults` instance from the :class:`Trace` object.

.. include:: trace_CoverageResults.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python trace_CoverageResults.py
    recurse(2)
    recurse(1)
    recurse(0)

    $ find coverdir2
    coverdir2/
    coverdir2//trace_example.recurse.cover

    $ cat coverdir2/trace_example.recurse.cover
           #!/usr/bin/env python
           # encoding: utf-8
           #
           # Copyright (c) 2008 Doug Hellmann All rights reserved.
           #
           """
           """

           #__version__ = "$Id: recurse.py 1732 2008-10-12 14:50:28Z dhellmann $"
           #end_pymotw_header

    >>>>>> def recurse(level):
        3:     print 'recurse(%s)' % level
        3:     if level:
        2:         recurse(level-1)
        3:     return

    >>>>>> def not_called():
    >>>>>>     print 'This function is never called.'

To save the counts data for generating reports, use the *infile* and *outfile* argument to :class:`Trace`.

.. include:: trace_report.py
    :literal:
    :start-after: #end_pymotw_header

Pass a filename to *infile* to read previously stored data, and a filename to *outfile* to write new results after tracing.  If *infile* and *outfile* are the same, it has the effect of updating the file with cummulative data.

::

    $ python trace_report.py
    recurse(2)
    recurse(1)
    recurse(0)
    lines   cov%   module   (path)
        7    57%   trace_example.recurse   (trace_example/recurse.py)


Trace Options
-------------

The constructor for :class:`Trace` takes several optional parameters to control runtime behavior.

*count*
  Boolean.  Turns on line number counting.  Defaults to True.
*countfuncs*
  Boolean.  Turns on list of functions called during the run.  Defaults to False.
*countcallers*
  Boolean.  Turns on tracking for callers and callees.  Defaults to False.
*ignoremods*
  Sequence.  List of modules or packages to ignore when tracking coverage.  Defaults to an empty tuple.
*ignoredirs*
  Sequence.  List of directories containing modules or packages to be ignored.  Defaults to an empty tuple.
*infile*
  Name of the file containing cached count values.  Defaults to None.
*outfile*
  Name of the file to use for storing cached count files.  Defaults to None, and data is not stored.


References
==========

Standard library documentation: `trace <http://docs.python.org/library/trace.html>`_

Other Code Coverage Tools
-------------------------

`Ned Batchelder's coverage.py <http://nedbatchelder.com/code/modules/coverage.html>`_

`Titus Brown's figleaf <http://darcs.idyll.org/~t/projects/figleaf/doc/>`_
