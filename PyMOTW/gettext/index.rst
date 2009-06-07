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

In this case I am using the Unicode version of the lookup string, ``ugettext()``.  The text ``"This message is in the script."`` is the message to be substituted from the catalog.  If we run the script without a message catalog, the in-lined message is printed:

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

For my configuration, I need to copy ``gettext_example.pot`` to ``locale/en_US/LC_MESSAGES/gettext_example.po`` and edit it to add my alternate messages.  The result looks like:

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


- python lib tools
- gnu tools

Finding Message Catalogs at Runtime
===================================

- always use explicit directory argument, since the default looks inside sys.prefix
- building the path to the message catalog(s)

Versions of Messages
====================

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

Dealing with Plural Values
==========================

.. seealso::

    `gettext <http://docs.python.org/library/gettext.html>`_
        The standard library documentation for this module.
