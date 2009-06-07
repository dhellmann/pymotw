===========================
gettext -- Message Catalogs
===========================

.. module:: gettext
    :synopsis: Message Catalogs

:Purpose: Message catalog API for internationalization.
:Python Version: 2.1.3 and later

The :mod:`gettext` module provides an all-Python implementation compatible with the GNU gettext library for message translation and catalog management.  The tools available with the Python source distribution enable you to extract messages from your source, build a message catalog containing translations, and use that message catalog to print an appropriate message for the user at runtime.

Message catalogs can be used to provide internationalized interfaces for your program, showing messages in a language appropriate to the user.  They can also be used for other message customizations, including "skinning" an interface for different wrappers or partners.

Translation Workflow Overview
=============================

The process for setting up and using translations includes five steps:

1. Mark up literal strings in your code that contain messages to translate.

   Start by identifying the messages within your program source that need to be translated,
   and marking the literal strings so the extraction program can find them.

2. Extract the messages.

   After you have identified the translatable strings in your program source, use
   ``pygettext.py`` to pull the strings out and create a ``.pot`` file, or translation
   template. The template is a text file with copies of all of the strings you identified
   and placeholders for their translations.

3. Translate the messages.

   Give a copy of the ``.pot`` file to the translator, changing the extension to ``.po``. The
   ``.po`` file is an editable source file used as input for the compilation step. The
   translator should update the header text in the file and provide translations for all of
   the strings.

4. "Compile" the message catalog from the translation.

   When the translator gives you back the completed ``.po`` file, compile the text file to
   the binary catalog format using ``msgfmt.py``. The binary format is used by the runtime
   catalog lookup code.

5. Load and activate the appropriate message catalog at runtime.

   The final step is to add a few lines to your application to configure and load the message
   catalog and install the translation function. There are a couple of ways to do that, with
   associated trade-offs, and each is covered below.

Let's go through those steps in a little more detail, starting with the modifications you need to make to your code.

Creating Message Catalogs from Source Code
==========================================

:mod:`gettext` works by finding literal strings embedded in your program in a database of translations, and pulling out the appropriate translated string.  There are several variations of the functions for accessing the catalog, depending on whether you are working with Unicode strings or not.  The usual pattern is to bind the lookup function you want to use to the name ``_`` so that your code is not cluttered with lots of calls to functions with longer names.  

The message extraction program looks for the function ``_()`` called around a literal string to identify messages to pull out when creating the ``.pot`` file.  If you don't want to use the name ``_()``, you can tell ``pygettext.py`` to look for messages marked in another way.

Here's a simple script with a single message ready to be translated:

.. include:: gettext_example.py
    :literal:
    :start-after: #end_pymotw_header

In this case I am using the Unicode version of the lookup function, ``ugettext()``.  The text ``"This message is in the script."`` is the message to be substituted from the catalog.  I've enabled fallback mode, so if we run the script without a message catalog, the in-lined message is printed:

.. {{{cog
.. sh('rm -f PyMOTW/gettext/locale/en_US/LC_MESSAGES/gettext_example.mo')
.. cog.out(run_script(cog.inFile, 'gettext_example.py'))
.. }}}
.. {{{end}}}

The next step is to extract the message(s) and create the ``.pot`` file, using ``pygettext.py``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'pygettext.py -v -d gettext_example gettext_example.py'))
.. }}}
.. {{{end}}}

.. note: 

    The message catalog management scripts provided with the Python source distribution may
    not be installed with your binary distribution, depending on how it was packaged. If you
    do not have pygettext.py, you can find a copy in the source distribution in
    ``Tools/i18n``.

The output file produced looks like:

.. include:: gettext_example.pot
    :literal:

Message catalogs are installed into directories organized by *domain* and *language*.  The domain is usually a unique value like your application name.  In this case, I used ``gettext_example``.  The language value is provided by the user's environment at runtime, through one of the environment variables ``LANGUAGE``, ``LC_ALL``, ``LC_MESSAGES``, or ``LANG``, depending on their configuration and platform.  My language is set to ``en_US`` so that's what I'll be using in all of the examples below.

Now that we have the template, the next step is to create the required directory structure and copy the template in to the right spot.  I'm going to use the ``locale`` directory inside the PyMOTW source tree as the root of my message catalog directory, but you would typically want to use a directory accessible system-wide.  The full path to the catalog input source is ``$localedir/$language/LC_MESSAGES/$domain.po``, and the actual catalog has the filename extension ``.mo``.

For my configuration, I need to copy ``gettext_example.pot`` to ``locale/en_US/LC_MESSAGES/gettext_example.po`` and edit it to change the values in the header and add my alternate messages.  The result looks like:

