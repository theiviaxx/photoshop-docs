.. _XML.insertChildBefore:

================================================
XML.insertChildBefore
================================================

   void **insertChildBefore** (:ref:`XML` **child1**, :ref:`XML` **child2**)


Parameters
----------

+------------+--------------------------+
| **child1** | The child to search for. |
+------------+--------------------------+
| **child2** | The XML to insert.       |
+------------+--------------------------+



Description
-----------

Inserts the given child2 before the given child1 in this XML object and returns this XML object.

If child1 is null, the method inserts child2 after all children of this XML object (that is, before none of them). If child1 does not exist in this XML object, the method returns without modifying this XML object.


