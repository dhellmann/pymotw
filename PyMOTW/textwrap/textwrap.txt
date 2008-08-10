========
textwrap
========
.. module:: textwrap
    :synopsis: Formatting text by adjusting where line breaks occur in a paragraph.

:Module: textwrap
:Purpose: Formatting text by adjusting where line breaks occur in a paragraph.
:Python Version: 2.5

Description
===========

The textwrap module can be used to format text for output in situations where
pretty-printing is desired. It offers programmatic functionality similar to
the paragraph wrapping or filling features found in many text editors.

Example
=======

::

    import textwrap

    # Provide some sample text
    sample_text = '''

     The textwrap module can be used to format text for output in situations
     where pretty-printing is desired.  It offers programmatic functionality similar
     to the paragraph wrapping or filling features found in many text editors.
     '''

The fill() convenience function takes text as input and produces formatted
text as output. Let's see what it does with the sample_text provided.

::

    print 'No dedent:\n'
    print textwrap.fill(sample_text)

The results are something less than what we want:

::

    No dedent:

            The textwrap module can be used to format text for output in
    situations         where pretty-printing is desired.  It offers
    programmatic functionality similar         to the paragraph wrapping
    or filling features found in many text editors.


Notice the embedded tabs and extra spaces mixed into the middle of the output.
It looks pretty rough. Of course, we can do better. We want to start by
removing any common whitespace prefix from all of the lines in the sample
text. This allows us to use docstrings or embedded multi-line strings straight
from our Python code while removing the formatting of the code itself. The
sample string has an artificial indent level introduced for illustrating this
feature.

::

    # Remove common whitespace prefix from the lines in the sample text
    dedented_text = textwrap.dedent(sample_text).strip()
    print 'Dedented:\n'
    print dedented_text


The results are starting to look better:

::

    Dedented:

    The textwrap module can be used to format text for output in situations
    where pretty-printing is desired.  It offers programmatic functionality similar
    to the paragraph wrapping or filling features found in many text editors.

Since "dedent" is the opposite of "indent", the result is a block of text with
the common initial whitespace from each line removed. If one line is already
indented more than another, some of the whitespace will not be removed.

::

     One tab.
     Two tabs.
    One tab.

becomes

::

    One tab.
    Two tabs.
    One tab.

Next, let's see what happens if we take the dedented text and pass it through
fill() with a few different width values.

::

    # Format the output with a few different max line width values
    for width in [ 20, 60, 80 ]:
        print
        print '%d Columns:\n' % width
        print textwrap.fill(dedented_text, width=width)


This gives several sets of output in the specified widths:

20 Columns::

    The textwrap module
    can be used to
    format text for
    output in situations
    where pretty-
    printing is desired.
    It offers
    programmatic
    functionality
    similar to the
    paragraph wrapping
    or filling features
    found in many text
    editors.

60 Columns::

    The textwrap module can be used to format text for output in
    situations where pretty-printing is desired.  It offers
    programmatic functionality similar to the paragraph wrapping
    or filling features found in many text editors.

80 Columns::

    The textwrap module can be used to format text for output in situations where
    pretty-printing is desired.  It offers programmatic functionality similar to the
    paragraph wrapping or filling features found in many text editors.

Besides the width of the output, you can control the indent of the first line
independently of subsequent lines. 

::

    # Demonstrate how to produce a hanging indent
    print '\nHanging indent:\n'
    print textwrap.fill(dedented_text, initial_indent='', subsequent_indent='    ')

This makes it relatively easy to produce a hanging indent, where the first
line is indented less than the other lines.

::

    Hanging indent:

    The textwrap module can be used to format text for output in
       situations where pretty-printing is desired.  It offers
       programmatic functionality similar to the paragraph wrapping or
       filling features found in many text editors.

The indent values can include non-whitespace characters, too, so the hanging
indent can be prefixed with * to produce bullet points, etc. That came in
handy when I converted my old zwiki content so I could import it into trac. I
used the StructuredText package from Zope to parse the zwiki data, then
created a formatter to produce trac's wiki markup as output. Using textwrap, I
was able to format the output pages so almost no manual tweaking was needed
after the conversion.


