.. _File.open:

================================================
File.open
================================================

   bool **open** (:ref:`string` **mode**, :ref:`string` **type**, :ref:`string` **creator**)


Parameters
----------

+-------------+----------------------------------------------------------------------------------------------------+
| **mode**    | The read-write mode, a single-character string.                                                    |
+-------------+----------------------------------------------------------------------------------------------------+
| **type**    | In Mac OS, the type of a newly created file, a 4-character string. Ignored in Windows and UNIX.    |
+-------------+----------------------------------------------------------------------------------------------------+
| **creator** | In Mac OS, the creator of a newly created file, a 4-character string. Ignored in Windows and UNIX. |
+-------------+----------------------------------------------------------------------------------------------------+



Description
-----------

Opens the referenced file for subsequent read/write operations. The method resolves any aliases to find the file.

Returns true if the file was opened successfully.The method attempts to detect the encoding of the open file. It reads a few bytes at the current location and tries to detect the Byte Order Mark character 0xFFFE. If found, the current position is advanced behind the detected character and the encoding property is set to one of the strings UCS-2BE, UCS-2LE, UCS4-BE, UCS-4LE, or UTF-8. If the marker character is not found, it checks for zero bytes at the current location and makes an assumption about one of the above formats (except UTF-8). If everything fails, the encoding property is set to the system encoding. IMPORTANT: Be careful about opening a file more than once. The operating system usually permits you to do so, but if you start writing to the file using two different File objects, you can destroy your data.


