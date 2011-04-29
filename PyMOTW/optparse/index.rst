=========================================================
optparse -- Command line option parser to replace getopt.
=========================================================

.. module:: optparse
    :synopsis: Command line option parser to replace :mod:`getopt`.

:Purpose: Command line option parser to replace :mod:`getopt`.
:Available In: 2.3

The :mod:`optparse` module is a modern alternative for command line
option parsing that offers several features not available in
:mod:`getopt`, including type conversion, option callbacks, and
automatic help generation. There are many more features to
:mod:`optparse` than can be covered here, but this section will
introduce some of the more commonly used capabilities.

Creating an OptionParser
========================

There are two phases to parsing options with :mod:`optparse`. First,
the :class:`OptionParser` instance is constructed and configured with
the expected options. Then a sequence of options is fed in and
processed.

::

    import optparse
    parser = optparse.OptionParser()

Usually, once the parser has been created, each option is added to the
parser explicitly, with information about what to do when the option
is encountered on the command line. It is also possible to pass a list
of options to the :class:`OptionParser` constructor, but that form is
not used as frequently.

Defining Options
----------------

Options should be added one at a time using the :func:`add_option()`
method. Any un-named string arguments at the beginning of the argument
list are treated as option names. To create aliases for an option
(i.e., to have a short and long form of the same option), simply pass
multiple names.

Parsing a Command Line
----------------------

After all of the options are defined, the command line is parsed by
passing a sequence of argument strings to :func:`parse_args()`. By
default, the arguments are taken from ``sys.argv[1:]``, but a list can
be passed explicitly as well. The options are processed using the
GNU/POSIX syntax, so option and argument values can be mixed in the
sequence.

The return value from :func:`parse_args()` is a two-part tuple
containing an :class:`Values` instance and the list of arguments to
the command that were not interpreted as options. The default
processing action for options is to store the value using the name
given in the *dest* argument to :func:`add_option`.  The
:class:`Values` instance returned by :func:`parse_args` holds the
option values as attributes, so if an option's :data:`dest` is set to
``"myoption"``, the value is accessed as ``options.myoption``.

Short and Long-Form Options
===========================

Here is a simple example with three different options: a boolean
option (``-a``), a simple string option (``-b``), and an integer
option (``-c``).

.. include:: optparse_short.py
    :literal:
    :start-after: #end_pymotw_header


The options on the command line are parsed with the same rules that
:func:`getopt.gnu_getopt()` uses, so there are two ways to pass values
to single character options. The example above uses both forms,
``-bval`` and ``-c val``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_short.py'))
.. }}}
.. {{{end}}}

Notice that the type of the value associated with ``'c'`` in the
output is an integer, since the :class:`OptionParser` was told to
convert the argument before storing it.

Unlike with :mod:`getopt`, "long" option names are not handled any
differently by :mod:`optparse`:

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

Since :mod:`optparse` is supposed to replace :mod:`getopt`, this
example re-implements the same example program used in the section
about :mod:`getopt`:

.. include:: optparse_getoptcomparison.py
    :literal:
    :start-after: #end_pymotw_header

Notice how the options ``-o`` and ``--output`` are aliased by being
added at the same time. Either option can be used on the command line.
The short form:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_getoptcomparison.py -o output.txt'))
.. }}}
.. {{{end}}}

or the long form:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_getoptcomparison.py --output output.txt'))
.. }}}
.. {{{end}}}


Any unique prefix of the long option can also be used:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_getoptcomparison.py --out output.txt'))
.. }}}
.. {{{end}}}


Option Values
=============

The default processing action is to store the argument to the option.
If a type is provided, the argument value is converted to that type
before it is stored.

Setting Defaults
----------------

Since options are by definition optional, applications should
establish default behavior when an option is not given on the command
line.  A default value for an individual option can be provided when
the option is defined.

.. include:: optparse_default.py
   :literal:
   :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_default.py'))
.. cog.out(run_script(cog.inFile, 'optparse_default.py -o "different value"', include_prefix=False))
.. }}}
.. {{{end}}}

Defaults can also be loaded after the options are defined using
keyword arguments to :func:`set_defaults`.

.. include:: optparse_set_defaults.py
   :literal:
   :start-after: #end_pymotw_header

This form is useful when loading defaults from a configuration file or
other source, instead of hard-coding them.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_set_defaults.py'))
.. cog.out(run_script(cog.inFile, 'optparse_set_defaults.py -o "different value"', include_prefix=False))
.. }}}
.. {{{end}}}

