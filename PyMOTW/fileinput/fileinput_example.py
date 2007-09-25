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

"""Example use of fileinput module.

See http://blog.doughellmann.com/2007/03/pymotw-fileinput.html

For a more complete example, see http://www.doughellmann.com/Projects/m3u2rss/

"""

__module_id__ = "$Id$"

#
# Import system modules
#
import fileinput
import sys

#
# Module
#

def generate_item(filename):
	"""Process the named file go generate an RSS item.
	"""
	print filename

for line in fileinput.input(sys.argv[1:]):
	mp3filename = line.strip()
	if not mp3filename or mp3filename.startswith('#'):
		continue
	generate_item(mp3filename)
