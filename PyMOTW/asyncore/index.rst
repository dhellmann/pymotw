====================================
asyncore -- Asynchronous I/O handler
====================================

.. module:: asyncore
    :synopsis: Asynchronous I/O handler

:Purpose: Asynchronous I/O handler
:Available In: 1.5.2 and later

The asyncore module includes tools for working with I/O objects such as sockets so they can be managed asynchronously (instead of, for example, using threads).  The main class provided is :class:`dispatcher`, a wrapper around a socket that provides hooks for handling events like connecting, reading, and writing when invoked from the main loop function, :func:`loop`.

Clients
=======

To create an asyncore-based client, subclass :class:`dispatcher` and provide implementations for creating the socket, reading, and writing.  Let's examine this HTTP client, based on the one from the standard library documentation.

.. include:: asyncore_http_client.py
    :literal:
    :start-after: #end_pymotw_header

First, the socket is created in ``__init__()`` using the base class method ``create_socket()``.  Alternative implementations of the method may be provided, but in this case we want a TCP/IP socket so the base class version is sufficient.

The ``handle_connect()`` hook is present simply to illustrate when it is called.  Other types of clients that need to do some sort of hand-shaking or protocol negotiation should do the work in ``handle_connect()``.

``handle_close()`` is similarly presented for the purposes of showing when the method is called.  The base class version closes the socket correctly, so if you don't need to do extra cleanup on close you can leave the method out.

The asyncore loop uses ``writable()`` and its sibling method ``readable()`` to decide what actions to take with each dispatcher.  Actual use of poll() or select() on the sockets or file descriptors managed by each dispatcher is handled inside the :mod:`asyncore` code, so you don't need to do that yourself.  Simply indicate whether the dispatcher cares at all about reading or writing.  In the case of this HTTP client, ``writable()`` returns True as long as there is data from the request to send to the server.  ``readable()`` always returns True because we want to read all of the data.

Each time through the loop when ``writable()`` responds positively, ``handle_write()`` is invoked.  In this version, the HTTP request string that was built in ``__init__()`` is sent to the server and the write buffer is reduced by the amount successfully sent.

Similarly, when ``readable()`` responds positively and there is data to read, ``handle_read()`` is invoked.

The example below the ``__main__`` test configures logging for debugging then creates two clients to download two separate web pages.  Creating the clients registers them in a "map" kept internally by asyncore.  The downloading occurs as the loop iterates over the clients.  When the client reads 0 bytes from a socket that seems readable, the condition is interpreted as a closed connection and ``handle_close()`` is called.

One example of how this client app may run is:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'asyncore_http_client.py'))
.. }}}
.. {{{end}}}

Servers
=======

The example below illustrates using asyncore on the server by re-implementing the EchoServer from the :mod:`SocketServer` examples.  There are three classes: ``EchoServer`` receives incoming connections from clients and creates ``EchoHandler`` instances to deal with each.  The ``EchoClient`` is an asyncore dispatcher similar to the HttpClient defined above.

.. include:: asyncore_echo_server.py
    :literal:
    :start-after: #end_pymotw_header

The EchoServer and EchoHandler are defined in separate classes because they do different things.  When EchoServer accepts a connection, a new socket is established.  Rather than try to dispatch to individual clients within EchoServer, an EchoHandler is created to take advantage of the socket map maintained by asyncore.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'asyncore_echo_server.py'))
.. }}}
.. {{{end}}}

In this example the server, handler, and client objects are all being maintained in the same socket map by asyncore in a single process. To separate the server from the client, simply instantiate them from separate scripts and run ``asyncore.loop()`` in both. When a dispatcher is closed, it is removed from the map maintained by asyncore and the loop exits when the map is empty.

Working with Other Event Loops
==============================

It is sometimes necessary to integrate the asyncore event loop with an event loop from the parent application.  For example, a GUI application would not want the UI to block until all asynchronous transfers are handled -- that would defeat the purpose of making them asynchronous.  To make this sort of integration easy, ``asyncore.loop()`` accepts arguments to set a timeout and to limit the number of times the loop is run.  We can see their effect on the client by re-using HttpClient from the first example.

.. include:: asyncore_loop.py
    :literal:
    :start-after: #end_pymotw_header

Here we see that the client is only asked to read or data once per call into ``asyncore.loop()``.  Instead of our own ``while`` loop, we could call ``asyncore.loop()`` like this from a GUI toolkit idle handler or other mechanism for doing a small amount of work when the UI is not busy with other event handlers.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'asyncore_loop.py'))
.. }}}
.. {{{end}}}

Working with Files
==================

Normally you would want to use asyncore with sockets, but there are times when it is useful to read files asynchronously, too (to use files when testing network servers without requiring the network setup, or to read or write large data files in parts).  For these situations, asyncore provides the :class:`file_dispatcher` and :class:`file_wrapper` classes.

.. include:: asyncore_file_dispatcher.py
    :literal:
    :start-after: #end_pymotw_header

This example was tested under Python 2.5.2, so I am using ``os.open()`` to get a file descriptor for the file.  For Python 2.6 and later, ``file_dispatcher`` automatically converts anything with a ``fileno()`` method to a file descriptor.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'asyncore_file_dispatcher.py'))
.. }}}
.. {{{end}}}


.. seealso::

    `asyncore <http://docs.python.org/library/asyncore.html>`_
        The standard library documentation for this module.
    
    :mod:`asynchat`
        The asynchat module builds on asyncore to make it easier to create clients
        and servers communicate by passing messages back and forth using a set protocol.

    :mod:`SocketServer`
        The SocketServer module article includes another example of the EchoServer with
        threading and forking variants.
