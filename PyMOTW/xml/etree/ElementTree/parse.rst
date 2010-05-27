.. _xml.etree.ElementTree.parsing:

========================================
 Parsing XML Documents with ElementTree
========================================

Parsed XML documents are represented in memory by :class:`ElementTree`
and :class:`Element` objects connected into a tree structure based on
the way the nodes in the XML document are nested.

Parsing an Entire Document
==========================

When you parse an entire document with :func:`parse()`, an
:class:`ElementTree` instance is returned.  The tree knows about all
of the data in the input document, and the nodes of the tree can be
searched or manipulated in place.  While this flexibility can make
working with the parsed document a little easier, it typically takes
more memory than an event-based parsing approach since the entire
document must be loaded at one time.

The memory footprint of small, simple documents such as this list of
podcasts represented as an OPML_ outline is not significant:

.. literalinclude:: podcasts.opml
   :language: xml

To parse the file, pass an open file handle to :func:`parse()`.  It
will read the data, parse the XML, and return an :class:`ElementTree`
object.

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
all of the children in order and examining their attributes and
contents.

.. include:: ElementTree_dump_opml.py
   :literal:
   :start-after: #end_pymotw_header

Here we print the entire tree, one tag at a time.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_dump_opml.py'))
.. }}}
.. {{{end}}}

If we wanted to print only the groups of names and feed URLs for the
podcasts, leaving out of all of the data in the header section, we
could iterate over only just the ``outline`` nodes and print the
*text* and *xmlUrl* attributes.

.. include:: ElementTree_show_feed_urls.py
   :literal:
   :start-after: #end_pymotw_header

Because we passed ``'outline'`` to :func:`getiterator()` processing is
limited to only nodes with the tag ``'outline'``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_show_feed_urls.py'))
.. }}}
.. {{{end}}}

Finding Nodes in a Document
===========================

Walking the entire tree yourself like this searching for relevant
nodes can be error prone.  In the example above, we had to look at
each outline node to determine if it was a group (nodes with only a
"text" attribute) or podcast (with both "text" and "xmlUrl").  If we
were writing a podcast downloader and needed to produce a simple list
of the podcast feed URLs, without names or groups, we could simplify
the logic using :func:`findall()` to look for nodes with more
descriptive search characteristics.

As a first pass at converting the above example, we can construct an
XPath_ argument to look for all outline nodes.

.. include:: ElementTree_find_feeds_by_tag.py
   :literal:
   :start-after: #end_pymotw_header

The logic in this version is not substantially different than the
version using :func:`getiterator()`.  We still have to check for the
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

We expect all of those outline nodes nested 2 levels deep in the input
will have the *xmlURL* attribute refering to the podcast feed, so if
we were brave we could skip checking for for the attribute before
using it.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_find_feeds_by_structure.py'))
.. }}}
.. {{{end}}}

This version is limited to our existing structure, though, so if the
outline nodes are ever rearranged into a deeper tree it will stop
working.

Parsed Node Attributes
======================

The items returned by :func:`findall()` and :func:`getiterator()` are
:class:`Element` objects, each representing a node in the XML parse
tree.  Each :class:`Element` has attributes for accessing data pulled
out of the XML.  This can be illustrated with a somewhat more
contrived example input file, ``data.xml``:

.. literalinclude:: data.xml
   :language: xml
   :linenos:

The "attributes" of a node are available in the *attrib* property,
which acts like a dictionary.

.. include:: ElementTree_node_attributes.py
   :literal:
   :start-after: #end_pymotw_header

The node on line 5 of the input file has 2 attributes, ``name`` and
``foo``.

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
line 4 has text with a tail (including any whitespace).

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_node_text.py'))
.. }}}
.. {{{end}}}

XML entity references embedded in the document are conveniently
converted to the appropriate characters before values are returned.

.. include:: ElementTree_entity_references.py
   :literal:
   :start-after: #end_pymotw_header

The automatic conversion saves you from having to worry about an
implementation detail of representing certain characters in an XML
document.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_entity_references.py'))
.. }}}
.. {{{end}}}


Watching Events While Parsing
=============================

