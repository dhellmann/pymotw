=======================
xmlrpclib
=======================
.. module:: xmlrpclib
    :synopsis: Client-side library for XML-RPC communication.

:Module: xmlrpclib
:Purpose: Client-side library for XML-RPC communication.
:Python Version: 2.2 and later
:Abstract: As a follow-up to last week's article on SimpleXMLRPCServer, this week covers the client-side library xmlrpclib.

Description
===========

Last week we looked at the library for creating an XML-RPC server. The
xmlrpclib module lets you communicate from Python with any XML-RPC server
written in any language. All of the examples below use the server defined in
xmlrpclib_server.py, available in the source distribution and repeated here for
reference:

Connecting to a Server
======================

The simplest way to connect a client to a server is to instantiate a
ServerProxy object, giving it the URI of the server. For example, the demo
server runs on port 9000 of localhost:

::

    import xmlrpclib

    server = xmlrpclib.ServerProxy('http://localhost:9000')
    print 'Ping:', server.ping()

In this case, the ping() method of the service takes no arguments and returns a
single boolean value.

::

    $ python xmlrpclib_ServerProxy.py
    Ping: True


Other options are available to support alternate transport. Both HTTP and HTTPS
are supported out of the box, as are basic authentication. You would only need
to provide a transport class if your communication channel was not one of the
supported types. It would be an interesting exercise, for example, to implement
XML-RPC over SMTP. Not terribly useful, but interesting.

The verbose option gives you debugging information useful for working out where
communication errors might be happening.

::

    import xmlrpclib

    server = xmlrpclib.ServerProxy('http://localhost:9000', verbose=True)
    print 'Ping:', server.ping()

::

    $ python xmlrpclib_ServerProxy_verbose.py
    Ping: connect: (localhost, 9000)
    connect fail: ('localhost', 9000)
    connect: (localhost, 9000)
    connect fail: ('localhost', 9000)
    connect: (localhost, 9000)
    send: 'POST /RPC2 HTTP/1.0\r\nHost: localhost:9000\r\nUser-Agent: xmlrpclib.py/1.0.1 (by www.pythonware.com)\r\nContent-Type: text/xml\r\nContent-Length: 98\r\n\r\n'
    send: "<?xml version='1.0'?>\n<methodCall>\n<methodName>ping</methodName>\n<params>\n</params>\n</methodCall>\n"
    reply: 'HTTP/1.0 200 OK\r\n'
    header: Server: BaseHTTP/0.3 Python/2.5.1
    header: Date: Sun, 06 Jul 2008 19:56:13 GMT
    header: Content-type: text/xml
    header: Content-length: 129
    body: "<?xml version='1.0'?>\n<methodResponse>\n<params>\n<param>\n<value><boolean>1</boolean></value>\n</param>\n</params>\n</methodResponse>\n"
    True

You can change the default encoding from UTF-8 if you need to use an alternate
system.

::

    import xmlrpclib

    server = xmlrpclib.ServerProxy('http://localhost:9000', encoding='ISO-8859-1')
    print 'Ping:', server.ping()

The server should automatically detect the correct encoding.

::

    $ python xmlrpclib_ServerProxy_encoding.py
    Ping: True


The allow_none option controls whether Python's None value is automatically
translated to a nil value or if it causes an error.

::

    import xmlrpclib

    server = xmlrpclib.ServerProxy('http://localhost:9000', allow_none=True)
    print 'Allowed:', server.show_type(None)

    server = xmlrpclib.ServerProxy('http://localhost:9000', allow_none=False)
    print 'Not allowed:', server.show_type(None)

Note that the error is raised locally if the client does not allow None, but
can also be raised from within the server if it is not configured to allow
None.

