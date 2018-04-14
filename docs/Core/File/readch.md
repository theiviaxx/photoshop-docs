File.readch {#File.readch}
===========

> [string]{role="ref"} **readch** ()

Description
-----------

Reads a single text character from the file at the current position.

Line feeds are recognized as CR, LF, CRLF or LFCR pairs. If the file is
encoded, multiple bytes might be read to create a single Unicode
character. Returns a string that contains the character.
