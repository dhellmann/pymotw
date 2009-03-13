#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""
#end_pymotw_header

import asynchat
import logging


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
