======================
warnings
======================
.. module:: warnings
    :synopsis: Deliver non-fatal alerts to the user about issues encountered when running a program.

:Module: warnings
:Purpose: Deliver non-fatal alerts to the user about issues encountered when running a program.
:Python Version: 2.1 and later
:Abstract: Manage non-error alerts through the warnings module.

Description
===========

The warnings module was introduced in `PEP 230`_ as a way to warn programmers
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

::

    import warnings

    print 'Before the warning'
    warnings.warn('This is a warning message')
    print 'After the warning'

Then when your program runs, the message is printed:

::

    $ python warnings_warn.py
    /Users/dhellmann/Documents/PyMOTW/in_progress/warnings/warnings_warn.py:14: UserWarning: This is a warning message
      warnings.warn('This is a warning message')
    Before the warning
    After the warning

Even though the warning is printed, the default behavior is to continue past
the warning and run the rest of the program. We can change that behavior with
a filter:

::

    import warnings

    warnings.simplefilter('error', UserWarning)

    print 'Before the warning'
    warnings.warn('This is a warning message')
    print 'After the warning'

This filter tells the warnings module to raise an exception when the warning
is issued.

::

    $ python warnings_warn_raise.py
    Before the warning
    Traceback (most recent call last):
      File "/Users/dhellmann/Documents/PyMOTW/in_progress/warnings/warnings_warn_raise.py", line 16, in <module>
        warnings.warn('This is a warning message')
      File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/warnings.py", line 62, in warn
        globals)
      File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/warnings.py", line 102, in warn_explicit
        raise message
    UserWarning: This is a warning message


We can, of course, also control the filter behavior from the command line. For
example, if we go back to warnings_warn.py and set the filter to raise an
error on UserWarning, we see the exception:

::

    $ python -W 'error::UserWarning::0' warnings_warn.py 
    Before the warning
    Traceback (most recent call last):
      File "warnings_warn.py", line 14, in 
        warnings.warn('This is a warning message')
      File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/warnings.py", line 62, in warn
        globals)
      File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/warnings.py", line 102, in warn_explicit
        raise message
    UserWarning: This is a warning message

Since I left the fields for message and module blank, they were interpreted as
matching anything.

Filtering with Patterns
=======================

To filter on more complex rules programmatically, use filterwarnings(). For
example, to filter based on the content of the message text:

::

    import warnings

    warnings.filterwarnings('ignore', '.*do not.*',)

    warnings.warn('Show this message')
    warnings.warn('Do not show this message')

Notice that I used "do not" in the pattern, but "Do not" in the warning. The
regular expression is always compiled to look for case insensitive matches.

::

    $ python warnings_filterwarnings_message.py
    /Users/dhellmann/Documents/PyMOTW/in_progress/warnings/warnings_filterwarnings_message.py:15: UserWarning: Show this message
      warnings.warn('Show this message')

Running this source from the command line::

    import warnings

    warnings.warn('Show this message')
    warnings.warn('Do not show this message')

yields::

    $ python -W 'ignore:do not:UserWarning::0' warnings_filtering.py 
    warnings_filtering.py:13: UserWarning: Show this message
      warnings.warn('Show this message')

The same pattern matching rules apply to the name of the source module
containing the warning call. To suppress all warnings from the
warnings_filtering module::

    import warnings

    warnings.filterwarnings('ignore', 
                            '.*', 
                            UserWarning,
                            'warnings_filtering',
                            )

    import warnings_filtering

Since the filter is in place, no warnings are emitted when warnings_filtering
is imported::

    $ python warnings_filterwarnings_module.py

To suppress only the warning on line 14 of warnings_filtering::

    import warnings

    warnings.filterwarnings('ignore', 
                            '.*', 
                            UserWarning,
                            'warnings_filtering',
                            14)

    import warnings_filtering

::

    $ python warnings_filterwarnings_lineno.py
    /Users/dhellmann/Documents/PyMOTW/in_progress/warnings/warnings_filtering.py:13: UserWarning: Show this message
      warnings.warn('Show this message')