All defined options are available as attributes of the :class:`Values`
instance returned by :func:`parse_args` so applications do not need to
check for the presence of an option before trying to use its value.

.. include:: optparse_no_default.py
   :literal:
   :start-after: #end_pymotw_header

If no default value is given for an option, and the option is not
specified on the command line, its value is ``None``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_no_default.py'))
.. cog.out(run_script(cog.inFile, 'optparse_no_default.py -o "different value"', include_prefix=False))
.. }}}
.. {{{end}}}


Type Conversion
---------------

:mod:`optparse` will convert option values from strings to integers,
floats, longs, and complex values.  To enable the conversion, specify
the *type* of the option as an argument to :func:`add_option`.

.. include:: optparse_types.py
   :literal:
   :start-after: #end_pymotw_header

If an option's value cannot be converted to the specified type, an
error is printed and the program exits.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_types.py -i 1 -f 3.14 -l 1000000 -c 1+2j'))
.. cog.out(run_script(cog.inFile, 'optparse_types.py -i a', ignore_error=True, include_prefix=False))
.. }}}
.. {{{end}}}

Custom conversions can be created by subclassing the :class:`Option`
class.  See the standard library documentation for complete details.

Enumerations
------------

The :const:`choice` type provides validation using a list of candidate
strings.  Set *type* to choice and provide the list of valid values
using the *choices* argument to :func:`add_option`.

.. include:: optparse_choice.py
   :literal:
   :start-after: #end_pymotw_header

Invalid inputs result in an error message that shows the allowed list
of values.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_choice.py -c a'))
.. cog.out(run_script(cog.inFile, 'optparse_choice.py -c b', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'optparse_choice.py -c d', include_prefix=False, ignore_error=True, break_lines_at=70))
.. }}}
.. {{{end}}}

Option Actions
==============

Unlike :mod:`getopt`, which only *parses* the options, :mod:`optparse`
is a full option *processing* library. Options can trigger different
actions, specified by the action argument to
:func:`add_option()`. Supported actions include storing the argument
(singly, or as part of a list), storing a constant value when the
option is encountered (including special handling for true/false
values for boolean switches), counting the number of times an option
is seen, and calling a callback.  The default action is
:const:`store`, and does not need to be specified explicitly.

Constants
---------

When options represent a selection of fixed alternatives, such as
operating modes of an application, creating separate explicit options
makes it easier to document them.  The :const:`store_const` action is
intended for this purpose.  

.. include:: optparse_store_const.py
   :literal:
   :start-after: #end_pymotw_header

The :const:`store_const` action associates a constant value in the
application with the option specified by the user.  Several options
can be configured to store different constant values to the same
*dest* name, so the application only has to check a single setting.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_store_const.py'))
.. cog.out(run_script(cog.inFile, 'optparse_store_const.py --fire', include_prefix=False))
.. }}}
.. {{{end}}}


Boolean Flags
-------------

Boolean options are implemented using special actions for storing true
and false constant values.

.. include:: optparse_boolean.py
   :literal:
   :start-after: #end_pymotw_header

True and false versions of the same flag can be created by configuring
their *dest* name to the same value.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_boolean.py'))
.. cog.out(run_script(cog.inFile, 'optparse_boolean.py -t', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'optparse_boolean.py -f', include_prefix=False))
.. }}}
.. {{{end}}}


Repeating Options
-----------------

There are three ways to handle repeated options.  The default is to
overwrite any existing value so that the last option specified is
used.  The :const:`store` action works this way.

Using the :const:`append` action, it is possible to accumulate values
as an option is repeated, creating a list of values.  Append mode is
useful when multiple responses are allowed, and specifying them
separately is easier for the user than constructing a parsable syntax.

.. include:: optparse_append.py
   :literal:
   :start-after: #end_pymotw_header

The order of the values given on the command line is preserved, in
case it is important for the application.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_append.py'))
.. cog.out(run_script(cog.inFile, 'optparse_append.py -o a.out', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'optparse_append.py -o a.out -o b.out', include_prefix=False))
.. }}}
.. {{{end}}}

Sometimes it is enough to know how many times an option was given, and
the associated value is not needed.  For example, many applications
allow the user to repeat the ``-v`` option to increase the level of
verbosity of their output.  The :const:`count` action increments a
value each time the option appears.

.. include:: optparse_count.py
   :literal:
   :start-after: #end_pymotw_header

