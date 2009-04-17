#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""
#end_pymotw_header

import multiprocessing

def consumer(tasks, results):
    while True:
        next_task = tasks.get()
        if next_task is None:
            # Poison pill means we should exit
            break
        answer = next_task()
        results.put(answer)
    return


class Task(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __call__(self):
        return '%s * %s = %s' % (self.a, self.b, self.a * self.b)


if __name__ == '__main__':
    # Establish communication queues
    tasks = multiprocessing.Queue()
    results = multiprocessing.Queue()
    
    # Start consumers
    num_consumers = multiprocessing.cpu_count() * 2
    print 'Creating %d consumers' % num_consumers
    consumers = [ multiprocessing.Process(target=consumer, args=(tasks, results))
                for i in xrange(num_consumers) ]
    for w in consumers:
        w.start()
    
    # Enqueue jobs
    num_jobs = 10
    for i in xrange(num_jobs):
        tasks.put(Task(i, i))
    
    # Add a poison pill for each consumer
    for i in xrange(num_consumers):
        tasks.put(None)
    
    # Start printing results
    while num_jobs:
        result = results.get()
        print result
        num_jobs -= 1
