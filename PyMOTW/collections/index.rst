===================================
collections -- Container data types
===================================

.. module:: collections
    :synopsis: Container data types.

:Purpose: Container data types.
:Python Version: 2.4 and later

Description
===========

The collections module includes container data types beyond the builtin
types list and dict.

Deque
=====

A double-ended queue, or "deque", supports adding and removing elements from
either end. The more commonly used stacks and queues are degenerate forms of
deques, where the inputs and outputs are restricted to a single end.

Since deques are a type of sequence container, they support some of the same
operations that lists support, such as examining the contents with
__getitem__(), determining length, and removing elements from the middle by
matching identity.

::

    import collections

    d = collections.deque('abcdefg')
    print 'Deque:', d
    print 'Length:', len(d)
    print 'Left end:', d[0]
    print 'Right end:', d[-1]

    d.remove('c')
    print 'remove(c):', d

::

    $ python collections_deque.py
    Deque: deque(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    Length: 7
    Left end: a
    Right end: g
    remove(c): deque(['a', 'b', 'd', 'e', 'f', 'g'])


A deque can be populated from either end, termed "left" and "right" in the
Python implementation.

::

    import collections

    # Add to the right
    d = collections.deque()
    d.extend('abcdefg')
    print 'extend    :', d
    d.append('h')
    print 'append    :', d

    # Add to the left
    d = collections.deque()
    d.extendleft('abcdefg')
    print 'extendleft:', d
    d.appendleft('h')
    print 'appendleft:', d

Notice that extendleft() iterates over its input and performs the equivalent
of an appendleft() for each item. The end result is the deque contains the
input sequence in reverse order.

::

    $ python collections_deque_populating.py
    extend    : deque(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    append    : deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
    extendleft: deque(['g', 'f', 'e', 'd', 'c', 'b', 'a'])
    appendleft: deque(['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a'])

Similarly, the elements of the deque can be consumed from both or either end,
depending on the algorithm you're applying.

::

    import collections

    print 'From the right:'
    d = collections.deque('abcdefg')
    while True:
        try:
            print d.pop()
        except IndexError:
            break

    print 'From the left:'
    d = collections.deque('abcdefg')
    while True:
        try:
            print d.popleft()
        except IndexError:
            break

::

    $ python collections_deque_consuming.py
    From the right:
    g
    f
    e
    d
    c
    b
    a
    From the left:
    a
    b
    c
    d
    e
    f
    g


Since deques are thread-safe, you can even consume the contents from both ends
at the same time in separate threads.

::

    import collections
    import threading
    import time

    candle = collections.deque(xrange(11))

    def burn(direction, nextSource):
        while True:
            try:
                next = nextSource()
            except IndexError:
                break
            else:
                print '%8s: %s' % (direction, next)
                time.sleep(0.1)
        print '%8s done' % direction
        return

    left = threading.Thread(target=burn, args=('Left', candle.popleft))
    right = threading.Thread(target=burn, args=('Right', candle.pop))

    left.start()
    right.start()

    left.join()
    right.join()

::

    $ python collections_deque_both_ends.py
        Left: 0
       Right: 10
        Left: 1
       Right: 9
        Left: 2
       Right: 8
        Left: 3
       Right: 7
        Left: 4
       Right: 6
        Left: 5
       Right done
        Left done


Another useful capability of the deque is to rotate it in either direction, to
skip over some item(s).

::

    import collections

    d = collections.deque(xrange(10))
    print 'Normal        :', d

    d = collections.deque(xrange(10))
    d.rotate(2)
    print 'Right rotation:', d

    d = collections.deque(xrange(10))
    d.rotate(-2)
    print 'Left rotation :', d

Rotating the deque to the right (using a positive rotation) takes items from
the right end and moves them to the left end. Rotating to the left (with a
negative value) takes items from the left end and moves them to the right end.
It may help to visualize the items in the deque as being engraved along the
edge of a dial.

::

    $ python collections_deque_rotate.py
    Normal        : deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    Right rotation: deque([8, 9, 0, 1, 2, 3, 4, 5, 6, 7])
    Left rotation : deque([2, 3, 4, 5, 6, 7, 8, 9, 0, 1])


defaultdict
===========

The standard dictionary includes the method setdefault() for retrieving a
value and establishing a default if the value does not exist. By contrast,
defaultdict lets you specify the default up front when it is initialized.

::

    import collections

    def default_factory():
        return 'default value'

    d = collections.defaultdict(default_factory, foo='bar')
    print d
    print d['foo']
    print d['bar']

::

    $ python collections_defaultdict.py
    defaultdict(<function default_factory at 0x7ca70>, {'foo': 'bar'})
    bar
    default value


This works well as long as it is appropriate for all keys to use that same
default. It can be especially useful if the default is a type used for
aggregating or accumulating values, such as a list, set, or even integer. The
standard library documentation includes several examples of using defaultdict
this way.


