============================================================================
platform -- Access system hardware, OS, and interpreter version information.
============================================================================

.. module:: platform
    :synopsis: Access system hardware, OS, and interpreter version information.

:Purpose: Probe the underlying platform's architecture and version information with the platform module.
:Python Version: 2.3+

Although Python is often used as a cross-platform language, it is occasionally
necessary to know what sort of system you're running on. Build tools obviously
need that information, but you might also know that some libraries or external
commands have different interfaces on different operating systems. For
example, if you are writing a tool to manage the network configuration of an
operating system, you can have a portable representation of network
interfaces, aliases, IP addresses, etc. But once you get down to actually
editing the configuration files, you need to know more about your host and how
it is configured. The platform module gives you some tools for learning about
the interpreter, operating system, and hardware platform where your program is
running.

.. note::

    The example output below was generated on a MacBook Pro running OS X 10.5.2
    and a VMware VM running CentOS 4.6. I don't have ready access to Windows, but
    these functions all work there, too. (If someone wants to run the scripts on
    Windows and post the output in the comments, I would appreciate it!)

Interpreter
===========

There are four functions for getting information about the current Python
interpreter. python_version() and python_version_tuple() return different
forms of the interpreter version with major, minor, and patchlevel components.
python_compiler() reports on the compiler used to build the interpreter. And
python_build() gives a version string for the build of the interpreter.

.. include:: platform_python.py
    :literal:
    :start-after: #end_pymotw_header


OS X::

    $ python platform_python.py
    Version      : 2.5.1
    Version tuple: ['2', '5', '1']
    Compiler     : GCC 4.0.1 (Apple Computer, Inc. build 5367)
    Build        : ('r251:54869', 'Apr 18 2007 22:08:04')


Linux::

    $ python platform_python.py 
    Version      : 2.4.4
    Version tuple: ['2', '4', '4']
    Compiler     : GCC 3.4.6 20060404 (Red Hat 3.4.6-9)
    Build        : (1, 'Mar 12 2008 15:09:04')

(It looks like I need to upgrade that system...)

Platform
========

A general purpose platform identifier is available via the platform()
function. platform() accepts two optional boolean arguments. If aliased is
True, the names in the return value are converted from a formal name to their
more common form. When terse is true, returns a minimal value with some parts
dropped.

.. include:: platform_platform.py
    :literal:
    :start-after: #end_pymotw_header

OS X::

    $ python platform_platform.py
    Normal : Darwin-9.2.2-i386-32bit
    Aliased: Darwin-9.2.2-i386-32bit
    Terse  : Darwin-9.2.2

Linux::

    $ python platform_platform.py 
    Normal : Linux-2.6.9-67.0.4.ELsmp-i686-with-redhat-4.6-Final
    Aliased: Linux-2.6.9-67.0.4.ELsmp-i686-with-redhat-4.6-Final
    Terse  : Linux-2.6.9-67.0.4.ELsmp-i686-with-glibc2.3

Operating System and Hardware Info
==================================

More detailed information about the operating system and hardware the
interpreter is running under can be retrieved as well. uname() returns a tuple
containing the system, node, release, version, machine, and processor values.
Individual values can be accessed through functions of the same names:

system() returns the operating system name. node() returns the hostname of the
server, not fully qualified. release() returns the operating system release
number. version() returns the more detailed system version. machine() gives a
hardware-type identifier such as 'i386'. processor() returns a real identifier
for the processor, or the same value as machine() in many cases.

.. include:: platform_os_info.py
    :literal:
    :start-after: #end_pymotw_header


OS X::

    $ python platform_os_info.py
    uname: ('Darwin', 'farnsworth.local', '9.2.2', 'Darwin Kernel Version 9.2.2: Tue Mar  4 21:17:34 PST 2008; root:xnu-1228.4.31~1/RELEASE_I386', 'i386', 'i386')

    system   : Darwin
    node     : farnsworth.local
    release  : 9.2.2
    version  : Darwin Kernel Version 9.2.2: Tue Mar  4 21:17:34 PST 2008; root:xnu-1228.4.31~1/RELEASE_I386
    machine  : i386
    processor: i386

Linux::

    $ python platform_os_info.py 
    uname: ('Linux', 'zoidberg', '2.6.9-67.0.4.ELsmp', '#1 SMP Sun Feb 3 07:08:57 EST 2008', 'i686', 'i686')

    system   : Linux
    node     : zoidberg
    release  : 2.6.9-67.0.4.ELsmp
    version  : #1 SMP Sun Feb 3 07:08:57 EST 2008
    machine  : i686
    processor: i686


Executable Architecture
=======================

Individual program architecture information can be probed using the
architecture() function. The first argument is the path to an executable
program (defaulting to sys.executable, the Python interpreter). The return
value is a tuple containing the bit architecture and the linkage format used.

.. include:: platform_architecture.py
    :literal:
    :start-after: #end_pymotw_header


OS X::

    $ python platform_architecture.py
    interpreter: ('32bit', '')
    /bin/ls    : ('32bit', '')

Linux::

    $ python platform_architecture.py 
    interpreter: ('32bit', 'ELF')
    /bin/ls    : ('32bit', 'ELF')


.. seealso::

    `platform <http://docs.python.org/lib/module-platform.html>`_
        Standard library documentation for this module.
