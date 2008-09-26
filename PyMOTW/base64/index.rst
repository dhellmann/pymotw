==================================================
base64 -- Encode binary data into ASCII characters
==================================================

.. module:: base64
    :synopsis: Encode binary data into ASCII characters.

:Purpose: The base64 module contains functions for translating binary data into a subset of ASCII suitable for transmission using plaintext protocols.
:Python Version: 1.4 and later

The base64, base32, and base16 encodings convert 8 bit bytes to values with 6, 5, or 4 bits of useful data per byte, allowing non-ASCII bytes to be encoded as ASCII characters for transmission over protocols that require plain ASCII, such as SMTP.  The *base* values correspond to the length of the alphabet used in each encoding.  There are also URL-safe variations of the original encodings that use slightly different results.

Base 64 Encoding
================

A basic example of encoding some text looks like this:

.. include:: base64_b64encode.py
    :literal:
    :start-after: #end_pymotw_header

The output shows the 558 bytes of the original source expand to 744 bytes after being encoded.

.. note::
    There are no carriage returns in the output produced by the library, but I have inserted them in the output here to make this page render more cleanly in HTML.

::

    558 bytes before encoding
    Expect 0 padding bytes
    744 bytes after encoding

    IyEvdXNyL2Jpbi9lbnYgcHl0aG9uCiMgZW5
    jb2Rpbmc6IHV0Zi04CiMKIyBDb3B5cmlnaH
    QgKGMpIDIwMDggRG91ZyBIZWxsbWFubiBBb
    GwgcmlnaHRzIHJlc2VydmVkLgojCiIiIgoi
    IiIKCl9fdmVyc2lvbl9fID0gIiRJZDogYmF
    zZTY0X2I2NGVuY29kZS5weSAxNTI1IDIwMD
    gtMDctMjAgMTM6MjM6MzVaIGRoZWxsbWFub
    iAkIgojZW5kX3B5bW90d19oZWFkZXIKCmlt
    cG9ydCBiYXNlNjQKCmluaXRpYWxfZGF0YSA
    9IG9wZW4oX19maWxlX18sICdydCcpLnJlYW
    QoKQoKZW5jb2RlZF9kYXRhID0gYmFzZTY0L
    mI2NGVuY29kZShpbml0aWFsX2RhdGEpCgpu
    dW1faW5pdGlhbCA9IGxlbihpbml0aWFsX2R
    hdGEpCnBhZGRpbmcgPSB7IDA6MCwgMToyLC
    AyOjEgfVtudW1faW5pdGlhbCAlIDNdCgpwc
    mludCAnJWQgYnl0ZXMgYmVmb3JlIGVuY29k
    aW5nJyAlIG51bV9pbml0aWFsCnByaW50ICd
    FeHBlY3QgJWQgcGFkZGluZyBieXRlcycgJS
    BwYWRkaW5nCnByaW50ICclZCBieXRlcyBhZ
    nRlciBlbmNvZGluZycgJSBsZW4oZW5jb2Rl
    ZF9kYXRhKQpwcmludApwcmludCBlbmNvZGV
    kX2RhdGEK


Base 64 Decoding
================

The encoded string can be converted back to the original form by taking 4 bytes and converting them to the original 3, using a reverse lookup.  The ``b64decode()`` function does that for you.

.. include:: base64_b64decode.py
    :literal:
    :start-after: #end_pymotw_header

The encoding process looks at each sequence of 24 bits in the input (3 bytes) and encodes those same 24 bits spread over 4 bytes in the output.  The last two characters, the ``==``, are padding because the number of bits in the original string was not evenly divisible by 24 in this example.

::

    Original: This is the data, in the clear.
    Encoded : VGhpcyBpcyB0aGUgZGF0YSwgaW4gdGhlIGNsZWFyLg==
    Decoded : This is the data, in the clear.

URL-safe Variations
===================

Because the default base64 alphabet may use ``+`` and ``/``, and those two characters are used in URLs, it became necessary to specify an alternate encoding with substitutes for those characters.  The ``+`` is replaced with a ``-``, and ``/`` is replaced with underscore (``_``).  Otherwise, the alphabet is the same.

.. include:: base64_urlsafe.py
    :literal:
    :start-after: #end_pymotw_header

::

    Original         : '\xfb\xef'
    Standard encoding: ++8=
    URL-safe encoding: --8=

    Original         : '\xff\xff'
    Standard encoding: //8=
    URL-safe encoding: __8=


Other Encodings
===============

Besides base 64, the module provides functions for working with base 32 and base 16 (hex) encoded data.

.. include:: base64_base32.py
    :literal:
    :start-after: #end_pymotw_header

::

    Original: This is the data, in the clear.
    Encoded : KRUGS4ZANFZSA5DIMUQGIYLUMEWCA2LOEB2GQZJAMNWGKYLSFY======
    Decoded : This is the data, in the clear.

The base 16 functions work with the hexadecimal alphabet.

.. include:: base64_base16.py
    :literal:
    :start-after: #end_pymotw_header

::

    Original: This is the data, in the clear.
    Encoded : 546869732069732074686520646174612C20696E2074686520636C6561722E
    Decoded : This is the data, in the clear.

References
==========

`RFC 3548 - The Base16, Base32, and Base64 Data Encodings <http://www.faqs.org/rfcs/rfc3548.html>`_

Standard library documentation: `base64 <http://docs.python.org/lib/module-base64.html>`_
