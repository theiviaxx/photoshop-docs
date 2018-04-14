PathItem.makeSelection {#PathItem.makeSelection}
======================

> void **makeSelection** ([number]{role="ref"} **feather**, bool
> **antiAlias**, [SelectionType]{role="ref"} **operation**)

Parameters
----------

  --------------- ------------------------------------------------------------
  **feather**     The feather amount in pixels. Range: 0.0 to 250.0.

  **antiAlias**   If true, the selection uses anti-aliasing.

  **operation**   The selection behavior relative to the existing selection
                  (when a selection already exists).
  --------------- ------------------------------------------------------------

Description
-----------

Makes a selection object, whose border is the path, from this path item
object.
