#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""
#end_pymotw_header
import collections
import functools
import multiprocessing

# TODO - Count lines of code and average them instead of counting words?

class SimpleMapReduce(object):
    
    def __init__(self, map_func, reduce_func, num_workers=None):
        """
        map_func
          Function to map inputs to intermediate data.
        
        reduce_func
          Function to reduce partitioned version of intermediate
          data to final output
         
        num_workers
          The number of workers to create in the pool.  Defaults
          to the number of CPUs available on the current host.
        """
        self.map_func = map_func
        self.reduce_func = reduce_func
        self.pool = multiprocessing.Pool(num_workers)
    
    def __call__(self, inputs):
        """Process the inputs through the map and reduce functions given.
        """
        # Convert inputs to mapped values
        mapped_values = self.pool.map(self.map_func, inputs)

        # Partition the results
        partitioned_data = collections.defaultdict(list)
        for sublist in mapped_values:
            for key, value in sublist:
                partitioned_data[key].append(value)

        # Reduce the partitioned values to the final result
        reduced_values = self.pool.map(self.reduce_func, partitioned_data.items())
        return reduced_values
        

if __name__ == '__main__':
    import glob
    import operator
    
    def file_to_words(filename):
        """Read a file and put individual words on the output queue.
        """
        import string
        STOP_WORDS = set([
            'a', 'and', 'are', 'as', 'be', 'for', 'if', 'in', 
            'is', 'it', 'of', 'or', 'the', 'to', 'with',
            ])
        TR = string.maketrans(string.punctuation, ' ' * len(string.punctuation))

        print multiprocessing.current_process().name, 'reading', filename
        output = []
    
        with open(filename, 'rt') as f:
            for line in f:
                if line.lstrip().startswith('..'):
                    continue
                # Strip punctuation
                line = line.translate(TR)
                for word in line.split():
                    word = word.lower()
                    if word.isalpha() and word not in STOP_WORDS:
                        output.append( (word, 1) )
        return output

    def count_words(item):
        """Returns a tuple with the word and number of occurances.
        """
        word, occurances = item
        return (word, sum(occurances))

    input_files = glob.glob('../*/*.rst')
    mapper = SimpleMapReduce(file_to_words, count_words)
    counts = mapper(input_files)
    counts.sort(key=operator.itemgetter(1))
    counts.reverse()
    for word, count in counts[:20]:
        print '%15s: %5s' % (word, count)
