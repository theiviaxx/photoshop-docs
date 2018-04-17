.. _File.seek:

================================================
File.seek
================================================

   bool **seek** (:ref:`number` **pos**, :ref:`number` **mode**)


Parameters
----------

+----------+-----------------------------------------------------------------------------------------------------------------------------+
| **pos**  | The new current position in the file as an offset in bytes from the start, current position, or end, depending on the?mode. |
+----------+-----------------------------------------------------------------------------------------------------------------------------+
| **mode** | The seek mode.                                                                                                              |
+----------+-----------------------------------------------------------------------------------------------------------------------------+



Description
-----------

Seeks to a given position in the file.

The new position cannot be less than 0 or greater than the current file size. Returns true if the position was changed.


