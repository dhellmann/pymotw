#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""
#end_pymotw_header
import collections
import multiprocessing
import string

# TODO - Count lines of code and average them instead of counting words?
class SimpleMapReduce(object):
    
    def __init__(self, map_func, reduce_func, num_workers=None):
        self.map_func = map_func
        self.reduce_func = reduce_func
        self.pool = multiprocessing.Pool(num_workers)
    
    def map(self, inputs):
        mapped_values = self.pool.map(self.map_func, inputs)

        # Partition the results
        partitioned_data = collections.defaultdict(list)
        for sublist in mapped_values:
            for key, value in sublist:
                partitioned_data[key].append(value)

        reduced_values = self.pool.map(self.reduce_func, partitioned_data.items())
        return reduced_values
        

def file_to_words(filename):
    """Read a file and put individual words on the output queue.
    """
    output = []
    
    TR = string.maketrans(string.punctuation, ' ' * len(string.punctuation))
    with open(filename, 'rt') as f:
        for line in f:
            # Strip punctuation
            line = line.translate(TR)
            for word in line.split():
                if word.isalpha():
                    output.append( (word.lower(), 1) )
    return output


def count_words(item):
    """Returns a tuple with the word and number of occurances.
    """
    word, occurances = item
    return (word, sum(occurances))



if __name__ == '__main__':
    input_files = ['basics.rst', 'communication.rst']
    mapper = SimpleMapReduce(file_to_words, count_words)
    counts = mapper.map(input_files)
    counts.sort()
    for word, count in counts:
        print '%15s: %5s' % (word, count)
