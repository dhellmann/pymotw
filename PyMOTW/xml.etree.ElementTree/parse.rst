=========
 Parsing
=========

Parsed documents are represented in memory by ElementTree and Element
objects connected into a tree structure based on the way the nodes in
the XML document are nested.

Parsing an Entire Document
==========================

When you parse an entire document with `parse()`, an ElementTree
instance is returned.  The tree knows about all of the data in the
input document, and can be searched or manipulated in place.  While
this can make working with the parsed document a little easier, it
does take more memory than an event-based parsing approach since the
entire document must be loaded.

The memory footprint of small, simple documents such as this list of
podcasts is not significant:

.. literalinclude:: podcasts.opml


Finding Nodes in a Document
===========================

Searching by Name
-----------------

Searching by Text Content
-------------------------

Searching with XPath
--------------------

Parsed Node Attributes
======================

- arbitrary attriubtes
- text content
- child nodes
- tail

Watching Events While Parsing
=============================

Creating Your Own Tree Builder
==============================
