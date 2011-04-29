======================================
uuid -- Universally unique identifiers
======================================

.. module:: uuid
    :synopsis: Universally unique identifiers

:Purpose: The :mod:`uuid` module implements Universally Unique Identifiers as described in :rfc:`4122`.
:Available In: 2.5 and later

:rfc:`4122` defines a system for creating universally unique
identifiers for resources in a way that does not require a central
registrar. UUID values are 128 bits long and "can guarantee uniqueness
across space and time". They are useful for identifiers for documents,
hosts, application clients, and other situations where a unique value
is necessary. The RFC is specifically geared toward creating a Uniform
Resource Name namespace.

Three main algorithms are covered by the spec:

+ Using IEEE 802 MAC addresses as a source of uniqueness
+ Using pseudo-random numbers
+ Using well-known strings combined with cryptographic hashing

In all cases the seed value is combined with the system clock and a
clock sequence value (to maintain uniqueness in case the clock was set
backwards).

UUID 1 - IEEE 802 MAC Address
=============================

UUID version 1 values are computed using the MAC address of the host.
The :mod:`uuid` module uses :func:`getnode()` to retrieve the MAC
value on a given system:


.. include:: uuid_getnode.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'uuid_getnode.py'))
.. }}}
.. {{{end}}}

If a system has more than one network card, and so more than one MAC,
any one of the values may be returned.

To generate a UUID for a given host, identified by its MAC address,
use the :func:`uuid1()` function. You can pass a node identifier, or
leave the field blank to use the value returned by :func:`getnode()`.


.. include:: uuid_uuid1.py
    :literal:
    :start-after: #end_pymotw_header


The components of the UUID object returned can be accessed through
read-only instance attributes. Some attributes, such as *hex*, *int*,
and *urn*, are different representations of the UUID value.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'uuid_uuid1.py'))
.. }}}
.. {{{end}}}

Because of the time component, each time :func:`uuid1()` is called a
new value is returned.

.. include:: uuid_uuid1_repeat.py
    :literal:
    :start-after: #end_pymotw_header


Notice in this output that only the time component (at the beginning
of the string) changes.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'uuid_uuid1_repeat.py'))
.. }}}
.. {{{end}}}

Because your computer has a different MAC address than mine, you will
see entirely different values if you run the examples, because the
node identifier at the end of the UUID will change, too.

.. include:: uuid_uuid1_othermac.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'uuid_uuid1_othermac.py'))
.. }}}
.. {{{end}}}


UUID 3 and 5 - Name-Based Values
================================

It is also useful in some contexts to create UUID values from names
instead of random or time-based values. Versions 3 and 5 of the UUID
specification use cryptographic hash values (MD5 or SHA-1) to combine
namespace-specific seed values with "names" (DNS hostnames, URLs,
object ids, etc.). There are several well-known namespaces, identified
by pre-defined UUID values, for working with DNS, URLs, ISO OIDs, and
X.500 Distinguished Names. You can also define your own application-
specific namespaces by generating and saving UUID values.

To create a UUID from a DNS name, pass ``uuid.NAMESPACE_DNS`` as the
namespace argument to :func:`uuid3()` or :func:`uuid5()`:

.. include:: uuid_uuid3_uuid5.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'uuid_uuid3_uuid5.py'))
.. }}}
.. {{{end}}}

The UUID value for a given name in a namespace is always the same, no
matter when or where it is calculated. Values for the same name in
different namespaces are different.

.. include:: uuid_uuid3_repeat.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'uuid_uuid3_repeat.py'))
.. }}}
.. {{{end}}}


UUID 4 - Random Values
======================

Sometimes host-based and namespace-based UUID values are not
"different enough". For example, in cases where you want to use the
UUID as a lookup key, a more random sequence of values with more
differentiation is desirable to avoid collisions in a hash
table. Having values with fewer common digits also makes it easier to
find them in log files. To add greater differentiation in your UUIDs,
use :func:`uuid4()` to generate them using random input values.

.. include:: uuid_uuid4.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'uuid_uuid4.py'))
.. }}}
.. {{{end}}}


Working with UUID Objects
=========================

In addition to generating new UUID values, you can parse strings in
various formats to create UUID objects. This makes it easier to
compare them, sort them, etc.

.. include:: uuid_uuid_objects.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'uuid_uuid_objects.py'))
.. }}}
.. {{{end}}}

.. seealso::

    `uuid <http://docs.python.org/lib/module-uuid.html>`_
        Standard library documentation for this module.

    :rfc:`4122`
        A Universally Unique IDentifier (UUID) URN Namespace
