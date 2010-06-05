===================================
site -- Site-specific configuration
===================================

.. module:: site
    :synopsis: Site-specific configuration

The :mod:`site` module handles site-specific configuration, especially
the :ref:`import path <sys-path>`.

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

::

	$ python -m site --user-base
	/Users/dhellmann/.local

	$ python -m site --user-site
	/Users/dhellmann/.local/lib/python2.6/site-packages

	$ PYTHONUSERBASE=/tmp/$USER python -m site --user-base
	/tmp/dhellmann

	$ PYTHONUSERBASE=/tmp/$USER python -m site --user-site
	/tmp/dhellmann/lib/python2.6/site-packages

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

::

	$ python site_enable_user_site.py
	Flag   : True
	Meaning: Enabled

	$ python -s site_enable_user_site.py
	Flag   : False
	Meaning: Disabled by command-line option

.. {{{end}}}

Path Configuration Files
========================

.. contents and processing of .pth files

As paths are added to the import path, they are also scanned for *path
configuration files*.  A path configuration file is a plain text file
with the extension ``.pth``.  Each line in the file can take one of
four forms:

1. A full or relative path to another location that should be added to
   the import path.
2. A Python statement to be executed.  All such lines must begin with
   an ``import`` statement.
3. Blank lines are ignored.
4. A line starting with ``#`` is treated as a comment and ignored.

Path configuration files can be used to extend the import path to look
in locations that would not have been added automatically.  For
example, Distribute_ adds paths to ``easy-install.pth`` when a package
is installed in "develop" mode using ``python setup.py develop``.

The function for extending ``sys.path`` is public, so we can use it in
example programs to show how the path configuration files work.  Given
a directory ``with_modules`` containing the file ``mymodule.py`` with
this ``print`` statement showing how the module was imported:

.. include:: with_modules/mymodule.py
   :literal:
   :start-after: #end_pymotw_header

This script shows how :func:`addsitedir()` extends the import path so
the interpreter can find the desired module.

.. include:: site_addsitedir.py
   :literal:
   :start-after: #end_pymotw_header

After the directory containing the module is added to ``sys.path``,
the script can import :mod:`mymodule` without issue.

.. {{{cog
.. (path(cog.inFile).dirname() / 'with_modules/mymodule.pyc').unlink()
.. cog.out(run_script(cog.inFile, 'site_addsitedir.py with_modules'))
.. }}}

::

	$ python site_addsitedir.py with_modules
	Could not import mymodule: No module named mymodule
	
	New paths:
	   /Users/dhellmann/Documents/PyMOTW/book/PyMOTW/site/with_modules
	
	Loaded mymodule from with_modules/mymodule.py

.. {{{end}}}

If the directory given to :func:`addsitedir()` includes any files
matching the pattern ``*.pth``, they are loaded as path configuration
files.  For example, if we create ``with_pth/pymotw.pth`` containing:

.. literalinclude:: with_pth/pymotw.pth

and copy ``mymodule.py`` to ``with_pth/subdir/mymodule.py``, then we
can import it by adding ``with_pth`` as a site directory, even though
the module is not in that directory.

.. {{{cog
.. (path(cog.inFile).dirname() / 'with_pth/subdir/mymodule.pyc').unlink()
.. cog.out(run_script(cog.inFile, 'site_addsitedir.py with_pth'))
.. }}}

::

	$ python site_addsitedir.py with_pth
	Could not import mymodule: No module named mymodule
	
	New paths:
	   /Users/dhellmann/Documents/PyMOTW/book/PyMOTW/site/with_pth
	   /Users/dhellmann/Documents/PyMOTW/book/PyMOTW/site/with_pth/subdir
	
	Loaded mymodule from with_pth/subdir/mymodule.py

.. {{{end}}}

If a site directory contains multiple ``.pth`` files, they are
processed in alphabetical order.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ls -F with_multiple_pth', interpreter=None))
.. cog.out(run_script(cog.inFile, 'cat with_multiple_pth/a.pth', interpreter=None, include_prefix=False))
.. cog.out(run_script(cog.inFile, 'cat with_multiple_pth/b.pth', interpreter=None, include_prefix=False))
.. }}}

::

	$ ls -F with_multiple_pth
	a.pth
	b.pth
	from_a/
	from_b/

	$ cat with_multiple_pth/a.pth
	./from_a

	$ cat with_multiple_pth/b.pth
	./from_b

.. {{{end}}}

In this case, the module is found in ``with_multiple_pth/from_a``
because ``a.pth`` is read before ``b.pth``.

.. {{{cog
.. (path(cog.inFile).dirname() / 'with_multiple_pth/from_a/mymodule.pyc').unlink()
.. cog.out(run_script(cog.inFile, 'site_addsitedir.py with_multiple_pth'))
.. }}}

::

	$ python site_addsitedir.py with_multiple_pth
	Could not import mymodule: No module named mymodule
	
	New paths:
	   /Users/dhellmann/Documents/PyMOTW/book/PyMOTW/site/with_multiple_pth
	   /Users/dhellmann/Documents/PyMOTW/book/PyMOTW/site/with_multiple_pth/from_a
	   /Users/dhellmann/Documents/PyMOTW/book/PyMOTW/site/with_multiple_pth/from_b
	
	Loaded mymodule from with_multiple_pth/from_a/mymodule.py

.. {{{end}}}


sitecustomize
=============

.. Show an example that prints something and modifies the import path
.. cd into the directory containing the sitecustomize.py before
.. running the wrapper script.  Talk about where the sitecustomize
.. file would really be written.

usercustomize
=============

.. replicate the sitecustomize example using usercustomize.py instead
.. and talk about where it can go

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
