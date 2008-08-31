======
shutil
======
.. module:: shutil
    :synopsis: High-level file operations.

:Module: shutil
:Purpose: High-level file operations.
:Python Version: 1.4
:Abstract:

    The shutil module includes high-level file operations such as copying,
    setting permissions, etc.

Description
===========

The shutil module provides several functions for copying and removing entire
files.

Copying Files
=============

copyfile() copies the contents of the source to the destination. Raises
IOError if you do not have permission to write to the destination file.
Because the function opens the input file for reading, regardless of its type,
special files cannot be copied as new special files with copyfile().

::

    import os
    from shutil import *

    print 'BEFORE:', os.listdir(os.getcwd())
    copyfile('shutil_copyfile.py', 'shutil_copyfile.py.copy')
    print 'AFTER:', os.listdir(os.getcwd())

::

    $ python shutil_copyfile.py 
    BEFORE: ['__init__.py', 'shutil_copyfile.py']
    AFTER: ['__init__.py', 'shutil_copyfile.py', 'shutil_copyfile.py.copy']


copyfile() is written using the lower-level function copyfileobj(). While the
arguments to copyfile() are file names, the arguments to copyfileobj() are
open file handles. The optional third argument is a buffer length to use for
reading in chunks (by default, the entire file is read at one time).

::

    import os
    from StringIO import StringIO
    import sys
    from shutil import *

    class VerboseStringIO(StringIO):
        def read(self, n=-1):
            next = StringIO.read(self, n)
            print 'read(%d) =>' % n, next
            return next

    lorem_ipsum = '''Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 
    Vestibulum aliquam mollis dolor. Donec vulputate nunc ut diam. 
    Ut rutrum mi vel sem. Vestibulum ante ipsum.'''

    print 'Default:'
    input = VerboseStringIO(lorem_ipsum)
    output = StringIO()
    copyfileobj(input, output)

    print

    print 'All at once:'
    input = VerboseStringIO(lorem_ipsum)
    output = StringIO()
    copyfileobj(input, output, -1)

    print

    print 'Blocks of 20:'
    input = VerboseStringIO(lorem_ipsum)
    output = StringIO()
    copyfileobj(input, output, 20)

The default behavior is to read using large blocks:

::

    $ python shutil_copyfileobj.py
    Default:
    read(16384) => Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 
    Vestibulum aliquam mollis dolor. Donec vulputate nunc ut diam. 
    Ut rutrum mi vel sem. Vestibulum ante ipsum.
    read(16384) => 

Use -1 to read all of the input at one time:

::

    All at once:
    read(-1) => Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 
    Vestibulum aliquam mollis dolor. Donec vulputate nunc ut diam. 
    Ut rutrum mi vel sem. Vestibulum ante ipsum.
    read(-1) => 

Or use another positive integer to set your own block size:

::

    Blocks of 20:
    read(20) => Lorem ipsum dolor si
    read(20) => t amet, consectetuer
    read(20) =>  adipiscing elit. 
    V
    read(20) => estibulum aliquam mo
    read(20) => llis dolor. Donec vu
    read(20) => lputate nunc ut diam
    read(20) => . 
    Ut rutrum mi vel 
    read(20) => sem. Vestibulum ante
    read(20) =>  ipsum.
    read(20) => 

The copy() function works like the Unix command line tool cp. If the named
destination refers to a directory instead of a file, a new file is created in
the directory using the base name of the source. The permissions of the file
are copied along with the contents.

::

    import os
    from shutil import *

    os.mkdir('example')
    print 'BEFORE:', os.listdir('example')
    copy('shutil_copy.py', 'example')
    print 'AFTER:', os.listdir('example')

::

    $ python shutil_copy.py
    BEFORE: []
    AFTER: ['shutil_copy.py']


copy2() works like copy(), but includes the access and modification times in
the meta-data copied to the new file.

::

    import os
    from shutil import *

    def show_file_info(filename):
        stat_info = os.stat(filename)
        print '\tMode    :', stat_info.st_mode
        print '\tCreated :', time.ctime(stat_info.st_ctime)
        print '\tAccessed:', time.ctime(stat_info.st_atime)
        print '\tModified:', time.ctime(stat_info.st_mtime)

    os.mkdir('example')
    print 'SOURCE:'
    show_file_info('shutil_copy2.py')
    copy2('shutil_copy2.py', 'example')
    print 'DEST:'
    show_file_info('example/shutil_copy2.py')

::

    $ python shutil_copy2.py
    SOURCE:
            Mode    : 33188
            Created : Sun Oct 21 15:16:07 2007
            Accessed: Sun Oct 21 15:16:11 2007
            Modified: Sun Oct 21 15:16:07 2007
    DEST:
            Mode    : 33188
            Created : Sun Oct 21 15:16:11 2007
            Accessed: Sun Oct 21 15:16:11 2007
            Modified: Sun Oct 21 15:16:07 2007


