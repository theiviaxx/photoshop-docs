Socket.read {#Socket.read}
===========

> [string]{role="ref"} **read** ([number]{role="ref"} **count**)

Parameters
----------

  ----------- -----------------------------------
  **count**   The number of characters to read.
  ----------- -----------------------------------

Description
-----------

Reads up to the specified number of characters from the connection. CR
characters are ignored unless the encoding is set to \"BINARY\".

Returns a string that contains up to the number of characters that were
supposed to be read, or the number of characters read before the
connection closed or timed out.
