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

To parse the file, pass an open file handle to ``parse()``.  It will
read the data, parse the XML, and return an ElementTree object.

.. include:: ElementTree_parse_opml.py
   :literal:
   :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'ElementTree_parse_opml.py'))
.. }}}

::

	$ python ElementTree_parse_opml.py
	<__builtin__.ElementTree instance at 0x82080>

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

::

	$ python ElementTree_dump_opml.py
	opml {'version': '1.0'}
	head {}
	title {}
	dateCreated {}
	dateModified {}
	body {}
	outline {'text': 'Science and Tech'}
	outline {'xmlUrl': 'http://www.publicradio.org/columns/futuretense/podcast.xml', 'text': 'APM: Future Tense', 'type': 'rss', 'htmlUrl': 'http://www.publicradio.org/columns/futuretense/'}
	outline {'xmlUrl': 'http://www.npr.org/rss/podcast.php?id=510030', 'text': 'Engines Of Our Ingenuity Podcast', 'type': 'rss', 'htmlUrl': 'http://www.uh.edu/engines/engines.htm'}
	outline {'xmlUrl': 'http://www.nyas.org/Podcasts/Atom.axd', 'text': 'Science & the City', 'type': 'rss', 'htmlUrl': 'http://www.nyas.org/WhatWeDo/SciencetheCity.aspx'}
	outline {'text': 'Books and Fiction'}
	outline {'xmlUrl': 'http://feeds.feedburner.com/podiobooks', 'text': 'Podiobooker', 'type': 'rss', 'htmlUrl': 'http://www.podiobooks.com/blog'}
	outline {'xmlUrl': 'http://web.me.com/normsherman/Site/Podcast/rss.xml', 'text': 'The Drabblecast', 'type': 'rss', 'htmlUrl': 'http://web.me.com/normsherman/Site/Podcast/Podcast.html'}
	outline {'xmlUrl': 'http://www.tor.com/rss/category/TorDotStories', 'text': 'tor.com / category / tordotstories', 'type': 'rss', 'htmlUrl': 'http://www.tor.com/'}
	outline {'text': 'Computers and Programming'}
	outline {'xmlUrl': 'http://leo.am/podcasts/mbw', 'text': 'MacBreak Weekly', 'type': 'rss', 'htmlUrl': 'http://twit.tv/mbw'}
	outline {'xmlUrl': 'http://leo.am/podcasts/floss', 'text': 'FLOSS Weekly', 'type': 'rss', 'htmlUrl': 'http://twit.tv'}
	outline {'xmlUrl': 'http://www.coreint.org/podcast.xml', 'text': 'Core Intuition', 'type': 'rss', 'htmlUrl': 'http://www.coreint.org/'}
	outline {'text': 'Python'}
	outline {'xmlUrl': 'http://advocacy.python.org/podcasts/pycon.rss', 'text': 'PyCon Podcast', 'type': 'rss', 'htmlUrl': 'http://advocacy.python.org/podcasts/'}
	outline {'xmlUrl': 'http://advocacy.python.org/podcasts/littlebit.rss', 'text': 'A Little Bit of Python', 'type': 'rss', 'htmlUrl': 'http://advocacy.python.org/podcasts/'}
	outline {'xmlUrl': 'http://djangodose.com/everything/feed/', 'text': 'Django Dose Everything Feed', 'type': 'rss'}
	outline {'text': 'Miscelaneous'}
	outline {'xmlUrl': 'http://www.castsampler.com/cast/feed/rss/dhellmann/', 'text': "dhellmann's CastSampler Feed", 'type': 'rss', 'htmlUrl': 'http://www.castsampler.com/users/dhellmann/'}

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

::

	$ python ElementTree_show_feed_urls.py
	Science and Tech
	  APM: Future Tense :: http://www.publicradio.org/columns/futuretense/podcast.xml
	  Engines Of Our Ingenuity Podcast :: http://www.npr.org/rss/podcast.php?id=510030
	  Science & the City :: http://www.nyas.org/Podcasts/Atom.axd
	Books and Fiction
	  Podiobooker :: http://feeds.feedburner.com/podiobooks
	  The Drabblecast :: http://web.me.com/normsherman/Site/Podcast/rss.xml
	  tor.com / category / tordotstories :: http://www.tor.com/rss/category/TorDotStories
	Computers and Programming
	  MacBreak Weekly :: http://leo.am/podcasts/mbw
	  FLOSS Weekly :: http://leo.am/podcasts/floss
	  Core Intuition :: http://www.coreint.org/podcast.xml
	Python
	  PyCon Podcast :: http://advocacy.python.org/podcasts/pycon.rss
	  A Little Bit of Python :: http://advocacy.python.org/podcasts/littlebit.rss
	  Django Dose Everything Feed :: http://djangodose.com/everything/feed/
	Miscelaneous
	  dhellmann's CastSampler Feed :: http://www.castsampler.com/cast/feed/rss/dhellmann/

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

::

	$ python ElementTree_find_feeds_by_tag.py
	http://www.publicradio.org/columns/futuretense/podcast.xml
	http://www.npr.org/rss/podcast.php?id=510030
	http://www.nyas.org/Podcasts/Atom.axd
	http://feeds.feedburner.com/podiobooks
	http://web.me.com/normsherman/Site/Podcast/rss.xml
	http://www.tor.com/rss/category/TorDotStories
	http://leo.am/podcasts/mbw
	http://leo.am/podcasts/floss
	http://www.coreint.org/podcast.xml
	http://advocacy.python.org/podcasts/pycon.rss
	http://advocacy.python.org/podcasts/littlebit.rss
	http://djangodose.com/everything/feed/
	http://www.castsampler.com/cast/feed/rss/dhellmann/

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

::

	$ python ElementTree_find_feeds_by_structure.py
	http://www.publicradio.org/columns/futuretense/podcast.xml
	http://www.npr.org/rss/podcast.php?id=510030
	http://www.nyas.org/Podcasts/Atom.axd
	http://feeds.feedburner.com/podiobooks
	http://web.me.com/normsherman/Site/Podcast/rss.xml
	http://www.tor.com/rss/category/TorDotStories
	http://leo.am/podcasts/mbw
	http://leo.am/podcasts/floss
	http://www.coreint.org/podcast.xml
	http://advocacy.python.org/podcasts/pycon.rss
	http://advocacy.python.org/podcasts/littlebit.rss
	http://djangodose.com/everything/feed/
	http://www.castsampler.com/cast/feed/rss/dhellmann/

.. {{{end}}}

This version is limited to our existing structure, though, so if the
outline nodes are ever rearranged into a deeper tree it will stop
working.  It would be better to provide an XPath expression to find
outline nodes anywhere in the document as long as they include the URL
we want.

.. HERE

Searching by Text Content
-------------------------

Parsed Node Attributes
======================

- arbitrary attributes
- text content
- child nodes
- tail

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
