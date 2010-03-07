=========
 Parsing
=========

Parsed documents are represented in memory by ElementTree and Element
objects connected into a tree structure based on the way the nodes in
the XML document are nested.

Parsing an Entire Document
==========================

When you parse an entire document with ``parse()``, an ElementTree
instance is returned.  The tree knows about all of the data in the
input document, and can be searched or manipulated in place.  While
this can make working with the parsed document a little easier, it
does take more memory than an event-based parsing approach since the
entire document must be loaded.

The memory footprint of small, simple documents such as this list of
podcasts represented as an OPML_ outline is not significant:

.. literalinclude:: podcasts.opml
   :language: xml
   :linenos:

To parse the file, pass an open file handle to ``parse()``.  It will
read the data, parse the XML, and return an ElementTree object.

.. include:: ElementTree_parse_opml.py
   :literal:
   :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_parse_opml.py'))
.. }}}
.. {{{end}}}

Traversing the Parsed Tree
==========================

Now that we have a parsed XML tree, we can iterate over it, visiting
all of the children in order and examining them.

.. include:: ElementTree_dump_opml.py
   :literal:
   :start-after: #end_pymotw_header

Here we print the entire tree, one tag at a time.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_dump_opml.py'))
.. }}}
.. {{{end}}}

If we wanted to print only the groups of names and feed URLs for the
podcasts, leaving out of all of the data in the header, we could
iterate only just the ``outline`` nodes and print the ``text`` and
``xmlUrl`` attributes.

.. include:: ElementTree_show_feed_urls.py
   :literal:
   :start-after: #end_pymotw_header

Because we passed ``'outline'`` to ``tree.getiterator()`` processing is
limited to only nodes with the tag ``'outline'``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_show_feed_urls.py'))
.. }}}
.. {{{end}}}

Finding Nodes in a Document
===========================

Walking the entire tree yourself can be error prone.  In the example
above, we had to look at each outline node to determine if it was a
group (nodes with only a "text" attribute) or podcast (with both
"text" and "xmlUrl").  If we were writing a podcast downloader and
needed to produce a simple list of the podcast feed URLs, without
names or groups, we might simplify the logic using ``findall()`` to
look for nodes with more descriptive search characteristics.

A first pass at converting the above example might construct an XPath
argument to look for all outline nodes.

.. include:: ElementTree_find_feeds_by_tag.py
   :literal:
   :start-after: #end_pymotw_header

The logic in this version is not substantially different than the
version using ``getiterator()``.  We still have to check for the
presence of the URL, except that we don't print the group name when
the URL is not found.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_find_feeds_by_tag.py'))
.. }}}
.. {{{end}}}

Another version can take advantage of the fact that we know the
outline nodes are only nested two levels deep.  If we change the
search path to ``.//outline/outline`` we will process only the second
level of outline nodes.

.. include:: ElementTree_find_feeds_by_structure.py
   :literal:
   :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_find_feeds_by_structure.py'))
.. }}}
.. {{{end}}}

This version is limited to our existing structure, though, so if the
outline nodes are ever rearranged into a deeper tree it will stop
working.

Parsed Node Attributes
======================

The items returned by ``findall()`` and ``getiterator()`` are
ElementTree objects, each representing a node in the XML parse tree.
Each ElementTree has attributes for accessing data pulled out of the
XML.  This can be illustrated with a somewhat more contrived example
input file, ``data.xml``:

.. literalinclude:: data.xml
   :language: xml
   :linenos:

The "attributes" of a node are available in the ``attrib`` property,
which acts like a dictionary.

.. include:: ElementTree_node_attributes.py
   :literal:
   :start-after: #end_pymotw_header

The node on line 5 of the input file has 2 attributes, ``name`` and ``foo``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_node_attributes.py'))
.. }}}
.. {{{end}}}

The text content of the nodes is available, along with the "tail" text
that comes after the end of a close tag.

.. include:: ElementTree_node_text.py
   :literal:
   :start-after: #end_pymotw_header

The ``child`` node on line 3 contains embedded text, and the node on
line 4 has text with a tail.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_node_text.py'))
.. }}}
.. {{{end}}}

Conveniently, XML entity references embedded in the document are
converted to the appropriate characters before values are returned.

.. include:: ElementTree_entity_references.py
   :literal:
   :start-after: #end_pymotw_header

The conversion saves you from having to worry about an implementation
detail of representing certain characters in an XML document.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_entity_references.py'))
.. }}}
.. {{{end}}}


Watching Events While Parsing
=============================

.. convert to csv as we see each outline node

Creating Your Own Tree Builder
==============================

.. seealso::

   Outline Processor Markup Language, OPML_
       Dave Winer's OPML specification and documentation.

   `XPath Support in ElementTree <http://effbot.org/zone/element-xpath.htm>`_
       Part of Fredrick Lundh's original documentation for ElementTree.

.. _OPML: http://www.opml.org/
