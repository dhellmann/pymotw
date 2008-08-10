==========
imp
==========
.. module:: imp
    :synopsis: Interface to module import mechanism.

:Module: imp
:Purpose: Interface to module import mechanism.
:Python Version: At least 2.2.1
:Abstract:

    The imp module exposes the implementation of Python's import statement.

Description
===========

The imp module includes functions that expose part of the underlying
implementation of Python's import mechanism for loading code in packages and
modules. It is one access point to importing modules dynamically, and useful
in some cases where you don't know the name of the module you need to import
when you write your code (e.g., for plugins or extensions to an application).

Example Package
===============

The examples below use a package called "example" with __init__.py::

    print 'Importing example package'

and module called submodule containing::

    print 'Importing submodule'

Watch for the output of the print statements in the sample output when the
package or module are imported.

Module Types
============

Python supports several styles of modules. Each requires its own handling when
opening the module and adding it to the namespace. Some of the supported types
and those parameters can be listed by the get_suffixes() function.

::

    import imp

    module_types = { imp.PY_SOURCE:   'source',
                     imp.PY_COMPILED: 'compiled',
                     imp.C_EXTENSION: 'extension',
                     imp.PY_RESOURCE: 'resource',
                     imp.PKG_DIRECTORY: 'package',
                     }

    def main():
        fmt = '%10s %10s %10s'
        print fmt % ('Extension', 'Mode', 'Type')
        print '-' * 32
        for extension, mode, module_type in imp.get_suffixes():
            print fmt % (extension, mode, module_types[module_type])

    if __name__ == '__main__':
        main()

get_suffixes() returns a sequence of tuples containing the file extension,
mode to use for opening the file, and a type code from a constant defined in
the module. This table is incomplete, because some of the importable module or
package types do not correspond to single files.

::

    $ python imp_get_suffixes.py
     Extension       Mode       Type
    --------------------------------
           .so         rb  extension
     module.so         rb  extension
           .py          U     source
          .pyc         rb   compiled

Finding Modules
===============

The first step to loading a module is finding. The find_module() function
scans the import search path looking for a package or module with the given
name. It returns an open file handle (if appropriate for the type), filename
where the module was found, and "description" (a tuple such as those returned
by get_suffixes()).

::

    import imp
    from imp_get_suffixes import module_types

    print 'Package:'
    f, filename, description = imp.find_module('example')
    print module_types[description[2]], filename
    print

    print 'Sub-module:'
    f, filename, description = imp.find_module('submodule', ['./example'])
    print module_types[description[2]], filename
    if f: f.close()

find_module() does not pay attention to dotted package names
(example.submodule), so the caller has to take care to pass the correct path
for any nested modules. That means that when importing the submodule from the
package, you need to give a path that points to the package directory for
find_module() to locate the module you're looking for. 

::

    $ python imp_find_module.py
    Package:
    package /Users/dhellmann/Documents/PyMOTW/in_progress/imp/example

    Sub-module:
    source ./example/submodule.py

If find_module() cannot locate the module, it raises an ImportError.

::

    import imp

    try:
        imp.find_module('no_such_module')
    except ImportError, err:
        print 'ImportError:', err

::

    $ python imp_find_module_error.py
    ImportError: No module named no_such_module

Loading Modules
===============

Once you have found the module, use load_module() to actually import it.
load_module() takes the full dotted path module name and the values returned
by find_module() (the open file handle, filename, and description tuple).

::

    import imp

    f, filename, description = imp.find_module('example')
    example_package = imp.load_module('example', f, filename, description)
    print 'Package:', example_package

    f, filename, description = imp.find_module('submodule', 
                                               example_package.__path__)
    try:
        submodule = imp.load_module('example.module', f, filename, description)
        print 'Sub-module:', submodule
    finally:
        f.close()

load_module() creates a new module object with the name given, loads the code
for it, and adds it to sys.modules.

::

    $ python imp_load_module.py
    Importing example package
    Package: <module 'example' from '/Users/dhellmann/Documents/PyMOTW/in_progress/imp/example/__init__.pyc'>
    Importing submodule
    Sub-module: <module 'example.module' from '/Users/dhellmann/Documents/PyMOTW/in_progress/imp/example/submodule.py'>

If you call load_module() for a module which has already been imported, the
effect is like calling reload() on the existing module object.

::

    import imp
    import sys

    for i in range(2):
        print i,
        try:
            m = sys.modules['example']
        except KeyError:
            print '(not in sys.modules)',
        else:
            print '(have in sys.modules)',
        f, filename, description = imp.find_module('example')
        example_package = imp.load_module('example', f, filename, description)

Instead of a creating a new module, the contents of the existing module are simply replaced.

::

    $ python imp_load_module_reload.py
    0 (not in sys.modules) Importing example package
    1 (have in sys.modules) Importing example package