::

    $ python xmlrpclib_ServerProxy_allow_none.py
    Allowed: ['None', "<type 'NoneType'>", None]
    Not allowed:
    Traceback (most recent call last):
      File "/Users/dhellmann/Documents/PyMOTW/in_progress/xmlrpclib/xmlrpclib_ServerProxy_allow_none.py", line 17, in <module>
        print 'Not allowed:', server.show_type(None)
      File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/xmlrpclib.py", line 1147, in __call__
        return self.__send(self.__name, args)
      File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/xmlrpclib.py", line 1431, in __request
        allow_none=self.__allow_none)
      File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/xmlrpclib.py", line 1080, in dumps
        data = m.dumps(params)
      File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/xmlrpclib.py", line 623, in dumps
        dump(v, write)
      File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/xmlrpclib.py", line 635, in __dump
        f(self, value, write)
      File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/xmlrpclib.py", line 639, in dump_nil
        raise TypeError, "cannot marshal None unless allow_none is enabled"
    TypeError: cannot marshal None unless allow_none is enabled


The use_datetime option lets you pass datetime.datetime and related objects in
to the proxy or receive them from the server. If use_datetime is False, the
internal DateTime class is used to represent dates instead.

Data Types
==========

The XML-RPC protocol recognizes a limited set of common data types. The types
can be passed as arguments or return values and combined to create more complex
data structures.

::

    import xmlrpclib
    import datetime

    server = xmlrpclib.ServerProxy('http://localhost:9000')

    for t, v in [ ('boolean', True), 
                  ('integer', 1),
                  ('floating-point number', 2.5),
                  ('string', 'some text'), 
                  ('datetime', datetime.datetime.now()),
                  ('array', ['a', 'list']),
                  ('array', ('a', 'tuple')),
                  ('structure', {'a':'dictionary'}),
                ]:
        print '%-22s:' % t, server.show_type(v)


The simple types::

    $ python xmlrpclib_types.py
    boolean               : ['True', "<type 'bool'>", True]
    integer               : ['1', "<type 'int'>", 1]
    floating-point number : ['2.5', "<type 'float'>", 2.5]
    string                : ['some text', "<type 'str'>", 'some text']
    datetime              : ['20080706T16:22:49', "<type 'instance'>", <DateTime '20080706T16:22:49' at a5d030>]
    array                 : ["['a', 'list']", "<type 'list'>", ['a', 'list']]
    array                 : ["['a', 'tuple']", "<type 'list'>", ['a', 'tuple']]
    structure             : ["{'a': 'dictionary'}", "<type 'dict'>", {'a': 'dictionary'}]


And of course, they can be nested to create values of arbitrary complexity::

    import xmlrpclib
    import datetime
    import pprint

    server = xmlrpclib.ServerProxy('http://localhost:9000')

    data = { 'boolean':True, 
             'integer': 1,
             'floating-point number': 2.5,
             'string': 'some text',
             'datetime': datetime.datetime.now(),
             'array': ['a', 'list'],
             'array': ('a', 'tuple'),
             'structure': {'a':'dictionary'},
             }
    arg = []
    for i in range(3):
        d = {}
        d.update(data)
        d['integer'] = i
        arg.append(d)

    print 'Before:'
    pprint.pprint(arg)

    print
    print 'After:'
    pprint.pprint(server.show_type(arg)[-1])

