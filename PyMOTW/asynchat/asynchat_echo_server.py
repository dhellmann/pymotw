#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""
#end_pymotw_header

import asyncore
import asynchat
import logging

class EchoServer(asyncore.dispatcher):
    """Receives connections and establishes handlers for each client.
    """
    
    def __init__(self, address):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind(address)
        self.address = self.socket.getsockname()
        self.listen(1)
        return

    def handle_accept(self):
        # Called when a client connects to our socket
        client_info = self.accept()
        EchoHandler(sock=client_info[0])
        # We only want to deal with one client at a time,
        # so close as soon as we set up the handler.
        # Normally you would not do this and the server
        # would run forever or until it received instructions
        # to stop.
        self.handle_close()
        return
    
    def handle_close(self):
        self.close()


class EchoHandler(asynchat.async_chat):
    """Handles echoing messages from a single client.
    """
    
    def __init__(self, sock):
        self.received_data = []
        self.logger = logging.getLogger('EchoHandler%s' % str(sock.getsockname()))
        asynchat.async_chat.__init__(self, sock)
        # Start looking for the ECHO command
        self.waiting_for_command = True
        self.set_terminator('\n')
        return

    def collect_incoming_data(self, data):
        """Read an incoming message from the client and put it into our outgoing queue."""
        self.logger.debug('collect_incoming_data() -> (%d) "%s"', len(data), data)
        self.received_data.append(data)

    def found_terminator(self):
        if self.waiting_for_command:
            # Have the full ECHO command
            command = ''.join(self.received_data)
            self.logger.debug('found_terminator() have command "%s"', command)
            command_verb, command_arg = command.strip().split(' ')
            expected_data_len = int(command_arg)
            self.set_terminator(expected_data_len)
            self.waiting_for_command = False
            self.received_data = []
        else:
            to_echo = ''.join(self.received_data)
            self.logger.debug('found_terminator() echoing "%s"', to_echo)
            self.push(to_echo)
            # Disconnect after sending the entire response
            self.close_when_done()
            

class EchoClient(asynchat.async_chat):
    """Sends messages to the server and receives responses.
    """
    
    def __init__(self, host, port, message):
        self.message = message
        self.received_data = []
        self.logger = logging.getLogger('EchoClient')
        asynchat.async_chat.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.logger.debug('connecting to %s', (host, port))
        self.connect((host, port))
        return
        
    def handle_connect(self):
        self.logger.debug('handle_connect()')
        # Send the command
        self.push('ECHO %d\n' % len(self.message))
        # Send the data
        self.push_with_producer(EchoProducer(self.message))
        # We expect the data to come back as-is, 
        # so set a length-based terminator
        self.set_terminator(len(self.message))
    
    def collect_incoming_data(self, data):
        """Read an incoming message from the client and put it into our outgoing queue."""
        self.logger.debug('collect_incoming_data() -> (%d) "%s"', len(data), data)
        self.received_data.append(data)

    def found_terminator(self):
        self.logger.debug('found_terminator()')
        received_message = ''.join(self.received_data)
        if received_message == self.message:
            self.logger.debug('RECEIVED COPY OF MESSAGE')
        else:
            self.logger.debug('ERROR IN TRANSMISSION')
            self.logger.debug('EXPECTED "%s"', self.message)
            self.logger.debug('RECEIVED "%s"', received_message)
        return


class EchoProducer(asynchat.simple_producer):
    
    logger = logging.getLogger('EchoProducer')
    
    def more(self):
        response = asynchat.simple_producer.more(self)
        self.logger.debug('more() -> (%s) "%s"', len(response), response)
        return response


if __name__ == '__main__':
    import socket

    logging.basicConfig(level=logging.DEBUG,
                        format='%(name)s: %(message)s',
                        )

    address = ('localhost', 0) # let the kernel give us a port
    server = EchoServer(address)
    ip, port = server.address # find out what port we were given

    client = EchoClient(ip, port, message=open('lorem.txt', 'r').read())

    asyncore.loop()
