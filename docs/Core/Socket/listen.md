Socket.listen {#Socket.listen}
=============

> bool **listen** ([number]{role="ref"} **port**, [string]{role="ref"}
> **encoding**)

Parameters
----------

  -------------- --------------------------------------------
  **port**       The TCP/IP port number to listen on.

  **encoding**   The encoding to be used for the connection
  -------------- --------------------------------------------

Description
-----------

Instructs the object to start listening for an incoming connection.

The call to open() and the call to listen()are mutually exclusive. Call
one function or the other, not both.
