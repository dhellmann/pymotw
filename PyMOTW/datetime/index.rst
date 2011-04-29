========================================
datetime -- Date/time value manipulation
========================================

.. module:: datetime
    :synopsis: Date/time value manipulation.

:Purpose: The datetime module includes functions and classes for doing date and time parsing, formatting, and arithmetic.
:Available In: 2.3 and later

:mod:`datetime` contains functions and classes for working with dates
and times, separatley and together.

Times
=====

Time values are represented with the :class:`time` class. Times have
attributes for hour, minute, second, and microsecond. They can also
include time zone information. The arguments to initialize a
:class:`time` instance are optional, but the default of ``0`` is
unlikely to be what you want.

.. include:: datetime_time.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_time.py'))
.. }}}
.. {{{end}}}

A time instance only holds values of time, and not a date associated
with the time.

.. include:: datetime_time_minmax.py
    :literal:
    :start-after: #end_pymotw_header

The *min* and *max* class attributes reflect the valid range of
times in a single day.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_time_minmax.py'))
.. }}}
.. {{{end}}}

The resolution for time is limited to whole microseconds.

.. include:: datetime_time_resolution.py
    :literal:
    :start-after: #end_pymotw_header

In fact, using floating point numbers for the microsecond argument
generates a :ref:`TypeError <exceptions-TypeError>`.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_time_resolution.py'))
.. }}}
.. {{{end}}}


Dates
=====

Calendar date values are represented with the :class:`date`
class. Instances have attributes for year, month, and day. It is easy
to create a date representing today's date using the :func:`today()`
class method.

.. include:: datetime_date.py
    :literal:
    :start-after: #end_pymotw_header

This example prints the current date in several formats:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_date.py'))
.. }}}
.. {{{end}}}

There are also class methods for creating instances from integers
(using proleptic Gregorian ordinal values, which starts counting from
Jan. 1 of the year 1) or POSIX timestamp values.

.. include:: datetime_date_fromordinal.py
    :literal:
    :start-after: #end_pymotw_header

This example illustrates the different value types used by
:func:`fromordinal()` and :func:`fromtimestamp()`.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_date_fromordinal.py'))
.. }}}
.. {{{end}}}

As with :class:`time`, the range of date values supported can be
determined using the *min* and *max* attributes.

.. include:: datetime_date_minmax.py
    :literal:
    :start-after: #end_pymotw_header

The resolution for dates is whole days.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_date_minmax.py'))
.. }}}
.. {{{end}}}

Another way to create new date instances uses the :func:`replace()`
method of an existing date. For example, you can change the year,
leaving the day and month alone.

.. include:: datetime_date_replace.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_date_replace.py'))
.. }}}
.. {{{end}}}

timedeltas
==========

Using :func:`replace()` is not the only way to calculate future/past
dates. You can use :mod:`datetime` to perform basic arithmetic on date
values via the :class:`timedelta` class. Subtracting dates produces a
:class:`timedelta`, and a :class:`timedelta` can be added or
subtracted from a date to produce another date. The internal values
for a :class:`timedelta` are stored in days, seconds, and
microseconds.

.. include:: datetime_timedelta.py
    :literal:
    :start-after: #end_pymotw_header

Intermediate level values passed to the constructor are converted into
days, seconds, and microseconds.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_timedelta.py'))
.. }}}
.. {{{end}}}


Date Arithmetic
===============

Date math uses the standard arithmetic operators. This example with
date objects illustrates using :class:`timedelta` objects to compute
new dates, and subtracting date instances to produce timedeltas
(including a negative delta value).

.. include:: datetime_date_math.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_date_math.py'))
.. }}}
.. {{{end}}}

Comparing Values
================

Both date and time values can be compared using the standard operators
to determine which is earlier or later.

.. include:: datetime_comparing.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_comparing.py'))
.. }}}
.. {{{end}}}

Combining Dates and Times
=========================

Use the :class:`datetime` class to hold values consisting of both date
and time components. As with :class:`date`, there are several
convenient class methods to make creating :class:`datetime` instances
from other common values.

.. include:: datetime_datetime.py
    :literal:
    :start-after: #end_pymotw_header

As you might expect, the :class:`datetime` instance has all of the
attributes of both a date and a time object.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_datetime.py'))
.. }}}
.. {{{end}}}

Just as with date, datetime provides convenient class methods for
creating new instances. It also includes :func:`fromordinal()` and
:func:`fromtimestamp()`. In addition, :func:`combine()` can be useful
if you already have a date instance and time instance and want to
create a datetime.

.. include:: datetime_datetime_combine.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_datetime_combine.py'))
.. }}}
.. {{{end}}}

Formatting and Parsing
======================

The default string representation of a datetime object uses the `ISO
8601`_ format (``YYYY-MM-DDTHH:MM:SS.mmmmmm``). Alternate formats can
be generated using :func:`strftime()`. Similarly, if your input data
includes timestamp values parsable with :func:`time.strptime()`, then
:func:`datetime.strptime()` is a convenient way to convert them to
datetime instances.

.. include:: datetime_datetime_strptime.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'datetime_datetime_strptime.py'))
.. }}}
.. {{{end}}}

Time Zones
==========

Within :mod:`datetime`, time zones are represented by subclasses of
:class:`tzinfo`. Since :class:`tzinfo` is an abstract base class, you
need to define a subclass and provide appropriate implementations for
a few methods to make it useful. Unfortunately, :mod:`datetime` does
not include any actual implementations ready to be used, although the
documentation does provide a few sample implementations. Refer to the
standard library documentation page for examples using fixed offsets
as well as a DST-aware class and more details about creating your own
class.  pytz_ is also a good source for time zone implementation
details.

.. seealso::

    `datetime <http://docs.python.org/lib/module-datetime.html>`_
        The standard library documentation for this module.

    :mod:`calendar`
        The :mod:`calendar` module.

    :mod:`time`
        The :mod:`time` module.

    `dateutil <http://labix.org/python-dateutil>`_
        dateutil from Labix extends the datetime module with additional features.

    `WikiPedia: Proleptic Gregorian calendar <http://en.wikipedia.org/wiki/Proleptic_Gregorian_calendar>`_
        A description of the Gregorian calendar system.

    pytz_
        World Time Zone database

    `ISO 8601`_
        The standard for numeric representation of Dates and Time

.. _ISO 8601: http://www.iso.org/iso/support/faqs/faqs_widely_used_standards/widely_used_standards_other/date_and_time_format.htm

.. _pytz: http://pytz.sourceforge.net/
