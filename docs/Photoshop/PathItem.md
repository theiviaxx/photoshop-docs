PathItem {#PathItem}
========

Description
-----------

A path or drawing object, such as the outline of a shape or a straight
or curved line, which contains sub paths that comprise its geometry.

### Properties

  ----------------------------------------------------- -------------------------------
  [kind\<PathItem.kind\>]{role="ref"} readonly          The type of path.

  [name\<PathItem.name\>]{role="ref"} readonly          The name of the path item.

  [parent\<PathItem.parent\>]{role="ref"} readonly      The object\'s container.

  [subPathItems\<PathItem.subPathItems\>]{role="ref"}   The sub path objects for this
  readonly                                              path item.

  [typename\<PathItem.typename\>]{role="ref"} readonly  The class name of the object.
  ----------------------------------------------------- -------------------------------

### Methods

  ------------------------------------------------------------- ----------------------------------------
  [add\<PathItem.add\>]{role="ref"} readonly                    Adds an element.

  [deselect\<PathItem.deselect\>]{role="ref"} readonly          Unselects the selection, no path items
                                                                are selected.

  [duplicate\<PathItem.duplicate\>]{role="ref"} readonly        Duplicate this object.

  [duplicate\<PathItem.duplicate\>]{role="ref"} readonly        Duplicates this path item.

  [fillPath\<PathItem.fillPath\>]{role="ref"} readonly          Fills the area enclosed by the path.

  [makeClippingPath\<PathItem.makeClippingPath\>]{role="ref"}   Makes this path item the clipping path
  readonly                                                      for this document.

  [makeSelection\<PathItem.makeSelection\>]{role="ref"}         Makes a selection object, whose border
  readonly                                                      is the path, from this path item object.

  [remove\<PathItem.remove\>]{role="ref"} readonly              Deletes this object.

  [removeAll\<PathItem.removeAll\>]{role="ref"} readonly        Deletes all elements.

  [select\<PathItem.select\>]{role="ref"} readonly              Makes this path item the active or
                                                                selected path item.

  [strokePath\<PathItem.strokePath\>]{role="ref"} readonly      Strokes the path.
  ------------------------------------------------------------- ----------------------------------------

::: {.container .hide}
::: {.toctree}
PathItem/parent.rst PathItem/typename.rst PathItem/name.rst
PathItem/subPathItems.rst PathItem/kind.rst

PathItem/add.rst PathItem/duplicate.rst PathItem/remove.rst
PathItem/removeAll.rst PathItem/duplicate.rst PathItem/makeSelection.rst
PathItem/fillPath.rst PathItem/strokePath.rst
PathItem/makeClippingPath.rst PathItem/select.rst PathItem/deselect.rst
:::
:::
