============================
abc -- Abstract Base Classes
============================

.. module:: abc
    :synopsis: Abstract Base Classes

:Purpose: Define and use abstract base classes for API checks in your code.
:Python Version: 2.6

Why use Abstract Base Classes?
==============================

- define the term
- introduce an example use case (plugins?, collections?)

Using ABCs
==========

- using metaclass and subclass directly
- registering an existing class with an abc

Concrete Methods in ABCs
========================

- implementations of abstract methods (why do this?)
- non-abstract methods

Abstract Properties
===================

- cover basic property API first, then show how abstract property is useful

Collection Types
================

- abcs from :mod:`collections`
  - Hashable
  - Iterable
  - Iterator
  - Sized
  - Container
  - Set
  - Mapping
  - MutableMapping
  - Sequence
  - MutableSequence
- are these abcs registered for the built-in types automatically?

Numeric Types
=============

- abcs for numbers

.. seealso::

    `abc <http://docs.python.org/library/abc.html>`_
        The standard library documentation for this module.

    :pep:`3119`
        Introducing Abstract Base Classes
    
    :mod:`collections`
        The collections module includes abstract base classes for several collection types.

    :pep:`3141`
        A Type Hierarchy for Numbers

    `Wikipedia: Strategy Pattern <http://en.wikipedia.org/wiki/Strategy_pattern>`_
        Description and examples of the strategy pattern.
