#!/usr/bin/env python
#
# Copyright 2007 Doug Hellmann.
#
#
#                         All Rights Reserved
#
# Permission to use, copy, modify, and distribute this software and
# its documentation for any purpose and without fee is hereby
# granted, provided that the above copyright notice appear in all
# copies and that both that copyright notice and this permission
# notice appear in supporting documentation, and that the name of Doug
# Hellmann not be used in advertising or publicity pertaining to
# distribution of the software without specific, written prior
# permission.
#
# DOUG HELLMANN DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
# INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN
# NO EVENT SHALL DOUG HELLMANN BE LIABLE FOR ANY SPECIAL, INDIRECT OR
# CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS
# OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,
# NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN
# CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#

"""Check the exit status and the text output.

"""

__version__ = "$Id$"
#end_pymotw_header

from commands import *

def run_command(cmd):
    print 'Running: "%s"' % cmd
    status, text = getstatusoutput(cmd)
    exit_code = status >> 8 # high byte
    signal_num = status % 256 # low byte
    print 'Status: x%04x' % status
    print 'Signal: x%02x (%d)' % (signal_num, signal_num)
    print 'Exit  : x%02x (%d)' % (exit_code, exit_code)
    print 'Core? : %s' % bool(signal_num & (1 << 8)) # high bit
    print 'Output:'
    print text
    print

run_command('ls -l *.py')
run_command('ls -l *.notthere')
run_command('./dumpscore')
run_command('echo "WAITING TO BE KILLED"; read input')
