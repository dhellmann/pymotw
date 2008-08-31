===============
optparse
===============
.. module:: optparse
    :synopsis: Command line option parser to replace getopt.

:Module: optparse
:Purpose: Command line option parser to replace getopt.
:Python Version: 2.3

Description
===========

The optparse module is a modern alternative for command line option parsing
that offers several features not available in getopt, including type
conversion, option callbacks, and automatic help generation. There are many
more features for to optparse than can be covered here, but hopefully this
introduction will get you started if you are writing a command line program
soon.

Creating an OptionParser
========================

There are two phases to parsing options with optparse. First, the OptionParser
instance is constructed and configured with the expected options. Then a
sequence of options is fed in and processed. 

::

    import optparse
    parser = optparse.OptionParser()

Usually, once the parser has been created, each option is added to the parser
explicitly, with information about what to do when the option is encountered
on the command line. It is also possible to pass a list of options to the
OptionParser constructor, but that form does not seem to be used as
frequently.

Defining Options
================

Options can be added one at a time using the add_option() method. Any un-named
string arguments at the beginning of the argument list are treated as option
names. To create aliases for an option, for example to have a short and long
form of the same option, simply pass both names.

Unlike getopt, which only parses the options, optparse is a full option
processing library. Options can be handled with different actions, specified
by the action argument to add_option(). Supported actions include storing the
argument (singly, or as part of a list), storing a constant value when the
option is encountered (including special handling for true/false values for
boolean switches), counting the number of times an option is seen, and calling
a callback. 

The default action is to store the argument to the option. In this case, if a
type is provided, the argument value is converted to that type before it is
stored. If the dest argument is provided, the option value is saved to an
attribute of that name on the options object returned when the command line
arguments are parsed.

Parsing a Command Line
======================

Once all of the options are defined, the command line is parsed by passing a
sequence of argument strings to parse_args(). By default, the arguments are
taken from sys.argv[1:], but you can also pass your own list. The options are
processed using the GNU/POSIX syntax, so option and argument values can be
mixed in the sequence.

The return value from parse_args() is a two-part tuple containing an
optparse.Values instance and the list of arguments to the command that were
not interpreted as options. The Values instance holds the option values as
attributes, so if your option dest is "myoption", you access the value as:
options.myoption.

Simple Examples
===============

Here is a simple example with 3 different options: a boolean option (-a), a
simple string option (-b), and an integer option (-c).

::

    import optparse
    parser = optparse.OptionParser()
    parser.add_option('-a', action="store_true", default=False)
    parser.add_option('-b', action="store", dest="b")
    parser.add_option('-c', action="store", dest="c", type="int")
    print parser.parse_args(['-a', '-bval', '-c', '3'])

The options on the command line are parsed with the same rules that
getopt.gnu_getopt() uses, so there are two ways to pass values to single
character options. The example above uses both forms, -bval and -c val.

::

    $ python optparse_short.py 
    (<Values at 0xe29b8: {'a': True, 'c': 3, 'b': 'val'}>, [])

Notice that the type of the value associated with 'c' in the output is an
integer, since the OptionParser was told to convert the argument before
storing it.

Unlike with getopt, "long" option names are not handled any differently by
optparse:

::

    parser = optparse.OptionParser()
    parser.add_option('--noarg', action="store_true", default=False)
    parser.add_option('--witharg', action="store", dest="witharg")
    parser.add_option('--witharg2', action="store", dest="witharg2", type="int")
    print parser.parse_args([ '--noarg', '--witharg', 'val', '--witharg2=3' ])

And the results are similar:

::

    $ python optparse_long.py
    (<Values at 0xd3ad0: {'noarg': True, 'witharg': 'val', 'witharg2': 3}>, [])

Comparing with getopt
=====================

Here is an implementation of the same example program used in the discussion
of getopt:

::

    import optparse
    import sys
    print 'ARGV      :', sys.argv[1:]
    parser = optparse.OptionParser()
    parser.add_option('-o', '--output', 
                      dest="output_filename", 
                      default="default.out",
                      )
    parser.add_option('-v', '--verbose',
                      dest="verbose",
                      default=False,
                      action="store_true",
                      )
    parser.add_option('--version',
                      dest="version",
                      default=1.0,
                      type="float",
                      )
    options, remainder = parser.parse_args()
    print 'VERSION   :', options.version
    print 'VERBOSE   :', options.verbose
    print 'OUTPUT    :', options.output_filename
    print 'REMAINING :', remainder

