Object {#Object}
======

Description
-----------

The base class of all JavaScript objects.

### Properties

  ------------------------------------------------- ---------------------------------------------
  [constructor\<Object.constructor\>]{role="ref"}   Points to the constructor function that
  readonly                                          created this object.

  [prototype\<Object.prototype\>]{role="ref"}       Points to the prototype object for this
  readonly                                          object.

  [reflect\<Object.reflect\>]{role="ref"} readonly  Retrieves and returns the Reflection object
                                                    associated with this method or a property.
  ------------------------------------------------- ---------------------------------------------

### Constructors

  --------------------------------------- ----------------------------------------
  [Object\<Object.Object\>]{role="ref"}   Creates and returns a new object of a
  readonly                                given type.
  --------------------------------------- ----------------------------------------

### Methods

  ------------------------------------------------------------------- -------------------------------------------
  [hasOwnProperty\<Object.hasOwnProperty\>]{role="ref"} readonly      Reports whether a given property is defined
                                                                      with an instance or within the prototype
                                                                      chain.

  [isPrototypeOf\<Object.isPrototypeOf\>]{role="ref"} readonly        Checks whether the given object is a
                                                                      prototype of this object.

  [propertyIsEnumerable\<Object.propertyIsEnumerable\>]{role="ref"}   Reports whether a given property is
  readonly                                                            enumerable.

  [toLocaleString\<Object.toLocaleString\>]{role="ref"} readonly      Creates and returns a string representing
                                                                      this object, localized for the current
                                                                      locale. See?toString().

  [toSource\<Object.toSource\>]{role="ref"} readonly                  Creates and returns a string representation
                                                                      of this object.

  [toString\<Object.toString\>]{role="ref"} readonly                  Creates and returns a string representing
                                                                      this object.

  [unwatch\<Object.unwatch\>]{role="ref"} readonly                    Removes the watch function of a property.

  [valueOf\<Object.valueOf\>]{role="ref"} readonly                    Retrieves and returns the primitive value
                                                                      of this object.

  [watch\<Object.watch\>]{role="ref"} readonly                        Adds a watch function to a property, which
                                                                      is called when the value changes.
  ------------------------------------------------------------------- -------------------------------------------

### Static Methods

  ----------------------------------------- ------------------------------------
  [isValid\<Object.isValid\>]{role="ref"}   Reports whether an object is still
  readonly                                  valid.
  ----------------------------------------- ------------------------------------

::: {.container .hide}
::: {.toctree}
Object/prototype.rst Object/constructor.rst Object/reflect.rst

Object/toString.rst Object/toLocaleString.rst Object/hasOwnProperty.rst
Object/propertyIsEnumerable.rst Object/isPrototypeOf.rst
Object/valueOf.rst Object/toSource.rst Object/unwatch.rst
Object/watch.rst

Object/isValid.rst

Object/Object.rst
:::
:::