Copying File Meta-data
======================

By default when a new file is created under Unix, it receives permissions based
on the umask of the current user. To copy the permissions from one file to
another, use copymode().

::

    from commands import *
    from shutil import *

    print 'BEFORE:', getstatus('file_to_change.txt')
    copymode('shutil_copymode.py', 'file_to_change.txt')
    print 'AFTER :', getstatus('file_to_change.txt')

First, I need to create a file to be modified:

::

    $ touch file_to_change.txt
    $ chmod ugo+w file_to_change.txt

Then running the example script will change the permissions.

::

    $ python shutil_copymode.py
    BEFORE: -rw-rw-rw-   1 dhellman  dhellman  0 Oct 21 14:43 file_to_change.txt
    AFTER : -rw-r--r--   1 dhellman  dhellman  0 Oct 21 14:43 file_to_change.txt

To copy other meta-data about the file (permissions, last access time, and last
modified time), use copystat().

::

    import os
    from shutil import *
    import time

    def show_file_info(filename):
        stat_info = os.stat(filename)
        print '\tMode    :', stat_info.st_mode
        print '\tCreated :', time.ctime(stat_info.st_ctime)
        print '\tAccessed:', time.ctime(stat_info.st_atime)
        print '\tModified:', time.ctime(stat_info.st_mtime)

    print 'BEFORE:'
    show_file_info('file_to_change.txt')
    copystat('shutil_copystat.py', 'file_to_change.txt')
    print 'AFTER :'
    show_file_info('file_to_change.txt')

::

    $ python shutil_copystat.py
    BEFORE:
            Mode    : 33206
            Created : Sun Oct 21 15:01:23 2007
            Accessed: Sun Oct 21 14:43:26 2007
            Modified: Sun Oct 21 14:43:26 2007
    AFTER :
            Mode    : 33188
            Created : Sun Oct 21 15:01:44 2007
            Accessed: Sun Oct 21 15:01:43 2007
            Modified: Sun Oct 21 15:01:39 2007

Working With Directory Trees
============================

The shutil module includes 3 functions for working with directory trees. To
copy a directory from one place to another, use copytree(). It recurses through
the source directory tree, copying files to the destination. The destination
directory must not exist in advance. The symlinks argument controls whether
symbolic links are copied as links or as files. The default is to copy the
contents to new files. If the option is true, new symlinks are created within
the destination tree.

Note: The documentation for copytree() says it should be considered a sample
implementation, rather than a tool. You may want to copy the implementation and
make it more robust, or add features like a progress meter.

::

    from commands import *
    from shutil import *

    print 'BEFORE:'
    print getoutput('ls -rlast /tmp/example')
    copytree('example', '/tmp/example')
    print 'AFTER:'
    print getoutput('ls -rlast /tmp/example')

::

    $ python shutil_copytree.py
    BEFORE:
    ls: /tmp/example: No such file or directory
    AFTER:
    total 8
    8 -rw-r--r--    1 dhellman  wheel  1627 Oct 21 15:16 shutil_copy2.py
    0 drwxr-xr-x    3 dhellman  wheel   102 Oct 21 15:16 .
    0 drwxrwxrwt   18 root      wheel   612 Oct 21 15:26 ..

To remove a directory and its contents, use rmtree(). Errors are raised as
exceptions by default. Errors can be ignored if the second argument is tree,
and a special error handler function can be provided in the third argument.

::

    from commands import *
    from shutil import *

    print 'BEFORE:'
    print getoutput('ls -rlast /tmp/example')
    rmtree('example', '/tmp/example')
    print 'AFTER:'
    print getoutput('ls -rlast /tmp/example')

::

    $ python shutil_rmtree.py
    BEFORE:
    total 8
    8 -rw-r--r--    1 dhellman  wheel  1627 Oct 21 15:16 shutil_copy2.py
    0 drwxr-xr-x    3 dhellman  wheel   102 Oct 21 15:16 .
    0 drwxrwxrwt   18 root      wheel   612 Oct 21 15:26 ..
    AFTER:
    ls: /tmp/example: No such file or directory

To move a file or directory from one place to another, use move(). The
semantics are similar to those of the Unix command mv. If the source and
destination are within the same filesystem, the source is simply renamed.
Otherwise the source is copied to the destination and then the source is
removed.

::

    import os
    from shutil import *

    print 'BEFORE: example : ', os.listdir('example')
    move('example', 'example2')
    print 'AFTER : example2: ', os.listdir('example2')

::

    $ python shutil_move.py
    BEFORE: example :  ['shutil_copy.py']
    AFTER : example2:  ['shutil_copy.py']


