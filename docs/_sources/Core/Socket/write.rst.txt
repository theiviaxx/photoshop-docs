.. _Socket.write:

================================================
Socket.write
================================================

   bool **write** (:ref:`string` **text**)


Parameters
----------

+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **text** | Any number of string values. All arguments are concatenated to form the string to be written. CRLF sequences are converted to LFs unless the encoding is set to "BINARY". |
+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+



Description
-----------

Concatenates all arguments into a single string and writes that string to the connection.




