File.encoding {#File.encoding}
=============

> [string]{role="ref"} **encoding**

Description
-----------

Gets or sets the encoding for subsequent read/write operations.

One of the encoding constants listed in the?JavaScript Tools Guide. If
the value is not recognized, uses the system default encoding.A special
encoder, BINARY, is used to read binary files. It stores each byte of
the file as one Unicode character regardless of any encoding. When
writing, the lower byte of each Unicode character is treated as a single
byte to write.
