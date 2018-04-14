PathItem.fillPath {#PathItem.fillPath}
=================

> void **fillPath** (any **fillColor**, [ColorBlendMode]{role="ref"}
> **mode**, [number]{role="ref"} **opacity**, bool
> **preserveTransparency**, [number]{role="ref"} **feather**, bool
> **antiAlias**, bool **wholePath**)

Parameters
----------

  -------------------------- -----------------------------------------------------
  **fillColor**              The color of the fill for this path.

  **mode**                   The blending mode of the fill for this path.

  **opacity**                The opacity of the fill for this path (as a
                             percentage). Range: 0.0 to 100.0.

  **preserveTransparency**   If true, transparency is preserved.

  **feather**                The feather amount in pixels. Range: 0.0 to 250.0.

  **antiAlias**              If true, uses anti-aliasing for the selection.

  **wholePath**              If true, uses all subpaths when doing the fill.
  -------------------------- -----------------------------------------------------

Description
-----------

Fills the area enclosed by the path.
