#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Using Events to synchronize threads.
"""

__version__ = "$Id$"

import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s (%(threadName)-10s) %(message)s',
                    )
                    
def wait_for_event(e):
    """Wait for the event to be set before doing anything"""
    logging.debug('wait_for_event starting')
    e.wait()
    logging.debug('e.isSet()->%s', e.isSet())

def wait_for_event_timeout(e, t):
    """Wait t seconds and then timeout"""
    logging.debug('wait_for_event_timeout starting')
    e.wait(t)
    logging.debug('e.isSet()->%s', e.isSet())


e = threading.Event()
t1 = threading.Thread(name='block', 
                      target=wait_for_event,
                      args=(e,))
t1.start()

t2 = threading.Thread(name='non-block', 
                      target=wait_for_event_timeout, 
                      args=(e, 2))
t2.start()

logging.debug('Waiting before calling Event.set()')
time.sleep(3)
e.set()
logging.debug('Event is set')