Since the ``-v`` option doesn't take an argument, it can be repeated
using the syntax ``-vv`` as well as through separate individual
options.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_count.py'))
.. cog.out(run_script(cog.inFile, 'optparse_count.py -v', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'optparse_count.py -v -v', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'optparse_count.py -vv', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'optparse_count.py -q', include_prefix=False))
.. }}}
.. {{{end}}}


Callbacks
---------

Beside saving the arguments for options directly, it is possible to
define callback functions to be invoked when the option is encountered
on the command line. Callbacks for options take four arguments: the
:class:`Option` instance causing the callback, the option string from
the command line, any argument value associated with the option, and
the :class:`OptionParser` instance doing the parsing work.

.. include:: optparse_callback.py
    :literal:
    :start-after: #end_pymotw_header

In this example, the ``--with`` option is configured to take a string
argument (other types such as integers and floats are support as
well).

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_callback.py'))
.. }}}
.. {{{end}}}

Callbacks can be configured to take multiple arguments using the *nargs*
option.

.. include:: optparse_callback_nargs.py
    :literal:
    :start-after: #end_pymotw_header


In this case, the arguments are passed to the callback function as a tuple via
the value argument.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_callback_nargs.py'))
.. }}}
.. {{{end}}}

Help Messages
=============

The :class:`OptionParser` automatically includes a help option to all
option sets, so the user can pass ``--help`` on the command line to
see instructions for running the program. The help message includes
all of the options with an indication of whether or not they take an
argument. It is also possible to pass help text to
:class:`add_option()` to give a more verbose description of an option.

.. include:: optparse_help.py
    :literal:
    :start-after: #end_pymotw_header


The options are listed in alphabetical order, with aliases included on
the same line. When the option takes an argument, the ``dest`` name is
included as an argument name in the help output. The help text is
printed in the right column.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_help.py --help'))
.. }}}
.. {{{end}}}

The name ``WITH`` printed with the option ``--with`` comes from the
destination variable for the option.  For cases where the internal
variable name is descriptive enough to serve in the documentation, the
*metavar* argument can be used to set a different name.

.. include:: optparse_metavar.py
   :literal:
   :start-after: #end_pymotw_header

The value is printed exactly as it is given, without any changes to
capitalization or punctuation.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_metavar.py -h'))
.. }}}
.. {{{end}}}


Organizing Options
------------------

Many applications include sets of related options.  For example,
:command:`rpm` includes separate options for each of its operating
modes.  :mod:`optparse` uses *option groups* to organize options in
the help output.  The option values are all still saved in a single
:class:`Values` instance, so the namespace for option names is still
flat.

.. include:: optparse_groups.py
   :literal:
   :start-after: #end_pymotw_header

Each group has its own section title and description, and the options
are displayed together.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_groups.py -h'))
.. }}}
.. {{{end}}}

Application Settings
--------------------

The automatic help generation facilities support configuration
settings to control several aspects of the help output.  The program's
*usage* string, which shows how the positional arguments are expected,
can be set when the :class:`OptionParser` is created.

.. include:: optparse_usage.py
   :literal:
   :start-after: #end_pymotw_header

The literal value ``%prog`` is expanded to the name of the program at
runtime, so it can reflect the full path to the script.  If the script
is run by :command:`python`, instead of running directly, the script
name is used.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_usage.py -h'))
.. }}}
.. {{{end}}}

The program name can be changed using the *prog* argument.

.. include:: optparse_prog.py
   :literal:
   :start-after: #end_pymotw_header

It is generally a bad idea to hard-code the program name in this way,
though, because if the program is renamed the help will not reflect
the change.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_prog.py -h'))
.. }}}
.. {{{end}}}

The application version can be set using the *version* argument.  When
a value is provided, :mod:`optparse` automatically adds a
``--version`` option to the parser.

.. include:: optparse_version.py
   :literal:
   :start-after: #end_pymotw_header

When the user runs the program with the ``--version`` option,
:mod:`optparse` prints the version string and then exits.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'optparse_version.py -h'))
.. cog.out(run_script(cog.inFile, 'optparse_version.py --version', include_prefix=False))
.. }}}
.. {{{end}}}

.. seealso::

    `optparse <http://docs.python.org/lib/module-optparse.html>`_
        Standard library documentation for this module.

    :mod:`getopt`
        The getopt module, replaced by optparse.

    :mod:`argparse`
        Newer replacement for optparse.
