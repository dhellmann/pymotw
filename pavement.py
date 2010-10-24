#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

# Standard library
import os
import sys
import tabnanny
import traceback
import types

# Set up Paver
import paver
import paver.doctools
import paver.misctasks
from paver.path import path
from paver.easy import *
import paver.setuputils
paver.setuputils.install_distutils_tasks()
import setuptools
try:
    from sphinxcontrib import paverutils
except:
    paverutils = None

# TODO
# - move these variables to options?

# What project are we building?
PROJECT = 'PyMOTW'

# What version is this?
VERSION = '1.132'

# The sphinx templates expect the VERSION in the shell environment
os.environ['VERSION'] = VERSION

# What is the current module being documented?
MODULE = path('module').text().rstrip()
os.environ['MODULE'] = MODULE

# Read the long description to give to setup
README = path('README.txt').text()

# Scan the input for package information
# to grab any data files (text, images, etc.) 
# associated with sub-packages.
PACKAGE_DATA = paver.setuputils.find_package_data(PROJECT, 
                                                  package=PROJECT,
                                                  only_in_packages=True,
                                                  )

options(
    setup=Bunch(
        name = PROJECT,
        version = VERSION,
        
        description = 'Python Module of the Week Examples: ' + MODULE,
        long_description = README,

        author = 'Doug Hellmann',
        author_email = 'doug.hellmann@gmail.com',

        url = 'http://www.doughellmann.com/PyMOTW/',
        download_url = 'http://www.doughellmann.com/downloads/%s-%s.tar.gz' % \
                        (PROJECT, VERSION),

        classifiers = [ 'Development Status :: 5 - Production/Stable',
                        'Environment :: Console',
                        'Intended Audience :: Developers',
                        'Intended Audience :: Education',
                        'License :: OSI Approved :: BSD License',
                        'Operating System :: POSIX',
                        'Programming Language :: Python',
                        'Topic :: Software Development',
                        ],

        platforms = ('Any',),
        keywords = ('python', 'PyMOTW', 'documentation'),

        # It seems wrong to have to list recursive packages explicitly.
        packages = setuptools.find_packages(),
        package_data=PACKAGE_DATA,
        zip_safe=False,
        
        scripts=['motw'],

        ),
    
    sdist = Bunch(
    ),
    
    sdistext = Bunch(
        outdir='~/Desktop',
    ),
    
    sphinx = Bunch(
        sourcedir=PROJECT,
        docroot = '.',
        builder = 'html',
        doctrees='sphinx/doctrees',
        confdir = 'sphinx',
        template_args = { 'module':MODULE }
    ),

    html = Bunch(
        builddir='%s/docs' % PROJECT,
        outdir='%s/docs' % PROJECT,
        templates='pkg',
    ),

    text = Bunch(
        builddir='%s/docs' % PROJECT,
        outdir='%s/docs' % PROJECT,
        templates='pkg',
        builder='text',
    ),

    website=Bunch(
        templates = 'web',
        builddir = 'web',
        
        # What server hosts the website?
        server = 'www.doughellmann.com',
        server_path = '/var/www/doughellmann/DocumentRoot/PyMOTW/',

        # What template should be used for the web site HTML?
        template_source = '~/Devel/doughellmann/doughellmann/templates/base.html',
        template_dest = 'sphinx/templates/web/base.html',        
    ),
    
    sitemap_gen=Bunch(
        # Where is the config file for sitemap_gen.py?
        config='sitemap_gen_config.xml',
    ),
    
    pdf=Bunch(
        templates='pkg',
        builddir='web',
        builder='latex',
    ),
    
    blog=Bunch(
        sourcedir=path(PROJECT)/MODULE,
        builddir='blog_posts',
        outdir='blog_posts',
        confdir='sphinx/blog',
        doctrees='blog_posts/doctrees',
        in_file='index.html',
        out_file='blog.html',
        no_edit=False,
    ),
    
    # Some of the files include [[[ as part of a nested list data structure,
    # so change the tags cog looks for to something less likely to appear.
    cog=Bunch(
        beginspec='{{{cog',
        endspec='}}}',
        endoutput='{{{end}}}',
        includedir='PyMOTW',
    ),

    # Tell Paver to include extra parts that we use
    # but it doesn't ship in the minilib by default.
    minilib = Bunch(
        extra_files=['doctools'],
    ),

)

