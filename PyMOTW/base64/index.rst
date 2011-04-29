==================================================
base64 -- Encode binary data into ASCII characters
==================================================

.. module:: base64
    :synopsis: Encode binary data into ASCII characters.

:Purpose: The base64 module contains functions for translating binary data into a subset of ASCII suitable for transmission using plaintext protocols.
:Available In: 1.4 and later

The base64, base32, and base16 encodings convert 8 bit bytes to values with 6, 5, or 4 bits of useful data per byte, allowing non-ASCII bytes to be encoded as ASCII characters for transmission over protocols that require plain ASCII, such as SMTP.  The *base* values correspond to the length of the alphabet used in each encoding.  There are also URL-safe variations of the original encodings that use slightly different results.

Base 64 Encoding
================

A basic example of encoding some text looks like this:

.. include:: base64_b64encode.py
    :literal:
    :start-after: #end_pymotw_header

The output shows the 558 bytes of the original source expand to 744 bytes after being encoded.

.. note::
    There are no carriage returns in the output produced by the library, so I have broken the encoded data up artificially to make it fit better on the page.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'base64_b64encode.py'))
.. }}}
.. {{{end}}}


Base 64 Decoding
================

The encoded string can be converted back to the original form by taking 4 bytes and converting them to the original 3, using a reverse lookup.  The ``b64decode()`` function does that for you.

.. include:: base64_b64decode.py
    :literal:
    :start-after: #end_pymotw_header

The encoding process looks at each sequence of 24 bits in the input (3 bytes) and encodes those same 24 bits spread over 4 bytes in the output.  The last two characters, the ``==``, are padding because the number of bits in the original string was not evenly divisible by 24 in this example.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'base64_b64decode.py'))
.. }}}
.. {{{end}}}

URL-safe Variations
===================

Because the default base64 alphabet may use ``+`` and ``/``, and those two characters are used in URLs, it became necessary to specify an alternate encoding with substitutes for those characters.  The ``+`` is replaced with a ``-``, and ``/`` is replaced with underscore (``_``).  Otherwise, the alphabet is the same.

.. include:: base64_urlsafe.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'base64_urlsafe.py'))
.. }}}
.. {{{end}}}


Other Encodings
===============

Besides base 64, the module provides functions for working with base 32 and base 16 (hex) encoded data.

.. include:: base64_base32.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'base64_base32.py'))
.. }}}
.. {{{end}}}

The base 16 functions work with the hexadecimal alphabet.

.. include:: base64_base16.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'base64_base16.py'))
.. }}}
.. {{{end}}}

.. seealso::

    `base64 <http://docs.python.org/library/base64.html>`_
        The standard library documentation for this module.

    :rfc:`3548`
        The Base16, Base32, and Base64 Data Encodings
