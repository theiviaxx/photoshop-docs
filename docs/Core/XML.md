XML {#XML}
===

Description
-----------

Wraps XML into an object.

### Static Properties

  -------------------------------------------------------------------------------- --------------------------------------
  [ignoreComments\<XML.ignoreComments\>]{role="ref"} readonly                      Controls whether XML comments should
                                                                                   be parsed (false) or ignored (true).

  [ignoreProcessingInstructions\<XML.ignoreProcessingInstructions\>]{role="ref"}   Controls whether XML preprocessing
  readonly                                                                         instructions should be parsed (false)
                                                                                   or ignored (true).

  [ignoreWhitespace\<XML.ignoreWhitespace\>]{role="ref"} readonly                  Controls whether whitespace should be
                                                                                   parsed (false) or ignored (true).

  [prettyIndent\<XML.prettyIndent\>]{role="ref"} readonly                          The number of spaces used to indent
                                                                                   pretty-printed XML.

  [prettyPrinting\<XML.prettyPrinting\>]{role="ref"} readonly                      When true, XML is pretty-printed when
                                                                                   converting to a string.
  -------------------------------------------------------------------------------- --------------------------------------

### Constructors

  ------------------------------ ------------------------------------------------
  [XML\<XML.XML\>]{role="ref"}   Parses an XML string. Throws an error if the XML
  readonly                       is incorrect.
  ------------------------------ ------------------------------------------------

### Methods

  -------------------------------------------------------------------- --------------------------------------------------
  [addNamespace\<XML.addNamespace\>]{role="ref"} readonly              Adds a namespace declaration to the node. Returns
                                                                       the XML object itself.

  [appendChild\<XML.appendChild\>]{role="ref"} readonly                Appends the given XML to this XML as a child.
                                                                       Returns the XML object itself.

  [attribute\<XML.attribute\>]{role="ref"} readonly                    Returns a list containing all attribute elements
                                                                       matching the given name.

  [attributes\<XML.attributes\>]{role="ref"} readonly                  Returns a list containing all attribute elements.

  [child\<XML.child\>]{role="ref"} readonly                            Returns a list containing all children of this XML
                                                                       matching the given element name.

  [childIndex\<XML.childIndex\>]{role="ref"} readonly                  Returns a number representing the ordinal position
                                                                       of this XML object within the context of its
                                                                       parent.

  [children\<XML.children\>]{role="ref"} readonly                      Returns an XML object containing all the
                                                                       properties of this XML object in order.

  [comments\<XML.comments\>]{role="ref"} readonly                      Returns an XML object containing the properties of
                                                                       this XML object that represent XML comments.

  [contains\<XML.contains\>]{role="ref"} readonly                      Checks if this XML object contains the given XML
                                                                       object.

  [copy\<XML.copy\>]{role="ref"} readonly                              Creates a copy of this XML object.

  [descendants\<XML.descendants\>]{role="ref"} readonly                Returns all the XML-valued descendants of this XML
                                                                       object with the given name.

  [elements\<XML.elements\>]{role="ref"} readonly                      Returns a list of XML children that are elements
                                                                       with a given name, or all children that are XML
                                                                       elements.

  [hasComplexContent\<XML.hasComplexContent\>]{role="ref"} readonly    Reports whether this XML object contains complex
                                                                       content.

  [hasSimpleContent\<XML.hasSimpleContent\>]{role="ref"} readonly      Reports whether this XML object contains simple
                                                                       content.

  [inScopeNamespaces\<XML.inScopeNamespaces\>]{role="ref"} readonly    Returns an array of Namespace objects mirroring
                                                                       the current list of valid namespaces at this
                                                                       element.

  [insertChildAfter\<XML.insertChildAfter\>]{role="ref"} readonly      Inserts the given child2 after the given child1 in
                                                                       this XML object and returns this XML object.

  [insertChildBefore\<XML.insertChildBefore\>]{role="ref"} readonly    Inserts the given child2 before the given child1
                                                                       in this XML object and returns this XML object.

  [length\<XML.length\>]{role="ref"} readonly                          Returns the number of elements contained in an XML
                                                                       list. If this XML object is not a list, returns 1.

  [localName\<XML.localName\>]{role="ref"} readonly                    Returns the local name of this XML object.

  [name\<XML.name\>]{role="ref"} readonly                              Returns a QName object containing the URI and the
                                                                       local name of the element.

  [namespace\<XML.namespace\>]{role="ref"} readonly                    Returns a Namespace object containing the
                                                                       namespace URI of the current element.

  [namespaceDeclarations\<XML.namespaceDeclarations\>]{role="ref"}     Returns an array containing all namespace
  readonly                                                             declarations of this XML object.

  [nodeKind\<XML.nodeKind\>]{role="ref"} readonly                      Returns the type of this XML object as one of the
                                                                       strings \"element\", \"attribute\", \"comment\",
                                                                       \"processing-instruction\", or \"text\".

  [normalize\<XML.normalize\>]{role="ref"} readonly                    Puts all text nodes in this and all descendant XML
                                                                       objects into a normal form by merging adjacent
                                                                       text nodes and eliminating empty text nodes.
                                                                       Returns this XML object.

  [parent\<XML.parent\>]{role="ref"} readonly                          Returns the parent object of this XML object.

  [prependChild\<XML.prependChild\>]{role="ref"} readonly              Inserts a given child into this object before its
                                                                       existing XML properties, and returns this XML
                                                                       object.

  [processingInstructions\<XML.processingInstructions\>]{role="ref"}   Returns a list of preprocessing instructions.
  readonly                                                             

  [removeNamespace\<XML.removeNamespace\>]{role="ref"} readonly        Removes the given namespace from this XML, and
                                                                       returns this XML.

  [replace\<XML.replace\>]{role="ref"} readonly                        Replaces the value of specified XML properties of
                                                                       this XML object returns this XML object.

  [setChildren\<XML.setChildren\>]{role="ref"} readonly                Replaces all of the XML-valued properties in this
                                                                       object with a new value, and returns this XML
                                                                       object.

  [setLocalName\<XML.setLocalName\>]{role="ref"} readonly              Replaces the local name of this XML object with a
                                                                       string constructed from the given name

  [setName\<XML.setName\>]{role="ref"} readonly                        Replaces the name of this XML object with the
                                                                       given QName object.

  [setNamespace\<XML.setNamespace\>]{role="ref"} readonly              Sets the namespace for this XML element.

  [text\<XML.text\>]{role="ref"} readonly                              Returns an XML list containing all XML properties
                                                                       of this XML object that represent XML text nodes.

  [toString\<XML.toString\>]{role="ref"} readonly                      Returns the string representation of this object.

  [toXMLString\<XML.toXMLString\>]{role="ref"} readonly                Returns an XML-encoded string representation of
                                                                       this XML object.

  [xpath\<XML.xpath\>]{role="ref"} readonly                            Evaluates the given XPath expression in accordance
                                                                       with the W3C XPath recommendation, using this XML
                                                                       object as the context node.
  -------------------------------------------------------------------- --------------------------------------------------

### Static Methods

  ------------------------------------------------------ ---------------------------------------------
  [defaultSettings\<XML.defaultSettings\>]{role="ref"}   Returns an object containing the default
  readonly                                               parsing and print settings for XML.

  [setSettings\<XML.setSettings\>]{role="ref"} readonly  Sets the parsing and print setting for XML
                                                         using an object returned by the settings()
                                                         method.

  [settings\<XML.settings\>]{role="ref"} readonly        Returns an object containing the current
                                                         parsing and print settings for XML.
  ------------------------------------------------------ ---------------------------------------------

::: {.container .hide}
::: {.toctree}
XML/ignoreComments.rst XML/ignoreProcessingInstructions.rst
XML/ignoreWhitespace.rst XML/prettyPrinting.rst XML/prettyIndent.rst

XML/addNamespace.rst XML/appendChild.rst XML/attribute.rst
XML/attributes.rst XML/child.rst XML/childIndex.rst XML/children.rst
XML/comments.rst XML/contains.rst XML/copy.rst XML/descendants.rst
XML/elements.rst XML/hasComplexContent.rst XML/hasSimpleContent.rst
XML/inScopeNamespaces.rst XML/insertChildAfter.rst
XML/insertChildBefore.rst XML/length.rst XML/localName.rst XML/name.rst
XML/namespace.rst XML/namespaceDeclarations.rst XML/nodeKind.rst
XML/normalize.rst XML/parent.rst XML/processingInstructions.rst
XML/prependChild.rst XML/removeNamespace.rst XML/replace.rst
XML/setChildren.rst XML/setLocalName.rst XML/setName.rst
XML/setNamespace.rst XML/text.rst XML/toString.rst XML/toXMLString.rst
XML/xpath.rst

XML/settings.rst XML/setSettings.rst XML/defaultSettings.rst

XML/XML.rst
:::
:::
