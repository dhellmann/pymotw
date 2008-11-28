===========================================================
os.path -- Platform-independent manipulation of file names.
===========================================================

.. module:: os.path
    :synopsis: Platform-independent manipulation of file names.

:Purpose: Parse, build, test, and otherwise work on file names and paths.
:Python Version: 1.4 and later

Writing code to work with files on multiple platforms is easy using the
functions included in the os.path module. Even programs not intended to be
ported between platforms should use os.path to make parsing path names
reliable.

Parsing Paths
=============

The first set of functions in os.path can be used to parse strings
representing filenames into their component parts. It is important to realize
that these functions do not depend on the paths actually existing. They
operate solely on the strings.

Path parsing depends on a few variable defined in the os module:

* os.sep - The separator between portions of the path (e.g., "/").

* os.extsep - The separator between a filename and the file "extension" (e.g.,
  ".").

* os.pardir - The path component that means traverse the directory tree up one
  level (e.g., "..").

* os.curdir - The path component that refers to the current directory (e.g.,
  ".").

* split() breaks the path into 2 separate parts and returns the tuple. The
  second element is the last component of the path, and the first element is
  everything that comes before it.

.. include:: ospath_split.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python ospath_split.py
    "/one/two/three" : "('/one/two', 'three')"
    "/one/two/three/" : "('/one/two/three', '')"
    "/" : "('/', '')"
    "." : "('', '.')"
    "" : "('', '')"

basename() returns a value equivalent to the second part of the split() value.

.. include:: ospath_basename.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python ospath_basename.py
    "/one/two/three" : "three"
    "/one/two/three/" : ""
    "/" : ""
    "." : "."
    "" : ""

dirname() returns the first path of the split path:

.. include:: ospath_dirname.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python ospath_dirname.py
    "/one/two/three" : "/one/two"
    "/one/two/three/" : "/one/two/three"
    "/" : "/"
    "." : ""
    "" : ""

splitext() works like split() but divides the path on the extension separator,
rather than the directory names.

.. include:: ospath_splitext.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python ospath_splitext.py
    "filename.txt" : ('filename', '.txt')
    "filename" : ('filename', '')
    "/path/to/filename.txt" : ('/path/to/filename', '.txt')
    "/" : ('/', '')
    "" : ('', '')

commonprefix() takes a list of paths as an argument and returns a single
string that represents a common prefix present in all of the paths. The value
may represent a path that does not actually exist, and the path separator is
not included in the consideration, so the prefix might not stop on a separator
boundary.

.. include:: ospath_commonprefix.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python ospath_commonprefix.py
    ['/one/two/three/four', '/one/two/threefold', '/one/two/three/']
    /one/two/three

Building Paths
==============

Besides taking existing paths apart, you will frequently need to build paths
from other strings.

To combine several path components into a single value, use join():

.. include:: ospath_join.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python ospath_join.py
    ('one', 'two', 'three') : one/two/three
    ('/', 'one', 'two', 'three') : /one/two/three
    ('/one', '/two', '/three') : /three

It's also easy to work with paths that include "variable" components that can
be expanded automatically. For example, expanduser() converts the tilde (~)
character to a user's home directory.

.. include:: ospath_expanduser.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python ospath_expanduser.py
    ~ : /Users/dhellmann
    ~dhellmann : /Users/dhellmann
    ~postgres : /var/empty

expandvars() is more general, and expands any shell environment variables
present in the path.

.. include:: ospath_expandvars.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python ospath_expandvars.py
    /path/to/VALUE

Normalizing Paths
=================

Paths assembled from separate strings using join() or with embedded variables
might end up with extra separators or relative path components. Use normpath()
to clean them up:

.. include:: ospath_normpath.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python ospath_normpath.py
    one//two//three : one/two/three
    one/./two/./three : one/two/three
    one/../one/two/three : one/two/three

To convert a relative path to a complete absolute filename, use abspath().

.. include:: ospath_abspath.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python ospath_abspath.py
    "." : "/Users/dhellmann/Documents/PyMOTW/in_progress/ospath"
    ".." : "/Users/dhellmann/Documents/PyMOTW/in_progress"
    "./one/two/three" : "/Users/dhellmann/Documents/PyMOTW/in_progress/ospath/one/two/three"
    "../one/two/three" : "/Users/dhellmann/Documents/PyMOTW/in_progress/one/two/three"

File Times
==========

Besides working with paths, os.path also includes some functions for
retrieving file properties, which can be more convenient than calling
os.stat():

.. include:: ospath_properties.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python ospath_properties.py
    File         : /Users/dhellmann/Documents/PyMOTW/in_progress/ospath/ospath_properties.py
    Access time  : Sun Jan 27 15:40:20 2008
    Modified time: Sun Jan 27 15:39:06 2008
    Change time  : Sun Jan 27 15:39:06 2008
    Size         : 478

Testing Files
=============

When your program encounters a path name, it often needs to know whether the
path refers to a file or directory. If you are working on a platform that
supports it, you may need to know if the path refers to a symbolic link or
mount point. You will also want to test whether the path exists or not.
os.path provides functions to test all of these conditions.

.. include:: ospath_tests.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ ln -s /does/not/exist broken_link
    $ python ospath_tests.py
    File        : /Users/dhellmann/Documents/PyMOTW/in_progress/ospath/ospath_tests.py
    Absolute    : True
    Is File?    : True
    Is Dir?     : False
    Is Link?    : False
    Mountpoint? : False
    Exists?     : True
    Link Exists?: True

    File        : /Users/dhellmann/Documents/PyMOTW/in_progress/ospath
    Absolute    : True
    Is File?    : False
    Is Dir?     : True
    Is Link?    : False
    Mountpoint? : False
    Exists?     : True
    Link Exists?: True

    File        : /
    Absolute    : True
    Is File?    : False
    Is Dir?     : True
    Is Link?    : False
    Mountpoint? : True
    Exists?     : True
    Link Exists?: True

    File        : ./broken_link
    Absolute    : False
    Is File?    : False
    Is Dir?     : False
    Is Link?    : True
    Mountpoint? : False
    Exists?     : False
    Link Exists?: True

Traversing a Directory Tree
===========================

os.path.walk() traverses all of the directories in a tree and calls a function
you provide passing the directory name and the names of the contents of that
directory. This example produces a recursive directory listing, ignoring .svn
directories.

.. include:: ospath_walk.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python ospath_walk.py
    .. (User data)
      .svn/
      ospath/

    ../ospath (User data)
      .svn/
      __init__.py
      ospath_abspath.py
      ospath_basename.py
      ospath_commonprefix.py
      ospath_dirname.py
      ospath_expanduser.py
      ospath_expandvars.py
      ospath_join.py
      ospath_normpath.py
      ospath_properties.py
      ospath_split.py
      ospath_splitext.py
      ospath_tests.py
      ospath_walk.py

.. seealso::

    `os.path <http://docs.python.org/lib/module-os.path.html>`_
        Standard library documentation for this module.

    :mod:`os`
        The os module is a parent of os.path.

