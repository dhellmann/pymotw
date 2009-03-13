=========================================
asynchat -- Asynchronous protocol handler
=========================================

.. module:: asynchat
    :synopsis: Asynchronous protocol handler

:Purpose: Asynchronous protocol handler
:Python Version: 1.5.2 and later

The asynchat module builds on :mod:`asyncore` to make it easier to implement protocols based on passing messages back and forth between server and client.  The ``async_chat`` class is an ``asyncore.dispatcher`` subclass that receives data and looks for a message terminator.  Your subclass only needs to specify what to do when data comes in and the terminator is found.  Outgoing data is queued for transmission via FIFO objects managed by ``async_chat``.

Message Terminators
===================

Incoming messages are broken up based on *terminators*, controlled on the instance via ``set_terminator()``.  There are three possible configurations:

 1. If a string argument is passed to ``set_terminator()``, the message is considered complete when that string appears in the input data.
 2. If a numeric argument is passed, the message is considered complete when that many bytes have been read.
 3. If ``None`` is passed, message termination is not managed by ``async_chat``.

The EchoServer example below uses both a simple string terminator and a message length terminator, depending on the context of the incoming data.  The HTTP request handler example in the standard library documentation offers another example of how to change the terminator based on the context to differentiate between HTTP headers and the HTTP POST request body.

Server and Handler
==================

To make it easier to understand how :mod:`asynchat` is different from :mod:`asyncore`, the examples here duplicate the functionality of the EchoServer example from the :mod:`asyncore` discussion.  The same basic structure is needed: a server object to accept connections, handler objects to deal with communication with each client, and client objects to initiate the conversation.

The EchoServer needed to work with asynchat is basically the same as the one created for the asyncore-based example, with fewer logging calls because they are less interesting this time around:

.. include:: asynchat_echo_server.py
    :literal:
    :start-after: #end_pymotw_header

The EchoHandler is based on ``asynchat.async_chat`` instead of the ``asyncore.dispatcher`` this time around.  It operates at a slightly higher level of abstraction, so reading and writing are handled automatically.  All we need to do is tell the handler:

 - what to do with incoming data (by overriding ``handle_incoming_data()``)
 - how to recognize the end of an incoming message (via ``set_terminator()``)
 - what to do when a complete message is received (in ``found_terminator()``)
 - what data to send (using ``push()``)

In this case, we have 2 operating modes.  We are either waiting for a command of the form ``ECHO length\n``, or we are waiting for the data to be echoed.  We toggle back and forth between the two modes by setting an instance variable ``process_data`` to the method to be invoked when the terminator is found and then changing the terminator as appropriate.

.. include:: asynchat_echo_handler.py
    :literal:
    :start-after: #end_pymotw_header

Once the complete command is found, we switch to message-processing mode and wait for the complete set of text to be received.  Once it is available, we push it onto the outgoing channel and set up the handler to be closed once the data is sent.

Client
======

The client works in much the same way as the handler.

.. include:: asynchat_echo_client.py
    :literal:
    :start-after: #end_pymotw_header


Putting It All Together
=======================

The main program for this example sets up the client and server in the same asyncore main loop.  Normally you would have them in separate processes, of course, but this makes it easier to show the combined output.

.. include:: asynchat_echo_main.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'asynchat_echo_main.py'))
.. }}}
.. {{{end}}}


.. seealso::

    `asynchat <http://docs.python.org/library/asynchat.html>`_
        The standard library documentation for this module.

    :mod:`asyncore`
        The asyncore module implements an lower-level asynchronous I/O event loop.