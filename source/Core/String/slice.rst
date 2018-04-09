.. _String.slice:

================================================
String.slice
================================================

   :ref:`string` **slice** (:ref:`number` **startSlice**, :ref:`number` **endSlice**)


Parameters
----------

+----------------+-----------------------------------------+
| **startSlice** | The index at which to begin extraction. |
+----------------+-----------------------------------------+
| **endSlice**   | The index at which to end extraction.   |
+----------------+-----------------------------------------+



Description
-----------

Extracts a substring of the given string and returns it as a new string.

The substring begins at startSlice, and includes all characters up to, but not including the character at the index endSlice.   A negative value indexes from the end of the string.  For example, a negative value for startSlice is resolved as: string. length + startSlice.  The original string is unchanged.  Returns a substring of characters from the given string, starting at startSlice and ending with endSlice-1.