::

    $ python xmlrpclib_types_nested.py
    Before:
    [{'array': ('a', 'tuple'),
      'boolean': True,
      'datetime': datetime.datetime(2008, 7, 6, 16, 24, 52, 348849),
      'floating-point number': 2.5,
      'integer': 0,
      'string': 'some text',
      'structure': {'a': 'dictionary'}},
     {'array': ('a', 'tuple'),
      'boolean': True,
      'datetime': datetime.datetime(2008, 7, 6, 16, 24, 52, 348849),
      'floating-point number': 2.5,
      'integer': 1,
      'string': 'some text',
      'structure': {'a': 'dictionary'}},
     {'array': ('a', 'tuple'),
      'boolean': True,
      'datetime': datetime.datetime(2008, 7, 6, 16, 24, 52, 348849),
      'floating-point number': 2.5,
      'integer': 2,
      'string': 'some text',
      'structure': {'a': 'dictionary'}}]

    After:
    [{'array': ['a', 'tuple'],
      'boolean': True,
      'datetime': <DateTime '20080706T16:24:52' at a5be18>,
      'floating-point number': 2.5,
      'integer': 0,
      'string': 'some text',
      'structure': {'a': 'dictionary'}},
     {'array': ['a', 'tuple'],
      'boolean': True,
      'datetime': <DateTime '20080706T16:24:52' at a5bf30>,
      'floating-point number': 2.5,
      'integer': 1,
      'string': 'some text',
      'structure': {'a': 'dictionary'}},
     {'array': ['a', 'tuple'],
      'boolean': True,
      'datetime': <DateTime '20080706T16:24:52' at a5bf80>,
      'floating-point number': 2.5,
      'integer': 2,
      'string': 'some text',
      'structure': {'a': 'dictionary'}}]


Passing Objects
===============

Instances of Python classes are treated as structures and passed as a
dictionary, with the attributes of the object as values in the dictionary.

::

    import xmlrpclib

    class MyObj:
        def __init__(self, a, b):
            self.a = a
            self.b = b
        def __repr__(self):
            return 'MyObj(%s, %s)' % (repr(self.a), repr(self.b))

    server = xmlrpclib.ServerProxy('http://localhost:9000')

    o = MyObj(1, 'b goes here')
    print 'o=', o
    print server.show_type(o)

    o2 = MyObj(2, o)
    print 'o2=', o2
    print server.show_type(o2)


Round-tripping the value gives a dictionary on the client, since there is
nothing encoded in the values to tell the server (or client) that it should be
instantiated as part of a class.

::

    $ python xmlrpclib_types_object.py
    o= MyObj(1, 'b goes here')
    ["{'a': 1, 'b': 'b goes here'}", "<type 'dict'>", {'a': 1, 'b': 'b goes here'}]
    o2= MyObj(2, MyObj(1, 'b goes here'))
    ["{'a': 2, 'b': {'a': 1, 'b': 'b goes here'}}", "<type 'dict'>", {'a': 2, 'b': {'a': 1, 'b': 'b goes here'}}]


Binary Data
===========

All values passed to the server are encoded and escaped automatically. However,
some data types may contain characters that are not valid XML. For example,
binary image data may include byte values in the ASCII control range 0 to 31.
If you need to pass binary data, it is best to use the Binary class to encode
it for transport.

::

    import xmlrpclib

    server = xmlrpclib.ServerProxy('http://localhost:9000')

    s = 'This is a string with control characters' + '\0'
    print 'Local string:', s

    data = xmlrpclib.Binary(s)
    print 'As binary:', server.send_back_binary(data)

    print 'As string:', server.show_type(s)

If we pass the string containing a NULL byte to show_type(), an exception is
raised in the XML parser:

::

    $ python xmlrpclib_Binary.py
    Local string: This is a string with control characters
    As binary: This is a string with control characters
    As string:
    Traceback (most recent call last):
      File "/Users/dhellmann/Documents/PyMOTW/in_progress/xmlrpclib/xmlrpclib_Binary.py", line 21, in <module>
        print 'As string:', server.show_type(s)
      File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/xmlrpclib.py", line 1147, in __call__
        return self.__send(self.__name, args)
      File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/xmlrpclib.py", line 1437, in __request
        verbose=self.__verbose
      File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/xmlrpclib.py", line 1201, in request
        return self._parse_response(h.getfile(), sock)
      File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/xmlrpclib.py", line 1340, in _parse_response
        return u.close()
      File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/xmlrpclib.py", line 787, in close
        raise Fault(**self._stack[0])
    xmlrpclib.Fault: <Fault 1: "<class 'xml.parsers.expat.ExpatError'>:not well-formed (invalid token): line 6, column 55">


