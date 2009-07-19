History
=======

1.97
  - 19 July 2009, :mod:`urllib2`

1.96
  - 12 July 2009, :ref:`article-file-access`

1.95
  - 5 July 2009, :mod:`abc`
  - Rearrange packaging to install the HTML files.
  - Add ``motw`` command line app to show PyMOTW article on a given module, similar to pydoc.

1.94
  - Moved ``run_script()`` from pavement.py to `sphinxcontrib-paverutils <http://pypi.python.org/pypi/sphinxcontrib-paverutils>`_ 1.1.
  - 28 June 2009, :mod:`pyclbr`

1.93
  - 21 Jun 2009, :mod:`robotparser`

1.92
  - 14 June 2009, :mod:`gettext`
  - Added Windows info to :mod:`platform`, courtesy of Scott Lyons.
  - Added process group example to :mod:`subprocess`, courtesy of Scott Leerssen.

1.91
  - Add :ref:`article-data-persistence` article.
  - Correct link to library table of contents on python.org from about page.  Thanks to Tetsuya Morimoto for pointing out the broken link.
  - Add information about Tetsuya Morimoto's Japanese translation.
  - Add link to jsonpickle on :mod:`json` article, courtesy of Sebastien Binet.
  - Add time-stamps to HTML output
  - Remove extraneous javascript file from web html template to avoid 404 errors

1.90
  - 24 May 2009, :mod:`json`
  - updated daemon process examples in :mod:`multiprocessing`
  
1.89
  - 28 April 2009, :mod:`multiprocessing` (part 2, communication and MapReduce example)

1.88
  - 19 April 2009, :mod:`multiprocessing` (part 1, basic usage)
  - Upgraded to Python 2.6.2.
  - Add options to blog command in pavement.py to let the user specify alternate input and output file names for the blog HTML.
  - Added namedtuple example to :mod:`collections`.

1.87.1
  - Added dialect example to :mod:`csv` to show how to parse files with ``|``-delimited fields.

1.87
  - 5 Apr 2009, :mod:`pipes`
  - Converted PEP links to use ``pep`` role.
  - Converted RFC references to use ``rfc`` role.
  - Updated examples in :mod:`warnings` and :mod:`string` to work with changes in Python 2.6.1.

1.86.1
  - Updated working environment to use Paver 1.0b1.
  - Corrected errors in *.rst files identified by update to new version of Paver that doesn't let cog errors slide.
  - Added ignore_error option to run_script() in pavement.py so scripts with errors I'm expecting can be quietly ignored.
  - Finished converting all articles to use cog, where appropriate.

1.86
  - 14 Mar 2009, :mod:`asynchat`
  - Move to bitbucket.org for DVCS hosting
  - Updated description of ``uuid4()`` in :mod:`uuid` based on feedback via O'Reilly blog comment.

1.85
  - 1 Mar 2009, :mod:`asyncore`
  - Continue converting older articles to use cog.
  - Fix subprocess examples so they work if the permissions on the "child" scripts haven't been changed from the default way they are installed.

1.84
  - 22 Feb 2009, :mod:`tarfile`
  - Updated DictWriter example in :mod:`csv` based on feedback from Trilok Khairnar.
  - Cleaned up use of cog in a few older modules

1.83
  - 15 Feb 2009, :mod:`grp`
  - Continue converting older articles to use cog.

1.82
  - 8 Feb 2009, :mod:`pwd`
  - Fix ``set_unixfrom()`` examples in :mod:`mailbox` article based on feedback from Tom Lynn.
  - Add this history section

1.81
  - 18 Jan 2009, :mod:`compileall`

1.80    
  - 4 Jan 2009, :mod:`bz2`

1.79    
  - 28 Dec 2008, :mod:`zlib`.

1.78.1  
  - Updated :mod:`gzip` examples to avoid using built-in names for local variables.

1.78    
  - 7 Dec 2008, :mod:`gzip`.

1.77    
  - 30 Nov 2008, :mod:`readline` and :mod:`rlcompleter`

1.76    
  -  9 Nov 2008, :mod:`array`

1.75    
  - 2 Nov 2008, :mod:`struct`.

1.74.1  
  - Update formatting of several modules to make them more consistent.

1.74    
  - 19 Oct 2008, :mod:`smtpd`.

1.73    
  - 12 Oct 2008, :mod:`trace`

1.72    
  - 5 Oct 2008, :mod:`smtplib`

1.71    
  - 26 Sept 2008, :mod:`mailbox`

1.70.4  
  - Update formatting of several modules and fix the examples on the :mod:`difflib` page.

1.70.3  
  - 21 Sept 2008 :mod:`imaplib`

1.70.2  
  - 21 Sept 2008 :mod:`imaplib`

1.70.1  
  - 21 Sept 2008 :mod:`imaplib` (markup fixed).

1.70    
  - 21 Sept 2008, :mod:`imaplib`.

1.69    
  - 14 Sept 2008, :mod:`anydbm` and related modules.

1.68    
  - Sept 12, 2008, :mod:`exceptions`

1.67.1  
  - minor changes to accommodate site redesign

