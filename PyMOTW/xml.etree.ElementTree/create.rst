.. _xml.etree.ElementTree.creating:

=========================================
 Creating XML Documents with ElementTree
=========================================

In addition to its parsing capabilities, ElementTree also supports
creating well-formed XML documents from Element objects constructed in
your application.  The Element class used when a document is parsed
also knows how to generate a serialized form of its contents, which
can then be written to a file or other data stream.

Building Element Nodes
======================

There are three helper functions useful for creating a hierarchy of
Element nodes.  ``Element()`` creates a standard node,
``SubElement()`` attaches a new node to a parent, and ``Comment()``
creates a node that serializes using XML's comment syntax.

.. include:: ElementTree_create.py
   :literal:
   :start-after: #end_pymotw_header

The output contains only the XML nodes in the tree, not the XML declaration
with version and encoding.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_create.py'))
.. }}}
.. {{{end}}}

Pretty-Printing XML
===================

No effort is made to "pretty print" the output produced by
``tostring()``, since adding extra whitespace changes the contents of
the document.  To make them easier to follow for human readers, the
rest of the examples below will use `a tip I found online
<http://renesd.blogspot.com/2007/05/pretty-print-xml-with-python.html>`_
and re-parse the XML with :mod:`xml.dom.minidom` then use its
``toprettyxml()`` method.

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
ElementTree to construct a similar XML file from a CSV input file,
setting all of the element attributes as the tree is constructed.

.. include:: ElementTree_csv_to_xml.py
   :literal:
   :start-after: #end_pymotw_header

The attribute values can be configured one at a time with ``set()``
(as with the ``root`` node), or all at once by passing a dictionary to
the node factory (as with each group and podcast node).

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_csv_to_xml.py'))
.. }}}
.. {{{end}}}

Setting Processing Instructions
===============================

Converting to a String
======================

QName
=====


.. seealso::

   Outline Processor Markup Language, OPML_
       Dave Winer's OPML specification and documentation.

.. _OPML: http://www.opml.org/
