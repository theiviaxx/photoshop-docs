UnitValue {#UnitValue}
=========

Description
-----------

Represents a measurement as a combination of values and unit.

Note that this object is not available in all applications.

### Properties

  ---------------------------------------------- --------------------
  [baseUnit\<UnitValue.baseUnit\>]{role="ref"}   The base unit.
  readonly                                       

  [type\<UnitValue.type\>]{role="ref"} readonly  The unit name.

  [value\<UnitValue.value\>]{role="ref"}         The numeric value.
  readonly                                       
  ---------------------------------------------- --------------------

### Static Properties

  ---------------------------------------------- -------------------------------
  [baseUnit\<UnitValue.baseUnit\>]{role="ref"}   The base unit for all
  readonly                                       conversions.
  ---------------------------------------------- -------------------------------

### Methods

  -------------------------------------------- -----------------------------------
  [as\<UnitValue.as\>]{role="ref"} readonly    Returns this instance as a
                                               different unit.

  [convert\<UnitValue.convert\>]{role="ref"}   Converts this instance to a
  readonly                                     different unit.
  -------------------------------------------- -----------------------------------

::: {.container .hide}
::: {.toctree}
UnitValue/type.rst UnitValue/value.rst UnitValue/baseUnit.rst

UnitValue/baseUnit.rst

UnitValue/convert.rst UnitValue/as.rst
:::
:::
