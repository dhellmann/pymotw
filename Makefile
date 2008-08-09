#
# $Id$
#

SVNHOME=$(shell svn info | grep "^URL" | cut -f2- -d:)
PROJECT=PyMOTW
VERSION=$(shell basename $(SVNHOME))
RELEASE=$(PROJECT)-$(VERSION)

package: setup.py html_docs
	rm -f MANIFEST.in
	$(MAKE) MANIFEST.in
	python setup.py sdist --force-manifest
	mv dist/*.gz ~/Desktop/

.PHONEY: html_docs
html_docs:
	mkdir -p html
	sphinx-build -b html $(PROJECT) html/
	
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

help:
	@echo "package - build tarball"
	@echo "register - update PyPI (update VERSION first!)"
	@echo "clean - remove build left-overs"
