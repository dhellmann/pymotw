=====================================================================
functools -- Tools for making decorators and other function wrappers.
=====================================================================

.. module:: functools
    :synopsis: Tools for making decorators and other function wrappers.

:Purpose: 
    The functools module includes tools for wrapping functions and other
    callable objects.
:Python Version: new in 2.5

The primary tool supplied by the functools module is the class partial, which
can be used to "wrap" a callable with default arguments. The resulting object
is itself callable and can be treated as though it is the original function.
It takes all of the same arguments as the original callable and can be invoked
with extra positional or named arguments as well.

partial
=======

This example shows two simple partial objects for the function myfunc().
Notice that show_details() prints the func, args, and keywords attributes of
the partial object.

.. include:: functools_partial.py
    :literal:
    :start-after: #end_pymotw_header

At the end of the example, the first partial created is invoked without
passing a value for a, causing an exception.

::

	$ python functools_partial.py
	myfunc:
		object: <function myfunc at 0x822b0>
		__name__: myfunc
		__doc__ 'Docstring for myfunc().'
		called myfunc with: ('a', 3)
	
	partial with named default:
		object: <functools.partial object at 0x880f0>
		__doc__ 'partial(func, *args, **keywords) - new function with partial application\n\tof the given arguments and keywords.\n'
		func: <function myfunc at 0x822b0>
		args: ()
		keywords: {'b': 4}
		called myfunc with: ('default a', 4)
		called myfunc with: ('override b', 5)
	
	partial with defaults:
		object: <functools.partial object at 0x88120>
		__doc__ 'partial(func, *args, **keywords) - new function with partial application\n\tof the given arguments and keywords.\n'
		func: <function myfunc at 0x822b0>
		args: ('default a',)
		keywords: {'b': 99}
		called myfunc with: ('default a', 99)
		called myfunc with: ('default a', 'override b')
	
	Insufficient arguments:
	Traceback (most recent call last):
	  File "functools_partial.py", line 49, in <module>
	    p1()
	TypeError: myfunc() takes at least 1 non-keyword argument (0 given)


update_wrapper
==============

As illustrated in the previous example, the partial object does not have a
__name__ or __doc__ attributes by default. Losing those attributes for
decorated functions makes them more difficult to debug. By using
update_wrapper, you can copy or add attributes from the original function to
the partial object.

.. include:: functools_update_wrapper.py
    :literal:
    :start-after: #end_pymotw_header

The attributes added to the wrapper are defined in
functools.WRAPPER_ASSIGNMENTS, while functools.WRAPPER_UPDATES lists values to
be modified.

::

	$ python functools_update_wrapper.py
	myfunc:
		object: <function myfunc at 0x82230>
		__name__: myfunc
		__doc__ 'Docstring for myfunc().'
	
	raw wrapper:
		object: <functools.partial object at 0x7bfc0>
		__name__: (no __name__)
		__doc__ 'partial(func, *args, **keywords) - new function with partial application\n\tof the given arguments and keywords.\n'
	
	Updating wrapper:
		assign: ('__module__', '__name__', '__doc__')
		update: ('__dict__',)
	
	updated wrapper:
		object: <functools.partial object at 0x7bfc0>
		__name__: myfunc
		__doc__ 'Docstring for myfunc().'

Methods and Other Callables
===========================

Partials work with any callable object, including methods and instances.

.. include:: functools_method.py
    :literal:
    :start-after: #end_pymotw_header

::

	$ python functools_method.py
	meth1 straight:
		object: <bound method MyClass.meth1 of <__main__.MyClass object at 0x85b10>>
		__name__: meth1
		__doc__ 'Docstring for meth1().'
		called meth1 with: (<__main__.MyClass object at 0x85b10>, 'no default for a', 3)
	
	meth1 wrapper:
		object: <functools.partial object at 0x88300>
		__name__: meth1
		__doc__ 'Docstring for meth1().'
		called meth1 with: (<__main__.MyClass object at 0x85b10>, 'a goes here', 4)
	
	meth2:
		object: <bound method MyClass.meth2 of <__main__.MyClass object at 0x85b10>>
		__name__: meth2
		__doc__ 'Docstring for meth2'
		called meth2 with: (<__main__.MyClass object at 0x85b10>, 'no default for c', 6)
	
	wrapped meth2:
		object: <functools.partial object at 0x88270>
		__name__: meth2
		__doc__ 'Docstring for meth2'
		called meth2 with: ('wrapped c', 'no default for c', 6)
	
	instance:
		object: <__main__.MyClass object at 0x85b10>
		__name__: (no __name__)
		__doc__ 'Demonstration class for functools'
		called object with: (<__main__.MyClass object at 0x85b10>, 'no default for e', 6)
	
	instance wrapper:
		object: <functools.partial object at 0x88330>
		__name__: (no __name__)
		__doc__ 'partial(func, *args, **keywords) - new function with partial application\n\tof the given arguments and keywords.\n'
		called object with: (<__main__.MyClass object at 0x85b10>, 'e goes here', 7)

wraps
=====

As mentioned earlier, these capabilities are especially useful when used in
decorators, since the decorated function ends up with properties of the
original, "raw", function. functools provides a convenience function, wraps(),
to be used as a decorator itself and to apply update_wrapper() automatically.

.. include:: functools_wraps.py
    :literal:
    :start-after: #end_pymotw_header

::

	$ python functools_wraps.py
	myfunc:
		object: <function myfunc at 0x82330>
		__name__: myfunc
		__doc__ None
	
		myfunc: ('unwrapped, default b', 2)
		myfunc: ('unwrapped, passing b', 3)
	
	wrapped_myfunc:
		object: <function myfunc at 0x82370>
		__name__: myfunc
		__doc__ None
	
		decorated: ('decorated defaults', 1)
			myfunc: ('decorated defaults', 1)
		decorated: ('args to decorated', 4)
			myfunc: ('args to decorated', 4)

.. seealso::

    `functools <http://docs.python.org/library/functools.html>`_
        The standard library documentation for this module.
    