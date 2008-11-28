========================================
pkgutil -- Extend the module search path
========================================

.. module:: pkgutil
    :synopsis: Extend the module search path

:Purpose: Add to the module search path for a specific package to combine separate directories into a single package.
:Python Version: 2.3 and later

The pkgutil module provides a single function, extend_path(), that is used to
modify the search path for modules in a given package to include other
directories in sys.path. This is very useful for overriding installed versions
of packages with development versions, or for combining os-specific and shared
modules into a single package namespace.

The most common way to call extend_path() is by adding these two lines to the
__init__.py inside the package::

    import pkgutil
    __path__ = pkgutil.extend_path(__path__, __name__)

extend_path() returns a new module search path for the package that includes
paths from sys.path that include a subdirectory with the package name. An
example will make that more clear. Set up a package called demopkg1 with empty
files::

    $ find demopkg1 -name '*.py'
    demopkg1/__init__.py
    demopkg1/shared.py

Now create a directory structure like::

    $ find extension -name '*.py'
    extension/__init__.py
    extension/demopkg1/__init__.py
    extension/demopkg1/not_shared.py

All of the files can be empty.

Now go back to demopkg1/__init__.py and edit it to contain:

.. include:: demopkg1/__init__.py
    :literal:
    :start-after: #end_pymotw_header

This shows what the search path is before and after it is modified, to
illustrate the difference.

Now a simple test program to import the package:

.. include:: pkgutil_extend_path.py
    :literal:
    :start-after: #end_pymotw_header

When this test program is run directly from the command line, the not_shared
module is not found. 

::

    $ python pkgutil_extend_path.py
    demopkg1.__path__ before:
    ['/Users/dhellmann/Documents/PyMOTW/in_progress/pkgutil/demopkg1']

    demopkg1.__path__ after:
    ['/Users/dhellmann/Documents/PyMOTW/in_progress/pkgutil/demopkg1']

    demopkg1: /Users/dhellmann/Documents/PyMOTW/in_progress/pkgutil/demopkg1/__init__.pyc
    demopkg1.shared: /Users/dhellmann/Documents/PyMOTW/in_progress/pkgutil/demopkg1/shared.pyc
    demopkg1.not_shared: Not found (No module named not_shared)

However, if we add "extension" to the PYTHONPATH and run it again, we see
different results::

    $ export PYTHONPATH=extension
    $ python pkgutil_extend_path.py
    demopkg1.__path__ before:
    ['/Users/dhellmann/Documents/PyMOTW/in_progress/pkgutil/demopkg1']

    demopkg1.__path__ after:
    ['/Users/dhellmann/Documents/PyMOTW/in_progress/pkgutil/demopkg1',
     '/Users/dhellmann/Documents/PyMOTW/in_progress/pkgutil/extension/demopkg1']

    demopkg1: /Users/dhellmann/Documents/PyMOTW/in_progress/pkgutil/demopkg1/__init__.pyc
    demopkg1.shared: /Users/dhellmann/Documents/PyMOTW/in_progress/pkgutil/demopkg1/shared.pyc
    demopkg1.not_shared: /Users/dhellmann/Documents/PyMOTW/in_progress/pkgutil/extension/demopkg1/not_shared.py

The version of demopkg1 inside the extension directory has been added to the
search path, so the not_shared module is found there.

Extending the path in this manner is useful for combining os-specific versions
of packages with common packages, especially if the os-specific versions
include C extension modules.

Developing with pkgutil
=======================

As I develop enhancements to my own projects, I commonly find that I need to
test changes to an installed package. I don't want to replace the installed
copy with my development version, since it is not necessarily correct (yet)
and other tools on my system may depend on the installed package. I could
configure a completely separate copy of the package in a development
environment using something like `virtualenv`_, but if I just need to modify one
file that could be overkill. Another option is to use pkgutil to modify the
module search path for modules that belong to the package I'm working on. In
this case, however, I need to reverse the path, since I want the development
version to override the installed version.

Suppose the package looks like this::

    $ find demopkg2 -name '*.py'
    demopkg2/__init__.py
    demopkg2/overloaded.py

The function I'm working on is in demopkg2/overloaded.py. The installed
version looks like:

.. include:: demopkg2/overloaded.py
    :literal:
    :start-after: #end_pymotw_header

And demopkg2/__init__.py contains:

.. include:: demopkg2/__init__.py
    :literal:
    :start-after: #end_pymotw_header

Note the use of reverse() there to ensure that any directories added to the
search path are scanned before the default location.

With another simple test program, I can run the function:

.. include:: pkgutil_devel.py
    :literal:
    :start-after: #end_pymotw_header

First, without any special path treatment::

    $ python pkgutil_devel.py
    demopkg2: /Users/dhellmann/Documents/PyMOTW/in_progress/pkgutil/demopkg2/__init__.py
    demopkg2.overloaded: /Users/dhellmann/Documents/PyMOTW/in_progress/pkgutil/demopkg2/overloaded.py

This is the installed version of func().

And now I can set up a development directory like this::

    $ find develop -name '*.py'
    develop/demopkg2/__init__.py
    develop/demopkg2/overloaded.py

And replace the overloaded module contents:

.. include:: develop/demopkg2/overloaded.py
    :literal:
    :start-after: #end_pymotw_header

Now, when the test program is run with the develop directory in the search
path, the overloaded module from the development directory is found and used.

