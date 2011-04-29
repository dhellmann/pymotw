===============================================
 functools -- Tools for Manipulating Functions
===============================================

.. module:: functools
    :synopsis: Tools for working with functions.

:Purpose: Functions that operate on other functions.
:Available In: 2.5 and later

The :mod:`functools` module provides tools for working with functions
and other callable objects, to adapt or extend them for new purposes
without completely rewriting them.

Decorators
==========

The primary tool supplied by the :mod:`functools` module is the class
:class:`partial`, which can be used to "wrap" a callable object with
default arguments. The resulting object is itself callable, and can be
treated as though it is the original function.  It takes all of the
same arguments as the original, and can be invoked with extra
positional or named arguments as well.

partial
-------

This example shows two simple :class:`partial` objects for the
function :func:`myfunc`.  Notice that :func:`show_details` prints the
:attr:`func`, :attr:`args`, and :attr:`keywords` attributes of the
partial object.

.. include:: functools_partial.py
    :literal:
    :start-after: #end_pymotw_header

At the end of the example, the first :class:`partial` created is
invoked without passing a value for *a*, causing an exception.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'functools_partial.py', ignore_error=True, break_lines_at=70))
.. }}}
.. {{{end}}}



update_wrapper
--------------

The partial object does not have :attr:`__name__` or :attr:`__doc__`
attributes by default, and without those attributes decorated
functions are more difficult to debug. Using :func:`update_wrapper`,
copies or adds attributes from the original function to the
:class:`partial` object.

.. include:: functools_update_wrapper.py
    :literal:
    :start-after: #end_pymotw_header

The attributes added to the wrapper are defined in
:const:`functools.WRAPPER_ASSIGNMENTS`, while
:const:`functools.WRAPPER_UPDATES` lists values to be modified.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'functools_update_wrapper.py', break_lines_at=70))
.. }}}
.. {{{end}}}

Other Callables
---------------

Partials work with any callable object, not just standalone functions.

.. include:: functools_method.py
    :literal:
    :start-after: #end_pymotw_header

This example creates partials from an instance, and methods of an
instance.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'functools_method.py', break_lines_at=68))
.. }}}
.. {{{end}}}


wraps
-----

Updating the properties of a wrapped callable is especially useful
when used in a decorator, since the transformed function ends up with
properties of the original, "bare", function.

.. include:: functools_wraps.py
    :literal:
    :start-after: #end_pymotw_header

:mod:`functools` provides a decorator, :func:`wraps`, which applies
:func:`update_wrapper` to the decorated function.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'functools_wraps.py'))
.. }}}
.. {{{end}}}

Comparison
==========

Under Python 2, classes can define a :func:`__cmp__` method that
returns ``-1``, ``0``, or ``1`` based on whether the object is less
than, equal to, or greater than the item being compared.  Python 2.1
introduces the *rich comparison* methods API, :func:`__lt__`,
:func:`__le__`, :func:`__eq__`, :func:`__ne__`, :func:`__gt__`, and
:func:`__ge__`, which perform a single comparison operation and return
a boolean value.  Python 3 deprecated :func:`__cmp__` in favor of
these new methods, so :mod:`functools` provides tools to make it
easier to write Python 2 classes that comply with the new comparison
requirements in Python 3.

Rich Comparison
---------------

The rich comparison API is designed to allow classes with complex
comparisons to implement each test in the most efficient way possible.
However, for classes where comparison is relatively simple, there is
no point in manually creating each of the rich comparison methods.
The :func:`total_ordering` class decorator takes a class that provides
some of the methods, and adds the rest of them.

.. include:: functools_total_ordering.py
   :literal:
   :start-after: #end_pymotw_header

The class must provide an implmentation of :func:`__eq__` and any one
of the other rich comparison methods.  The decorator adds
implementations of the other methods that work by using the
comparisons provided.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'functools_total_ordering.py'))
.. }}}
.. {{{end}}}

Collation Order
---------------

Since old-style comparison functions are deprecated in Python 3, the
:data:`cmp` argument to functions like :func:`sort` are also no longer
supported.  Python 2 programs that use comparison functions can use
:func:`cmp_to_key` to convert them to a function that returns a
*collation key*, which is used to determine the position in the final
sequence.

.. include:: functools_cmp_to_key.py
   :literal:
   :start-after: #end_pymotw_header

.. note::

  Normally :func:`cmp_to_key` would be used directly, but in this
  example an extra wrapper function is introduced to print out more
  information as the key function is being called.

The output shows that :func:`sorted` starts by calling
:func:`get_key_wrapper` for each item in the sequence to produce a
key.  The keys returned by :func:`cmp_to_key` are instances of a class
defined in :mod:`functools` that implements the rich comparison API
based on the return value of the provided old-style comparison
function.  After all of the keys are created, the sequence is sorted
by comparing the keys.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'functools_cmp_to_key.py'))
.. }}}
.. {{{end}}}



.. seealso::

    `functools <http://docs.python.org/library/functools.html>`_
        The standard library documentation for this module.
    
    `Rich comparison methods <http://docs.python.org/reference/datamodel.html#object.__lt__>`__
        Description of the rich comparison methods from the Python Reference Guide.
