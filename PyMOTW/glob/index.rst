===========
glob
===========
.. module:: glob
    :synopsis: Use Unix shell rules to fine filenames matching a pattern.

:Module: glob
:Purpose: Use Unix shell rules to fine filenames matching a pattern.
:Python Version: 1.4

Description
===========

Even though the glob API is very simple, the module packs a lot of power. It
is useful in any situation where your program needs to look for a list of
files on the filesystem with names matching a pattern. If you need a list of
filenames that all have a certain extension, prefix, or any common string in
the middle, use glob instead of writing code to scan the directory contents
yourself.

The pattern rules for glob are not regular expressions. Instead, they follow
standard Unix path expansion rules. Shell variable names and tilde (~) are not
expanded. There are only a few special characters: two different wild-cards,
and character ranges are supported. The patterns rules are applied to segments
of the filename (stopping at /), but paths in the pattern can be relative or
absolute.

Example Data
============

The examples below assume the following test files are present in the current
working directory:

::

    dir/
    dir/file.txt
    dir/file1.txt
    dir/file2.txt
    dir/filea.txt
    dir/fileb.txt
    dir/subdir/
    dir/subdir/subfile.txt

Use the glob_maketestdata.py script in the sample code to create these files
if you want to run the examples.

Wildcards
=========

An asterisk (`*`) matches zero or more characters in a segment of a name. For
example, `dir/*`.

::

    import glob
    print glob.glob('dir/*')

The pattern matches every pathname (file or directory) in the directory dir,
without recursing further into subdirectories.

::

    $ python glob_asterisk.py
    ['dir/file.txt', 'dir/file1.txt', 'dir/file2.txt',
    'dir/filea.txt', 'dir/fileb.txt', 'dir/subdir']

To list files in a subdirectory, you must include the subdirectory in the
pattern:

::

    print 'Named explicitly:'
    print glob.glob('dir/subdir/*')

    print 'Named with wildcard:'
    print glob.glob('dir/*/*')

The first case above lists the subdirectory name explicitly, while the second
case depends on a wildcard to find the directory.

::

    $ python glob_subdir.py
    Named explicitly:
    ['dir/subdir/subfile.txt']
    Named with wildcard:
    ['dir/subdir/subfile.txt']

The results, in this case, are the same. If there was another subdirectory,
the wildcard would match both subdirectories and include the filenames from
both.

Single Character Wildcard
=========================

The other wildcard character supported is the question mark (?). It matches
any single character in that position in the name. For example,

::

    print glob.glob('dir/file?.txt')

Matches all of the filenames which begin with "file", have one more character
of any type, then end with ".txt".

::

    $ python glob_question.py
    ['dir/file1.txt', 'dir/file2.txt',
    'dir/filea.txt', 'dir/fileb.txt']


Character Ranges
================

When you need to match a specific character, use a character range instead of
a question mark. For example, to find all of the files which have a digit in
the name before the extension:

::

    print glob.glob('dir/*[0-9].*')

The character range [0-9] matches any single digit. The range is ordered based
on the character code for each letter/digit, and the dash indicates an
unbroken range of sequential characters. The same range value could be written
[0123456789], in this case.

::

    $ python glob_charrange.py
    ['dir/file1.txt', 'dir/file2.txt']


