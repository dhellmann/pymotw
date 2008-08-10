==========
csv
==========
.. module:: csv
    :synopsis: Read and write comma separated value files.

:Module: csv
:Purpose: Read and write comma separated value files.
:Python Version: 2.3 and later

Description
===========

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

::

    import csv
    import sys

    f = open(sys.argv[1], 'rt')
    try:
        reader = csv.reader(f)
        for row in reader:
            print row
    finally:
        f.close()

The first argument to reader() is the source of text lines. In this case, it
is a file, but any iterable is accepted (StringIO instances, lists, etc.).
Other optional arguments can be given to control how the input data is parsed.

::

    The example file "testdata.csv" was exported from NeoOffice.

    $ cat testdata.csv 
    "Title 1","Title 2","Title 3"
    1,"a",08/18/07
    2,"b",08/19/07
    3,"c",08/20/07
    4,"d",08/21/07
    5,"e",08/22/07
    6,"f",08/23/07
    7,"g",08/24/07
    8,"h",08/25/07
    9,"i",08/26/07

As it is read, each row of the input data is converted to a list of strings.

::

    $ python csv_reader.py testdata.csv
    ['Title 1', 'Title 2', 'Title 3']
    ['1', 'a', '08/18/07']
    ['2', 'b', '08/19/07']
    ['3', 'c', '08/20/07']
    ['4', 'd', '08/21/07']
    ['5', 'e', '08/22/07']
    ['6', 'f', '08/23/07']
    ['7', 'g', '08/24/07']
    ['8', 'h', '08/25/07']
    ['9', 'i', '08/26/07']

If you know that certain columns have specific types, you can convert the
strings yourself, but csv does not automatically convert the input. It does
handle line breaks embedded within strings in a row (which is why a "row" is
not always the same as a "line" of input from the file).

::

    $ cat testlinebreak.csv 
    "Title 1","Title 2","Title 3"
    1,"first line
    second line",08/18/07

    $ python csv_reader.py testlinebreak.csv 
    ['Title 1', 'Title 2', 'Title 3']
    ['1', 'first line\nsecond line', '08/18/07']

Writing
=======

When you have data to be imported into some other application, writing CSV
files is just as easy as reading them. Use the writer() function to create a
writer object. For each row, use writerow() to print the row.

::

    import csv
    import sys

    f = open(sys.argv[1], 'wt')
    try:
        writer = csv.writer(f)
        writer.writerow( ('Title 1', 'Title 2', 'Title 3') )
        for i in range(10):
            writer.writerow( (i+1, chr(ord('a') + i), '08/%02d/07' % (i+1)) )
    finally:
        f.close()

The output does not look exactly like the exported data used in the reader
example:

::

    $ python csv_writer.py testout.csv 
    $ cat testout.csv 
    Title 1,Title 2,Title 3
    1,a,08/01/07
    2,b,08/02/07
    3,c,08/03/07
    4,d,08/04/07
    5,e,08/05/07
    6,f,08/06/07
    7,g,08/07/07
    8,h,08/08/07
    9,i,08/09/07
    10,j,08/10/07

The default quoting behavior is different for the writer, so the string column
is not quoted. That is easy to change by adding a quoting argument to quote
non-numeric values:

::

    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)

And now the strings are quoted:

::

    $ python csv_writer_quoted.py testout_quoted.csv 
    $ cat testout_quoted.csv 
    "Title 1","Title 2","Title 3"
    1,"a","08/01/07"
    2,"b","08/02/07"
    3,"c","08/03/07"
    4,"d","08/04/07"
    5,"e","08/05/07"
    6,"f","08/06/07"
    7,"g","08/07/07"
    8,"h","08/08/07"
    9,"i","08/09/07"
    10,"j","08/10/07"


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

There are many parameters to control how the csv module parses or writes data.
Rather than passing each of these parameters to the reader and writer
separately, they are grouped together conveniently into a "dialect" object.
Dialect classes can be registered by name, so that callers of the csv module
do not need to know the parameter settings in advance. The standard library
includes two dialects: excel, and excel-tabs. The "excel" dialect is for
working with data in the default export format for Microsoft Excel, and also
works with OpenOffice or NeoOffice. For details on the dialect parameters and
how they are used, refer to section 9.1.2 the the standard library
documentation for the csv module.

DictReader and DictWriter
=========================

In addition to working with sequences of data, the csv module includes classes
for working with rows as dictionaries. The DictReader and DictWriter classes
translate rows to dictionaries. Keys for the dictionary can be passed in, or
inferred from the first row in the input (when the row contains headers). 

::

    import csv
    import sys

    f = open(sys.argv[1], 'rt')
    try:
        reader = csv.DictReader(f)
        for row in reader:
            print row
    finally:
        f.close()


The dictionary-based reader and writer are implemented as wrappers around the
sequence-based classes, and use the same arguments and API. The only
difference is that rows are dictionaries instead of lists or tuples.

::

    $ python csv_dictreader.py testdata.csv 
    {'Title 1': '1', 'Title 3': '08/18/07', 'Title 2': 'a'}
    {'Title 1': '2', 'Title 3': '08/19/07', 'Title 2': 'b'}
    {'Title 1': '3', 'Title 3': '08/20/07', 'Title 2': 'c'}
    {'Title 1': '4', 'Title 3': '08/21/07', 'Title 2': 'd'}
    {'Title 1': '5', 'Title 3': '08/22/07', 'Title 2': 'e'}
    {'Title 1': '6', 'Title 3': '08/23/07', 'Title 2': 'f'}
    {'Title 1': '7', 'Title 3': '08/24/07', 'Title 2': 'g'}
    {'Title 1': '8', 'Title 3': '08/25/07', 'Title 2': 'h'}
    {'Title 1': '9', 'Title 3': '08/26/07', 'Title 2': 'i'}

The DictWriter must be given a list of field names so it knows how the columns
should be ordered in the output.

::

    import csv
    import sys

    f = open(sys.argv[1], 'wt')
    try:
        fieldnames = ('Title 1', 'Title 2', 'Title 3')
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        headers = {}
        for n in fieldnames:
            headers[n] = n
        writer.writerow(headers)
        for i in range(10):
            writer.writerow({ 'Title 1':i+1,
                              'Title 2':chr(ord('a') + i),
                              'Title 3':'08/%02d/07' % (i+1),
                              })
    finally:
        f.close()

::

    $ python csv_dictwriter.py testout.csv 
    $ cat testout.csv 
    Title 1,Title 2,Title 3
    1,a,08/01/07
    2,b,08/02/07
    3,c,08/03/07
    4,d,08/04/07
    5,e,08/05/07
    6,f,08/06/07
    7,g,08/07/07
    8,h,08/08/07
    9,i,08/09/07
    10,j,08/10/07