Notice how the options -o and --output are aliased by being added at the same
time. Either option can be used on the command line:

::

    $ python optparse_getoptcomparison.py -o output.txtARGV      : ['-o', 'output.txt']
    VERSION   : 1.0
    VERBOSE   : False
    OUTPUT    : output.txt
    REMAINING : []
    $ python optparse_getoptcomparison.py --output output.txt
    ARGV      : ['--output', 'output.txt']
    VERSION   : 1.0
    VERBOSE   : False
    OUTPUT    : output.txt
    REMAINING : []

And, any unique prefix of the long option can also be used:

::

    $ python optparse_getoptcomparison.py --out output.txt
    ARGV      : ['--out', 'output.txt']
    VERSION   : 1.0
    VERBOSE   : False
    OUTPUT    : output.txt
    REMAINING : []


Option Callbacks
================

Beside saving the arguments for options directly, it is possible to define
callback functions to be invoked when the option is encountered on the command
line. Callbacks for options take 4 arguments: the optparse.Option instance
causing the callback, the option string from the command line, any argument
value associated with the option, and the optparse.OptionParser instance doing
the parsing work.

::

    import optparse
    def flag_callback(option, opt_str, value, parser):
        print 'flag_callback:'
        print '\toption:', repr(option)
        print '\topt_str:', opt_str
        print '\tvalue:', value
        print '\tparser:', parser
        return
    def with_callback(option, opt_str, value, parser):
        print 'with_callback:'
        print '\toption:', repr(option)
        print '\topt_str:', opt_str
        print '\tvalue:', value
        print '\tparser:', parser
        return
    parser = optparse.OptionParser()
    parser.add_option('--flag', action="callback", callback=flag_callback)
    parser.add_option('--with', 
                      action="callback",
                      callback=with_callback,
                      type="string",
                      help="Include optional feature")
    parser.parse_args(['--with', 'foo', '--flag'])

In this example, the --with option is configured to take a string argument
(other types are support as well, of course).

::

    $ python optparse_callback.py
    with_callback:
            option: <Option at 0x78b98: --with>
            opt_str: --with
            value: foo
            parser: <optparse.OptionParser instance at 0x78b48>
    flag_callback:
            option: <Option at 0x7c620: --flag>
            opt_str: --flag
            value: None
            parser: <optparse.OptionParser instance at 0x78b48>


Help Messages
=============

The OptionParser automatically includes a help option to all option sets, so
the user can pass --help on the command line to see instructions for running
the program. The help message includes all of the options an indication of
whether or not they take an argument. It is also possible to pass help text to
add_option() to give a more verbose description of an option.

::

    parser = optparse.OptionParser()
    parser.add_option('--no-foo', action="store_true", 
                      default=False, 
                      dest="foo",
                      help="Turn off foo",
                      )
    parser.add_option('--with', action="store", help="Include optional feature")
    parser.parse_args()

The options are listed in alphabetical order, with aliases included on the
same line. When the option takes an argument, the dest value is included as an
argument name in the help output. The help text is printed in the right
column.

::

    $ python optparse_help.py --help
    Usage: optparse_help.py [options]

    Options:
      -h, --help   show this help message and exit
      --no-foo     Turn off foo
      --with=WITH  Include optional feature

Callbacks can be configured to take multiple arguments using the nargs option.

::

    def with_callback(option, opt_str, value, parser):
        print 'with_callback:'
        print '\toption:', repr(option)
        print '\topt_str:', opt_str
        print '\tvalue:', value
        print '\tparser:', parser
        return
    parser = optparse.OptionParser()
    parser.add_option('--with', 
                      action="callback",
                      callback=with_callback,
                      type="string",
                      nargs=2,
                      help="Include optional feature")
    parser.parse_args(['--with', 'foo', 'bar'])

In this case, the arguments are passed to the callback function as a tuple via
the value argument.

::

    $ python optparse_callback_nargs.py 
    with_callback:
            option: <Option at 0x7c4e0: --with>
            opt_str: --with
            value: ('foo', 'bar')
            parser: <optparse.OptionParser instance at 0x78a08>

