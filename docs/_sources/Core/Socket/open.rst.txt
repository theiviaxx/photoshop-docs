.. _Socket.open:

================================================
Socket.open
================================================

   bool **open** (:ref:`string` **host**, :ref:`string` **encoding**)


Parameters
----------

+--------------+--------------------------------------------+
| **host**     | The server to connect to.                  |
+--------------+--------------------------------------------+
| **encoding** | The encoding to be used for the connection |
+--------------+--------------------------------------------+



Description
-----------

Opens the connection for subsequent read/write operations.

The call to open() and the call to listen() are mutually exclusive. Call one function or the other, not both.


