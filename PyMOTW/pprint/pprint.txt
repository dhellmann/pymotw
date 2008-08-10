======
pprint
======
.. module:: pprint
    :synopsis: Pretty-print data structures

:Module: pprint
:Purpose: Pretty-print data structures
:Python Version: 1.4
:Abstract:

    The pprint module includes a "pretty printer" for producing aesthetically
    pleasing representations of your data structures.

Description
===========

The formatter used in the pprint module prints representations of data
structures in a format which can be parsed correctly by the interpreter, and
which are also easy for a human to read. The output is kept on a single line,
if possible, and indented correctly when split across multiple lines.

The examples here all depend on pprint_data.py, which contains::

    data = [ (i, { 'a':'A',
                   'b':'B',
                   'c':'C',
                   'd':'D',
                   'e':'E',
                   'f':'F',
                   'g':'G',
                   'h':'H',
                   })
             for i in xrange(3)
             ]

Printing
========

The simplest way to use the module is with the pprint() function. It formats
your object and writes it to the data stream passed as argument (or sys.stdout
by default).

::

    from pprint import pprint

    from pprint_data import data

    print 'PRINT:'
    print data
    print
    print 'PPRINT:'
    pprint(data)

::

    $ python pprint_pprint.py
    PRINT:
    [(0, {'a': 'A', 'c': 'C', 'b': 'B', 'e': 'E', 'd': 'D', 'g': 'G', 'f': 'F', 'h': 'H'}), (1, {'a': 'A', 'c': 'C', 'b': 'B', 'e': 'E', 'd': 'D', 'g': 'G', 'f': 'F', 'h': 'H'}), (2, {'a': 'A', 'c': 'C', 'b': 'B', 'e': 'E', 'd': 'D', 'g': 'G', 'f': 'F', 'h': 'H'})]

    PPRINT:
    [(0,
      {'a': 'A',
       'b': 'B',
       'c': 'C',
       'd': 'D',
       'e': 'E',
       'f': 'F',
       'g': 'G',
       'h': 'H'}),
     (1,
      {'a': 'A',
       'b': 'B',
       'c': 'C',
       'd': 'D',
       'e': 'E',
       'f': 'F',
       'g': 'G',
       'h': 'H'}),
     (2,
      {'a': 'A',
       'b': 'B',
       'c': 'C',
       'd': 'D',
       'e': 'E',
       'f': 'F',
       'g': 'G',
       'h': 'H'})]


Formatting
==========

If you need to format a data structure, but do not want to write it directly
to a stream (for logging purposes, for example) you can use pformat() to build
a string representation that can then be passed to another function.

::

    import logging
    from pprint import pformat
    from pprint_data import data

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        )

    logging.debug('Logging pformatted data')
    logging.debug(pformat(data))

::

    $ python pprint_pformat.py
    2007-10-21 18:10:32,881 DEBUG    Logging pformatted data
    2007-10-21 18:10:32,884 DEBUG    [(0,
      {'a': 'A',
       'b': 'B',
       'c': 'C',
       'd': 'D',
       'e': 'E',
       'f': 'F',
       'g': 'G',
       'h': 'H'}),
     (1,
      {'a': 'A',
       'b': 'B',
       'c': 'C',
       'd': 'D',
       'e': 'E',
       'f': 'F',
       'g': 'G',
       'h': 'H'}),
     (2,
      {'a': 'A',
       'b': 'B',
       'c': 'C',
       'd': 'D',
       'e': 'E',
       'f': 'F',
       'g': 'G',
       'h': 'H'})]


Arbitrary Classes
=================

The PrettyPrinter class used by pprint() can also work with your own classes,
if they define a __repr__ method.

::

    from pprint import pprint

    class node(object):
        def __init__(self, name, contents=[]):
            self.name = name
            self.contents = contents[:]
        def __repr__(self):
            return 'node(' + repr(self.name) + ', ' + repr(self.contents) + ')'

    trees = [ node('node-1'),
             node('node-2', [ node('node-2-1')]),
             node('node-3', [ node('node-3-1')]),
             ]
    pprint(trees)

::

     $ python pprint_arbitrary_object.py
    [node('node-1', []),
     node('node-2', [node('node-2-1', [])]),
     node('node-3', [node('node-3-1', [])])]


Recursion
=========

Recursive data structures are represented with a reference to the original
source of the data, with the form <Recursion on typename with id=number>. For
example::

    local_data = [ 'a', 'b', 1, 2 ]
    local_data.append(local_data)

    print 'id(local_data) =>', id(local_data)
    pprint(local_data)

::

    $ python pprint_recursion.py
    id(local_data) => 486936
    ['a', 'b', 1, 2, <Recursion on list with id=486936>]


Limiting Nested Output
======================

For very deep data structures, you may not want the output to include all of
the details. It might be impossible to format the data properly, the formatted
text might be too large to manage, or you may need all of it. In that case,
the depth argument can control how far down into the nested data structure the
pretty printer goes.

::

    from pprint import pprint

    from pprint_data import data

    pprint(data, depth=1)

::

     $ python pprint_depth.py 
    [(0, {...}), (1, {...}), (2, {...})]


Controlling Output Width
========================

The default output width for the formatted text is 80 columns. To adjust that
width, use the width argument to pprint().

::

    from pprint import pprint

    from pprint_data import data

    for d in data:
        for c in 'defgh':
            del d[1][c]

    for width in [ 80, 20, 5 ]:
        print 'WIDTH =', width
        pprint(data, width=width)
        print


Notice that when the width is too low to accommodate the formatted data
structure, the lines are not truncated or wrapped if that would introduce
invalid syntax.

::

    $ python pprint_width.py 
    WIDTH = 80
    [(0, {'a': 'A', 'b': 'B', 'c': 'C'}),
     (1, {'a': 'A', 'b': 'B', 'c': 'C'}),
     (2, {'a': 'A', 'b': 'B', 'c': 'C'})]

    WIDTH = 20
    [(0,
      {'a': 'A',
       'b': 'B',
       'c': 'C'}),
     (1,
      {'a': 'A',
       'b': 'B',
       'c': 'C'}),
     (2,
      {'a': 'A',
       'b': 'B',
       'c': 'C'})]

    WIDTH = 5
    [(0,
      {'a': 'A',
       'b': 'B',
       'c': 'C'}),
     (1,
      {'a': 'A',
       'b': 'B',
       'c': 'C'}),
     (2,
      {'a': 'A',
       'b': 'B',
       'c': 'C'})]
