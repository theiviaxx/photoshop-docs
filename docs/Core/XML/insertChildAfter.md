XML.insertChildAfter {#XML.insertChildAfter}
====================

> void **insertChildAfter** ([XML]{role="ref"} **child1**,
> [XML]{role="ref"} **child2**)

Parameters
----------

  ------------ --------------------------------------------
  **child1**   The child to insert the other child after.

  **child2**   The XML to insert.
  ------------ --------------------------------------------

Description
-----------

Inserts the given child2 after the given child1 in this XML object and
returns this XML object.

If child1 is null, the method inserts child2 before all children of this
XML object (that is, after none of them). If child1 does not exist in
this XML object, the method returns without modifying this XML object.
