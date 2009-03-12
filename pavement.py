#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
TODO

 - make sure all of the files from the manifests are included
 
"""

__version__ = "$Id$"

# Standard library
import os

# Third-party
import cog
import paver
import paver.doctools
import sphinx

# TODO
# - move these variables to options?
# - see about adding more args to sphinx runner to avoid having to write my own
# 

# What project are we building?
PROJECT = 'PyMOTW'

# What version is this? (take from path in svn tree)
VERSION = '1.85.1'

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
PACKAGE_DATA = setuputils.find_package_data(PROJECT, 
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
        packages = sorted(PACKAGE_DATA.keys()),
        package_data=PACKAGE_DATA,
        zip_safe=False,

        ),
    
    sdist = Bunch(
        outdir='~/Desktop',
    ),
    
    sphinx = Bunch(
        sourcedir=PROJECT,
        docroot = '.',
        builder = 'html',
        doctrees='sphinx/doctrees',
        confdir = 'sphinx',
    ),

    html = Bunch(
        builddir='docs',
        outdir='docs',
        templates='pkg',
    ),

    website=Bunch(
        templates = 'web',
        builddir = 'web',
        
        # What server hosts the website?
        server = 'www.doughellmann.com',
        server_path = '/var/www/doughellmann/DocumentRoot/PyMOTW/',
        # What template should be used for the web site HTML?
        template_source = '~/Devel/personal/doughellmann/templates/base.html',
        template_dest = 'sphinx/templates/web/base.html',
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
    ),
    
    # Some of the files include [[[ as part of a nested list data structure,
    # so change the tags cog looks for to something less likely to appear.
    cog=Bunch(
        beginspec='{{{cog',
        endspec='}}}',
        endoutput='{{{end}}}',
    ),

)

def run_script(input_file, script_name, interpreter='python', include_prefix=True):
    """Run a script in the context of the input_file's directory, 
    return the text output formatted to be included as an rst
    literal text block.
    """
    from paver.runtime import sh
    from paver.path import path
    rundir = path(input_file).dirname()
    output_text = sh('cd %(rundir)s; %(interpreter)s %(script_name)s 2>&1' % vars(),
                    capture=True)
    if include_prefix:
        response = '\n::\n\n'
    else:
        response = ''
    response += '\t$ %(interpreter)s %(script_name)s\n\t' % vars()
    response += '\n\t'.join(output_text.splitlines())
    while not response.endswith('\n\n'):
        response += '\n'
    return response
# Stuff run_script() into the builtins so we don't have to
# import it in all of the cog blocks where we want to use it.
__builtins__['run_script'] = run_script

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
@needs(['generate_setup', 'minilib', 'html_clean', 
        'setuptools.command.sdist'
        ])
def sdist():
    """Create a source distribution.
    """
    # Copy the output file to the desktop
    dist_files = path('dist').glob('*.tar.gz')
    dest_dir = path(options.sdist.outdir).expanduser()
    for f in dist_files:
        f.move(dest_dir)
    return

@task
def html_clean():
    """Remove sphinx output directories before building the HTML.
    """
    remake_directories(options.sphinx.doctrees, options.html.outdir)
    call_task('html')
    return

###########################
# Adapted from paver source

def _get_paths():
    """look up the options that determine where all of the files are."""
    opts = options
    
    docroot = path(opts.get('docroot', 'docs'))
    if not docroot.exists():
        raise BuildFailure("Sphinx documentation root (%s) does not exist."
                           % docroot)
    
    builddir = docroot / opts.get("builddir", ".build")
    builddir.mkdir()
    
    srcdir = docroot / opts.get("sourcedir", "")
    if not srcdir.exists():
        raise BuildFailure("Sphinx source file dir (%s) does not exist" 
                            % srcdir)
    
    # Where is the sphinx conf.py file?
    confdir = path(opts.get('confdir', srcdir))
    
    # Where should output files be generated?
    outdir = opts.get('outdir', '')
    if outdir:
        outdir = path(outdir)
    else:
        outdir = builddir / opts.get('builder', 'html')
    outdir.mkdir()
    
    # Where are doctrees cached?
    doctrees = opts.get('doctrees', '')
    if not doctrees:
        doctrees = builddir / "doctrees"
    else:
        doctrees = path(doctrees)
    doctrees.mkdir()

    return Bunch(locals())

def run_sphinx(*option_sets):
    """Helper function to run sphinx with common options.
    
    Pass the names of namespaces to be used in the search path
    for options.
    """
    if 'sphinx' not in option_sets:
        option_sets += ('sphinx',)
    kwds = dict(add_rest=False)
    options.order(*option_sets, **kwds)
    paths = _get_paths()
    sphinxopts = ['', 
                  '-b', options.get('builder', 'html'), 
                  '-d', paths.doctrees, 
                  '-c', paths.confdir,
                  paths.srcdir, paths.outdir]
    dry("sphinx-build %s" % (" ".join(sphinxopts),), sphinx.main, sphinxopts)
    return

@task
@needs(['cog'])
def html():
    """Build HTML documentation using Sphinx. This uses the following
    options in a "sphinx" section of the options.
    
    docroot
      the root under which Sphinx will be working.
      default: docs
    builddir
      directory under the docroot where the resulting files are put.
      default: build
    sourcedir
      directory under the docroot for the source files
      default: (empty string)
    doctrees
      the location of the cached doctrees
      default: $builddir/doctrees
    confdir
      the location of the sphinx conf.py
      default: $sourcedir
    outdir
      the location of the generated output files
      default: $builddir/$builder
    builder
      the name of the sphinx builder to use
      default: html
    """
    set_templates(options.html.templates)
    run_sphinx('html')
    return

###########################

def set_templates(template_name):
    """Set the TEMPLATES environment variable, used by sphinx/conf.py.
    """
    os.environ['TEMPLATES'] = template_name
    print 'Set TEMPLATES = "%s"' % template_name
    return

@task
@needs(['cog'])
def pdf():
    """Generate the PDF book.
    """
    set_templates(options.pdf.templates)
    run_sphinx('pdf')
    latex_dir = path(options.pdf.builddir) / 'latex'
    sh('cd %s; make' % latex_dir)
    return

@task
@needs([ 'webhtml', 'pdf'])
def website():
    """Create local copy of website files.
    """
    # Copy the PDF to the files to be copied to the directory to install
    pdf_file = path(options.pdf.builddir) / 'latex' / (PROJECT + '-' + VERSION + '.pdf')
    pdf_file.copy(path(options.website.builddir) / 'html')
    return

@task
def installwebsite():
    """Rebuild and copy website files to the remote server.
    """
    # Clean up
    remake_directories(options.pdf.builddir, options.website.builddir)
    # Rebuild
    call_task('website')
    # Copy to the server
    os.environ['RSYNC_RSH'] = '/usr/bin/ssh'
    src_path = path(options.website.builddir) / 'html'
    sh('cd %s; rsync --archive --delete --verbose . %s:%s' % 
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
@needs(['webtemplatebase', 'cog'])
def webhtml():
    """Generate HTML files for website.
    """
    set_templates(options.website.templates)
    run_sphinx('website')
    return

def clean_blog_html(body):
    # Clean up the HTML
    import re
    import sys
    from BeautifulSoup import BeautifulSoup
    from cStringIO import StringIO

    # The post body is passed to stdin.
    soup = BeautifulSoup(body)

    # Remove the permalinks to each header since the blog does not have
    # the styles to hide them.
    links = soup.findAll('a', attrs={'class':"headerlink"})
    [l.extract() for l in links]

    # Get BeautifulSoup's version of the string
    s = soup.__str__(prettyPrint=False)

    # Remove extra newlines.  This depends on the fact that
    # code blocks are passed through pygments, which wraps each part of the line
    # in a span tag.
    pattern = re.compile(r'([^s][^p][^a][^n]>)\n$', re.DOTALL|re.IGNORECASE)
    s = ''.join(pattern.sub(r'\1', l) for l in StringIO(s))
    
    return s

def gen_blog_post(index_file, blog_file):
    """Generate the blog post body.
    """
    # Add link to project home page at the end
    body = index_file.text().strip()
    output_body = clean_blog_html(body) + '''<p><a class="reference external" href="http://www.doughellmann.com/PyMOTW/">PyMOTW Home</a></p>'''
    
    blog_file.write_text(output_body)
    return

@task
@needs(['cog'])
def blog():
    """Generate the blog post version of the HTML for the current module.
    """
    # Clean and recreate output directory
    remake_directories(options.blog.outdir)
    outdir = path(options.blog.outdir)
    
    # Generate html from sphinx
    run_sphinx('blog')
    
    index_file = outdir / 'index.html'
    blog_file = outdir / 'blog.html'
    dry("Write blog post body to %s" % blog_file, 
        gen_blog_post, index_file=index_file, blog_file=blog_file)
    
    if 'EDITOR' in os.environ:
        sh('$EDITOR %s' % blog_file)
    return
    