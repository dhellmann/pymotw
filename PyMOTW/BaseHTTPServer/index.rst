===========================================================
BaseHTTPServer -- base classes for implementing web servers
===========================================================

.. module:: BaseHTTPServer
    :synopsis: Provides base classes for implementing web servers.

:Purpose: BaseHTTPServer includes classes that can form the basis of a web server.
:Python Version: 1.4 and later


BaseHTTPServer uses classes from :mod:`SocketServer` to create base
classes for making HTTP servers. HTTPServer can be used directly, but
the BaseHTTPRequestHandler is intended to be extended to handle each
protocol method (GET, POST, etc.).

Simple GET Example
==================

To add support for an HTTP method in your request handler class, implement the
method do_METHOD(), replacing METHOD with the name of the HTTP method. For
example, do_GET(), do_POST(), etc. For consistency, the method takes no
arguments. All of the parameters for the request are parsed by
BaseHTTPRequestHandler and stored as instance attributes where you can easily
retrieve them.

This example request handler illustrates how to return a response to the
client and some of the local attributes which can be useful in building the
response:

.. include:: BaseHTTPServer_GET.py
    :literal:
    :start-after: #end_pymotw_header

The message text is assembled and then written to self.wfile, the file handle
wrapping the response socket. Each response needs a response code, set via
self.send_response(). If an error code is used (404, 501, etc.), an
appropriate default error message is included in the header, or you can pass a
message along with the error code.

To run the request handler in a server, pass it to the constructor of
HTTPServer, as in the ``__main__`` processing portion of the sample script.

Then start the server:

::

    $ python BaseHTTPServer_GET.py 
    Starting server, use <Ctrl-C> to stop

And in a separate terminal, use curl to access it:

::

    $ curl -i http://localhost:8080/?foo=barHTTP/1.0 200 OK
    Server: BaseHTTP/0.3 Python/2.5.1
    Date: Sun, 09 Dec 2007 16:00:34 GMT

    CLIENT VALUES:
    client_address=('127.0.0.1', 51275) (localhost)
    command=GET
    path=/?foo=bar
    real path=/
    query=foo=bar
    request_version=HTTP/1.1

    SERVER VALUES:
    server_version=BaseHTTP/0.3
    sys_version=Python/2.5.1
    protocol_version=HTTP/1.0


Threading and Forking
=====================

HTTPServer is a simple subclass of SocketServer.TCPServer, and does not use
multiple threads or processes to handle requests. To add threading or forking,
create a new class using the appropriate mix-in from SocketServer.

.. include:: BaseHTTPServer_threads.py
    :literal:
    :start-after: #end_pymotw_header

Each time a request comes in, a new thread or process is created to handle it:

::

    $ curl http://localhost:8080/
    Thread-1
    $ curl http://localhost:8080/
    Thread-2
    $ curl http://localhost:8080/
    Thread-3

Swapping ForkingMixIn for ThreadingMixIn above would achieve similar results,
using separate processes instead of threads.


POST
====

Supporting POST requests is a little more work, because the base class
does not parse the form data for us. The :mod:`cgi` module provides
the FieldStorage class which knows how to parse the form, if we give
it the correct inputs.

.. include:: BaseHTTPServer_POST.py
    :literal:
    :start-after: #end_pymotw_header

Using curl again, we can include form data, which automatically sets the
method to POST. The last argument, ``-F datafile=@BaseHTTPServer_GET.py``, posts
the contents of the file BaseHTTPServer_GET.py to illustrate reading file data
from the form.

::

    $ curl http://localhost:8080/ -F name=dhellmann -F foo=bar -F  datafile=@BaseHTTPServer_GET.py
    Client: ('127.0.0.1', 51128)
    Path: /
    Form data:
            name=dhellmann
            foo=bar
            Uploaded datafile (2222 bytes)


Errors
======

Error handling is made easy with :meth:`send_error()`. Simply pass the
appropriate error code and an optional error message, and the entire response
(with headers, status code, and body) is generated for you.

.. include:: BaseHTTPServer_errors.py
    :literal:
    :start-after: #end_pymotw_header

In this case, a 404 error is always returned.

::

    $ curl -i http://localhost:8080/
    HTTP/1.0 404 Not Found
    Server: BaseHTTP/0.3 Python/2.5.1
    Date: Sun, 09 Dec 2007 15:49:44 GMT
    Content-Type: text/html
    Connection: close

    <head>
    <title>Error response</title>
    </head>
    <body>
    <h1>Error response</h1>
    <p>Error code 404.
    <p>Message: Not Found.
    <p>Error code explanation: 404 = Nothing matches the given URI.
    </body>


.. seealso::

    `BaseHTTPServer <http://docs.python.org/library/basehttpserver.html>`_
        The standard library documentation for this module.

    :mod:`SocketServer`
        The SocketServer module provides the base class which handles
        the raw socket connection.
