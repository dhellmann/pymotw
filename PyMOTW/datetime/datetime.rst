===============
datetime
===============
.. module:: datetime
    :synopsis: Date/time value manipulation.

:Module: datetime
:Purpose: Date/time value manipulation.
:Python Version: 2.3 and later
:Abstract:

    The datetime module includes functions and classes for doing date parsing,
    formatting, and arithmetic.

Times
=====

Time values are represented with the time class. Times have attributes for
hour, minute, second, and microsecond. They also, optionally, include time
zone information. The arguments to initialize a time instance are optional,
but the default of 0 is unlikely to be what you want.

::

    import datetime

    t = datetime.time(1, 2, 3)
    print t
    print 'hour  :', t.hour
    print 'minute:', t.minute
    print 'second:', t.second
    print 'microsecond:', t.microsecond
    print 'tzinfo:', t.tzinfo

::

    $ python datetime_time.py
    01:02:03
    hour  : 1
    minute: 2
    second: 3
    microsecond: 0
    tzinfo: None

A time instance only holds values of time, and not dates. 

::

    import datetime

    print 'Earliest  :', datetime.time.min
    print 'Latest    :', datetime.time.max
    print 'Resolution:', datetime.time.resolution

The min and max class attributes reflect the valid range of times in a single
day.

::

    $ python datetime_time_minmax.py
    Earliest  : 00:00:00
    Latest    : 23:59:59.999999
    Resolution: 0:00:00.000001

The resolution for time is limited to microseconds. More precise values are
truncated.

::

    import datetime

    for m in [ 1, 0, 0.1, 0.6 ]:
        print '%02.1f :' % m, datetime.time(0, 0, 0, microsecond=m)

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

::

    import datetime

    today = datetime.date.today()
    print today
    print 'ctime:', today.ctime()
    print 'tuple:', today.timetuple()
    print 'ordinal:', today.toordinal()
    print 'Year:', today.year
    print 'Mon :', today.month
    print 'Day :', today.day

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

::

    import datetime
    import time

    o = 733114
    print 'o:', o
    print 'fromordinal(o):', datetime.date.fromordinal(o)
    t = time.time()
    print 't:', t
    print 'fromtimestamp(t):', datetime.date.fromtimestamp(t)

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

::

    import datetime

    print 'Earliest  :', datetime.date.min
    print 'Latest    :', datetime.date.max
    print 'Resolution:', datetime.date.resolution

The resolution for dates is whole days.

::

    $ python datetime_date_minmax.py
    Earliest  : 0001-01-01
    Latest    : 9999-12-31
    Resolution: 1 day, 0:00:00

Another way to create new date instances uses the replace() method of an
existing date. For example, you can change the year, leaving the day and month
alone.

::

    import datetime

    d1 = datetime.date(2008, 3, 12)
    print 'd1:', d1

    d2 = d1.replace(year=2009)
    print 'd2:', d2

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

::

    import datetime

    print "microseconds:", datetime.timedelta(microseconds=1)
    print "milliseconds:", datetime.timedelta(milliseconds=1)
    print "seconds     :", datetime.timedelta(seconds=1)
    print "minutes     :", datetime.timedelta(minutes=1)
    print "hours       :", datetime.timedelta(hours=1)
    print "days        :", datetime.timedelta(days=1)
    print "weeks       :", datetime.timedelta(weeks=1)

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

::

    import datetime

    today = datetime.date.today()
    print 'Today    :', today

    one_day = datetime.timedelta(days=1)
    print 'One day  :', one_day

    yesterday = today - one_day
    print 'Yesterday:', yesterday

    tomorrow = today + one_day
    print 'Tomorrow :', tomorrow

    print 'tomorrow - yesterday:', tomorrow - yesterday
    print 'yesterday - tomorrow:', yesterday - tomorrow

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

::

    import datetime
    import time

    print 'Times:'
    t1 = datetime.time(12, 55, 0)
    print '\tt1:', t1
    t2 = datetime.time(13, 5, 0)
    print '\tt2:', t2
    print '\tt1 < t2:', t1 < t2

    print 'Dates:'
    d1 = datetime.date.today()
    print '\td1:', d1
    d2 = datetime.date.today() + datetime.timedelta(days=1)
    print '\td2:', d2
    print '\td1 > d2:', d1 > d2

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

::

    import datetime

    print 'Now    :', datetime.datetime.now()
    print 'Today  :', datetime.datetime.today()
    print 'UTC Now:', datetime.datetime.utcnow()

    d = datetime.datetime.now()
    for attr in [ 'year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']:
        print attr, ':', getattr(d, attr)

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

::

    import datetime

    t = datetime.time(1, 2, 3)
    print 't :', t

    d = datetime.date.today()
    print 'd :', d

    dt = datetime.datetime.combine(d, t)
    print 'dt:', dt

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

::

    import datetime

    format = "%a %b %d %H:%M:%S %Y"

    today = datetime.datetime.today()
    print 'ISO     :', today

    s = today.strftime(format)
    print 'strftime:', s

    d = datetime.datetime.strptime(s, format)
    print 'strptime:', d.strftime(format)

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


