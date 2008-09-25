========================================
datetime -- Date/time value manipulation
========================================

.. module:: datetime
    :synopsis: Date/time value manipulation.

:Purpose: The datetime module includes functions and classes for doing date parsing, formatting, and arithmetic.
:Python Version: 2.3 and later

Times
=====

Time values are represented with the time class. Times have attributes for
hour, minute, second, and microsecond. They also, optionally, include time
zone information. The arguments to initialize a time instance are optional,
but the default of 0 is unlikely to be what you want.

.. include:: datetime_time.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python datetime_time.py
    01:02:03
    hour  : 1
    minute: 2
    second: 3
    microsecond: 0
    tzinfo: None

A time instance only holds values of time, and not dates. 

.. include:: datetime_time_minmax.py
    :literal:
    :start-after: #end_pymotw_header

The min and max class attributes reflect the valid range of times in a single
day.

::

    $ python datetime_time_minmax.py
    Earliest  : 00:00:00
    Latest    : 23:59:59.999999
    Resolution: 0:00:00.000001

The resolution for time is limited to microseconds. More precise values are
truncated.

.. include:: datetime_time_resolution.py
    :literal:
    :start-after: #end_pymotw_header

In fact, using floating point numbers for the microsecond argument generates a
DeprecationWarning.

::

    $ python datetime_time_resolution.py
    /Users/dhellmann/Documents/PyMOTW/in_progress/datetime/datetime_time_resolution.py:14: DeprecationWarning: integer argument expected, got float
      print '%02.1f :' % m, datetime.time(0, 0, 0, microsecond=m)
    1.0 : 00:00:00.000001
    0.0 : 00:00:00
    0.1 : 00:00:00
    0.6 : 00:00:00


Dates
=====

Basic date values are represented with the date class. Instances have
attributes for year, month, and day. It is easy to create a date representing
today's date using the today() class method.

.. include:: datetime_date.py
    :literal:
    :start-after: #end_pymotw_header

This example prints today's date in several formats:

::

    $ python datetime_date.py
    2008-03-13
    ctime: Thu Mar 13 00:00:00 2008
    tuple: (2008, 3, 13, 0, 0, 0, 3, 73, -1)
    ordinal: 733114
    Year: 2008
    Mon : 3
    Day : 13

There are also class methods for creating instances from integers (using
proleptic Gregorian ordinal values, which starts counting from Jan. 1 of the
year 1) or POSIX timestamp values.

.. include:: datetime_date_fromordinal.py
    :literal:
    :start-after: #end_pymotw_header

This example illustrates the different value types used by fromordinal() and
fromtimestamp().

::

    $ python datetime_date_fromordinal.py
    o: 733114
    fromordinal(o): 2008-03-13
    t: 1205436039.53
    fromtimestamp(t): 2008-03-13

The range of date values supported can be determined using the min and max
attributes.

.. include:: datetime_date_minmax.py
    :literal:
    :start-after: #end_pymotw_header

The resolution for dates is whole days.

::

    $ python datetime_date_minmax.py
    Earliest  : 0001-01-01
    Latest    : 9999-12-31
    Resolution: 1 day, 0:00:00

Another way to create new date instances uses the replace() method of an
existing date. For example, you can change the year, leaving the day and month
alone.

.. include:: datetime_date_replace.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python datetime_date_replace.py
    d1: 2008-03-12
    d2: 2009-03-12

timedeltas
==========

Using replace() is not the only way to calculate future/past dates. You can
use datetime to perform basic arithmetic on date values via the timedelta
class. Subtracting dates produces a timedelta, and a timedelta can be added or
subtracted from a date to produce another date. The internal values for
timedeltas are stored in days, seconds, and microseconds. 

.. include:: datetime_timedelta.py
    :literal:
    :start-after: #end_pymotw_header

Intermediate level values passed to the constructor are converted into days,
seconds, and microseconds.

::

    $ python datetime_timedelta.py
    microseconds: 0:00:00.000001
    milliseconds: 0:00:00.001000
    seconds     : 0:00:01
    minutes     : 0:01:00
    hours       : 1:00:00
    days        : 1 day, 0:00:00
    weeks       : 7 days, 0:00:00


Arithmetic
==========

Date math uses the standard arithmetic operators. This example with date
objects illustrates using timedeltas to compute new dates, and subtracting
date instances to produce timedeltas (including a negative delta value).

.. include:: datetime_date_math.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python datetime_date_math.py
    Today    : 2008-03-13
    One day  : 1 day, 0:00:00
    Yesterday: 2008-03-12
    Tomorrow : 2008-03-14
    tomorrow - yesterday: 2 days, 0:00:00
    yesterday - tomorrow: -2 days, 0:00:00

Comparing Values
================

Both date and time values can be compared using the standard operators to
determine which is earlier or later.

.. include:: datetime_comparing.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python datetime_comparing.py
    Times:
        t1: 12:55:00
        t2: 13:05:00
        t1 < t2: True
    Dates:
        d1: 2008-03-13
        d2: 2008-03-14
        d1 > d2: False

Combining Dates and Times
=========================

You should use the datetime class to hold values consisting of both date and
time components. Like with date, there are several convenient class methods to
make creating datetime objects from other common values easier. 

.. include:: datetime_datetime.py
    :literal:
    :start-after: #end_pymotw_header

As you might expect, the datetime instance has all of the attributes of a date
and time object.

::

    $ python datetime_datetime.py
    Now    : 2008-03-15 22:58:14.770074
    Today  : 2008-03-15 22:58:14.779804
    UTC Now: 2008-03-16 03:58:14.779858
    year : 2008
    month : 3
    day : 15
    hour : 22
    minute : 58
    second : 14
    microsecond : 780399

Just as with date, the datetime class provides convenient class methods for
creating new instances. Of course it includes fromordinal() and
fromtimestamp(). In addition, combine() can be useful if you already have a
date instance and time instance and want to create a datetime.

.. include:: datetime_datetime_combine.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python datetime_datetime_combine.py
    t : 01:02:03
    d : 2008-03-16
    dt: 2008-03-16 01:02:03

Formatting and Parsing
======================

The default string representation of a datetime object uses the ISO 8601
format (YYYY-MM-DDTHH:MM:SS.mmmmmm). Alternate formats can be generated using
strftime(). Similarly, if your input data includes timestamp values parsable
with time.strptime() strptime() is a convenient way to convert them to
datetime instances. 

.. include:: datetime_datetime_strptime.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python datetime_datetime_strptime.py
    ISO     : 2008-03-16 08:08:16.275134
    strftime: Sun Mar 16 08:08:16 2008
    strptime: Sun Mar 16 08:08:16 2008

Time Zones
==========

Within datetime, time zones are represented by subclasses of datetime.tzinfo.
Since tzinfo is an abstract base class, you need to define a subclass and
provide appropriate implementations for a few methods to make it useful.
Unfortunately, datetime does not include any actual implementations ready to
be used. Ironically, the documentation does provide a few sample
implementations. Refer to the tzinfo page for examples using fixed offsets as
well as a DST-aware class and more details about creating your own class.

References
==========

`WikiPedia: Proleptic Gregorian calendar <http://en.wikipedia.org/wiki/Proleptic_Gregorian_calendar>`_

Standard library documentation: `datetime <http://docs.python.org/lib/module-datetime.html>`_

See also :mod:`calendar` and :mod:`time`.
