========================================
doctest -- Testing through documentation
========================================

.. module:: doctest
    :synopsis: Write automated tests as part of the documentation for a module.

:Purpose: Write automated tests as part of the documentation for a module.
:Available In: 2.1

:mod:`doctest` lets you test your code by running examples embedded in
the documentation and verifying that they produce the expected
results.  It works by parsing the help text to find examples, running
them, then comparing the output text against the expected value.  Many
developers find :mod:`doctest` easier than :mod:`unittest` because in
its simplest form, there is no API to learn before using it.  However,
as the examples become more complex the lack of fixture management can
make writing :mod:`doctest` tests more cumbersome than using
:mod:`unittest`.

Getting Started
===============

The first step to setting up doctests is to use the interactive
interpreter to create examples and then copy and paste them into the
docstrings in your module.  Here, :func:`my_function` has two examples
given:

.. include:: doctest_simple.py
   :literal:
   :start-after: #end_pymotw_header

To run the tests, use :mod:`doctest` as the main program via the
``-m`` option to the interpreter.  Usually no output is produced while
the tests are running, so the example below includes the ``-v`` option
to make the output more verbose.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-m doctest -v doctest_simple.py'))
.. }}}
.. {{{end}}}

Examples cannot usually stand on their own as explanations of a
function, so :mod:`doctest` also lets you keep the surrounding text
you would normally include in the documentation.  It looks for lines
beginning with the interpreter prompt, ``>>>``, to find the beginning
of a test case.  The case is ended by a blank line, or by the next
interpreter prompt.  Intervening text is ignored, and can have any
format as long as it does not look like a test case.

.. include:: doctest_simple_with_docs.py
   :literal:
   :start-after: #end_pymotw_header

The surrounding text in the updated docstring makes it more useful to
a human reader, and is ignored by :mod:`doctest`, and the results are
the same.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-m doctest -v doctest_simple_with_docs.py'))
.. }}}
.. {{{end}}}

Handling Unpredictable Output
=============================

There are other cases where the exact output may not be predictable,
but should still be testable.  Local date and time values and object
ids change on every test run.  The default precision used in the
representation of floating point values depend on compiler options.
Object string representations may not be deterministic.  Although
these conditions are outside of your control, there are techniques for
dealing with them.

For example, in CPython, object identifiers are based on the memory
address of the data structure holding the object.  

.. include:: doctest_unpredictable.py
   :literal:
   :start-after: #end_pymotw_header

These id values change each time a program runs, because it is loaded
into a different part of memory.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-m doctest -v doctest_unpredictable.py', ignore_error=True))
.. }}}
.. {{{end}}}

When the tests include values that are likely to change in
unpredictable ways, and where the actual value is not important to the
test results, you can use the ``ELLIPSIS`` option to tell
:mod:`doctest` to ignore portions of the verification value.

.. include:: doctest_ellipsis.py
   :literal:
   :start-after: #end_pymotw_header

The comment after the call to :func:`unpredictable` (``#doctest:
+ELLIPSIS``) tells :mod:`doctest` to turn on the ``ELLIPSIS`` option
for that test.  The ``...`` replaces the memory address in the object
id, so that portion of the expected value is ignored and the actual
output matches and the test passes.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-m doctest -v doctest_ellipsis.py'))
.. }}}
.. {{{end}}}

There are cases where you cannot ignore the unpredictable value,
because that would obviate the test.  For example, simple tests
quickly become more complex when dealing with data types whose string
representations are inconsistent.  The string form of a dictionary,
for example, may change based on the order the keys are added.

.. include:: doctest_hashed_values.py
   :literal:
   :start-after: #end_pymotw_header

Because of cache collision, the internal key list order is different
for the two dictionaries, even though they contain the same values and
are considered to be equal.  Sets use the same hashing algorithm, and
exhibit the same behavior.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'doctest_hashed_values.py'))
.. }}}
.. {{{end}}}

