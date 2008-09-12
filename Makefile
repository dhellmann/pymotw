#
# $Id$
#

SVNHOME=$(shell svn info | grep "^URL" | cut -f2- -d:)
PROJECT=PyMOTW
VERSION=$(shell basename $(SVNHOME))
export VERSION
RELEASE=$(PROJECT)-$(VERSION)

help:
	@echo "package        - build tarball"
	@echo "installwebsite - copy new HTML files to website"
	@echo "webisite       - build new HTML files for website but do not install"
	@echo "register       - update PyPI"
	@echo "clean          - remove build left-overs"
	@echo "html_docs      - run sphinx to create docs to go in package"
	@echo "blog           - run sphinx to create the blog post"

package: setup.py html_docs website
	rm -f MANIFEST.in
	$(MAKE) MANIFEST.in
	python setup.py sdist --force-manifest
	mv dist/*.gz ~/Desktop/

.PHONEY: html_docs
html_docs:
	mkdir -p docs
	TEMPLATES='pkg' sphinx-build -b html -d sphinx/doctrees -c sphinx $(PROJECT) docs/

export MODULE=$(shell cat module)
.PHONEY: blog
blog: module
	mkdir -p blog_posts
	sphinx-build -b html -d blog_posts -c sphinx/blog $(PROJECT)/$(MODULE)/ blog_posts/

.PHONEY: website
website: sphinx/templates/web/base.html
	mkdir -p web
	TEMPLATES='web' sphinx-build -a -b html -d sphinx/doctrees -c sphinx $(PROJECT) web/

sphinx/templates/web/base.html: $(HOME)/Devel/personal/doughellmann/templates/base.html
	cp $< $@

.PHONEY: installwebsite
installwebsite: website
	scp -r web/* homer:/var/www/doughellmann/DocumentRoot/PyMOTW/
	
MANIFESTS=MANIFEST.in.in $(wildcard PyMOTW/*/MANIFEST.in)

.PHONEY: MANIFEST.in
MANIFEST.in: $(MANIFESTS)
	cat $(MANIFESTS) > MANIFEST.in

register: setup.py
	python setup.py register

%: %.in
	cat $< | sed 's/VERSION/$(VERSION)/g' > $@

setup.py: module setup.py.in
	cat setup.py.in | sed 's/VERSION/$(VERSION)/g' | sed "s/MODULE/`cat module`/g" > $@

clean:
	rm -f MANIFEST
	rm -rf dist
	rm -rf docs

