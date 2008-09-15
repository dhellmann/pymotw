#############################################
:mod:`dumbdbm` - Portable DBM Implementation
#############################################

.. module:: dumbdbm
    :synopsis: Portable DBM Implementation

:Purpose: Last-resort backend implementation for :mod:`anydbm`.
:Python Version: 1.4 and later

The :mod:`dumbdbm` module is a portable fallback implementation of the DBM API when no other implementations are available.  No external dependencies are required to use :mod:`dumbdbm`, but it is slower than most other implementations.

It follows the semantics of the :mod:`anydbm` module.

References
==========

See also :mod:`anydbm`

Standard library documentation: `dumbdbm <http://docs.python.org/lib/module-dumbdbm.html>`_
