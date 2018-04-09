.. _ShapeOperation:

================================================
ShapeOperation
================================================


Description
-----------



Specifies how to combine the shapes if the destination image already has a selection.




Static Properties
^^^^^^^^^^^^^^^^^

+---------------------------------------------------------------+-------------------------------------------------------------------------+
| :ref:`SHAPEADD<ShapeOperation.SHAPEADD>` readonly             | Adds the shapes.                                                        |
+---------------------------------------------------------------+-------------------------------------------------------------------------+
| :ref:`SHAPEINTERSECT<ShapeOperation.SHAPEINTERSECT>` readonly | The resulting shape is the area of intersection between the two shapes. |
+---------------------------------------------------------------+-------------------------------------------------------------------------+
| :ref:`SHAPESUBTRACT<ShapeOperation.SHAPESUBTRACT>` readonly   | Subtracts the loaded shape from the selection is the destination image. |
+---------------------------------------------------------------+-------------------------------------------------------------------------+
| :ref:`SHAPEXOR<ShapeOperation.SHAPEXOR>` readonly             | Replaces the shape in the destination image with the loaded selection.  |
+---------------------------------------------------------------+-------------------------------------------------------------------------+












.. container:: hide

   .. toctree::
      :hidden:
      :maxdepth: 1

      
      ShapeOperation/SHAPEADD.rst
      ShapeOperation/SHAPEXOR.rst
      ShapeOperation/SHAPEINTERSECT.rst
      ShapeOperation/SHAPESUBTRACT.rst
      

      
      
      
      