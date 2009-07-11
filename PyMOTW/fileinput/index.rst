================
fileinput
================
.. module:: fileinput
    :synopsis: Create command-line filter programs.


To start this series, let's take a look at the fileinput module, a very useful
module for creating command line programs for processing text files in a
filter-ish manner. For example, the m3utorss app I recently wrote for my
friend `Patrick <http://events.mediumloud.com/>`_ to convert some of his 
demo recordings into a podcastable format.

The inputs to the program are one or more m3u file listing the mp3 files to be
distributed. The output is a single blob of XML that looks like an RSS feed
(output is written to stdout, for simplicity). To process the input, I need to
iterate over the list of filenames and:

* Open each file.
* Read each line of the file.
* Figure out if the line refers to an mp3 file.
* If it does, extract the information from the mp3 file needed for the RSS feed.
* Print the output.

I could have written all of that file handling out by hand. It isn't that
complicated, and with some testing I'm sure I could even get the error
handling right. But with the fileinput module, I don't need to worry about
that. I just write something like:

.. include:: fileinput_example.py
    :literal:
    :start-after: #end_pymotw_header

The relevant bit in that snippet is the for loop. The fileinput.input()
function takes as argument a list of filenames to examine. If the list is
empty, the module reads data from standard input. The function returns an
iterator which returns individual lines from the text files being processed.
So, all I have to do is loop over each line, skipping blanks and comments, to
find the references to mp3 files.

In this example, I don't care what file or line number we are processing in
the input. For other tools (grep-like searching, for example) you might. The
fileinput module includes functions for accessing that information
(filename(), filelineno(), lineno(), etc.).

.. seealso::

    `fileinput <http://docs.python.org/library/fileinput.html>`_
        The standard library documentation for this module.

    `Patrick Bryant <http://events.mediumloud.com/>`_
        Atlanta-based singer/song-writer.

    :ref:`article-text-processing`
