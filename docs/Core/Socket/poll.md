Socket.poll {#Socket.poll}
===========

> [Socket]{role="ref"} **poll** ()

Description
-----------

Checks a listening object for a new incoming connection.

If a connection request was detected, the method returns a new Socket
object that wraps the new connection. Use this connection object to
communicate with the remote computer. After use, close the connection
and delete the JavaScript object. If no new connection request was
detected, the method returns null.
