Reflection {#Reflection}
==========

Description
-----------

Provides information about a class.

### Properties

  --------------------------------------------------------------- -----------------------------
  [description\<Reflection.description\>]{role="ref"} readonly    The long description text.

  [help\<Reflection.help\>]{role="ref"} readonly                  The short description text.

  [methods\<Reflection.methods\>]{role="ref"} readonly            An array of method
                                                                  descriptions.

  [name\<Reflection.name\>]{role="ref"} readonly                  The class name.

  [properties\<Reflection.properties\>]{role="ref"} readonly      An array of property
                                                                  descriptions.

  [sampleCode\<Reflection.sampleCode\>]{role="ref"} readonly      Sample code, if present.

  [sampleFile\<Reflection.sampleFile\>]{role="ref"} readonly      A file containing sample
                                                                  code. May be null.

  [staticMethods\<Reflection.staticMethods\>]{role="ref"}         An array of class method
  readonly                                                        descriptions.

  [staticProperties\<Reflection.staticProperties\>]{role="ref"}   An array of class property
  readonly                                                        descriptions.
  --------------------------------------------------------------- -----------------------------

### Methods

  ----------------------------------------- ----------------------------------------
  [find\<Reflection.find\>]{role="ref"}     Finds an element description by name.
  readonly                                  

  [toXML\<Reflection.toXML\>]{role="ref"}   Returns this class information as XML in
  readonly                                  OMV format.
  ----------------------------------------- ----------------------------------------

::: {.container .hide}
::: {.toctree}
Reflection/name.rst Reflection/methods.rst Reflection/properties.rst
Reflection/staticMethods.rst Reflection/staticProperties.rst
Reflection/description.rst Reflection/help.rst Reflection/sampleCode.rst
Reflection/sampleFile.rst

Reflection/find.rst Reflection/toXML.rst
:::
:::