# Stuff commonly used symbols into the builtins so we don't have to
# import them in all of the cog blocks where we want to use them.
__builtins__['path'] = path

# Modified from paver.doctools._runcog
from paver.doctools import Includer, _cogsh
def _runcog(options, files, uncog=False):
    """Common function for the cog and runcog tasks."""
    
    from paver.cog import Cog
    options.order('cog', 'sphinx', add_rest=True)
    c = Cog()
    if uncog:
        c.options.bNoGenerate = True
    c.options.bReplace = True
    c.options.bDeleteCode = options.get("delete_code", False)
    includedir = options.get('includedir', None)
    if includedir:
        include = Includer(includedir, cog=c, 
                           include_markers=options.get("include_markers"))
        # load cog's namespace with our convenience functions.
        c.options.defines['include'] = include
        c.options.defines['sh'] = _cogsh(c)
    
    c.sBeginSpec = options.get('beginspec', '[[[cog')
    c.sEndSpec = options.get('endspec', ']]]')
    c.sEndOutput = options.get('endoutput', '[[[end]]]')
    
    basedir = options.get('basedir', None)
    if basedir is None:
        basedir = path(options.get('docroot', "docs")) / options.get('sourcedir', "")
    basedir = path(basedir)
        
    if not files:
        pattern = options.get("pattern", "*.rst")
        if pattern:
            files = basedir.walkfiles(pattern)
        else:
            files = basedir.walkfiles()
    for f in files:
        dry("cog %s" % f, c.processOneFile, f)
#

@task
@consume_args
def cog(options):
    """Run cog against all or a subset of the input source files.
    
    Examples::
    
      $ paver cog PyMOTW/atexit
      $ paver cog PyMOTW/atexit/index.rst
      $ paver cog
    
    See help on paver.doctools.cog for details on the standard
    options.
    """
    options.order('cog', 'sphinx', add_rest=True)
    # Figure out if we were given a filename or
    # directory, and scan the directory for files
    # if we need to.
    files_to_cog = getattr(options, 'args', [])
    if files_to_cog and os.path.isdir(files_to_cog[0]):
        dir_to_scan = path(files_to_cog[0])
        files_to_cog = dir_to_scan.walkfiles(options.get("pattern", "*.rst"))
    _runcog(options, files_to_cog)
    return

def remake_directories(*dirnames):
    """Remove the directories and recreate them.
    """
    for d in dirnames:
        d = path(d)
        if d.exists():
            d.rmtree()
        d.mkdir()
    return

@task
def html(options):
    "Generate HTML files."
    set_templates(options.html.templates)
    if paverutils is None:
        raise RuntimeError('Could not find sphinxcontrib.paverutils, will not be able to build HTML output.')
    paverutils.html(options)
    return

@task
@consume_args
def tabcheck(options):
    """Run tabnanny against the current module.
    """
    args = getattr(options, 'args', [])
    if not args:
        args = path('PyMOTW').glob('*')
    tabnanny.verbose = 1
    for module in args:
        tabnanny.check(module)
    return

@task
@consume_args
def update(options):
    """Run cog against the named module, then re-build the HTML.
    
    Examples::
    
      $ paver update atexit
    """
    options.order('update', 'sphinx', add_rest=True)
    args = getattr(options, 'args', [])
    if args:
        module = args[0]
    else:
        module = MODULE
    module_dir = 'PyMOTW/' + module
    tabnanny.check(module_dir)
    options.order('cog', 'sphinx', add_rest=True)
    options.args = [module_dir]
    cog(options)
    html(options)
    return
    

