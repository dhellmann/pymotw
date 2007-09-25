#
# $Id$
#

SVNHOME=$(shell svn info | grep "^URL" | cut -f2- -d:)
PROJECT=PyMOTW
VERSION=$(shell basename $(SVNHOME))
RELEASE=$(PROJECT)-$(VERSION)

package: setup.py MANIFEST.in
	python setup.py sdist --force-manifest
	mv dist/*.gz ~/Desktop/

register: setup.py
	python setup.py register

%: %.in
	cat $< | sed 's/VERSION/$(VERSION)/g' > $@

clean:
	rm -f MANIFEST
	rm -rf dist

help:
	@echo "package - build tarball"
	@echo "register - update PyPI (update VERSION first!)"
	@echo "clean - remove build left-overs"