The best way to deal with these potential discrepancies is to create
tests that produce values that are not likely to change.  In the case
of dictionaries and sets, that might mean looking for specific keys
individually, generating a sorted list of the contents of the data
structure, or comparing against a literal value for equality instead
of depending on the string representation.

.. include:: doctest_hashed_values_tests.py
   :literal:
   :start-after: #end_pymotw_header

Notice that the single example is actually interpreted as two separate
tests, with the first expecting no console output and the second
expecting the boolean result of the comparison operation.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-m doctest -v doctest_hashed_values_tests.py'))
.. }}}
.. {{{end}}}

Tracebacks
==========

Tracebacks are a special case of changing data.  Since the paths in a
traceback depend on the location where a module is installed on the
filesystem on a given system, it would be impossible to write portable
tests if they were treated the same as other output.

.. include:: doctest_tracebacks.py
   :literal:
   :start-after: #end_pymotw_header

:mod:`doctest` makes a special effort to recognize tracebacks, and
ignore the parts that might change from system to system.  

.. {{{cog
.. cog.out(run_script(cog.inFile, '-m doctest -v doctest_tracebacks.py'))
.. }}}
.. {{{end}}}

In fact, the entire body of the traceback is ignored and can be
omitted.

.. include:: doctest_tracebacks_no_body.py
   :literal:
   :start-after: #end_pymotw_header

When :mod:`doctest` sees a traceback header line (either ``Traceback
(most recent call last):`` or ``Traceback (innermost last):``,
depending on the version of Python you are running), it skips ahead to
find the exception type and message, ignoring the intervening lines
entirely.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-m doctest -v doctest_tracebacks_no_body.py'))
.. }}}
.. {{{end}}}

Working Around Whitespace
=========================

In real world applications, output usually includes whitespace such as
blank lines, tabs, and extra spacing to make it more readable.  Blank
lines, in particular, cause issues with :mod:`doctest` because they
are used to delimit tests.  

.. include:: doctest_blankline_fail.py
   :literal:
   :start-after: #end_pymotw_header

:func:`double_space` takes a list of input lines, and prints them
double-spaced with blank lines between.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-m doctest doctest_blankline_fail.py', ignore_error=True))
.. }}}
.. {{{end}}}

The test fails, because it interprets the blank line after ``Line
one.`` in the docstring as the end of the sample output.  To match the
blank lines, replace them in the sample input with the string
``<BLANKLINE>``.

.. include:: doctest_blankline.py
   :literal:
   :start-after: #end_pymotw_header

:mod:`doctest` replaces actual blank lines with the same literal
before performing the comparison, so now the actual and expected
values match and the test passes.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-m doctest -v doctest_blankline.py'))
.. }}}
.. {{{end}}}

Another pitfall of using text comparisons for tests is that embedded
whitespace can also cause tricky problems with tests.  This example
has a single extra space after the ``6``.

.. include:: doctest_extra_space.py
   :literal:
   :start-after: #end_pymotw_header

Extra spaces can find their way into your code via copy-and-paste
errors, but since they come at the end of the line, they can go
unnoticed in the source file and be invisible in the test failure
report as well.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-m doctest -v doctest_extra_space.py', ignore_error=True))
.. }}}
.. {{{end}}}

Using one of the diff-based reporting options, such as
``REPORT_NDIFF``, shows the difference between the actual and expected
values with more detail, and the extra space becomes visible.

.. include:: doctest_ndiff.py
   :literal:
   :start-after: #end_pymotw_header

Unified (``REPORT_UDIFF``) and context (``REPORT_CDIFF``) diffs are
also available, for output where those formats are more readable.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-m doctest -v doctest_ndiff.py', ignore_error=True))
.. }}}
.. {{{end}}}

There are cases where it is beneficial to add extra whitespace in the
sample output for the test, and have :mod:`doctest` ignore it.  For
example, data structures can be easier to read when spread across
several lines, even if their representation would fit on a single
line.

