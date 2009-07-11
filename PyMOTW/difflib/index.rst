================================================
difflib -- Compute differences between sequences
================================================

.. module:: difflib
    :synopsis: Library of tools for computing and working with differences between sequences, especially of lines in text files.

:Purpose: Library of tools for computing and working with differences between sequences, especially of lines in text files.
:Python Version: 2.1


The SequenceMatcher class compares any 2 sequences of values, as long as the
values are hashable. It uses a recursive algorithm to identify the longest
contiguous matching blocks from the sequences, eliminating "junk" values. The
Differ class works on sequences of text lines and produces human-readable
deltas, including differences within individual lines. The HtmlDiff class
produces similar results formatted as an HTML table.

Test Data
=========

The examples below will all use this common test data in the difflib_data
module:

.. include:: difflib_data.py
    :literal:
    :start-after: #end_pymotw_header

Differ Example
==============

Reproducing output similar to the diff command line tool is simple with the
Differ class:

.. include:: difflib_differ.py
    :literal:
    :start-after: #end_pymotw_header

The output includes the original input values from both lists, including
common values, and markup data to indicate what changes were made. Lines may
be prefixed with - to indicate that they were in the first sequence, but not
the second. Lines prefixed with + were in the second sequence, but not the
first. If a line has an incremental change between versions, an extra line
prefixed with ? is used to try to indicate where the change occurred within
the line. If a line has not changed, it is printed with an extra blank space
on the left column to let it line up with the other lines which may have other
markup.

The beginning of both text segments is the same.

::

     1:   Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Integer

The second line has been changed to include a comma in the modified text. Both
versions of the line are printed, with the extra information on line 4 showing
the column where the text was modified, including the fact that the ,
character was added.

::

     2: - eu lacus accumsan arcu fermentum euismod. Donec pulvinar porttitor
     3: + eu lacus accumsan arcu fermentum euismod. Donec pulvinar, porttitor
     4: ?                                                         +
     5: 

Lines 6-9 of the output shows where an extra space was removed.

::

     6: - tellus. Aliquam venenatis. Donec facilisis pharetra tortor.  In nec
     7: ?                                                             -
     8: 
     9: + tellus. Aliquam venenatis. Donec facilisis pharetra tortor. In nec

Next a more complex change was made, replacing several words in a phrase.

::

    10: - mauris eget magna consequat convallis. Nam sed sem vitae odio
    11: ?                                              - --
    12: 
    13: + mauris eget magna consequat convallis. Nam cras vitae mi vitae odio
    14: ?                                            +++ +++++   +
    15: 

The last sentence in the paragraph was changed significantly, so the
difference is represented by simply removing the old version and adding the
new (lines 20-23).

::

    16:   pellentesque interdum. Sed consequat viverra nisl. Suspendisse arcu
    17:   metus, blandit quis, rhoncus ac, pharetra eget, velit. Mauris
    18:   urna. Morbi nonummy molestie orci. Praesent nisi elit, fringilla ac,
    19:   suscipit non, tristique vel, mauris. Curabitur vel lorem id nisl porta
    20: - adipiscing. Suspendisse eu lectus. In nunc. Duis vulputate tristique
    21: - enim. Donec quis lectus a justo imperdiet tempus.
    22: + adipiscing. Duis vulputate tristique enim. Donec quis lectus a justo
    23: + imperdiet tempus. Suspendisse eu lectus. In nunc.

The ndiff() function produces essentially the same output. The processing is
specifically tailored to working with text data and eliminating "noise" in the
input.

.. include:: difflib_ndiff.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'difflib_ndiff.py'))
.. }}}
.. {{{end}}}

Other Diff Formats
==================

Where the Differ class shows all of the inputs, a unified diff only includes
modified lines and a bit of context. In version 2.3, a unified_diff() function
was added to produce this sort of output:

.. include:: difflib_unified.py
    :literal:
    :start-after: #end_pymotw_header

The output should look familiar to users of svn or other version control
tools:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'difflib_unified.py'))
.. }}}
.. {{{end}}}

Using context_diff() produces similar readable output:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'difflib_context.py'))
.. }}}
.. {{{end}}}

HTML Output
===========

HtmlDiff (new in Python 2.4) produces HTML output with the same information as
the Diff class. This example uses make_table(), but the make_file() method
produces a fully-formed HTML file as output.

.. include:: difflib_html.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'difflib_html.py'))
.. }}}
.. {{{end}}}


Junk Data
=========

All of the functions which produce diff sequences accept arguments to indicate
which lines should be ignored, and which characters within a line should be
ignored. This can be used to ignore markup or whitespace changes in two
versions of file, for example.

.. include:: difflib_junk.py
    :literal:
    :start-after: #end_pymotw_header

The default for Differ is to not ignore any
lines or characters explicitly, but to rely on the SequenceMatcher's ability
to detect noise. The default for ndiff is to ignore space and tab characters.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'difflib_junk.py'))
.. }}}
.. {{{end}}}


SequenceMatcher
===============

SequenceMatcher, which implements the comparison algorithm, can be used with
sequences of any type of object as long as the object is hashable. For
example, two lists of integers can be compared, and using get_opcodes() a set
of instructions for converting the original list into the newer can be
printed:

.. include:: difflib_seq.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'difflib_seq.py'))
.. }}}
.. {{{end}}}


You can use SequenceMatcher with your own classes, as well as built-in types.

.. seealso::

    `difflib <http://docs.python.org/library/difflib.html>`_
        The standard library documentation for this module.

    `Pattern Matching: The Gestalt Approach <http://www.ddj.com/documents/s=1103/ddj8807c/>`_
        Discussion of a similar algorithm by John W. Ratcliff and D. E. Metzener published in Dr. Dobb’s Journal in July, 1988.

    :ref:`article-text-processing`
