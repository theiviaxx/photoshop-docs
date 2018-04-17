.. _global.parseInt:

================================================
global.parseInt
================================================

   :ref:`number` **parseInt** (:ref:`string` **text**, :ref:`number` **base**)


Parameters
----------

+----------+-----------------------------------------------------------+
| **text** | The string from which to extract an integer.              |
+----------+-----------------------------------------------------------+
| **base** | The base of the string to parse (from base 2 to base 36). |
+----------+-----------------------------------------------------------+



Description
-----------

Extracts an integer from a string.

Parses a string to find the first set of characters, in a specified base, that can be converted to an integer, and returns that integer, or NaN if it does not encounter characters that it can convert to a number.


