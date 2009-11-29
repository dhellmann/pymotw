===============================================
plistlib -- Manipulate OS X property list files
===============================================

.. module:: plistlib
    :synopsis: Manipulate OS X property list files

:Purpose: Read and write OS X property list files
:Python Version: 2.6

plistlib provides an interface for working with property list files
used under OS X.  plist files are typically XML, sometimes compressed.
They are used by the operating system and applications to store
preferences or other configuration settings.  The contents are usually
structured as a dictionary containing key value pairs of basic
built-in types (unicode strings, integers, dates, etc.).  Values can
also be nested data structures such as other dictionaries or lists.
Binary data, or strings with control characters, can be encoded using
the ``data`` type.

Reading plist Files
===================

OS X applications such as iCal use plist files to store meta-data
about objects they manage.  For example, iCal stores the definitions
of all of your calendars as a series of plist files in the Library
directory.  

.. include:: Info.plist
   :literal:

.. note::

   I've removed some personal information from the sample.

This sample script finds the calendar defintions, reads
them, and prints the titles of any calendars being displayed by iCal
(having the property "Checked" set to a true value).

.. include:: plistlib_checked_calendars.py
   :literal:
   :start-after: #end_pymotw_header

The type of the ``Checked`` property is defined by the plist file, so
our script does not need to do the conversion.

::

	$ python plistlib_checked_calendars.py
	Doug Hellmann
	Tasks
	Vacation Schedule
	EarthSeasons
	US Holidays
	Athens, GA Weather - By Weather Underground
	Birthdays
	Georgia Bulldogs Calendar (NCAA Football)
	Home
	Meetup: Django
	Meetup: Python


Writing plist Files
===================

Accessing plist Data in Resource Forks
======================================

Binary Data
===========


.. seealso::

    `plistlib <http://docs.python.org/library/plistlib.html>`_
        The standard library documentation for this module.

    `plist manual page <http://developer.apple.com/documentation/Darwin/Reference/ManPages/man5/plist.5.html>`_
        Documentation of the plist file format.

    `Weather Underground <http://www.wunderground.com/>`_
        Free weather information, including ICS and RSS feeds.
