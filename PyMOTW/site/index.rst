===================================
site -- Site-specific configuration
===================================

.. module:: site
    :synopsis: Site-specific configuration

The :mod:`site` module handles site-specific configuration, especially
:ref:`the import path <sys-path>`.

Import Path
===========

:mod:`site` is automatically imported each time the interpreter starts
up.  On import, it extends :ref:`sys.path <sys-path>` with
site-specific paths constructed by combining the prefix values
:ref:`sys.prefix <sys-prefix>` and :ref:`sys.exec_prefix <sys-prefix>`
with several suffixes.  Under Windows, the suffixes are an empty
string and ``lib/site-packages``.  For Unix-like platforms, the values
are ``lib/python$version/site-packages`` and ``lib/site-python``.

.. include:: site_import_path.py
   :literal:
   :start-after: #end_pymotw_header

Each of the paths resulting from the combinations is tested, and those
that exist are added to :ref:`sys.path <sys-path>`.

::
    
    $ python site_import_path.py 
    Path prefixes:
       sys.prefix     : /Library/Frameworks/Python.framework/Versions/2.6
       sys.exec_prefix: /Library/Frameworks/Python.framework/Versions/2.6
    
    /Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/site-packages
       exists: True
      in path: True
    /Library/Frameworks/Python.framework/Versions/2.6/lib/site-python
       exists: False
      in path: False

User Directories
================

In addition to the global site-packages paths, :mod:`site` is
responsible for adding the user-specific locations to the import path.
The user-specific paths are all based on the ``USER_BASE`` directory,
usually located in a part of the filesystem that is owned (and
writable) by the current user.  The path can be set through the
``PYTHONUSERBASE`` environment variable, and has platform-specific
defaults (``~/Python$version/site-packages`` for Windows and
``~/.local`` for non-Windows).

You can check the ``USER_BASE`` value by running :mod:`site` from the
command line.  :mod:`site` will give you the name of the directory
whether or not it exists, but it is only added to the import path when
it does.

.. {{{cog
.. cog.out(run_script(cog.inFile, '-m site --user-base'))
.. cog.out(run_script(cog.inFile, '-m site --user-site', include_prefix=False))
.. cog.out(run_script(cog.inFile, 'PYTHONUSERBASE=/tmp/$USER python -m site --user-base', interpreter=None, include_prefix=False))
.. cog.out(run_script(cog.inFile, 'PYTHONUSERBASE=/tmp/$USER python -m site --user-site', interpreter=None, include_prefix=False))
.. }}}
.. {{{end}}}

The user directory is disabled under some circumstances that would
pose security issues.  For example, if the process is running with a
different effective user or group id than the actual user that started
it.  Your application can check the setting by examining
``ENABLE_USER_SITE``.

.. include:: site_enable_user_site.py
   :literal:
   :start-after: #end_pymotw_header

The user directory can also be explicitly disabled on the command line
with :option:`-s`.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'site_enable_user_site.py'))
.. cog.out(run_script(cog.inFile, '-s site_enable_user_site.py', include_prefix=False))
.. }}}
.. {{{end}}}

Extending the Import Path from Your Code
========================================

.. using addsitedir()

Path Configuration Files
========================

.. contents and processing of .pth files

Flags and Constants
===================

.. the values defined in the module and how they change based on settings

Disabling site
==============

To maintain backwards-compatibility with versions of Python from
before the automatic import was added, the interpreter accepts an
:option:`-S` option.

::

    $ python -S site_import_path.py 
    Path prefixes:
       sys.prefix     : /Library/Frameworks/Python.framework/Versions/2.6
       sys.exec_prefix: /Library/Frameworks/Python.framework/Versions/2.6
    
    /Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/site-packages
       exists: True
      in path: False
    /Library/Frameworks/Python.framework/Versions/2.6/lib/site-python
       exists: False
      in path: False

.. seealso::

    `site <http://docs.python.org/library/site.html>`_
        The standard library documentation for this module.

    :ref:`sys-imports`
        Discussion from :mod:`sys` about how the import path works.
