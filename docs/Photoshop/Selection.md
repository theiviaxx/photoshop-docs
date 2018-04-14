Selection {#Selection}
=========

Description
-----------

The selected area of the document or layer.

### Properties

  ---------------------------------------------- -------------------------------------
  [bounds\<Selection.bounds\>]{role="ref"}       The bounding rectangle of the entire
  readonly                                       selection.

  [parent\<Selection.parent\>]{role="ref"}       The object\'s container.
  readonly                                       

  [solid\<Selection.solid\>]{role="ref"}         If true, the bounding rectangle a
  readonly                                       solid rectangle.

  [typename\<Selection.typename\>]{role="ref"}   The class name of the object.
  readonly                                       
  ---------------------------------------------- -------------------------------------

### Methods

  ---------------------------------------------------------------- -----------------------------------------------
  [clear\<Selection.clear\>]{role="ref"} readonly                  Clears the selection and does not copy it to
                                                                   the clipboard.

  [contract\<Selection.contract\>]{role="ref"} readonly            Contracts the selection.

  [copy\<Selection.copy\>]{role="ref"} readonly                    Copies the selection to the clipboard.

  [cut\<Selection.cut\>]{role="ref"} readonly                      Cuts the current selection to the clipboard.

  [deselect\<Selection.deselect\>]{role="ref"} readonly            Deselects the current selection.

  [expand\<Selection.expand\>]{role="ref"} readonly                Expands the selection.

  [feather\<Selection.feather\>]{role="ref"} readonly              Feathers the edges of the selection.

  [fill\<Selection.fill\>]{role="ref"} readonly                    Fills the selection.

  [grow\<Selection.grow\>]{role="ref"} readonly                    Grows the selection to include all adjacent
                                                                   pixels falling within the specified tolerance
                                                                   range.

  [invert\<Selection.invert\>]{role="ref"} readonly                Inverts the selection.

  [load\<Selection.load\>]{role="ref"} readonly                    Loads the selection from the specified channel.

  [makeWorkPath\<Selection.makeWorkPath\>]{role="ref"} readonly    Makes this selection item the workpath for this
                                                                   document.

  [resize\<Selection.resize\>]{role="ref"} readonly                Resizes the selected area to the specified
                                                                   dimensions and anchor position.

  [resizeBoundary\<Selection.resizeBoundary\>]{role="ref"}         Scales the boundary of the selection.
  readonly                                                         

  [rotate\<Selection.rotate\>]{role="ref"} readonly                Rotates the object.

  [rotateBoundary\<Selection.rotateBoundary\>]{role="ref"}         Rotates the boundary of the selection.
  readonly                                                         

  [select\<Selection.select\>]{role="ref"} readonly                Selects the specified region.

  [selectAll\<Selection.selectAll\>]{role="ref"} readonly          Selects the entire layer.

  [selectBorder\<Selection.selectBorder\>]{role="ref"} readonly    Selects the selection border only (in the
                                                                   specified width); subsequent actions do not
                                                                   affect the selected area within the borders.

  [similar\<Selection.similar\>]{role="ref"} readonly              Grows the selection to include pixels
                                                                   throughout the image falling within the
                                                                   tolerance range.

  [smooth\<Selection.smooth\>]{role="ref"} readonly                Cleans up stray pixels left inside or outside a
                                                                   color-based selection (within the radius
                                                                   specified in pixels).

  [store\<Selection.store\>]{role="ref"} readonly                  Saves the selection as a channel.

  [stroke\<Selection.stroke\>]{role="ref"} readonly                Strokes the selection.

  [translate\<Selection.translate\>]{role="ref"} readonly          Moves the object relative to its current
                                                                   position.

  [translateBoundary\<Selection.translateBoundary\>]{role="ref"}   Moves the boundary of selection relative to its
  readonly                                                         current position.
  ---------------------------------------------------------------- -----------------------------------------------

::: {.container .hide}
::: {.toctree}
Selection/parent.rst Selection/typename.rst Selection/bounds.rst
Selection/solid.rst

Selection/clear.rst Selection/copy.rst Selection/cut.rst
Selection/selectBorder.rst Selection/contract.rst Selection/fill.rst
Selection/stroke.rst Selection/selectAll.rst Selection/deselect.rst
Selection/select.rst Selection/expand.rst Selection/feather.rst
Selection/grow.rst Selection/invert.rst Selection/similar.rst
Selection/smooth.rst Selection/store.rst Selection/load.rst
Selection/translate.rst Selection/translateBoundary.rst
Selection/rotate.rst Selection/rotateBoundary.rst Selection/resize.rst
Selection/resizeBoundary.rst Selection/makeWorkPath.rst
:::
:::
