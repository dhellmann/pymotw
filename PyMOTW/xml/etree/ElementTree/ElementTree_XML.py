#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Embedded XML string
"""
#end_pymotw_header

from xml.etree.ElementTree import XML

parsed = XML('''
<root>
  <group>
    <child id="a">This is child "a".</child>
    <child id="b">This is child "b".</child>
  </group>
  <group>
    <child id="c">This is child "c".</child>
  </group>
</root>
''')

print 'parsed =', parsed

for elem in parsed:
    print elem.tag
    if elem.text is not None and elem.text.strip():
        print '  text: "%s"' % elem.text
    if elem.tail is not None and elem.tail.strip():
        print '  tail: "%s"' % elem.tail
    for name, value in sorted(elem.attrib.items()):
        print '  %-4s = "%s"' % (name, value)
    print
