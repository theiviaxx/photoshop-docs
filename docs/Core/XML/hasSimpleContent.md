XML.hasSimpleContent {#XML.hasSimpleContent}
====================

> bool **hasSimpleContent** ()

Description
-----------

Reports whether this XML object contains simple content.

An XML object is considered to contain simple content if it represents a
text node, represents an attribute node or if it represents an XML
element that has no child elements. XML objects representing comments
and processing instructions do not have simple content. The existence of
attributes, comments, processing instructions and text nodes within an
XML object is not significant in determining if it has simple content.
