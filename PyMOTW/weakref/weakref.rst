=======
weakref
=======
.. module:: weakref
    :synopsis: Refer to an "expensive" object, but allow it to be garbage collected if there are no other non-weak references.

:Module: weakref
:Purpose: Refer to an "expensive" object, but allow it to be garbage collected if there are no other non-weak references.
:Python Version: Since 2.1
:Abstract:

    The weakref module lets you refer to an object without preventing it from
    being garbage collected.

Description
===========

The weakref module supports weak references to objects. A normal reference
increments the reference count on the object and prevents it from being
garbage collected. This is not always desirable, either when a circular
reference might be present or when building a cache of objects that should be
deleted when memory is needed.

References
==========

Weak references to your objects are managed through the ref class. To retrieve
the original object, call the reference object.

::

    import weakref

    class ExpensiveObject(object):
        def __del__(self):
            print '(Deleting %s)' % self

    obj = ExpensiveObject()
    r = weakref.ref(obj)

    print 'obj:', obj
    print 'ref:', r
    print 'r():', r()

    print 'deleting obj'
    del obj
    print 'r():', r()

In this case, since obj is deleted before the second call to the reference,
None is returned.

::

    $ python weakref_ref.py
    obj: <__main__.ExpensiveObject object at 0x68df0>
    ref: <weakref at 0x65b10; to 'ExpensiveObject' at 0x68df0>
    r(): <__main__.ExpensiveObject object at 0x68df0>
    deleting obj
    (Deleting <__main__.ExpensiveObject object at 0x68df0>)
    r(): None

Reference Callbacks
===================

The ref constructor takes an optional second argument that should be a
callback function to invoke when the referenced object is deleted.

::

    import weakref

    class ExpensiveObject(object):
        def __del__(self):
            print '(Deleting %s)' % self
            
    def callback(reference):
        """Invoked when referenced object is deleted"""
        print 'callback(', reference, ')'

    obj = ExpensiveObject()
    r = weakref.ref(obj, callback)

    print 'obj:', obj
    print 'ref:', r
    print 'r():', r()

    print 'deleting obj'
    del obj
    print 'r():', r()

The callback receives the reference as an argument, after the reference is
"dead" and no longer refers to the original object. This lets you remove the
weak reference object from a cache, for example.

::

    $ python weakref_ref_callback.py
    obj: <__main__.ExpensiveObject object at 0x69e50>
    ref: <weakref at 0x65ba0; to 'ExpensiveObject' at 0x69e50>
    r(): <__main__.ExpensiveObject object at 0x69e50>
    deleting obj
    callback( <weakref at 0x65ba0; dead> )
    (Deleting <__main__.ExpensiveObject object at 0x69e50>)
    r(): None

Proxies
=======

Instead of using ref directly, it can be more convenient to use a proxy.
Proxies can be used as though they were the original object, so you do not
need to call the ref first to access the object.

::

    import weakref

    class ExpensiveObject(object):
        def __init__(self, name):
            self.name = name
        def __del__(self):
            print '(Deleting %s)' % self

    obj = ExpensiveObject('My Object')
    r = weakref.ref(obj)
    p = weakref.proxy(obj)

    print 'via obj:', obj.name
    print 'via ref:', r().name
    print 'via proxy:', p.name
    del obj
    print 'via proxy:', p.name

If the proxy is access after the referent object is removed, a ReferenceError
exception is raised.

::

    $ python weakref_proxy.py
    via obj: My Object
    via ref: My Object
    via proxy: My Object
    (Deleting <__main__.ExpensiveObject object at 0x6e2d0>)
    via proxy:
    Traceback (most recent call last):
      File "/Users/dhellmann/Documents/PyMOTW/in_progress/weakref/weakref_proxy.py", line 27, in <module>
        print 'via proxy:', p.name
    ReferenceError: weakly-referenced object no longer exists

Cyclic References
=================

One use for weak references is to allow cyclic references without preventing
garbage collection. This example illustrates the difference between using
regular objects and proxies when a graph includes a cycle.

First we set up the gc module to help us debug the leak. The DEBUG_LEAK flag
causes it to print information about objects which cannot be seen other than
through the reference the garbage collector has to them. 

::

    import gc
    from pprint import pprint
    import weakref

    gc.set_debug(gc.DEBUG_LEAK)

    def collect_and_show_garbage():
        "Show what garbage is present."
        print 'Unreachable:', gc.collect()
        print 'Garbage:', 
        pprint(gc.garbage)

