XML.processingInstructions {#XML.processingInstructions}
==========================

> [XML]{role="ref"} **processingInstructions** ([string]{role="ref"}
> **name**)

Parameters
----------

  ---------- ------------------------------------------------------
  **name**   The name of the preprocessing instruction to return.
  ---------- ------------------------------------------------------

Description
-----------

Returns a list of preprocessing instructions.

Collects processing-instructions with the given name, if supplied.
Otherwise, returns an XML list containing all the children of this XML
object that are processing-instructions regardless of their name.
