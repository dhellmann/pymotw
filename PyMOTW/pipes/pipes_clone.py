#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""
#end_pymotw_header

import pipes
import tempfile

count_word_substring = pipes.Template()
#count_word_substring.debug(True)
count_word_substring.append('grep -f - /usr/share/dict/words', '--')
count_word_substring.append('wc -l', '--')

count_py = count_word_substring.clone()
count_py.prepend('echo "py"', '--')
f = count_py.open('/dev/null', 'r')
try:
    print '  "py": %5s' % f.read().strip()
finally:
    f.close()

count_perl = count_word_substring.clone()
count_perl.prepend('echo "perl"', '--')
f = count_perl.open('/dev/null', 'r')
try:
    print '"perl": %5s' % f.read().strip()
finally:
    f.close()
