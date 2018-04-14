XML.toString {#XML.toString}
============

> [string]{role="ref"} **toString** ()

Description
-----------

Returns the string representation of this object.

For text and attribute nodes, this is the textual value of the node; for
other elements, this is the result of calling the toXMLString() method.
If this XML object is a list, concatenates the result of calling
toString() on each element.