The other API useful for processing XML documents is event-based.  The
parser generates ``start`` events for opening tags and ``end`` events
for closing tags.  Iterating over the event stream lets you extract
data from the document while parsing it, which is convenient if you
don't need to manipulate the entire document afterwards and if you
want to avoid holding the entire parsed document in memory.

:func:`iterparse()` returns an iterable that produces tuples
containing the name of the event and the node triggering the event.
Events can be one of:

``start``
  A new tag has been encountered.  The closing angle bracket of the
  tag was processed, but not the contents.
``end``
  The closing angle bracket of a closing tag has been processed.  All
  of the children were already processed.
``start-ns``
  Start a namespace declaration.
``end-ns``
  End a namespace declaration.

.. include:: ElementTree_show_all_events.py
   :literal:
   :start-after: #end_pymotw_header

By default, only ``end`` events are generated.  To see other events,
pass the list of event names you want to receive to
:func:`iterparse()`, as in this example:

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_show_all_events.py'))
.. }}}
.. {{{end}}}

The event-style of processing may be more natural for some operations,
such as converting XML input to some other format.  For example,
suppose we want to convert the list of podcasts we have been working
with from an XML file to a data file we can load into a spreadsheet or
database application.  We don't need to hold the entire data set in
memory at a time, since we're simply changing the format.

.. include:: ElementTree_write_podcast_csv.py
   :literal:
   :start-after: #end_pymotw_header

This example program converts our podcast list to a CSV file, ready to
be imported into another application.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_write_podcast_csv.py'))
.. }}}
.. {{{end}}}


Creating Your Own Tree Builder
==============================

A potentially more efficient means of handling parse events is to
replace the standard tree builder behavior with your own.  The
:class:`ElementTree` parser uses an :class:`XMLTreeBuilder` to process
the XML and call methods on a target class to save the results.  The
usual output is an :class:`ElementTree` instance created by the
default :class:`TreeBuilder` class.  By replacing :class:`TreeBuilder`
with your own class, you can receive the events before the
:class:`Element` nodes are instantiated, saving that portion of the
overhead.

The XML-to-CSV converter from the previous section can be translated
to a tree builder.

.. include:: ElementTree_podcast_csv_treebuilder.py
   :literal:
   :start-after: #end_pymotw_header

:class:`PodcastListToCSV` implements the :class:`TreeBuilder`
protocol.  Each time a new XML tag is encountered, :func:`start()` is
called with the tag name and attributes.  When a closing tag is seen
:func:`end()` is called with the name.  In between, :func:`data()` is
called when a node has content (the tree builder is expected to keep
up with the "current" node).  When all of the input is processed,
:func:`close()` is called.  It can return a value, which will be
returned to the user of the :class:`XMLTreeBuilder`.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_podcast_csv_treebuilder.py'))
.. }}}
.. {{{end}}}



Parsing Strings
===============

To work with smaller bits of XML text, especially string literals as
might be embedded in the source of a program, use :func:`XML()` and
the string containing the XML to be parsed as the only argument.

.. include:: ElementTree_XML.py
   :literal:
   :start-after: #end_pymotw_header

Notice that unlike with :func:`parse()`, the return value is an
:class:`Element` instance instead of an :class:`ElementTree`.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_XML.py'))
.. }}}
.. {{{end}}}

For structured XML that uses the "id" attribute to identify unique
nodes of interest, :func:`XMLID()` is a convenient way to access the
parse results.

.. include:: ElementTree_XMLID.py
   :literal:
   :start-after: #end_pymotw_header

:func:`XMLID()` returns the parsed tree as an :class:`Element` object,
along with a dictionary mapping the id attribute strings to the
individual nodes in the tree.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_XMLID.py'))
.. }}}
.. {{{end}}}


.. seealso::

   Outline Processor Markup Language, OPML_
       Dave Winer's OPML specification and documentation.

   XML Path Language, XPath_
       A syntax for identifying parts of an XML document.

   `XPath Support in ElementTree <http://effbot.org/zone/element-xpath.htm>`_
       Part of Fredrick Lundh's original documentation for ElementTree.

   :mod:`csv`
       Read and write comma-separated-value files

.. _OPML: http://www.opml.org/

.. _XPath: http://www.w3.org/TR/xpath/
