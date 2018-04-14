XML.appendChild {#XML.appendChild}
===============

> [XML]{role="ref"} **appendChild** ([XML]{role="ref"} **child**)

Parameters
----------

  ----------- -----------------------
  **child**   The child XML to add.
  ----------- -----------------------

Description
-----------

Appends the given XML to this XML as a child. Returns the XML object
itself.

If the argument is not XML, creates a new XML element containing the
argument as text. The element name of that new XML is the same as the
last element in the original XML.
