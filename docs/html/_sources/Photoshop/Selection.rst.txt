.. _Selection:

================================================
Selection
================================================


Description
-----------

The selected area of the document or layer.




Properties
^^^^^^^^^^

+----------------------------------------------+----------------------------------------------------+
| :ref:`bounds<Selection.bounds>` readonly     | The bounding rectangle of the entire selection.    |
+----------------------------------------------+----------------------------------------------------+
| :ref:`parent<Selection.parent>` readonly     | The object's container.                            |
+----------------------------------------------+----------------------------------------------------+
| :ref:`solid<Selection.solid>` readonly       | If true, the bounding rectangle a solid rectangle. |
+----------------------------------------------+----------------------------------------------------+
| :ref:`typename<Selection.typename>` readonly | The class name of the object.                      |
+----------------------------------------------+----------------------------------------------------+







Methods
^^^^^^^

+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`clear<Selection.clear>` readonly                         | Clears the selection and does not copy it to the clipboard.                                                                        |
+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`contract<Selection.contract>` readonly                   | Contracts the selection.                                                                                                           |
+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`copy<Selection.copy>` readonly                           | Copies the selection to the clipboard.                                                                                             |
+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`cut<Selection.cut>` readonly                             | Cuts the current selection to the clipboard.                                                                                       |
+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`deselect<Selection.deselect>` readonly                   | Deselects the current selection.                                                                                                   |
+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`expand<Selection.expand>` readonly                       | Expands the selection.                                                                                                             |
+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`feather<Selection.feather>` readonly                     | Feathers the edges of the selection.                                                                                               |
+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`fill<Selection.fill>` readonly                           | Fills the selection.                                                                                                               |
+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`grow<Selection.grow>` readonly                           | Grows the selection to include all adjacent pixels falling within the specified tolerance range.                                   |
+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`invert<Selection.invert>` readonly                       | Inverts the selection.                                                                                                             |
+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`load<Selection.load>` readonly                           | Loads the selection from the specified channel.                                                                                    |
+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`makeWorkPath<Selection.makeWorkPath>` readonly           | Makes this selection item the workpath for this document.                                                                          |
+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`resize<Selection.resize>` readonly                       | Resizes the selected area to the specified dimensions and anchor position.                                                         |
+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`resizeBoundary<Selection.resizeBoundary>` readonly       | Scales the boundary of the selection.                                                                                              |
+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`rotate<Selection.rotate>` readonly                       | Rotates the object.                                                                                                                |
+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`rotateBoundary<Selection.rotateBoundary>` readonly       | Rotates the boundary of the selection.                                                                                             |
+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`select<Selection.select>` readonly                       | Selects the specified region.                                                                                                      |
+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`selectAll<Selection.selectAll>` readonly                 | Selects the entire layer.                                                                                                          |
+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`selectBorder<Selection.selectBorder>` readonly           | Selects the selection border only (in the specified width); subsequent actions do not affect the selected area within the borders. |
+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`similar<Selection.similar>` readonly                     | Grows the selection to include pixels throughout the image falling within the tolerance range.                                     |
+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`smooth<Selection.smooth>` readonly                       | Cleans up stray pixels left inside or outside a color-based selection (within the radius specified in pixels).                     |
+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`store<Selection.store>` readonly                         | Saves the selection as a channel.                                                                                                  |
+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`stroke<Selection.stroke>` readonly                       | Strokes the selection.                                                                                                             |
+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`translate<Selection.translate>` readonly                 | Moves the object relative to its current position.                                                                                 |
+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`translateBoundary<Selection.translateBoundary>` readonly | Moves the boundary of selection relative to its current position.                                                                  |
+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+






.. container:: hide

   .. toctree::
      :hidden:
      :maxdepth: 1

      Selection/parent.rst
      Selection/typename.rst
      Selection/bounds.rst
      Selection/solid.rst
      
      

      Selection/clear.rst
      Selection/copy.rst
      Selection/cut.rst
      Selection/selectBorder.rst
      Selection/contract.rst
      Selection/fill.rst
      Selection/stroke.rst
      Selection/selectAll.rst
      Selection/deselect.rst
      Selection/select.rst
      Selection/expand.rst
      Selection/feather.rst
      Selection/grow.rst
      Selection/invert.rst
      Selection/similar.rst
      Selection/smooth.rst
      Selection/store.rst
      Selection/load.rst
      Selection/translate.rst
      Selection/translateBoundary.rst
      Selection/rotate.rst
      Selection/rotateBoundary.rst
      Selection/resize.rst
      Selection/resizeBoundary.rst
      Selection/makeWorkPath.rst
      
      
      
      