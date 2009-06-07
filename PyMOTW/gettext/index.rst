===========================
gettext -- Message Catalogs
===========================

.. module:: gettext
    :synopsis: Message Catalogs

:Purpose: Message catalog API for internationalization.
:Python Version: 2.1.3 and later

Translation Workflow
====================

- mark up the code
- extract the messages
- translate the messages
- "compile" the message catalog(s)
- translate messages as they are used in the app

Creating Message Catalogs from Source Code
==========================================

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



.. seealso::

    `gettext <http://docs.python.org/library/gettext.html>`_
        The standard library documentation for this module.
