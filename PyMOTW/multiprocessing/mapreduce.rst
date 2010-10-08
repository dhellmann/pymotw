###########################################
Implementing MapReduce with multiprocessing
###########################################

The :class:`Pool` class can be used to create a simple single-server
MapReduce implementation.  Although it does not give the full benefits
of distributed processing, it does illustrate how easy it is to break
some problems down into distributable units of work.

SimpleMapReduce
===============

In a MapReduce-based system, input data is broken down into chunks for
processing by different worker instances.  Each chunk of input data is
*mapped* to an intermediate state using a simple transformation.  The
intermediate data is then collected together and partitioned based on
a key value so that all of the related values are together.  Finally,
the partitioned data is *reduced* to a result set.

.. include:: multiprocessing_mapreduce.py
    :literal:
    :start-after: #end_pymotw_header

Counting Words in Files
=======================

The following example script uses SimpleMapReduce to counts the
"words" in the reStructuredText source for this article, ignoring some
of the markup.

.. include:: multiprocessing_wordcount.py
    :literal:
    :start-after: #end_pymotw_header

The :func:`file_to_words` function converts each input file to a
sequence of tuples containing the word and the number 1 (representing
a single occurrence) .The data is partitioned by :func:`partition`
using the word as the key, so the partitioned data consists of a key
and a sequence of 1 values representing each occurrence of the word.
The partioned data is converted to a set of suples containing a word
and the count for that word by :func:`count_words` during the
reduction phase.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'multiprocessing_wordcount.py'))
.. }}}
.. {{{end}}}

.. seealso::

    `MapReduce - Wikipedia <http://en.wikipedia.org/wiki/MapReduce>`_
        Overview of MapReduce on Wikipedia.
    
    `MapReduce: Simplified Data Processing on Large Clusters <http://labs.google.com/papers/mapreduce.html>`_
        Google Labs presentation and paper on MapReduce.

    :mod:`operator`
        Operator tools such as ``itemgetter()``.

    

*Special thanks to Jesse Noller for helping review this information.*