Next a utility function to exercise the graph class by creating a cycle and
then removing various references.

::

    def demo(graph_factory):
        print 'Set up graph:'
        one = graph_factory('one')
        two = graph_factory('two')
        three = graph_factory('three')
        one.set_next(two)
        two.set_next(three)
        three.set_next(one)
        
        print
        print 'Graphs:'
        print str(one)
        print str(two)
        print str(three)
        collect_and_show_garbage()

        print
        three = None
        two = None
        print 'After 2 references removed:'
        print str(one)
        collect_and_show_garbage()

        print
        print 'Removing last reference:'
        one = None
        collect_and_show_garbage()

Now a naive Graph class that accepts any object given to it as the "next" node
in the sequence. For the sake of brevity, this Graph supports a single
outgoing reference from each node, which results in very boring graphs but
makes it easy to recreate cycles.

::

    class Graph(object):
        def __init__(self, name):
            self.name = name
            self.other = None
        def set_next(self, other):
            print '%s.set_next(%s (%s))' % (self.name, other, type(other))
            self.other = other
        def all_nodes(self):
            "Generate the nodes in the graph sequence."
            yield self
            n = self.other
            while n and n.name != self.name:
                yield n
                n = n.other
            if n is self:
                yield n
            return
        def __str__(self):
            return '->'.join([n.name for n in self.all_nodes()])
        def __repr__(self):
            return '%s(%s)' % (self.__class__.__name__, self.name)
        def __del__(self):
            print '(Deleting %s)' % self.name
            self.set_next(None)

If we run demo() with the Graph class like this:

::

    print 'WITHOUT PROXY'
    print
    demo(Graph)

We get output like:

::

    WITHOUT PROXY

    Set up graph:
    one.set_next(two (<class '__main__.Graph'>))
    two.set_next(three (<class '__main__.Graph'>))
    three.set_next(one->two->three (<class '__main__.Graph'>))

    Graphs:
    one->two->three->one
    two->three->one->two
    three->one->two->three
    Unreachable: 0
    Garbage:[]

    After 2 references removed:
    one->two->three->one
    Unreachable: 0
    Garbage:[]

    Removing last reference:
    gc: uncollectable <Graph 0x766270>
    gc: uncollectable <Graph 0x7669b0>
    gc: uncollectable <Graph 0x7669d0>
    gc: uncollectable <dict 0x751810>
    gc: uncollectable <dict 0x751390>
    gc: uncollectable <dict 0x751ae0>
    Unreachable: 6
    Garbage:[Graph(one),
     Graph(two),
     Graph(three),
     {'name': 'one', 'other': Graph(two)},
     {'name': 'two', 'other': Graph(three)},
     {'name': 'three', 'other': Graph(one)}]

Notice that even after deleting the local references to the Graph instances in
demo(), the graphs all show up in the garbage list and cannot be collected.
The dictionaries in the garbage list hold the attributes of the Graph
instances. We can forcibly delete the graphs, since we know what they are:

::

    print
    print 'BREAKING CYCLE AND CLEARING GARBAGE'
    print
    gc.garbage[0].set_next(None)
    while gc.garbage:
        del gc.garbage[0]
    collect_and_show_garbage()

Giving us:

::

    BREAKING CYCLE AND CLEARING GARBAGE

    one.set_next(None (<type 'NoneType'>))
    (Deleting two)
    two.set_next(None (<type 'NoneType'>))
    (Deleting three)
    three.set_next(None (<type 'NoneType'>))
    (Deleting one)
    one.set_next(None (<type 'NoneType'>))
    Unreachable: 0
    Garbage:[]

And now let's define a more intelligent WeakGraph class that knows not to
create cycles using regular references, but to use a weakref.ref when a cycle
is detected.

::

    print
    print 'WITH PROXY'
    print

    class WeakGraph(Graph):
        def set_next(self, other):
            if other is not None:
                # See if we should replace the reference
                # to other with a weakref.
                if self in other.all_nodes():
                    other = weakref.proxy(other)
            super(WeakGraph, self).set_next(other)
            return

When we run demo() using WeakGraph, we see much better memory behavior:

