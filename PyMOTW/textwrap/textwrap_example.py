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

"""Examples of using the textwrap module.

See http://blog.doughellmann.com/2007/04/pymotw-textwrap.html
"""

__module_id__ = "$Id$"

import textwrap

# Provide some sample text
sample_text = '''
	The textwrap module can be used to format text for output in situations
	where pretty-printing is desired.  It offers programmatic functionality similar
	to the paragraph wrapping or filling features found in many text editors.
	'''

# Illustrate wrapping without dedenting first
print 'No dedent:\n'
print textwrap.fill(sample_text)

# Remove common whitespace prefix from the lines in the sample text
dedented_text = textwrap.dedent(sample_text).strip()
print '\nDedented:\n'
print dedented_text

# Format the output with a few different max line width values
for width in [ 20, 60, 80 ]:
	print
	print '%d Columns:\n' % width
	print textwrap.fill(dedented_text, width=width)

# Demonstrate how to produce a hanging indent
print '\nHanging indent:\n'
print textwrap.fill(dedented_text, initial_indent='', subsequent_indent='    ')

