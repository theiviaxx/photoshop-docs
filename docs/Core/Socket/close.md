Socket.close {#Socket.close}
============

> bool **close** ()

Description
-----------

Terminates the open connection.

Returns true if the connection was closed, false on I/O errors. Deleting
the object also closes the connection, but not until JavaScript
garbage-collects the object. The connection might stay open longer than
you wish if you do not close it explicitly.