@task
def text(options):
    "Generate text files from rst input."
    if paverutils is None:
        raise RuntimeError('Could not find sphinxcontrib.paverutils, will not be able to build text output.')
    paverutils.run_sphinx(options, 'text')
    return

@task
@needs(['generate_setup', 
        'minilib', 
        'cog',
        'html_clean', 
        #'text',
        'setuptools.command.sdist',
        ])
def sdist(options):
    """Create a source distribution.
    """
    # Move the output file to the desktop
    dist_files = path('dist').glob('*.tar.gz')
    dest_dir = path(options.sdistext.outdir).expanduser()
    for f in dist_files:
        dest_file = dest_dir / f.basename()
        dest_file.unlink()
        f.move(dest_dir)
    
    sh('growlnotify -m "package built"')
    return

@task
def html_clean(options):
    """Remove sphinx output directories before building the HTML.
    """
    remake_directories(options.sphinx.doctrees, options.html.outdir)
    html(options)
    return

def set_templates(template_name):
    """Set the TEMPLATES environment variable, used by sphinx/conf.py.
    """
    os.environ['TEMPLATES'] = template_name
    print 'Set TEMPLATES = "%s"' % template_name
    return

@task
def pdf():
    """Generate the PDF book.
    """
    set_templates(options.pdf.templates)
    if paverutils is None:
        raise RuntimeError('Could not find sphinxcontrib.paverutils, will not be able to build PDF output.')
    paverutils.pdf(options)
    return

@task
def website(options):
    """Create local copy of website files.
    """
    pdf(options)
    webhtml(options)
    # Copy the PDF to the files to be copied to the directory to install
    pdf_file = path(options.pdf.builddir) / 'latex' / (PROJECT + '-' + VERSION + '.pdf')
    pdf_file.copy(path(options.website.builddir) / 'html')
    return

@task
def installwebsite(options):
    """Rebuild and copy website files to the remote server.
    """
    # Clean up
    remake_directories(options.pdf.builddir, options.website.builddir)
    # Rebuild
    website(options)
    # Install
    rsyncwebsite(options)
    return
    
@task
def rsyncwebsite(options):
    # Copy to the server
    os.environ['RSYNC_RSH'] = '/usr/bin/ssh'
    src_path = path(options.website.builddir) / 'html'
    sh('(cd %s; rsync --archive --delete --verbose . %s:%s)' % 
        (src_path, options.website.server, options.website.server_path))
    return

@task
def webtemplatebase():
    """Import the latest version of the web page template from the source.
    """
    dest = path(options.website.template_dest).expanduser()
    src = path(options.website.template_source).expanduser()
    if not dest.exists() or (src.mtime > dest.mtime):
        src.copy(dest)
    return

@task
@needs(['webtemplatebase'])
def webhtml(options):
    """Generate HTML files for website.
    """
    set_templates(options.website.templates)
    if paverutils is None:
        raise RuntimeError('Could not find sphinxcontrib.paverutils, will not be able to build HTML output.')
    paverutils.run_sphinx(options, 'website')
    sitemap_gen()
    return

@task
def sitemap_gen():
    sh('sitemap_gen.py --testing --config=%s' % options.sitemap_gen.config)
    return
            

def get_post_title(filename):
    f = open(filename, 'rt')
    try:
        body = f.read()
    finally:
        f.close()

    # Clean up the HTML
    from BeautifulSoup import BeautifulSoup, Tag

    # The post body is passed to stdin.
    soup = BeautifulSoup(body)

    # Get the heading(s)
    h1 = soup.find('h1')

    # Get BeautifulSoup's version of the string
    #title = ' '.join(h1.string)
    title = ' '.join(s for s in h1 if type(s) != Tag)

    return title


