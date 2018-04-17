.. _File.read:

================================================
File.read
================================================

   :ref:`string` **read** (:ref:`number` **chars**)


Parameters
----------

+-----------+---------------------------------------------------------+
| **chars** | An integer specifying the number of characters to read. |
+-----------+---------------------------------------------------------+



Description
-----------

Reads the contents of the file, starting at the current position.

Returns a string that contains up to the specified number of characters. If a number of characters is not supplied, reads from the current position to the end of the file. If the file is encoded, multiple bytes might be read to create single Unicode characters.


