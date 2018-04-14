ShapeOperation {#ShapeOperation}
==============

Description
-----------

Specifies how to combine the shapes if the destination image already has
a selection.

### Static Properties

  --------------------------------------------------------------- --------------------------------------
  [SHAPEADD\<ShapeOperation.SHAPEADD\>]{role="ref"} readonly      Adds the shapes.

  [SHAPEINTERSECT\<ShapeOperation.SHAPEINTERSECT\>]{role="ref"}   The resulting shape is the area of
  readonly                                                        intersection between the two shapes.

  [SHAPESUBTRACT\<ShapeOperation.SHAPESUBTRACT\>]{role="ref"}     Subtracts the loaded shape from the
  readonly                                                        selection is the destination image.

  [SHAPEXOR\<ShapeOperation.SHAPEXOR\>]{role="ref"} readonly      Replaces the shape in the destination
                                                                  image with the loaded selection.
  --------------------------------------------------------------- --------------------------------------

::: {.container .hide}
::: {.toctree}
ShapeOperation/SHAPEADD.rst ShapeOperation/SHAPEXOR.rst
ShapeOperation/SHAPEINTERSECT.rst ShapeOperation/SHAPESUBTRACT.rst
:::
:::
