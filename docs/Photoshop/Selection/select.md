Selection.select {#Selection.select}
================

> void **select** (any **region**, [SelectionType]{role="ref"} **type**,
> [number]{role="ref"} **feather**, bool **antiAlias**)

Parameters
----------

  --------------- ---------------------------------------------------------------
  **region**      Array of x and y coordinates that describe the corners of the
                  selection, in the format \[\[x1, y1\], \[x2,y2\],\[x3, y3\],
                  \[x4,y4\]\]

  **type**        The method for combining the new selection with the existing
                  selection.

  **feather**     The feather amount.

  **antiAlias**   If true, anti-aliasing is used.
  --------------- ---------------------------------------------------------------

Description
-----------

Selects the specified region.