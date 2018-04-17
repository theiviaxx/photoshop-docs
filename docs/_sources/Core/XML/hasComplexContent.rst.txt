.. _XML.hasComplexContent:

================================================
XML.hasComplexContent
================================================

   bool **hasComplexContent** ()




Description
-----------

Reports whether this XML object contains complex content.

An XML object is considered to contain complex content if it represents an XML element that has child elements. XML objects representing attributes, comments, processing instructions and text nodes do not have complex content. The existence of attributes, comments, processing instructions and text nodes within an XML object is not significant in determining if it has complex content.


