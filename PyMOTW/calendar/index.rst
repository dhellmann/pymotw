===========================
calendar -- Work with dates
===========================

.. module:: calendar
    :synopsis: The calendar module implements classes for working with dates to manage year/month/week oriented values.

:Purpose: The calendar module implements classes for working with dates to manage year/month/week oriented values.
:Available In: 1.4, with updates in 2.5

The calendar module defines the Calendar class, which encapsulates
calculations for values such as the dates of the weeks in a given month or
year. In addition, the TextCalendar and HTMLCalendar classes can produce
pre-formatted output.

Formatting Examples
===================

A very simple example which produces formatted text output for a month
using TextCalendar might use the prmonth() method.

.. include:: calendar_textcalendar.py
    :literal:
    :start-after: #end_pymotw_header

The example configures TextCalendar to start weeks on Sunday,
following the American convention. The default is to use the European
convention of starting a week on Monday.

The output looks like:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'calendar_textcalendar.py'))
.. }}}
.. {{{end}}}


The HTML output for the same time period is slightly different, since there is
no prmonth() method:

.. include:: calendar_htmlcalendar.py
    :literal:
    :start-after: #end_pymotw_header

The rendered output looks roughly the same, but is wrapped with HTML tags.  You can also see that each table cell has a class attribute corresponding to the day of the week.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'calendar_htmlcalendar.py'))
.. }}}
.. {{{end}}}

If you need to produce output in a format other than one of the available
defaults, you can use :mod:`calendar` to calculate the dates and organize
the values into week and month ranges, then iterate over the result yourself.
The weekheader(), monthcalendar(), and yeardays2calendar() methods of Calendar
are especially useful for that sort of work.

Calling yeardays2calendar() produces a sequence of "month row" lists. Each
list includes the months as another list of weeks. The weeks are lists of
tuples made up of day number (1-31) and weekday number (0-6). Days that fall
outside of the month have a day number of 0.

.. include:: calendar_yeardays2calendar.py
    :literal:
    :start-after: #end_pymotw_header

Calling yeardays2calendar(2007, 2) returns data for 2007, organized with 2
months per row.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'calendar_yeardays2calendar.py'))
.. }}}
.. {{{end}}}


This is equivalent to the data used by formatyear()

.. include:: calendar_formatyear.py
    :literal:
    :start-after: #end_pymotw_header

which for the same arguments produces output like:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'calendar_formatyear.py'))
.. }}}
.. {{{end}}}

If you want to format the output yourself for some reason (such as including
links in HTML output), you will find the day_name, day_abbr, month_name, and
month_abbr module attributes useful. They are automatically configured
correctly for the current locale.

Calculating Dates
=================

Although the calendar module focuses mostly on printing full calendars in
various formats, it also provides functions useful for working with dates in
other ways, such as calculating dates for a recurring event. For example, the
Python Atlanta User's Group meets the 2nd Thursday of every month. To
calculate the dates for the meetings for a year, you could use the return
value of monthcalendar().

.. include:: calendar_monthcalendar.py
    :literal:
    :start-after: #end_pymotw_header

Notice that some days are 0. Those are days of the week that overlap
with the given month but which are part of another month.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'calendar_monthcalendar.py'))
.. }}}
.. {{{end}}}


As mentioned earlier, the first day of the week is Monday. It is possible
to change that by calling setfirstweekday(). On the other hand, since the
calendar module includes constants for indexing into the date ranges returned
by monthcalendar(), it is more convenient to skip that step in this case.

To calculate the PyATL meeting dates for 2007, assuming the second Thursday of
every month, we can use the 0 values to tell us whether the Thursday of the
first week is included in the month (or if the month starts, for example on a
Friday).

.. include:: calendar_secondthursday.py
    :literal:
    :start-after: #end_pymotw_header

So the PyATL meeting schedule for the year is:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'calendar_secondthursday.py'))
.. }}}
.. {{{end}}}


.. seealso::

    `calendar <http://docs.python.org/library/calendar.html>`_
        The standard library documentation for this module.

    :mod:`time`
        Lower-level time functions.

    :mod:`datetime`
        Manipulate date values, including timestamps and time zones.

