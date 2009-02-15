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

::

	$ python difflib_ndiff.py
	  Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Integer
	- eu lacus accumsan arcu fermentum euismod. Donec pulvinar porttitor
	+ eu lacus accumsan arcu fermentum euismod. Donec pulvinar, porttitor
	?                                                         +
	
	- tellus. Aliquam venenatis. Donec facilisis pharetra tortor.  In nec
	?                                                             -
	
	+ tellus. Aliquam venenatis. Donec facilisis pharetra tortor. In nec
	- mauris eget magna consequat convallis. Nam sed sem vitae odio
	?                                             ------
	
	+ mauris eget magna consequat convallis. Nam cras vitae mi vitae odio
	?                                            +++        +++++++++
	
	  pellentesque interdum. Sed consequat viverra nisl. Suspendisse arcu
	  metus, blandit quis, rhoncus ac, pharetra eget, velit. Mauris
	  urna. Morbi nonummy molestie orci. Praesent nisi elit, fringilla ac,
	  suscipit non, tristique vel, mauris. Curabitur vel lorem id nisl porta
	- adipiscing. Suspendisse eu lectus. In nunc. Duis vulputate tristique
	- enim. Donec quis lectus a justo imperdiet tempus.
	+ adipiscing. Duis vulputate tristique enim. Donec quis lectus a justo
	+ imperdiet tempus. Suspendisse eu lectus. In nunc. 

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

::

	$ python difflib_unified.py
	---  
	+++  
	@@ -1,10 +1,10 @@
	 Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Integer
	-eu lacus accumsan arcu fermentum euismod. Donec pulvinar porttitor
	-tellus. Aliquam venenatis. Donec facilisis pharetra tortor.  In nec
	-mauris eget magna consequat convallis. Nam sed sem vitae odio
	+eu lacus accumsan arcu fermentum euismod. Donec pulvinar, porttitor
	+tellus. Aliquam venenatis. Donec facilisis pharetra tortor. In nec
	+mauris eget magna consequat convallis. Nam cras vitae mi vitae odio
	 pellentesque interdum. Sed consequat viverra nisl. Suspendisse arcu
	 metus, blandit quis, rhoncus ac, pharetra eget, velit. Mauris
	 urna. Morbi nonummy molestie orci. Praesent nisi elit, fringilla ac,
	 suscipit non, tristique vel, mauris. Curabitur vel lorem id nisl porta
	-adipiscing. Suspendisse eu lectus. In nunc. Duis vulputate tristique
	-enim. Donec quis lectus a justo imperdiet tempus.
	+adipiscing. Duis vulputate tristique enim. Donec quis lectus a justo
	+imperdiet tempus. Suspendisse eu lectus. In nunc. 

.. {{{end}}}

Using context_diff() produces similar readable output:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'difflib_context.py'))
.. }}}

::

	$ python difflib_context.py
	***  
	---  
	***************
	*** 1,10 ****
	  Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Integer
	! eu lacus accumsan arcu fermentum euismod. Donec pulvinar porttitor
	! tellus. Aliquam venenatis. Donec facilisis pharetra tortor.  In nec
	! mauris eget magna consequat convallis. Nam sed sem vitae odio
	  pellentesque interdum. Sed consequat viverra nisl. Suspendisse arcu
	  metus, blandit quis, rhoncus ac, pharetra eget, velit. Mauris
	  urna. Morbi nonummy molestie orci. Praesent nisi elit, fringilla ac,
	  suscipit non, tristique vel, mauris. Curabitur vel lorem id nisl porta
	! adipiscing. Suspendisse eu lectus. In nunc. Duis vulputate tristique
	! enim. Donec quis lectus a justo imperdiet tempus.
	--- 1,10 ----
	  Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Integer
	! eu lacus accumsan arcu fermentum euismod. Donec pulvinar, porttitor
	! tellus. Aliquam venenatis. Donec facilisis pharetra tortor. In nec
	! mauris eget magna consequat convallis. Nam cras vitae mi vitae odio
	  pellentesque interdum. Sed consequat viverra nisl. Suspendisse arcu
	  metus, blandit quis, rhoncus ac, pharetra eget, velit. Mauris
	  urna. Morbi nonummy molestie orci. Praesent nisi elit, fringilla ac,
	  suscipit non, tristique vel, mauris. Curabitur vel lorem id nisl porta
	! adipiscing. Duis vulputate tristique enim. Donec quis lectus a justo
	! imperdiet tempus. Suspendisse eu lectus. In nunc. 

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

