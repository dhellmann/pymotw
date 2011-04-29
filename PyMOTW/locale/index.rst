=========================================
locale -- POSIX cultural localization API
=========================================

.. module:: locale
    :synopsis: POSIX cultural localization API

:Purpose: Format and parse values that depend on location or language.
:Available In: 1.5 and later

The :mod:`locale` module is part of Python's internationalization and
localization support library. It provides a standard way to handle
operations that may depend on the language or location of a user. For
example, it handles formatting numbers as currency, comparing strings
for sorting, and working with dates. It does not cover translation
(see the :mod:`gettext` module) or Unicode encoding.

.. note::

  Changing the locale can have application-wide ramifications, so the
  recommended practice is to avoid changing the value in a library and
  to let the application set it one time. In the examples below, the
  locale is changed several times within a short program to highlight
  the differences in the settings of various locales. It is far more
  likely that your application will set the locale once at startup and
  not change it.

Probing the Current Locale
==========================

The most common way to let the user change the locale settings for an
application is through an environment variable (:data:`LC_ALL`,
:data:`LC_CTYPE`, :data:`LANG`, or :data:`LANGUAGE`, depending on the
platform). The application then calls :func:`setlocale` without a
hard-coded value, and the environment value is used.

.. include:: locale_env_example.py
    :literal:
    :start-after: #end_pymotw_header

The :func:`localeconv` method returns a dictionary containing the
locale's conventions.  The full list of value names and definitions is
covered in the standard library documentation.

A Mac running OS X 10.6 with all of the variables unset produces this output:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'export LANG=; export LC_CTYPE=; python locale_env_example.py', interpreter=None))
.. }}}
.. {{{end}}}


Running the same script with the :data:`LANG` variable set shows how
the locale and default encoding change:

France (``fr_FR``):

.. {{{cog
.. cog.out(run_script(cog.inFile, 'LANG=fr_FR LC_CTYPE=fr_FR LC_ALL=fr_FR python locale_env_example.py', interpreter=None))
.. }}}
.. {{{end}}}


Spain (``es_ES``):


.. {{{cog
.. cog.out(run_script(cog.inFile, 'LANG=es_ES LC_CTYPE=es_ES LC_ALL=es_ES python locale_env_example.py', interpreter=None))
.. }}}
.. {{{end}}}

Portgual (``pt_PT``):


.. {{{cog
.. cog.out(run_script(cog.inFile, 'LANG=pt_PT LC_CTYPE=pt_PT LC_ALL=pt_PT python locale_env_example.py', interpreter=None))
.. }}}
.. {{{end}}}


Poland (``pl_PL``):


.. {{{cog
.. cog.out(run_script(cog.inFile, 'LANG=pl_PL LC_CTYPE=pl_PL LC_ALL=pl_PL python locale_env_example.py', interpreter=None))
.. }}}
.. {{{end}}}


Currency
========

The example output above shows that changing the locale updates the
currency symbol setting and the character to separate whole numbers
from decimal fractions.  This example loops through several different
locales to print a positive and negative currency value formatted for
each locale:

.. include:: locale_currency_example.py
    :literal:
    :start-after: #end_pymotw_header

The output is this small table:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'locale_currency_example.py'))
.. }}}
.. {{{end}}}

Formatting Numbers
==================

Numbers not related to currency are also formatted differently
depending on the locale.  In particular, the *grouping* character used
to separate large numbers into readable chunks is changed:

.. include:: locale_grouping.py
   :literal:
   :start-after: #end_pymotw_header

To format numbers without the currency symbol, use :func:`format`
instead of :func:`currency`.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'locale_grouping.py'))
.. }}}
.. {{{end}}}



Parsing Numbers
===============

Besides generating output in different formats, the :mod:`locale`
module helps with parsing input. It includes :func:`atoi` and
:func:`atof` functions for converting the strings to integer and
floating point values based on the locale's numerical formatting
conventions.

.. include:: locale_atof_example.py
    :literal:
    :start-after: #end_pymotw_header

The grouping and decimal separator values 

.. {{{cog
.. cog.out(run_script(cog.inFile, 'locale_atof_example.py'))
.. }}}
.. {{{end}}}


Dates and Times
===============

Another important aspect of localization is date and time formatting:

.. include:: locale_date_example.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'locale_date_example.py'))
.. }}}
.. {{{end}}}

This discussion only covers some of the high-level functions in the
:mod:`locale` module. There are others which are lower level
(:func:`format_string`) or which relate to managing the locale for
your application (:func:`resetlocale`).

.. seealso::

    `locale <http://docs.python.org/library/locale.html>`_
        The standard library documentation for this module.

    :mod:`gettext`
        Message catalogs for translations.
