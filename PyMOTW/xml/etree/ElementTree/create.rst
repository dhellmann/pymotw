.. _xml.etree.ElementTree.creating:

========================
 Creating XML Documents
========================

In addition to its parsing capabilities, :mod:`xml.etree.ElementTree`
also supports creating well-formed XML documents from :class:`Element`
objects constructed in an application.  The :class:`Element` class
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
.. cog.out(run_script(cog.inFile, 'ElementTree_create.py', break_lines_at=68))
.. }}}
.. {{{end}}}

The ``&`` character in the text of ``child_with_entity_ref`` is
converted to the entity reference ``&amp;`` automatically.

Pretty-Printing XML
===================

:class:`ElementTree` makes no effort to "pretty print" the output
produced by :func:`tostring()`, since adding extra whitespace changes
the contents of the document.  To make the output easier to follow for
human readers, the rest of the examples below will use `a tip I found
online
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
attributes for the group names and podcast properties.
:class:`ElementTree` can be used to construct a similar XML file from
a CSV input file, setting all of the element attributes as the tree is
constructed.

.. include:: ElementTree_csv_to_xml.py
   :literal:
   :start-after: #end_pymotw_header

The attribute values can be configured one at a time with
:func:`set()` (as with the ``root`` node), or all at once by passing a
dictionary to the node factory (as with each group and podcast node).

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_csv_to_xml.py', break_lines_at=68))
.. }}}
.. {{{end}}}

Building Trees from Lists of Nodes
==================================

Multiple children can be added to an :class:`Element` instance with
the :func:`extend` method.  The argument to :func:`extend` is any
iterable, including a :class:`list` or another :class:`Element`
instance.

.. include:: ElementTree_extend.py
   :literal:
   :start-after: #end_pymotw_header

When a :class:`list` is given, the nodes in the list are added
directly to the new parent.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_extend.py'))
.. }}}
.. {{{end}}}

When another :class:`Element` instance is given, the children of that
node are added to the new parent.

.. include:: ElementTree_extend_node.py
   :literal:
   :start-after: #end_pymotw_header

In this case, the node with tag ``root`` created by parsing the XML
string has three children, which are added to the ``parent`` node.
The ``root`` node is not part of the output tree.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_extend_node.py'))
.. }}}
.. {{{end}}}

It is important to understand that :func:`extend` does not modify any
existing parent-child relationships with the nodes.  If the values
passed to extend exist somewhere in the tree already, they will still
be there, and will be repeated in the output.

.. include:: ElementTree_extend_node_copy.py
   :literal:
   :start-after: #end_pymotw_header

Setting the :attr:`id` attribute of these children to the Python
unique object identifier exposes the fact that the same node objects
appear in the output tree more than once.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_extend_node_copy.py'))
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
.. cog.out(run_script(cog.inFile, 'ElementTree_write.py', break_lines_at=68))
.. }}}
.. {{{end}}}

The last node in the tree contains no text or sub-nodes, so it is
written as an empty tag, ``<empty_child />``.  :func:`write` takes a
*method* argument to control the handling for empty nodes.  

.. include:: ElementTree_write_method.py
   :literal:
   :start-after: #end_pymotw_header

Three methods are supported:

``xml``
  The default method, produces ``<empty_child />``.
``html``
  Produce the tag pair, as is required in HTML documents
  (``<empty_child></empty_child>``).
``text``
  Prints only the text of nodes, and skips empty tags entirely.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_write_method.py'))
.. }}}
.. {{{end}}}



.. seealso::

   Outline Processor Markup Language, OPML_
       Dave Winer's OPML specification and documentation.

.. _OPML: http://www.opml.org/
