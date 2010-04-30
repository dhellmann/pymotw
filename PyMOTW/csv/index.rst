==================================
csv -- Comma-separated value files
==================================

.. module:: csv
    :synopsis: Read and write comma separated value files.

:Purpose: Read and write comma separated value files.
:Python Version: 2.3 and later

The csv module is useful for working with data exported from
spreadsheets and databases into text files using a "comma-separated
value" format. There is no well-defined standard for comma-separated
value files, so the csv module uses *dialects* to support parsing
using different parameters. Along with a generic reader and writer,
the module includes a dialect for working with data exported from
Microsoft Excel.

Limitations
===========

The Python 2.5 version of csv does not support Unicode data. There are also
"issues with ASCII NUL characters". Using UTF-8 or printable ASCII is
recommended.

Reading
=======

Use ``reader()`` to create a an object for reading data from a csv
file.  The reader can be used as an iterator to process the rows of
the file in order. For example:

.. include:: csv_reader.py
    :literal:
    :start-after: #end_pymotw_header

The first argument to ``reader()`` is the source of text lines. In
this case, it is a file, but any iterable is accepted (:mod:`StringIO`
instances, lists, etc.).  Other optional arguments can be given to
control how the input data is parsed.

The example file ``testdata.csv`` was exported from NeoOffice_.

.. include:: testdata.csv
    :literal:

As it is read, each row of the input data is parsed and converted to a
list of strings.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'csv_reader.py testdata.csv'))
.. }}}
.. {{{end}}}

If you know that certain columns have specific types, you can convert
the strings to that type, but csv does not automatically convert the
input. It does handle line breaks embedded within strings in a row
(which is why a "row" is not always the same as a "line" of input from
the file).

.. include:: testlinebreak.csv
    :literal:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'csv_reader.py testlinebreak.csv'))
.. }}}
.. {{{end}}}

Writing
=======

When you have data to be imported into some other application, writing
CSV files is just as easy as reading them. Use ``writer()`` to create
an object for writing, then iterate over the rows, using
``writerow()`` to print them.

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

There are many parameters to control how the csv module parses or
writes data. Rather than passing each of these parameters to the
reader and writer separately, they are grouped together conveniently
into a "dialect" object. Dialect classes can be registered by name, so
that callers of the csv module do not need to know the parameter
settings in advance. The standard library includes two dialects:
``excel``, and ``excel-tabs``. The ``excel`` dialect is for working
with data in the default export format for Microsoft Excel, and also
works with OpenOffice or NeoOffice.

Suppose instead of using commas to delimit fields, the input file uses
``|``, like this:

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

For details on the dialect parameters and how they are used, refer to
`the standard library documentation for the csv module
<http://docs.python.org/library/csv.html#dialects-and-formatting-parameters>`_.

DictReader and DictWriter
=========================

In addition to working with sequences of data, the csv module includes
classes for working with rows as dictionaries. The DictReader and
DictWriter classes translate rows to dictionaries instead of
lists. Keys for the dictionary can be passed in, or inferred from the
first row in the input (when the row contains headers).

.. include:: csv_dictreader.py
    :literal:
    :start-after: #end_pymotw_header

The dictionary-based reader and writer are implemented as wrappers
around the sequence-based classes, and use the same methods and
arguments. The only difference in the reader API is that rows are
returned as dictionaries instead of lists or tuples.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'csv_dictreader.py testdata.csv'))
.. }}}
.. {{{end}}}

The DictWriter must be given a list of field names so it knows how to
order the columns in the output.

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

.. _NeoOffice: http://www.neooffice.org/