::

    $ export PYTHONPATH=develop 
    $ python pkgutil_devel.py

    demopkg2: /Users/dhellmann/Documents/PyMOTW/in_progress/pkgutil/demopkg2/__init__.pyc
    demopkg2.overloaded: /Users/dhellmann/Documents/PyMOTW/in_progress/pkgutil/develop/demopkg2/overloaded.pyc

This is the development version of func().

Using .pkg files
================

The first example illustrated how to extend the search path using extra
directories included in the PYTHONPATH. It is also possible to add to the
search path using ``*.pkg`` files containing directory names. PKG files are
similar to the PTH files used by the site module. They can contain directory
names, one per line, to be added to the search path for the package.

Another way to structure the os-specific portions of the application from the
first example is to have a directory for each operating system, and use a .pkg
file to extend the search path.

This example uses the same demopkg1 files, and also includes the following
files::

    $ find os_* -type f
    os_one/demopkg1/__init__.py
    os_one/demopkg1/not_shared.py
    os_one/demopkg1.pkg
    os_two/demopkg1/__init__.py
    os_two/demopkg1/not_shared.py
    os_two/demopkg1.pkg

The PKG files are named demopkg1.pkg to match the package we are extending.
They both contain::

    demopkg

This demo program shows the version of the module being imported:

.. include:: pkgutil_os_specific.py
    :literal:
    :start-after: #end_pymotw_header

A simple run script can be used to switch between the two packages:

.. include:: with_os.sh
    :literal:
    :start-after: #end_pymotw_header

And when run with "one" or "two" as the arguments, the path is adjusted
appropriately:

::

    $ ./with_os.sh one
    PYTHONPATH=os_one

    demopkg1.__path__ before:
    ['/Users/dhellmann/Documents/PyMOTW/in_progress/pkgutil/demopkg1']

    demopkg1.__path__ after:
    ['/Users/dhellmann/Documents/PyMOTW/in_progress/pkgutil/demopkg1',
     '/Users/dhellmann/Documents/PyMOTW/in_progress/pkgutil/os_one/demopkg1',
     'demopkg']

    demopkg1: /Users/dhellmann/Documents/PyMOTW/in_progress/pkgutil/demopkg1/__init__.pyc
    demopkg1.shared: /Users/dhellmann/Documents/PyMOTW/in_progress/pkgutil/demopkg1/shared.pyc
    demopkg1.not_shared: /Users/dhellmann/Documents/PyMOTW/in_progress/pkgutil/os_one/demopkg1/not_shared.pyc

::

    $ ./with_os.sh two
    PYTHONPATH=os_two

    demopkg1.__path__ before:
    ['/Users/dhellmann/Documents/PyMOTW/in_progress/pkgutil/demopkg1']

    demopkg1.__path__ after:
    ['/Users/dhellmann/Documents/PyMOTW/in_progress/pkgutil/demopkg1',
     '/Users/dhellmann/Documents/PyMOTW/in_progress/pkgutil/os_two/demopkg1',
     'demopkg']

    demopkg1: /Users/dhellmann/Documents/PyMOTW/in_progress/pkgutil/demopkg1/__init__.pyc
    demopkg1.shared: /Users/dhellmann/Documents/PyMOTW/in_progress/pkgutil/demopkg1/shared.pyc
    demopkg1.not_shared: /Users/dhellmann/Documents/PyMOTW/in_progress/pkgutil/os_two/demopkg1/not_shared.pyc

Of course, PKG files can appear anywhere in the normal search path, so a
single PKG file in the current working directory could also be used to include
a development tree.

Nested Packages
===============

For nested packages, it is only necessary to modify the path of the top-level
package. For example, with a directory structure like::

    $ find nested -name '*.py'
    nested/__init__.py
    nested/second/__init__.py
    nested/second/deep.py
    nested/shallow.py

Where nested/__init__.py contains:

.. include:: nested/__init__.py
    :literal:
    :start-after: #end_pymotw_header

And a development tree like::

    $ find develop/nested -name '*.py'
    develop/nested/__init__.py
    develop/nested/second/__init__.py
    develop/nested/second/deep.py
    develop/nested/shallow.py

Both the shallow and deep modules contain a simple function to print out a
message indicating whether or not they come from the installed or development
version.

Again, we need a simple test program:

.. include:: pkgutil_nested.py
    :literal:
    :start-after: #end_pymotw_header

When pkgutil_nested.py is run without any special path considerations, we see
the installed version of both modules::

    $ python pkgutil_nested.py
    nested.shallow: /Users/dhellmann/Documents/PyMOTW/in_progress/pkgutil/nested/shallow.pyc
    This func() comes from the installed version of nested.shallow

    nested.second.deep: /Users/dhellmann/Documents/PyMOTW/in_progress/pkgutil/nested/second/deep.pyc
    This func() comes from the installed version of nested.second.deep

And when the develop directory is added to the path, we see the development
version of both functions::

    $ PYTHONPATH=develop python pkgutil_nested.py 
    nested.shallow: /Users/dhellmann/Documents/PyMOTW/in_progress/pkgutil/develop/nested/shallow.pyc
    This func() comes from the development version of nested.shallow

    nested.second.deep: /Users/dhellmann/Documents/PyMOTW/in_progress/pkgutil/develop/nested/second/deep.pyc
    This func() comes from the development version of nested.second.deep


.. seealso::

    `pkgutil <http://docs.python.org/lib/module-pkgutil.html>`_
        Standard library documentation for this module.

    `virtualenv`_
        Ian Bicking's virtual environment script.

.. _virtualenv: http://pypi.python.org/pypi/virtualenv