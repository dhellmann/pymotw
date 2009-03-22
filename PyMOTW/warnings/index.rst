============================
warnings -- Non-fatal alerts
============================

.. module:: warnings
    :synopsis: Deliver non-fatal alerts to the user about issues encountered when running a program.

:Purpose: Deliver non-fatal alerts to the user about issues encountered when running a program.
:Python Version: 2.1 and later

The warnings module was introduced in :pep:`230` as a way to warn programmers
about changes in language or library features in anticipation of backwards
incompatible changes coming with Python 3.0. Since warnings are not fatal, a
program may encounter the same warn-able situation many times in the course of
running. The warnings module suppresses repeated warnings from the same source
to cut down on the annoyance factor of showing the same message over and over.
You can control the messages printed on a case-by-case basis using the -W
option to the interpreter or by calling functions inside warnings from your
code.

Categories and Filtering
========================

Warnings are categorized using subclasses of the builtin exception class
Warning. Several standard values are described in the documentation, and you
can add your own by subclassing from Warning to create a new class.

Messages are filtered using settings controlled through the -W option to the
interpreter. A filter consists of 5 parts, the action, message, category,
module, and line number. When a warning is generated, it is compared against
all of the registered filters. The first filter that matches controls the
action taken for the warning. If no filter matches, the default action is
taken.

The actions understood by the filtering mechanism are:

* error: Turn the warning into an exception.
* ignore: Discard the warning.
* always: Always emit a warning.
* default: Print the warning the first time it is generated from each location.
* module: Print the warning the first time it is generated from each module.
* once: Print the warning the first time it is generated.

The message portion of the filter is a regular expression that is used to
match the warning text.

The category is a name of an exception class, as described above.

The module contains a regular expression to be matched against the module name
generating the warning.

And the line number can be used to change the handling on specific occurrences
of a warning. Use 0 for the line number to have the filter apply to all
occurrences.

Generating Warnings
===================

The simplest way to emit a warning from your own code is to just call
warnings.warn() with the message as an argument:

.. include:: warnings_warn.py
    :literal:
    :start-after: #end_pymotw_header

Then when your program runs, the message is printed:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'warnings_warn.py'))
.. }}}
.. {{{end}}}

Even though the warning is printed, the default behavior is to continue past
the warning and run the rest of the program. We can change that behavior with
a filter:

.. include:: warnings_warn_raise.py
    :literal:
    :start-after: #end_pymotw_header

This filter tells the warnings module to raise an exception when the warning
is issued.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'warnings_warn_raise.py', ignore_error=True))
.. }}}
.. {{{end}}}


We can, of course, also control the filter behavior from the command line. For
example, if we go back to warnings_warn.py and set the filter to raise an
error on UserWarning, we see the exception:

.. {{{cog
.. cog.out(run_script(cog.inFile, '-W "error::UserWarning::0" warnings_warn.py', ignore_error=True))
.. }}}
.. {{{end}}}

Since I left the fields for message and module blank, they were interpreted as
matching anything.

Filtering with Patterns
=======================

To filter on more complex rules programmatically, use filterwarnings(). For
example, to filter based on the content of the message text:

.. include:: warnings_filterwarnings_message.py
    :literal:
    :start-after: #end_pymotw_header

Notice that I used "do not" in the pattern, but "Do not" in the warning. The
regular expression is always compiled to look for case insensitive matches.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'warnings_filterwarnings_message.py'))
.. }}}
.. {{{end}}}

Running this source from the command line:

.. include:: warnings_filtering.py
    :literal:
    :start-after: #end_pymotw_header

yields:

.. {{{cog
.. cog.out(run_script(cog.inFile, '-W "ignore:do not:UserWarning::0" warnings_filtering.py'))
.. }}}
.. {{{end}}}

The same pattern matching rules apply to the name of the source module
containing the warning call. To suppress all warnings from the
warnings_filtering module:

.. include:: warnings_filterwarnings_module.py
    :literal:
    :start-after: #end_pymotw_header

Since the filter is in place, no warnings are emitted when warnings_filtering
is imported:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'warnings_filterwarnings_module.py'))
.. }}}
.. {{{end}}}

To suppress only the warning on line 14 of warnings_filtering:

.. include:: warnings_filterwarnings_lineno.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'warnings_filterwarnings_lineno.py'))
.. }}}
.. {{{end}}}


Repeated Warnings
=================

By default, most types of warnings are only printed the first time they occur
in a given location, where location is defined as the combination of module
and line number.

.. include:: warnings_repeated.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'warnings_repeated.py'))
.. }}}
.. {{{end}}}


The "once" action can be used to suppress instances of the same message from
different locations.

.. include:: warnings_once.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'warnings_once.py'))
.. }}}
.. {{{end}}}

Similarly, "module" will suppress repeated messages from the same module, no
matter what line number.

Alternate Message Delivery Functions
====================================

Normally warnings are printed to sys.stderr. You can change that behavior by
replacing the showwarning() function inside the warnings module. For example,
if you wanted warnings to go to a log file instead of stderr, you could
replace showwarning() with a function like this:

.. include:: warnings_showwarning.py
    :literal:
    :start-after: #end_pymotw_header

So that when warnings.warn() is called, the warnings are emitted with the rest
of the log messages.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'warnings_showwarning.py'))
.. }}}
.. {{{end}}}

Formatting
==========

If it is OK for warnings to go to stderr, but you don't like the formatting,
you can replace formatwarning() instead.

.. include:: warnings_formatwarning.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'warnings_formatwarning.py'))
.. }}}
.. {{{end}}}

Stack Level in Warnings
=======================

You'll notice that by default the warning message includes the source line
that generated it, when available. It's not all that useful to see the line of
code with the actual warning message, though. Instead, you can tell
warnings.warn() how far up the stack it has to go to find the line the called
the function containing the warning. That way users of a deprecated function
see where the function is called, instead of the implementation of the
function.

.. include:: warnings_warn_stacklevel.py
    :literal:
    :start-after: #end_pymotw_header


Notice that in this example warnings.warn() needs to go up the stack 2 levels,
one for itself and one for old_function().

.. {{{cog
.. cog.out(run_script(cog.inFile, 'warnings_warn_stacklevel.py'))
.. }}}
.. {{{end}}}

.. seealso::

    `warnings <http://docs.python.org/lib/module-warnings.html>`_
        Standard library documentation for this module.

    :pep:`230`
        Warning Framework