.. include:: doctest_normalize_whitespace.py
   :literal:
   :start-after: #end_pymotw_header

When ``NORMALIZE_WHITESPACE`` is turned on, any whitespace in the
actual and expected values is considered a match.  You cannot add
whitespace to the expected value where none exists in the output, but
the length of the whitespace sequence and actual whitespace characters
do not need to match.  The first test example gets this rule correct,
and passes, even though there are extra spaces and newlines.  The
second has extra whitespace after ``[`` and before ``]``, so it fails.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-m doctest -v doctest_normalize_whitespace.py', ignore_error=True))
.. }}}
.. {{{end}}}

Test Locations
==============

All of the tests in the examples so far have been written in the
docstrings of the functions they are testing.  That is convenient for
users who examine the docstrings for help using the funcion
(especially with :mod:`pydoc`), but :mod:`doctest` looks for tests in
other places, too.  The obvious location for additional tests is in
the docstrings elsewhere in the module.

.. include:: doctest_docstrings.py
   :literal:

Every docstring can contain tests at the module, class and function
level.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-m doctest -v doctest_docstrings.py'))
.. }}}
.. {{{end}}}

In cases where you have tests that you want to include with your
source code, but do not want to have appear in the help for your
module, you need to put them somewhere other than the docstrings.
:mod:`doctest` also looks for a module-level variable called
``__test__`` and uses it to locate other tests.  ``__test__`` should
be a dictionary mapping test set names (as strings) to strings,
modules, classes, or functions.

.. include:: doctest_private_tests.py
   :literal:
   :start-after: #end_pymotw_header

If the value associated with a key is a string, it is treated as a
docstring and scanned for tests.  If the value is a class or function,
:mod:`doctest` searchs them recursivesly for docstrings, which are
then scanned for tests.  In this example, the module
:mod:`doctest_private_tests_external` has a single test in its
docstring.

.. include:: doctest_private_tests_external.py
   :literal:

:mod:`doctest` finds a total of five tests to run.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-m doctest -v doctest_private_tests.py'))
.. }}}
.. {{{end}}}

External Documentation
======================

Mixing tests in with your code isn't the only way to use
:mod:`doctest`.  Examples embedded in external project documentation
files, such as reStructuredText files, can be used as well.

.. include:: doctest_in_help.py
   :literal:
   :start-after: #end_pymotw_header

The help for :mod:`doctest_in_help` is saved to a separate file,
``doctest_in_help.rst``.  The examples illustrating how to use the
module are included with the help text, and :mod:`doctest` can be used
to find and run them.

.. include:: doctest_in_help.rst
   :literal:

The tests in the text file can be run from the command line, just as
with the Python source modules.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-m doctest -v doctest_in_help.rst'))
.. }}}
.. {{{end}}}

Normally :mod:`doctest` sets up the test execution environment to
include the members of the module being tested, so your tests don't
need to import the module explicitly.  In this case, however, the
tests aren't defined in a Python module, :mod:`doctest` does not know
how to set up the global namespace, so the examples need to do the
import work themselves.  All of the tests in a given file share the
same execution context, so importing the module once at the top of the
file is enough.

Running Tests
=============

The previous examples all use the command line test runner built into
:mod:`doctest`.  It is easy and convenient for a single module, but
will quickly become tedious as your package spreads out into multiple
files.  There are several alternative approaches.

By Module
---------

You can include instructions to run :mod:`doctest` against your source
at the bottom of your modules.  Use :func:`testmod` without any
arguments to test the current module.

.. include:: doctest_testmod.py
   :literal:
   :start-after: #end_pymotw_header

Ensure the tests are only run when the module is called as a main
program by invoking :func:`testmod` only if the current module name is
``__main__``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'doctest_testmod.py -v'))
.. }}}
.. {{{end}}}

