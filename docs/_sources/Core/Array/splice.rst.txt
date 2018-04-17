.. _Array.splice:

================================================
Array.splice
================================================

   :ref:`Array` **splice** (:ref:`number` **start**, :ref:`number` **num**, any **value**)


Parameters
----------

+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| **start** | The index of the first element to remove. Negative values are relative to the end of the array.                                               |
+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| **num**   | The number of array elements to remove, including start. If omitted, all elements from array index start to the end of the array are removed. |
+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| **value** | A list of one or more values to be added to the array starting at index start.                                                                |
+-----------+-----------------------------------------------------------------------------------------------------------------------------------------------+



Description
-----------

Removes num elements from the array beginning with index, start.

Optionally insert new elements beginning at index start.  To ensure contiguity, elements are moved up to fill in any gaps.  Returns a new array containing any elements deleted from the original array.


