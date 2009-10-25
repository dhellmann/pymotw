#!/usr/bin/env python
# encoding: utf-8

import sys
import threading
import time

io_lock = threading.Lock()

def block():
    t = threading.current_thread()
    with io_lock:
        print '%s with ident %s going to sleep' % (t.name, t.ident)
    time.sleep(1)
    with io_lock:
        print t.name, 'finishing'
    return

# Create and start several threads that "block"
threads = [ threading.Thread(target=block) for i in range(3) ]
for t in threads:
    t.start()

# Map the threads from their identifier to the thread object
threads_by_ident = dict((t.ident, t) for t in threads)

# Show where each thread is "blocked"
for ident, frame in sys._current_frames().items():
    t = threads_by_ident.get(ident)
    if not t:
        # Main thread
        continue
    with io_lock:
        print t.name, 'stopped at line', frame.f_lineno

# Let the threads finish
for t in threads:
    t.join()
