.. _xml.etree.ElementTree.creating:

=========================================
 Creating XML Documents with ElementTree
=========================================

In addition to its parsing capabilities, :mod:`xml.etree.ElementTree`
also supports creating well-formed XML documents from :class:`Element`
objects constructed in your application.  The :class:`Element` class
used when a document is parsed also knows how to generate a serialized
form of its contents, which can then be written to a file or other
data stream.

Building Element Nodes
======================

There are three helper functions useful for creating a hierarchy of
:class:`Element` nodes.  :func:`Element()` creates a standard node,
:func:`SubElement()` attaches a new node to a parent, and
:func:`Comment()` creates a node that serializes using XML's comment
syntax.

.. include:: ElementTree_create.py
   :literal:
   :start-after: #end_pymotw_header

The output contains only the XML nodes in the tree, not the XML declaration
with version and encoding.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_create.py'))
.. }}}
.. {{{end}}}

Notice that the ``&`` character in the text of
``child_with_entity_ref`` is converted to the entity reference
``&amp;`` automatically.

Pretty-Printing XML
===================

ElementTree makes no effort to "pretty print" the output produced by
:func:`tostring()`, since adding extra whitespace changes the contents
of the document.  To make the output easier to follow for human
readers, the rest of the examples below will use `a tip I found online
<http://renesd.blogspot.com/2007/05/pretty-print-xml-with-python.html>`_
and re-parse the XML with :mod:`xml.dom.minidom` then use its
:func:`toprettyxml()` method.

.. include:: ElementTree_pretty.py
   :literal:
   :start-after: #end_pymotw_header

The updated example now looks like:

.. include:: ElementTree_create_pretty.py
   :literal:
   :start-after: #end_pymotw_header

and the output is easier to read:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_create_pretty.py'))
.. }}}
.. {{{end}}}

In addition to the extra whitespace for formatting, the
:mod:`xml.dom.minidom` pretty-printer also adds an XML declaration to
the output.


Setting Element Properties
==========================

The previous example created nodes with tags and text content, but did
not set any attributes of the nodes.  Many of the examples from
:ref:`xml.etree.ElementTree.parsing` worked with an OPML_ file listing
podcasts and their feeds.  The ``outline`` nodes in the tree used
attributes for the group names and podcast properties.  We can use
:class:`ElementTree` to construct a similar XML file from a CSV input
file, setting all of the element attributes as the tree is
constructed.

.. include:: ElementTree_csv_to_xml.py
   :literal:
   :start-after: #end_pymotw_header

The attribute values can be configured one at a time with
:func:`set()` (as with the ``root`` node), or all at once by passing a
dictionary to the node factory (as with each group and podcast node).

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_csv_to_xml.py'))
.. }}}
.. {{{end}}}

Serializing XML to a Stream
===========================

:func:`tostring()` is implemented to write to an in-memory file-like
object and then return a string representing the entire element tree.
When working with large amounts of data, it will take less memory and
make more efficient use of the I/O libraries to write directly to a
file handle using the :func:`write()` method of :class:`ElementTree`.

.. include:: ElementTree_write.py
   :literal:
   :start-after: #end_pymotw_header

The example uses :ref:`sys.stdout <sys-input-output>` to write to the
console, but it could also write to an open file or socket.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_write.py'))
.. }}}
.. {{{end}}}



.. seealso::

   Outline Processor Markup Language, OPML_
       Dave Winer's OPML specification and documentation.

.. _OPML: http://www.opml.org/