The first argument to :func:`testmod` is a module containing code to
be scanned for tests.  This feature lets you create a separate test
script that imports your real code and runs the tests in each module
one after another.

.. include:: doctest_testmod_other_module.py
   :literal:
   :start-after: #end_pymotw_header

You can build a test suite for your project by importing each module
and running its tests.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'doctest_testmod_other_module.py -v'))
.. }}}
.. {{{end}}}

By File
-------

:func:`testfile` works in a way similar to :func:`testmod`, allowing
you to explicitly invoke the tests in an external file from within
your test program.

.. include:: doctest_testfile.py
   :literal:
   :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'doctest_testfile.py -v'))
.. }}}
.. {{{end}}}

Both :func:`testmod` and :func:`testfile` include optional parameters
to let you control the behavior of the tests through the
:mod:`doctest` options, global namespace for the tests, etc.  Refer to
the standard library documentation for more details if you need those
features -- most of the time you won't need them.

Unittest Suite
--------------

If you use both :mod:`unittest` and :mod:`doctest` for testing the
same code in different situations, you may find the :mod:`unittest`
integration in :mod:`doctest` useful for running the tests together.
Two classes, :class:`DocTestSuite` and :class:`DocFileSuite` create
test suites compatible with the test-runner API of :mod:`unittest`.

.. include:: doctest_unittest.py
   :literal:
   :start-after: #end_pymotw_header

The tests from each source are collapsed into a single outcome,
instead of being reported individually.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'doctest_unittest.py'))
.. }}}
.. {{{end}}}


Test Context
============

The execution context created by :mod:`doctest` as it runs tests
contains a copy of the module-level globals for the module containing
your code.  This isolates the tests from each other somewhat, so they
are less likely to interfere with one another.  Each test source
(function, class, module) has its own set of global values.

.. include:: doctest_test_globals.py
   :literal:
   :start-after: #end_pymotw_header

:class:`TestGlobals` has two methods, :func:`one` and :func:`two`.
The tests in the docstring for :func:`one` set a global variable, and
the test for :func:`two` looks for it (expecting not to find it).

.. {{{cog
.. cog.out(run_script(cog.inFile, '-m doctest -v doctest_test_globals.py'))
.. }}}
.. {{{end}}}

That does not mean the tests *cannot* interfere with each other,
though, if they change the contents of mutable variables defined in
the module.

.. include:: doctest_mutable_globals.py
   :literal:
   :start-after: #end_pymotw_header

The module varabile ``_module_data`` is changed by the tests for
:func:`one`, causing the test for :func:`two` to fail.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-m doctest -v doctest_mutable_globals.py', ignore_error=True))
.. }}}
.. {{{end}}}

If you need to set global values for the tests, to parameterize them
for an environment for example, you can pass values to :func:`testmod`
and :func:`testfile` and have the context set up using data you
control.

.. seealso::

    `doctest <http://docs.python.org/library/doctest.html>`_
        The standard library documentation for this module.

    `The Mighty Dictionary <http://blip.tv/file/3332763>`__
        Presentation by Brandon Rhodes at PyCon 2010 about the
        internal operations of the :class:`dict`.

    :mod:`difflib`
        Python's sequence difference computation library, used to
        produce the ndiff output.

    `Sphinx <http://sphinx.pocoo.org/>`_
        As well as being the documentation processing tool for
        Python's standard library, Sphinx has been adopted by many
        third-party projects because it is easy to use and produces
        clean output in several digital and print formats.  Sphinx
        includes an extension for running doctests as is processes
        your documentation, so you know your examples are always
        accurate.

    `nose <http://somethingaboutorange.com/mrl/projects/nose/>`_
        Third-party test runner with :mod:`doctest` support.

    `py.test <http://codespeak.net/py/dist/test/>`_
        Third-party test runner with :mod:`doctest` support.

    `Manuel <http://packages.python.org/manuel/>`_
        Third-party documentation-based test runner with more advanced
        test case extraction and integration with Sphinx.
