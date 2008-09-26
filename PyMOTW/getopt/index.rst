=============
getopt
=============
.. module:: getopt
    :synopsis: Command line option parsing

:Module: getopt
:Purpose: Command line option parsing
:Python Version: 1.4

Description
===========

The getopt module is the old-school command line option parser which supports
the conventions established by the Unix function getopt(). It parses an
argument sequence, such as sys.argv and returns a sequence of (option,
argument) pairs and a sequence of non-option arguments.

Supported option syntax includes:

::

    -a
    -bval
    -b val
    --noarg
    --witharg=val
    --witharg val


Function Arguments
==================

The getopt function takes three arguments:

* The first argument is the sequence of arguments to be parsed. This usually
  comes from sys.argv[1:] (ignoring the program name in sys.arg[0]).

* The second argument is the option definition string for single character
  options. If one of the options requires an argument, its letter is followed
  by a colon. 

* The third argument, if used, should be a sequence of the long-style option
  names. Long style options can be more than a single character, such as
  --noarg or --witharg. The option names in the sequence should not include
  the -- prefix. If any long option requires an argument, its name should have
  a suffix of =.

Short and long form options can be combined in a single call.

Short Form Options
==================

If a program wants to take 2 options, -a, and -b with the b option requiring
an argument, the value should be "ab:".

::

    print getopt.getopt(['-a', '-bval', '-c', 'val'], 'ab:c:')

::

    $ python getopt_short.py 
    ([('-a', ''), ('-b', 'val'), ('-c', 'val')], [])


Long Form Options
=================

If a program wants to take 2 options, --noarg and --witharg the sequence
should be [ 'noarg', 'witharg=' ].

::

    print getopt.getopt([ '--noarg', '--witharg', 'val', '--witharg2=another' ],
                        '',
                        [ 'noarg', 'witharg=', 'witharg2=' ])

::

    $ python getopt_long.py 
    ([('--noarg', ''), ('--witharg', 'val'), ('--witharg2', 'another')], [])


Example
=======

Below is a more complete example program which takes 5 options: -o, -v,
--output, --verbose, and --version. The -o, --output, and --version options
require an argument.

::

    import getopt
    import sys

    version = '1.0'
    verbose = False
    output_filename = 'default.out'

    print 'ARGV      :', sys.argv[1:]

    options, remainder = getopt.getopt(sys.argv[1:], 'o:v', ['output=', 
                                                             'verbose',
                                                             'version=',
                                                             ])
    print 'OPTIONS   :', options

    for opt, arg in options:
        if opt in ('-o', '--output'):
            output_filename = arg
        elif opt in ('-v', '--verbose'):
            verbose = True
        elif opt == '--version':
            version = arg

    print 'VERSION   :', version
    print 'VERBOSE   :', verbose
    print 'OUTPUT    :', output_filename
    print 'REMAINING :', remainder


The program can be called in a variety of ways.

::

    $ python ./getopt_example.py
    ARGV      : []
    OPTIONS   : []
    VERSION   : 1.0
    VERBOSE   : False
    OUTPUT    : default.out
    REMAINING : []

A single letter option can be a separate from its argument:

::

    $ python ./getopt_example.py -o foo
    ARGV      : ['-o', 'foo']
    OPTIONS   : [('-o', 'foo')]
    VERSION   : 1.0
    VERBOSE   : False
    OUTPUT    : foo
    REMAINING : []

or combined:

::

    $ python ./getopt_example.py -ofoo
    ARGV      : ['-ofoo']
    OPTIONS   : [('-o', 'foo')]
    VERSION   : 1.0
    VERBOSE   : False
    OUTPUT    : foo
    REMAINING : []

A long form option can similarly be separate:

::

    $ python ./getopt_example.py --output foo    
    ARGV      : ['--output', 'foo']
    OPTIONS   : [('--output', 'foo')]
    VERSION   : 1.0
    VERBOSE   : False
    OUTPUT    : foo
    REMAINING : []

or combined, with =:

::

    $ python ./getopt_example.py --output=foo
    ARGV      : ['--output=foo']
    OPTIONS   : [('--output', 'foo')]
    VERSION   : 1.0
    VERBOSE   : False
    OUTPUT    : foo
    REMAINING : []


Abbreviating Long Form Options
==============================

The long form option does not have to be spelled out entirely, so long as a
unique prefix is provided:

::

    $ python ./getopt_example.py --o foo
    ARGV      : ['--o', 'foo']
    OPTIONS   : [('--output', 'foo')]
    VERSION   : 1.0
    VERBOSE   : False
    OUTPUT    : foo
    REMAINING : []

If a unique prefix is not provided, an exception is raised.

::

    $ python ./getopt_example.py --ver 2.0
    ARGV      : ['--ver', '2.0']
    Traceback (most recent call last):
      File "./getopt_example.py", line 43, in 
        'version=',
      File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/getopt.py", line 89, in getopt
        opts, args = do_longs(opts, args[0][2:], longopts, args[1:])
      File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/getopt.py", line 153, in do_longs
        has_arg, opt = long_has_args(opt, longopts)
      File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/getopt.py", line 180, in long_has_args
        raise GetoptError('option --%s not a unique prefix' % opt, opt)
    getopt.GetoptError: option --ver not a unique prefix

Option processing stops as soon as the first non-option argument is
encountered.

::

    $ python ./getopt_example.py -v not_an_option --output foo
    ARGV      : ['-v', 'not_an_option', '--output', 'foo']
    OPTIONS   : [('-v', '')]
    VERSION   : 1.0
    VERBOSE   : True
    OUTPUT    : default.out
    REMAINING : ['not_an_option', '--output', 'foo']


GNU-style Option Parsing
========================

New in Python 2.3, an additional function gnu_getopt() was added. It allows
option and non-option arguments to be mixed on the command line in any order.
After changing the call in the previous example, the difference becomes clear:

::

    $ python ./getopt_gnu.py -v not_an_option --output foo
    ARGV      : ['-v', 'not_an_option', '--output', 'foo']
    OPTIONS   : [('-v', ''), ('--output', 'foo')]
    VERSION   : 1.0
    VERBOSE   : True
    OUTPUT    : foo
    REMAINING : ['not_an_option']


Special Case: --
================

If getopt encounters -- in the input arguments, it stops processing the
remaining arguments as options.

::

    $ python ./getopt_example.py -v -- --output foo
    ARGV      : ['-v', '--', '--output', 'foo']
    OPTIONS   : [('-v', '')]
    VERSION   : 1.0
    VERBOSE   : True
    OUTPUT    : default.out
    REMAINING : ['--output', 'foo']