Binary data can also be used to send objects using pickles. The normal security
issues related to sending what amounts to executable code over the wire apply
here (i.e., don't do this unless you're sure your communication channel is
secure).

::

    import xmlrpclib
    import cPickle as pickle

    class MyObj:
        def __init__(self, a, b):
            self.a = a
            self.b = b
        def __repr__(self):
            return 'MyObj(%s, %s)' % (repr(self.a), repr(self.b))

    server = xmlrpclib.ServerProxy('http://localhost:9000')

    o = MyObj(1, 'b goes here')
    print 'Local:', o, id(o)

    print 'As object:', server.show_type(o)

    p = pickle.dumps(o)
    b = xmlrpclib.Binary(p)
    r = server.send_back_binary(b)

    o2 = pickle.loads(r.data)
    print 'From pickle:', o2, id(o2)

Remember, the data attribute of the Binary instance contains the pickled
version of the object, so it has to be unpickled before it can be used. That
results in a different object (with a new id value).

::

    $ python xmlrpclib_Binary_pickle.py
    Local: MyObj(1, 'b goes here') 9620936
    As object: ["{'a': 1, 'b': 'b goes here'}", "<type 'dict'>", {'a': 1, 'b': 'b goes here'}]
    From pickle: MyObj(1, 'b goes here') 11049200


Exception Handling
==================

Since the XML-RPC server might be written in any language, exception classes
cannot be transmitted directly. Instead, exceptions raised in the server are
converted to Fault objects and raised as exceptions locally.

::

    import xmlrpclib

    server = xmlrpclib.ServerProxy('http://localhost:9000')
    try:
        server.raises_exception('A message')
    except Exception, err:
        print 'Fault code:', err.faultCode
        print 'Message   :', err.faultString

::

    $ python xmlrpclib_exception.py
    Fault code: 1
    Message   : <type 'exceptions.RuntimeError'>:A message


MultiCall
=========

Multicall is an extension to the XML-RPC protocol to allow more than one call
to be sent at the same time, with the responses collected and returned to the
caller. The MultiCall class was added to xmlrpclib in Python 2.4. To use a
MultiCall instance, invoke the methods on it as with a ServerProxy, then call
the object with no arguments. The result is an iterator with the results.

::

    import xmlrpclib

    server = xmlrpclib.ServerProxy('http://localhost:9000')

    multicall = xmlrpclib.MultiCall(server)
    multicall.ping()
    multicall.show_type(1)
    multicall.show_type('string')

    for i, r in enumerate(multicall()):
        print i, r


::

    $ python xmlrpclib_MultiCall.py
    0 True
    1 ['1', "<type 'int'>", 1]
    2 ['string', "<type 'str'>", 'string']


If one of the calls causes a Fault or otherwise raises an exception, the
exception is raised when the result is produced from the iterator and no more
results are available.

::

    import xmlrpclib

    server = xmlrpclib.ServerProxy('http://localhost:9000')

    multicall = xmlrpclib.MultiCall(server)
    multicall.ping()
    multicall.show_type(1)
    multicall.raises_exception('Next to last call stops execution')
    multicall.show_type('string')

    for i, r in enumerate(multicall()):
        print i, r

::

    $ python xmlrpclib_MultiCall_exception.py
    0 True
    1 ['1', "<type 'int'>", 1]
    Traceback (most recent call last):
      File "/Users/dhellmann/Documents/PyMOTW/in_progress/xmlrpclib/xmlrpclib_MultiCall_exception.py", line 21, in <module>
        for i, r in enumerate(multicall()):
      File "/Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/xmlrpclib.py", line 949, in __getitem__
        raise Fault(item['faultCode'], item['faultString'])
    xmlrpclib.Fault: <Fault 1: "<type 'exceptions.RuntimeError'>:Next to last call stops execution">


