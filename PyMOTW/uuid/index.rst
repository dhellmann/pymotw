======================================
uuid -- Universally unique identifiers
======================================

.. module:: uuid
    :synopsis: Universally unique identifiers

:Purpose: The `uuid` module implements Universally Unique Identifiers as described in RFC 4122.
:Python Version: 2.5 and later

RFC 4122 defines a system for creating universally unique identifiers
for resources in a way that does not require a central registrar. UUID
values are 128 bits long and "can guarantee uniqueness across space
and time". They are useful for ids for documents, hosts, application
clients, and other situations where a unique value is necessary. The
RFC is specifically geared toward creating a Uniform Resource Name
namespace.

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
The `uuid` module uses `getnode()` to retrieve the MAC value on a
given system:


.. include:: uuid_getnode.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python uuid_getnode.py
    0x1ec200d9e0L

If a system has more than one network card, and so more than one MAC,
any one of the values may be returned.

To generate a UUID for a given host, identified by its MAC address,
use the `uuid1()` function. You can pass a node identifier, or leave
the field blank to use the value returned by `getnode()`.


.. include:: uuid_uuid1.py
    :literal:
    :start-after: #end_pymotw_header


The components of the UUID object returned can be accessed through
read-only instance attributes. Some attributes, such as hex, int, and
urn, are different representations of the UUID value.

::

    $ python uuid_uuid1.py
    6e1680de-8c15-11dd-82d9-001ec200d9e0
    <class 'uuid.UUID'>
    bytes   : 'n\x16\x80\xde\x8c\x15\x11\xdd\x82\xd9\x00\x1e\xc2\x00\xd9\xe0'
    hex     : 6e1680de8c1511dd82d9001ec200d9e0
    int     : 146331923847663230991333091899900746208
    urn     : urn:uuid:6e1680de-8c15-11dd-82d9-001ec200d9e0
    variant : specified in RFC 4122
    version : 1
    fields  : (1846968542L, 35861L, 4573L, 130L, 217L, 132103854560L)
    	time_low            :  1846968542
    	time_mid            :  35861
    	time_hi_version     :  4573
    	clock_seq_hi_variant:  130
    	clock_seq_low       :  217
    	node                :  132103854560
    	time                :  134417587560153310
    	clock_seq           :  729

Because of the time component, each time `uuid1()` is called a new
value is returned.

.. include:: uuid_uuid1_repeat.py
    :literal:
    :start-after: #end_pymotw_header


Notice in this output that only the time component (at the beginning
of the string) changes.

::

    $ python uuid_uuid1_repeat.py
    834a7582-8c15-11dd-8bf2-001ec200d9e0
    834a7c30-8c15-11dd-8bf2-001ec200d9e0
    834a7dd4-8c15-11dd-8bf2-001ec200d9e0

Of course, since your computer has a different MAC address than mine,
you will see entirely different values if you run the examples,
because the node identifier at the end of the UUID will change, too.

.. include:: uuid_uuid1_othermac.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python uuid_uuid1_othermac.py
    0x1ec200d9e0L 9c3a7d11-8c15-11dd-a8be-001ec200d9e0
    0x1e5274040eL 9c3b0407-8c15-11dd-8ea5-001e5274040e


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

To create a UUID from a DNS name, pass uuid.NAMESPACE_DNS as the
namespace argument to `uuid3()` or `uuid5()`:

.. include:: uuid_uuid3_uuid5.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python uuid_uuid3_uuid5.py
    www.doughellmann.com
    	MD5   : bcd02e22-68f0-3046-a512-327cca9def8f
    	SHA-1 : e3329b12-30b7-57c4-8117-c2cd34a87ce9
    blog.doughellmann.com
    	MD5   : 9bdabfce-dfd6-37ab-8a3f-7f7293bcf111
    	SHA-1 : fa829736-7ef8-5239-9906-b4775a5abacb

The UUID value for the same name in a namespace is always the same, no
matter when or where it is calculated. Values for the same name in
different namespaces are different, of course.

.. include:: uuid_uuid3_repeat.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python uuid_uuid3_repeat.py
    bcd02e22-68f0-3046-a512-327cca9def8f
    bcd02e22-68f0-3046-a512-327cca9def8f
    bcd02e22-68f0-3046-a512-327cca9def8f


UUID 4 - Random Values
======================

Sometimes host-based and namespace-based UUID values are not "different enough". For example, in cases where you want to use the UUID as a lookup key, a more random sequence of values with more differentiation is desirable to avoid collisions in a hash table. Having values with fewer common digits also makes it easier to find them in log files. To add greater differentiation in your UUIDs, use `uuid4()` to generate UUIDs from random values.

.. include:: uuid_uuid4.py
    :literal:
    :start-after: #end_pymotw_header

::

    $ python uuid_uuid4.py
    31326f00-92cd-42a8-a85d-ab94e77eb1ee
    a16102fc-a87e-4eb9-a479-746f3ecb3a62
    1a7bc5a2-b6d5-4049-be9a-86638dc1a6eb


Working with UUID Objects
=========================

In addition to generating new UUID values, you can parse strings in
various formats to create UUID objects. This makes it easier to
compare them, sort them, etc.

.. include:: uuid_uuid_objects.py
    :literal:
    :start-after: #end_pymotw_header


::

    $ python uuid_uuid_objects.py
    input_values
    	urn:uuid:f2f84497-b3bf-493a-bba9-7c68e6def80b
    	{417a5ebb-01f7-4ed5-aeac-3d56cd5037b0}
    	2115773a-5bf1-11dd-ab48-001ec200d9e0
    
    converted to uuids
    	f2f84497-b3bf-493a-bba9-7c68e6def80b
    	417a5ebb-01f7-4ed5-aeac-3d56cd5037b0
    	2115773a-5bf1-11dd-ab48-001ec200d9e0
    
    sorted
    	2115773a-5bf1-11dd-ab48-001ec200d9e0
    	417a5ebb-01f7-4ed5-aeac-3d56cd5037b0
    	f2f84497-b3bf-493a-bba9-7c68e6def80b
    

References
==========

`RFC 4122: A Universally Unique IDentifier (UUID) URN Namespace <http://www.faqs.org/rfcs/rfc4122.html>`_

Standard library documentation: `uuid <http://docs.python.org/lib/module-uuid.html>`_