::

	$ python difflib_html.py
	
	    <table class="diff" id="difflib_chg_to0__top"
	           cellspacing="0" cellpadding="0" rules="groups" >
	        <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup>
	        <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup>
	        
	        <tbody>
	            <tr><td class="diff_next" id="difflib_chg_to0__0"><a href="#difflib_chg_to0__0">f</a></td><td class="diff_header" id="from0_1">1</td><td nowrap="nowrap">Lorem&nbsp;ipsum&nbsp;dolor&nbsp;sit&nbsp;amet,&nbsp;consectetuer&nbsp;adipiscing&nbsp;elit.&nbsp;Integer</td><td class="diff_next"><a href="#difflib_chg_to0__0">f</a></td><td class="diff_header" id="to0_1">1</td><td nowrap="nowrap">Lorem&nbsp;ipsum&nbsp;dolor&nbsp;sit&nbsp;amet,&nbsp;consectetuer&nbsp;adipiscing&nbsp;elit.&nbsp;Integer</td></tr>
	            <tr><td class="diff_next"><a href="#difflib_chg_to0__1">n</a></td><td class="diff_header" id="from0_2">2</td><td nowrap="nowrap">eu&nbsp;lacus&nbsp;accumsan&nbsp;arcu&nbsp;fermentum&nbsp;euismod.&nbsp;Donec&nbsp;pulvinar&nbsp;porttitor</td><td class="diff_next"><a href="#difflib_chg_to0__1">n</a></td><td class="diff_header" id="to0_2">2</td><td nowrap="nowrap">eu&nbsp;lacus&nbsp;accumsan&nbsp;arcu&nbsp;fermentum&nbsp;euismod.&nbsp;Donec&nbsp;pulvinar<span class="diff_add">,</span>&nbsp;porttitor</td></tr>
	            <tr><td class="diff_next"></td><td class="diff_header" id="from0_3">3</td><td nowrap="nowrap">tellus.&nbsp;Aliquam&nbsp;venenatis.&nbsp;Donec&nbsp;facilisis&nbsp;pharetra&nbsp;tortor.&nbsp;<span class="diff_sub">&nbsp;</span>In&nbsp;nec</td><td class="diff_next"></td><td class="diff_header" id="to0_3">3</td><td nowrap="nowrap">tellus.&nbsp;Aliquam&nbsp;venenatis.&nbsp;Donec&nbsp;facilisis&nbsp;pharetra&nbsp;tortor.&nbsp;In&nbsp;nec</td></tr>
	            <tr><td class="diff_next" id="difflib_chg_to0__1"></td><td class="diff_header" id="from0_4">4</td><td nowrap="nowrap">mauris&nbsp;eget&nbsp;magna&nbsp;consequat&nbsp;convallis.&nbsp;Nam&nbsp;s<span class="diff_sub">ed&nbsp;sem</span>&nbsp;vitae&nbsp;odio</td><td class="diff_next"></td><td class="diff_header" id="to0_4">4</td><td nowrap="nowrap">mauris&nbsp;eget&nbsp;magna&nbsp;consequat&nbsp;convallis.&nbsp;Nam&nbsp;<span class="diff_add">cra</span>s&nbsp;vitae&nbsp;<span class="diff_add">mi&nbsp;vitae&nbsp;</span>odio</td></tr>
	            <tr><td class="diff_next"></td><td class="diff_header" id="from0_5">5</td><td nowrap="nowrap">pellentesque&nbsp;interdum.&nbsp;Sed&nbsp;consequat&nbsp;viverra&nbsp;nisl.&nbsp;Suspendisse&nbsp;arcu</td><td class="diff_next"></td><td class="diff_header" id="to0_5">5</td><td nowrap="nowrap">pellentesque&nbsp;interdum.&nbsp;Sed&nbsp;consequat&nbsp;viverra&nbsp;nisl.&nbsp;Suspendisse&nbsp;arcu</td></tr>
	            <tr><td class="diff_next"></td><td class="diff_header" id="from0_6">6</td><td nowrap="nowrap">metus,&nbsp;blandit&nbsp;quis,&nbsp;rhoncus&nbsp;ac,&nbsp;pharetra&nbsp;eget,&nbsp;velit.&nbsp;Mauris</td><td class="diff_next"></td><td class="diff_header" id="to0_6">6</td><td nowrap="nowrap">metus,&nbsp;blandit&nbsp;quis,&nbsp;rhoncus&nbsp;ac,&nbsp;pharetra&nbsp;eget,&nbsp;velit.&nbsp;Mauris</td></tr>
	            <tr><td class="diff_next"></td><td class="diff_header" id="from0_7">7</td><td nowrap="nowrap">urna.&nbsp;Morbi&nbsp;nonummy&nbsp;molestie&nbsp;orci.&nbsp;Praesent&nbsp;nisi&nbsp;elit,&nbsp;fringilla&nbsp;ac,</td><td class="diff_next"></td><td class="diff_header" id="to0_7">7</td><td nowrap="nowrap">urna.&nbsp;Morbi&nbsp;nonummy&nbsp;molestie&nbsp;orci.&nbsp;Praesent&nbsp;nisi&nbsp;elit,&nbsp;fringilla&nbsp;ac,</td></tr>
	            <tr><td class="diff_next"></td><td class="diff_header" id="from0_8">8</td><td nowrap="nowrap">suscipit&nbsp;non,&nbsp;tristique&nbsp;vel,&nbsp;mauris.&nbsp;Curabitur&nbsp;vel&nbsp;lorem&nbsp;id&nbsp;nisl&nbsp;porta</td><td class="diff_next"></td><td class="diff_header" id="to0_8">8</td><td nowrap="nowrap">suscipit&nbsp;non,&nbsp;tristique&nbsp;vel,&nbsp;mauris.&nbsp;Curabitur&nbsp;vel&nbsp;lorem&nbsp;id&nbsp;nisl&nbsp;porta</td></tr>
	            <tr><td class="diff_next"><a href="#difflib_chg_to0__top">t</a></td><td class="diff_header" id="from0_9">9</td><td nowrap="nowrap"><span class="diff_sub">adipiscing.&nbsp;Suspendisse&nbsp;eu&nbsp;lectus.&nbsp;In&nbsp;nunc.&nbsp;Duis&nbsp;vulputate&nbsp;tristique</span></td><td class="diff_next"><a href="#difflib_chg_to0__top">t</a></td><td class="diff_header" id="to0_9">9</td><td nowrap="nowrap"><span class="diff_add">adipiscing.&nbsp;Duis&nbsp;vulputate&nbsp;tristique&nbsp;enim.&nbsp;Donec&nbsp;quis&nbsp;lectus&nbsp;a&nbsp;justo</span></td></tr>
	            <tr><td class="diff_next"></td><td class="diff_header" id="from0_10">10</td><td nowrap="nowrap"><span class="diff_sub">enim.&nbsp;Donec&nbsp;quis&nbsp;lectus&nbsp;a&nbsp;justo&nbsp;imperdiet&nbsp;tempus.</span></td><td class="diff_next"></td><td class="diff_header" id="to0_10">10</td><td nowrap="nowrap"><span class="diff_add">imperdiet&nbsp;tempus.&nbsp;Suspendisse&nbsp;eu&nbsp;lectus.&nbsp;In&nbsp;nunc.&nbsp;</span></td></tr>
	        </tbody>
	    </table>

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

::

	$ python difflib_junk.py
	A = " abcd"
	B = "abcd abcd"
	isjunk=None     : (0, 4, 5) " abcd" " abcd"
	isjunk=(x==" ") : (1, 0, 4) "abcd" "abcd"

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

::

	$ python difflib_seq.py
	 delete s1[0:1] ([1]) s2[0:0] ([])
	  equal s1[1:4] ([2, 3, 5]) s2[0:3] ([2, 3, 5])
	 insert s1[4:4] ([]) s2[3:4] ([4])
	  equal s1[4:5] ([6]) s2[4:5] ([6])
	replace s1[5:6] ([4]) s2[5:6] ([1])

.. {{{end}}}


You can use SequenceMatcher with your own classes, as well as built-in types.

.. seealso::

    `difflib <http://docs.python.org/library/difflib.html>`_
        The standard library documentation for this module.

    `Pattern Matching: The Gestalt Approach <http://www.ddj.com/documents/s=1103/ddj8807c/>`_
        Discussion of a similar algorithm by John W. Ratcliff and D. E. Metzener published in Dr. Dobb’s Journal in July, 1988.
