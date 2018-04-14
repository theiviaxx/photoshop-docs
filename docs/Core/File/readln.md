File.readln {#File.readln}
===========

> [string]{role="ref"} **readln** ()

Description
-----------

Reads a single line of text from the file at the current position.

Line feeds are recognized as CR, LF, CRLF or LFCR pairs.. If the file is
encoded, multiple bytes might be read to create single Unicode
characters. Returns a string that contains the text.