def gen_blog_post(outdir, input_base, blog_base, url_base):
    """Generate the blog post body.
    """
    outdir = path(outdir)
    input_file = outdir / input_base
    blog_file = outdir/ blog_base
    
    canonical_url = "http://www.doughellmann.com/" + url_base
    if not canonical_url.endswith('/'):
        canonical_url += '/'
    if input_base != "index.html":
        canonical_url += input_base

    module_name = MODULE
    title = '%s - ' % module_name

    # Get the intro paragraph
    from BeautifulSoup import BeautifulSoup, Tag
    raw_body = input_file.text().strip()
    soup = BeautifulSoup(raw_body)
    intro = soup.find('p')

    # Strip hyperlinks by replacing those nodes with their contents.
    for link in intro.findAll('a'):
        new_span = Tag(soup, 'span')
        for c in link.contents:
            new_span.append(c)
        link.replaceWith(new_span)

    output_body = '''%(intro)s
<p><a href="%(canonical_url)s">Read more...</a></p>
''' % locals()
    blog_file.write_text(output_body)

    home_page_reference = '''<p><a class="reference external" href="http://www.doughellmann.com/PyMOTW/">PyMOTW Home</a></p>'''
    canonical_reference = '''<p>The <a class="reference external" href="%(canonical_url)s">canonical version</a> of this article</p>''' % locals()
    
    blog_file.write_text(output_body)
    return

@task
@cmdopts([
    ('in-file=', 'b', 'Blog input filename (e.g., "-b index.html")'),
    ('out-file=', 'B', 'Blog output filename (e.g., "-B blog.html")'),
    ('sourcedir=', 's', 'Source directory name (e.g., "-s PyMOTW/articles")'),
    ('no-edit', 'n', 'Do not open the post in an editor'),
])
def blog(options):
    """Generate the blog post version of the HTML for the current module.
    
    The default behavior generates the post for the current module using 
    its index.html file as input.
    
    To use a different file within the module directory, use the 
    --in-file or -b option::
    
      paver blog -b communication.html
      
    To run against a directory other than a module, use the 
    -s or --sourcedir option::
    
      paver blog -s PyMOTW/articles -b text_processing.html
    """    
    # Clean and recreate output directory
    remake_directories(options.blog.outdir)
    
    # Generate html from sphinx
    if paverutils is None:
        raise RuntimeError('Could not find sphinxcontrib.paverutils, will not be able to build HTML output.')
    paverutils.run_sphinx(options, 'blog')
    
    blog_file = path(options.blog.outdir) / options.blog.out_file
    dry("Write blog post body to %s" % blog_file, 
        gen_blog_post, 
        outdir=options.blog.outdir, 
        input_base=options.blog.in_file, 
        blog_base=options.blog.out_file,
        url_base=options.blog.sourcedir,
        )

    title = get_post_title(path(options.blog.outdir) / options.blog.in_file)
    
    if not options.no_edit:
        if os.path.exists('bin/SendToMarsEdit.applescript'):
            sh('osascript bin/SendToMarsEdit.applescript "%s" "%s"' % 
                (blog_file, "PyMOTW: %s" % title)
                )

        elif 'EDITOR' in os.environ:
            sh('$EDITOR %s' % blog_file)
    return
    

@task
@needs(['uncog'])
def commit():
    """Commit the changes to hg.
    """
    sh('hg commit')
    return

@task
@needs(['uncog'])
def bitbucket_push(options):
    sh('hg push')
    return

@task
def release(options):
    """Run the automatable steps of the release process."""
    sdist(options)
    installwebsite(options)
    blog(options)
    bitbucket_push(options)
    print 'NEXT: upload package, "paver register", post to blog'
    return

@task
def checklist(options):
    """Show the release checklist.
    """
    print """
Checklist
=========    

- hg pull into src sandbox
- Change version in pavement.py
- Update history file
- hg commit
- hg tag
- paver sdist
- Upload package
- paver installwebsite
- paver register
- paver blog
- Post to blog
- Post to O'Reilly
- hg push from src to bitbucket
    """