Repeated Warnings
=================

By default, most types of warnings are only printed the first time they occur
in a given location, where location is defined as the combination of module
and line number.

::

    import warnings

    def function_with_warning():
        warnings.warn('This is a warning!')
        
    function_with_warning()
    function_with_warning()
    function_with_warning()

::

    $ python warnings_repeated.py
    /Users/dhellmann/Documents/PyMOTW/in_progress/warnings/warnings_repeated.py:14: UserWarning: This is a warning!
      warnings.warn('This is a warning!')

The "once" action can be used to suppress instances of the same message from
different locations.

::

    import warnings

    warnings.simplefilter('once', UserWarning)

    warnings.warn('This is a warning!')
    warnings.warn('This is a warning!')
    warnings.warn('This is a warning!')

::

    $ python warnings_once.py
    /Users/dhellmann/Documents/PyMOTW/in_progress/warnings/warnings_once.py:15: UserWarning: This is a warning!
      warnings.warn('This is a warning!')

Similarly, "module" will suppress repeated messages from the same module, no
matter what line number.

Alternate Message Delivery Functions
====================================

Normally warnings are printed to sys.stderr. You can change that behavior by
replacing the showwarning() function inside the warnings module. For example,
if you wanted warnings to go to a log file instead of stderr, you could
replace showwarning() with a function like this:

::

    import warnings
    import logging

    logging.basicConfig(level=logging.INFO)

    def send_warnings_to_log(message, category, filename, lineno, file=None):
        logging.warning(
            '%s:%s: %s:%s' % 
            (filename, lineno, category.__name__, message))
        return

    old_showwarning = warnings.showwarning
    warnings.showwarning = send_warnings_to_log

    warnings.warn('This is a warning message')

So that when warnings.warn() is called, the warnings are emitted with the rest
of the log messages.

::

    $ python warnings_showwarning.py
    WARNING:root:/Users/dhellmann/Documents/PyMOTW/in_progress/warnings/warnings_showwarning.py:25: UserWarning:This is a warning message

Formatting
==========

If it is OK for warnings to go to stderr, but you don't like the formatting,
you can replace formatwarning() instead.

::

    import warnings

    def warning_on_one_line(message, category, filename, lineno):
        return '%s:%s: %s:%s' % (filename, lineno, category.__name__, message)

    warnings.warn('This is a warning message, before')
    warnings.formatwarning = warning_on_one_line
    warnings.warn('This is a warning message, after')

    $ python warnings_formatwarning.py
    /Users/dhellmann/Documents/PyMOTW/in_progress/warnings/warnings_formatwarning.py:16: UserWarning: This is a warning message, before
      warnings.warn('This is a warning message, before')
    /Users/dhellmann/Documents/PyMOTW/in_progress/warnings/warnings_formatwarning.py:18: UserWarning:This is a warning message, after

Stack Level in Warnings
=======================

You'll notice that by default the warning message includes the source line
that generated it, when available. It's not all that useful to see the line of
code with the actual warning message, though. Instead, you can tell
warnings.warn() how far up the stack it has to go to find the line the called
the function containing the warning. That way users of a deprecated function
see where the function is called, instead of the implementation of the
function.

::

    import warnings

    def old_function():
        warnings.warn(
            'old_function() is deprecated, use new_function() instead', 
            stacklevel=2)

    def caller_of_old_function():
        old_function()
        
    caller_of_old_function()


Notice that in this example warnings.warn() needs to go up the stack 2 levels,
one for itself and one for old_function().

::

    $ python warnings_warn_stacklevel.py
    /Users/dhellmann/Documents/PyMOTW/in_progress/warnings/warnings_warn_stacklevel.py:19: UserWarning: old_function() is deprecated, use new_function() instead
      old_function()


References
==========

`PEP 230 <http://www.python.org/peps/pep-0230.html>`_ -- Warning Framework
