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

The example below uses a simple string message terminator.  The HTTP request handler example in the standard library documentation shows how to change the terminator based on the context to differentiate between HTTP headers and the HTTP POST request body.




.. seealso::

    `asynchat <http://docs.python.org/library/asynchat.html>`_
        The standard library documentation for this module.

    :mod:`asyncore`
        The asyncore module implements an lower-level asynchronous I/O event loop.