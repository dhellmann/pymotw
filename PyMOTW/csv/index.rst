==================================
csv -- Comma-separated value files
==================================

.. module:: csv
    :synopsis: Read and write comma separated value files.

:Purpose: Read and write comma separated value files.
:Python Version: 2.3 and later

The csv module is very useful for working with data exported from spreadsheets
and databases into text files. There is no well-defined standard, so the csv
module uses "dialects" to support parsing using different parameters. Along
with a generic reader and writer, the module includes a dialect for working
with Microsoft Excel.

Limitations
===========

The Python 2.5 version of csv does not support Unicode data. There are also
"issues with ASCII NUL characters". Using UTF-8 or printable ASCII is
recommended.

Reading
=======

To read data from a csv file, use the reader() function to create a reader
object. The reader can be used as an iterator to process the rows of the file
in order. For example:

.. include:: csv_reader.py
    :literal:
    :start-after: #end_pymotw_header

The first argument to reader() is the source of text lines. In this case, it
is a file, but any iterable is accepted (StringIO instances, lists, etc.).
Other optional arguments can be given to control how the input data is parsed.

The example file "testdata.csv" was exported from NeoOffice.

.. include:: testdata.csv
    :literal:

As it is read, each row of the input data is converted to a list of strings.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'csv_reader.py testdata.csv'))
.. }}}
.. {{{end}}}

If you know that certain columns have specific types, you can convert the
strings yourself, but csv does not automatically convert the input. It does
handle line breaks embedded within strings in a row (which is why a "row" is
not always the same as a "line" of input from the file).

.. include:: testlinebreak.csv
    :literal:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'csv_reader.py testlinebreak.csv'))
.. }}}
.. {{{end}}}

Writing
=======

When you have data to be imported into some other application, writing CSV
files is just as easy as reading them. Use the writer() function to create a
writer object. For each row, use writerow() to print the row.

.. include:: csv_writer.py
    :literal:
    :start-after: #end_pymotw_header

The output does not look exactly like the exported data used in the reader
example:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'csv_writer.py testout.csv'))
.. }}}
.. {{{end}}}

The default quoting behavior is different for the writer, so the string column
is not quoted. That is easy to change by adding a quoting argument to quote
non-numeric values:

::

    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)

And now the strings are quoted:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'csv_writer_quoted.py testout_quoted.csv'))
.. }}}
.. {{{end}}}

Quoting
=======

There are four different quoting options, defined as constants in the csv
module.

QUOTE_ALL
  Quote everything, regardless of type.

QUOTE_MINIMAL
  Quote fields with special characters (anything that would confuse a parser
  configured with the same dialect and options). This is the default

QUOTE_NONNUMERIC
  Quote all fields that are not integers or floats. When used with the reader,
  input fields that are not quoted are converted to floats.

QUOTE_NONE
  Do not quote anything on output. When used with the reader, quote characters
  are included in the field values (normally, they are treated as delimiters and
  stripped).


Dialects
========

There are many parameters to control how the csv module parses or writes data. Rather than
passing each of these parameters to the reader and writer separately, they are grouped
together conveniently into a "dialect" object. Dialect classes can be registered by name, so
that callers of the csv module do not need to know the parameter settings in advance. The
standard library includes two dialects: ``excel``, and ``excel-tabs``. The ``excel`` dialect
is for working with data in the default export format for Microsoft Excel, and also works
with OpenOffice or NeoOffice.

Suppose instead of using commas to delimit fields, the input file uses ``|``, like this:

.. include:: testdata.pipes
    :literal:

A new dialect can be registered using the appropriate delimiter:

.. include:: csv_dialect.py
    :literal:
    :start-after: #end_pymotw_header

and the file can be read just as with the comma-delimited file:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'csv_dialect.py'))
.. }}}
.. {{{end}}}

For details on the dialect parameters and how they are used, refer to `the standard library documentation for the csv module <http://docs.python.org/library/csv.html#dialects-and-formatting-parameters>`_.

DictReader and DictWriter
=========================

In addition to working with sequences of data, the csv module includes classes
for working with rows as dictionaries. The DictReader and DictWriter classes
translate rows to dictionaries. Keys for the dictionary can be passed in, or
inferred from the first row in the input (when the row contains headers). 

.. include:: csv_dictreader.py
    :literal:
    :start-after: #end_pymotw_header

The dictionary-based reader and writer are implemented as wrappers around the
sequence-based classes, and use the same arguments and API. The only
difference is that rows are dictionaries instead of lists or tuples.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'csv_dictreader.py testdata.csv'))
.. }}}
.. {{{end}}}

The DictWriter must be given a list of field names so it knows how the columns
should be ordered in the output.

.. include:: csv_dictwriter.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'csv_dictwriter.py testout.csv'))
.. }}}
.. {{{end}}}

.. seealso::

    `csv <http://docs.python.org/library/csv.html>`_
        The standard library documentation for this module.

    :pep:`305`
        CSV File API

    :ref:`article-data-persistence`
