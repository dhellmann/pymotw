=========================================================
optparse -- Command line option parser to replace getopt.
=========================================================

.. module:: optparse
    :synopsis: Command line option parser to replace getopt.

:Purpose: Command line option parser to replace getopt.
:Python Version: 2.3

The optparse module is a modern alternative for command line option parsing
that offers several features not available in :mod:`getopt`, including type
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

Options can be added one at a time using the ``add_option()`` method. Any un-named
string arguments at the beginning of the argument list are treated as option
names. To create aliases for an option, for example to have a short and long
form of the same option, simply pass both names.

Unlike :mod:`getopt`, which only parses the options, optparse is a full option
processing library. Options can be handled with different actions, specified
by the action argument to ``add_option()``. Supported actions include storing the
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
sequence of argument strings to ``parse_args()``. By default, the arguments are
taken from ``sys.argv[1:]``, but you can also pass your own list. The options are
processed using the GNU/POSIX syntax, so option and argument values can be
mixed in the sequence.

The return value from ``parse_args()`` is a two-part tuple containing an
optparse.Values instance and the list of arguments to the command that were
not interpreted as options. The Values instance holds the option values as
attributes, so if your option dest is "myoption", you access the value as:
``options.myoption``.

Simple Examples
===============

Here is a simple example with 3 different options: a boolean option (``-a``), a
simple string option (``-b``), and an integer option (``-c``).

.. include:: optparse_short.py
    :literal:
    :start-after: #end_pymotw_header


The options on the command line are parsed with the same rules that
``getopt.gnu_getopt()`` uses, so there are two ways to pass values to single
character options. The example above uses both forms, ``-bval`` and ``-c val``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_short.py'))
.. }}}
.. {{{end}}}

Notice that the type of the value associated with 'c' in the output is an
integer, since the OptionParser was told to convert the argument before
storing it.

Unlike with getopt, "long" option names are not handled any differently by
optparse:

.. include:: optparse_long.py
    :literal:
    :start-after: #end_pymotw_header

And the results are similar:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_long.py'))
.. }}}
.. {{{end}}}

Comparing with getopt
=====================

Here is an implementation of the same example program used in the PyMOTW article
about :mod:`getopt`:

.. include:: optparse_getoptcomparison.py
    :literal:
    :start-after: #end_pymotw_header

Notice how the options ``-o`` and ``--output`` are aliased by being added at the same
time. Either option can be used on the command line:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_getoptcomparison.py -o output.txt'))
.. cog.out(run_script(cog.inFile, 'optparse_getoptcomparison.py --output output.txt'))
.. }}}
.. {{{end}}}


And, any unique prefix of the long option can also be used:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_getoptcomparison.py --out output.txt'))
.. }}}
.. {{{end}}}


Option Callbacks
================

Beside saving the arguments for options directly, it is possible to define
callback functions to be invoked when the option is encountered on the command
line. Callbacks for options take 4 arguments: the optparse.Option instance
causing the callback, the option string from the command line, any argument
value associated with the option, and the optparse.OptionParser instance doing
the parsing work.

.. include:: optparse_callback.py
    :literal:
    :start-after: #end_pymotw_header

In this example, the ``--with`` option is configured to take a string argument
(other types are support as well, of course).

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_callback.py'))
.. }}}
.. {{{end}}}


Help Messages
=============

The OptionParser automatically includes a help option to all option sets, so
the user can pass ``--help`` on the command line to see instructions for running
the program. The help message includes all of the options an indication of
whether or not they take an argument. It is also possible to pass help text to
``add_option()`` to give a more verbose description of an option.

.. include:: optparse_help.py
    :literal:
    :start-after: #end_pymotw_header


The options are listed in alphabetical order, with aliases included on the
same line. When the option takes an argument, the dest value is included as an
argument name in the help output. The help text is printed in the right
column.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_help.py --help'))
.. }}}
.. {{{end}}}

Callbacks can be configured to take multiple arguments using the nargs option.

.. include:: optparse_callback_nargs.py
    :literal:
    :start-after: #end_pymotw_header


In this case, the arguments are passed to the callback function as a tuple via
the value argument.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_callback-nargs.py'))
.. }}}
.. {{{end}}}

.. seealso::

    `optparse <http://docs.python.org/lib/module-optparse.html>`_
        Standard library documentation for this module.

    :mod:`getopt`
        The getopt module.