1.67    
  - 31 Aug 2008, overing :mod:`profile`, :mod:`cProfile`, and :mod:`pstats`.

1.66.1  
  - Fix a logic bug in the code that prints the currently registered signals.

1.66    
  - 17 Aug 2008, :mod:`signal`

1.65    
  - 10 Aug 2008, adding Sphinx-generated documentation all of the modules covered so far.

1.64    
  - 3 Aug 2008 :mod:`webbrowser`

1.63    
  - 27 July 2008, :mod:`uuid`

1.62    
  - 20 July 2008 :mod:`base64`.

1.61    
  - 6 July 2008, :mod:`xmlrpclib`.

1.60    
  - 29 June 2008, :mod:`SimpleXMLRPCServer`

1.59    
  - 22 June 2008, :mod:`warnings`

1.58    
  - 15 June 2008, :mod:`platform`

1.57    
  - 8 June 2008, :mod:`dircache`.

1.56    
  - 1 June 2008, :mod:`Cookie`

1.55    
  - 25 May 2008, :mod:`contextlib`

1.54    
  - 18 May 2008, :mod:`traceback`.

1.53    
  - 11 May 2008, :mod:`heapq`.

1.52    
  - 4 May 2008, :mod:`cmd`.

1.51    
  - 27 Apr 2008, :mod:`functools`.

1.50    
  - 20 Apr 2008, :mod:`filecmp`.

1.49    
  - 13 April 2008, :mod:`fnmatch`.

1.48    
  - 4 April 2008, :mod:`operator`.

1.47    
  - 30 March 2008, :mod:`urllib`.

1.46    
  - 23 March 2008, :mod:`collections`.

1.45    
  - PyCon 2008 edition for 16 Mar 2008, :mod:`datetime`.

1.44    
  - 9 Mar 2008, :mod:`time`

1.43    
  - 2 March 2008, :mod:`EasyDialogs`.

1.42    
  - 24 Feb 2008 :mod:`imp`.

1.41    
  - 17 Feb 2008, :mod:`pkgutil`.

1.40    
  - 10 Feb 2008, :mod:`tempfile`.

1.39    
  - 3 Feb 2008, :mod:`string`.

1.38    
  - 26 Jan 2008, :mod:`os.path`.

1.37    
  - 19 Jan 2008, :mod:`hashlib`.

1.36    
  - 13 Jan 2008, :mod:`threading`

1.35    
  - 6 Jan 2008, :mod:`weakref`.

1.34    
  - 30 Dec 2007, :mod:`mmap`.

1.33.1  
  - Correction for release 1.33 for 22 Dec 2007 the :mod:`zipimport` module.

1.33    
  - 22 Dec 2007, :mod:`zipimport`.

1.32    
  -  16 Dec 2007 :mod:`zipfile`.

1.31    
  - 9 Dec 2007, :mod:`BaseHTTPServer`

1.30    
  - Dec 2, 2007 :mod:`SocketServer`

1.29    
  - Nov 25, 2007 :mod:`inspect`.

1.28    
  - Nov 15, 2007 :mod:`urlparse`

1.27    
  - 10 Nov 2007, :mod:`pprint`

1.26    
  - 4 Nov 2007, :mod:`shutils`

1.25    
  - 28 Oct 2007, :mod:`commands`

1.24    
  - 20 Oct 2007, :mod:`itertools`

1.23    
  - Added another :mod:`difflib` example based on comments on that post.

1.22    
  - 14 Oct 2007, :mod:`shlex`.

1.21    
  - 7 Oct 2007, :mod:`difflib`.

1.20    
  - 30 Sept 2007, :mod:`copy`

1.19    
  - 25 Sept 2007, :mod:`sched`

1.18    
  -  20 September 2007, :mod:`timeit`

1.17    
  -  12 Sept 2007, :mod:`hmac`

1.16    
  - 3 Sept 2007, :mod:`unittest`

1.15    
  - 27 Aug, 2007 :mod:`optparse`.

1.14    
  -  20 Aug 2007, :mod:`csv`

1.13    
  - 12 Aug 2007, :mod:`getopt`.

1.12    
  - August 5, 2007, :mod:`shelve`

1.11    
  -  July 30, 2007, :mod:`glob`

1.10    
  -  July 22, 2007, :mod:`calendar`

1.9     
  -  July 15, 2007, :mod:`getpass`

1.8     
  -  July 8, 2007, :mod:`atexit`

1.7     
  -  July 1, 2007, :mod:`subprocess`

1.6     
  - June 24, 2007, :mod:`pickle`

1.5     
  - June 17, 2007, wrapping up the :mod:`os` module.

1.4     
  - June 10, 2007, :mod:`os` module files and directories.

1.3     
  -  June 3, 2007, continuing coverage of :mod:`os`

1.2     
  -  May 27, 2007, :mod:`os`

1.1     
  -  May 20, 2007, :mod:`locale`

1.0     
  - First packaged release, includes :mod:`fileinput`, :mod:`ConfigParser`, :mod:`Queue`, :mod:`StringIO`, :mod:`textwrap`, :mod:`linecache`, :mod:`bisect`, and :mod:`logging`.
