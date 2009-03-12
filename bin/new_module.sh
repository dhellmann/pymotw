#!/bin/sh
#
# $Id: new_module.sh 1692 2008-09-26 19:19:35Z dhellmann $
#
# Create a new module directory.
#

name="$1"
if [ "$name" = "" ]
then
	echo "Usage: $0 module_name"
	echo "Creates PyMOTW/module_name and contents"
	exit 1
fi

bindir=`dirname $0`
module_dir=PyMOTW/$name

echo "Creating module directory and contents ..."
mkdir $module_dir
touch $module_dir/__init__.py
cat $bindir/template.rst | sed "s/MODULE/$name/g" > $module_dir/index.rst
echo $name > module