.. include:: locale/en_US/LC_MESSAGES/gettext_example.po
    :literal:

The catalog is built from the ``.po`` file using ``msgformat.py``:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'msgfmt.py locale/en_US/LC_MESSAGES/gettext_example.po'))
.. }}}
.. {{{end}}}

And now when we run the script, the message from the catalog is printed instead of the in-line string:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'gettext_example.py'))
.. }}}
.. {{{end}}}


Finding Message Catalogs at Runtime
===================================

As described above, the *locale directory* containing the message catalogs is organized based on the language with catalogs named for the *domain* of the program.  Different operating systems define their own default value, but :mod:`gettext` does not know all of these defaults.  The default locale directory is ``sys.prefix + '/share/locale'``, but most of the time it is safer for you to always explicitly give a ``localedir`` value than to depend on any default behavior.

The language portion of the path is taken from one of several environment variables that can be used to configure localization features (LANGUAGE, LC_ALL, LC_MESSAGES, and LANG).  The first variable found to be set is used.  Multiple languages can be selected by separating the values with a colon (``:``).  We can illustrate how that works by creating a second message catalog and running a few experiments.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'msgfmt.py locale/en_CA/LC_MESSAGES/gettext_example.po', trailing_newlines=False))
.. cog.out(run_script(cog.inFile, 'gettext_find.py', include_prefix=False, trailing_newlines=False))
.. cog.out(run_script(cog.inFile, 'LANGUAGE=en_CA python gettext_find.py', interpreter=None, include_prefix=False, trailing_newlines=False))
.. cog.out(run_script(cog.inFile, 'LANGUAGE=en_CA:en_US python gettext_find.py', interpreter=None, include_prefix=False, trailing_newlines=False))
.. cog.out(run_script(cog.inFile, 'LANGUAGE=en_US:en_CA python gettext_find.py', interpreter=None, include_prefix=False))
.. }}}
.. {{{end}}}

Although ``find()`` shows the complete list of catalogs, only the first one in the sequence is actually loaded for message lookups.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'gettext_example.py', trailing_newlines=False))
.. cog.out(run_script(cog.inFile, 'LANGUAGE=en_CA python gettext_example.py', interpreter=None, include_prefix=False, trailing_newlines=False))
.. cog.out(run_script(cog.inFile, 'LANGUAGE=en_CA:en_US python gettext_example.py', interpreter=None, include_prefix=False, trailing_newlines=False))
.. cog.out(run_script(cog.inFile, 'LANGUAGE=en_US:en_CA python gettext_example.py', interpreter=None, include_prefix=False))
.. }}}
.. {{{end}}}


Versions of Messages
====================

While simple message substitution will handle most of your translation needs, one of the special cases handled explicitly by :mod:`gettext` is pluralization.  Depending on the language, the difference between the singular and plural forms of a message may vary only by the ending of a single word, or the entire sentence structure may be different.  There may also be `different forms depending on the level of plurality <http://www.gnu.org/software/gettext/manual/gettext.html#Plural-forms>`_.  To make managing plurals easier (and possible), there is a separate set of functions for asking for the plural form of a message.

.. include:: gettext_plural.py
    :literal:
    :start-after: #end_pymotw_header

Since the messages in this case are not wrapped in ``_()``, we need to tell ``pygettext.py`` to also look for ``ungettext`` arguments as messages.  And since ``ungettext`` takes multiple strings as arguments (singular and plural forms of default messages), we need to tell it which arguments we want it to pay attention to.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'pygettext.py --keyword ungettext:1,2 -d gettext_plural gettext_plural.py'))
.. }}}
.. {{{end}}}



- simple substitution
- handling plurals

Applying Application-wide Translation
=====================================

- using _() globally

Applying Module-level Translation
=================================

- using _() within a module

Switching Message Catalogs at Runtime
=====================================

- different messages for different users of web app

Translation and the Interactive Interpreter
===========================================

- competing definitions of _()


.. seealso::

    `gettext <http://docs.python.org/library/gettext.html>`_
        The standard library documentation for this module.

    `GNU gettext <http://www.gnu.org/software/gettext/>`_
        The message catalog formats, API, etc. for this module are all based on the original gettext package from GNU.  The catalog file formats are compatible, and the command line scripts have similar options (if not identical).  ``pygettext.py`` knows about Python syntax, but not other languages, so unless you have a mixture of source languages in your project you can probably work with just the tools included with Python.  The `GNU gettext manual <http://www.gnu.org/software/gettext/manual/gettext.html>`_ has a detailed description of the file formats and describes GNU versions of the tools for working with them.

    `Internationalizing Python <http://www.python.org/workshops/1997-10/proceedings/loewis.html>`_
        A paper by Martin von Löwis about techniques for internationalization of Python applications.