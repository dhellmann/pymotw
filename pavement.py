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
import traceback
import types

# Third-party
import sphinx

# Set up Paver
import paver
import paver.doctools
import paver.misctasks
from paver.path import path
from paver.easy import *
import paver.setuputils
paver.setuputils.install_distutils_tasks()
try:
    from sphinxcontrib import paverutils
except:
    import warnings
    warnings.warn('Could not find sphinxcontrib.paverutils, will not be able to build HTML or PDF output.')

# TODO
# - move these variables to options?

# What project are we building?
PROJECT = 'PyMOTW'

# What version is this?
VERSION = '1.93'

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
        packages = sorted(PACKAGE_DATA.keys()),
        package_data=PACKAGE_DATA,
        zip_safe=False,

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

def run_script(input_file, script_name, 
                interpreter='python',
                include_prefix=True, 
                ignore_error=False, 
                trailing_newlines=True,
                ):
    """Run a script in the context of the input_file's directory, 
    return the text output formatted to be included as an rst
    literal text block.
    
    Arguments:
    
     input_file
       The name of the file being processed by cog.  Usually passed as cog.inFile.
     
     script_name
       The name of the Python script living in the same directory as input_file to be run.
       If not using an interpreter, this can be a complete command line.  If using an
       alternate interpreter, it can be some other type of file.
     
     include_prefix=True
       Boolean controlling whether the :: prefix is included.
     
     ignore_error=False
       Boolean controlling whether errors are ignored.  If not ignored, the error
       is printed to stdout and then the command is run *again* with errors ignored
       so that the output ends up in the cogged file.
     
     trailing_newlines=True
       Boolean controlling whether the trailing newlines are added to the output.
       If False, the output is passed to rstrip() then one newline is added.  If
       True, newlines are added to the output until it ends in 2.
    """
    rundir = path(input_file).dirname()
    if interpreter:
        cmd = '%(interpreter)s %(script_name)s' % vars()
    else:
        cmd = script_name
    real_cmd = 'cd %(rundir)s; %(cmd)s 2>&1' % vars()
    try:
        output_text = sh(real_cmd, capture=True, ignore_error=ignore_error)
    except Exception, err:
        print '*' * 50
        print 'ERROR run_script(%s) => %s' % (real_cmd, err)
        print '*' * 50
        output_text = sh(real_cmd, capture=True, ignore_error=True)
        print output_text
        print '*' * 50
    if include_prefix:
        response = '\n::\n\n'
    else:
        response = ''
    response += '\t$ %(cmd)s\n\t' % vars()
    response += '\n\t'.join(output_text.splitlines())
    if trailing_newlines:
        while not response.endswith('\n\n'):
            response += '\n'
    else:
        response = response.rstrip()
        response += '\n'
    return response

# Stuff commonly used symbols into the builtins so we don't have to
# import them in all of the cog blocks where we want to use them.
__builtins__['path'] = path
__builtins__['run_script'] = run_script
#__builtins__['sh'] = sh

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
@needs(['cog'])
def html(options):
    set_templates(options.html.templates)
    paverutils.html(options)
    return

@task
@needs(['generate_setup', 'minilib', 
        'html_clean', 
        'setuptools.command.sdist'
        ])
def sdist(options):
    """Create a source distribution.
    """
    # Copy the output file to the desktop
    dist_files = path('dist').glob('*.tar.gz')
    dest_dir = path(options.sdistext.outdir).expanduser()
    for f in dist_files:
        f.move(dest_dir)
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
@needs(['cog'])
def pdf():
    """Generate the PDF book.
    """
    set_templates(options.pdf.templates)
    paverutils.pdf(options)
    return

@task
def website(options):
    """Create local copy of website files.
    """
    pdf(options) # this also calls cog
    webhtml(options) # this does not call cog
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
@needs(['webtemplatebase', 'sitemap_gen'])
def webhtml(options):
    """Generate HTML files for website.
    """
    set_templates(options.website.templates)
    paverutils.run_sphinx(options, 'website')
    sitemap_gen()
    return

@task
def sitemap_gen():
    sh('sitemap_gen.py --testing --config=%s' % options.sitemap_gen.config)
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
    s = str(soup)

    # Remove extra newlines.  This depends on the fact that
    # code blocks are passed through pygments, which wraps each part of the line
    # in a span tag.
    pattern = re.compile(r'([^s][^p][^a][^n]>)\n$', re.DOTALL|re.IGNORECASE)
    s = ''.join(pattern.sub(r'\1', l) for l in StringIO(s))
    
    return s

def gen_blog_post(outdir, input_base, blog_base):
    """Generate the blog post body.
    """
    outdir = path(outdir)
    input_file = outdir / input_base
    blog_file = outdir/ blog_base
    
    canonical_url = "http://www.doughellmann.com/PyMOTW/" + MODULE + "/"
    if input_base != "index.html":
        canonical_url += input_base
    home_page_reference = '''<p><a class="reference external" href="http://www.doughellmann.com/PyMOTW/">PyMOTW Home</a></p>'''
    canonical_reference = '''<p>The <a class="reference external" href="%(canonical_url)s">canonical version</a> of this article</p>''' % locals()
    
    # Add links to project pages at the end
    body = input_file.text().strip()
    output_body = clean_blog_html(body) + home_page_reference + canonical_reference
    
    blog_file.write_text(output_body)
    return

@task
@needs(['cog'])
@cmdopts([
    ('in-file=', 'b', 'Blog input filename'),
    ('out-file=', 'B', 'Blog output filename'),    
])
def blog(options):
    """Generate the blog post version of the HTML for the current module.
    """
    # Clean and recreate output directory
    remake_directories(options.blog.outdir)
    
    # Generate html from sphinx
    paverutils.run_sphinx(options, 'blog')
    
    blog_file = path(options.blog.outdir) / options.blog.out_file
    dry("Write blog post body to %s" % blog_file, 
        gen_blog_post, 
        outdir=options.blog.outdir, 
        input_base=options.blog.in_file, 
        blog_base=options.blog.out_file,
        )
    
    if 'EDITOR' in os.environ:
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