::

    WITH PROXY

    Set up graph:
    one.set_next(two (<class '__main__.WeakGraph'>))
    two.set_next(three (<class '__main__.WeakGraph'>))
    three.set_next(one->two->three (<type 'weakproxy'>))

    Graphs:
    one->two->three
    two->three->one->two
    three->one->two->three
    Unreachable: 0
    Garbage:[]

    After 2 references removed:
    one->two->three
    Unreachable: 0
    Garbage:[]

    Removing last reference:
    (Deleting one)
    one.set_next(None (<type 'NoneType'>))
    (Deleting two)
    two.set_next(None (<type 'NoneType'>))
    (Deleting three)
    three.set_next(None (<type 'NoneType'>))
    Unreachable: 0
    Garbage:[]

Caching Objects
===============

The ref and proxy classes are considered "low level". While they are useful
for maintaining weak references to individual objects and allowing cycles to
be garbage collected, if you need to create a cache of several objects the
WeakKeyDictionary and WeakValueDictionary provide a more appropriate API.

As you might expect, the WeakValueDictionary uses weak references to the
values it holds, allowing them to be garbage collected when other code is not
actually using them.

To illustrate the difference between memory handling with a regular dictionary
and WeakValueDictionary, let's go experiment with explicitly calling the
garbage collector again::

    import gc
    from pprint import pprint
    import weakref

    gc.set_debug(gc.DEBUG_LEAK)

    class ExpensiveObject(object):
        def __init__(self, name):
            self.name = name
        def __repr__(self):
            return 'ExpensiveObject(%s)' % self.name
        def __del__(self):
            print '(Deleting %s)' % self
            
    def demo(cache_factory):
        # hold objects so any weak references 
        # are not removed immediately
        all_refs = {}
        # the cache using the factory we're given
        print 'CACHE TYPE:', cache_factory
        cache = cache_factory()
        for name in [ 'one', 'two', 'three' ]:
            o = ExpensiveObject(name)
            cache[name] = o
            all_refs[name] = o
            del o # decref

        print 'all_refs =',
        pprint(all_refs)
        print 'Before, cache contains:', cache.keys()
        for name, value in cache.items():
            print '  %s = %s' % (name, value)
            del value # decref
            
        # Remove all references to our objects except the cache
        print 'Cleanup:'
        del all_refs
        gc.collect()

        print 'After, cache contains:', cache.keys()
        for name, value in cache.items():
            print '  %s = %s' % (name, value)
        print 'demo returning'
        return

    demo(dict)
    print
    demo(weakref.WeakValueDictionary)

Notice that any loop variables that refer to the values we are caching must be
cleared explicitly to decrement the reference count on the object. Otherwise
the garbage collector would not remove the objects and they would remain in
the cache. Similarly, the all_refs variable is used to hold references to
prevent them from being garbage collected prematurely.

::

    $ python weakref_valuedict.py
    CACHE TYPE: <type 'dict'>
    all_refs ={'one': ExpensiveObject(one),
     'three': ExpensiveObject(three),
     'two': ExpensiveObject(two)}
    Before, cache contains: ['three', 'two', 'one']
      three = ExpensiveObject(three)
      two = ExpensiveObject(two)
      one = ExpensiveObject(one)
    Cleanup:
    After, cache contains: ['three', 'two', 'one']
      three = ExpensiveObject(three)
      two = ExpensiveObject(two)
      one = ExpensiveObject(one)
    demo returning
    (Deleting ExpensiveObject(three))
    (Deleting ExpensiveObject(two))
    (Deleting ExpensiveObject(one))

    CACHE TYPE: weakref.WeakValueDictionary
    all_refs ={'one': ExpensiveObject(one),
     'three': ExpensiveObject(three),
     'two': ExpensiveObject(two)}
    Before, cache contains: ['three', 'two', 'one']
      three = ExpensiveObject(three)
      two = ExpensiveObject(two)
      one = ExpensiveObject(one)
    Cleanup:
    (Deleting ExpensiveObject(three))
    (Deleting ExpensiveObject(two))
    (Deleting ExpensiveObject(one))
    After, cache contains: []
    demo returning

The WeakKeyDictionary works similarly but uses weak references for the keys
instead of the values in the dictionary.

The library documentation for weakref contains this warning::

    Caution: Because a WeakValueDictionary is built on top of a Python
    dictionary, it must not change size when iterating over it. This can be
    difficult to ensure for a WeakValueDictionary because actions performed by
    the program during iteration may cause items in the dictionary to vanish
    "by magic" (as a side effect of garbage collection).
