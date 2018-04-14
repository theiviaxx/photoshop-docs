.. _Layer:

================================================
Layer
================================================


Description
-----------

A layer object.

Layers may contain nested layers, which are called sublayers in the user interface. The layer object contains all of the page items in the specific layer as elements. Your script can access page items as elements of either the layer object or the document object.


Properties
^^^^^^^^^^

+--------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| :ref:`allLocked<Layer.allLocked>` readonly             | If true, the layer's contents and settings are locked.                                                |
+--------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| :ref:`blendMode<Layer.blendMode>` readonly             | The mode to use when compositing an object.                                                           |
+--------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| :ref:`bounds<Layer.bounds>` readonly                   | If the Layer is a layer set, this property returns a reference to the corresponding layer set object. |
+--------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| :ref:`boundsNoEffects<Layer.boundsNoEffects>` readonly | Bounding rectangle of the Layer not including effects.                                                |
+--------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| :ref:`id<Layer.id>` readonly                           | The unique ID of this layer.                                                                          |
+--------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| :ref:`itemIndex<Layer.itemIndex>` readonly             | The layer index sans layer groups, how Photoshop would index them.                                    |
+--------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| :ref:`linkedLayers<Layer.linkedLayers>` readonly       | The layers linked to this layer.                                                                      |
+--------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| :ref:`name<Layer.name>` readonly                       | The name of the layer.                                                                                |
+--------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| :ref:`opacity<Layer.opacity>` readonly                 | The layer's master opacity (as a percentage). Range: 0.0 to 100.0.                                    |
+--------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| :ref:`parent<Layer.parent>` readonly                   | The object's container.                                                                               |
+--------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| :ref:`typename<Layer.typename>` readonly               | The class name of the object.                                                                         |
+--------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| :ref:`visible<Layer.visible>` readonly                 | If true, the layer is visible.                                                                        |
+--------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| :ref:`xmpMetadata<Layer.xmpMetadata>` readonly         | XMP metadata associated with the Layer.                                                               |
+--------------------------------------------------------+-------------------------------------------------------------------------------------------------------+







Methods
^^^^^^^

+--------------------------------------------+----------------------------------------------------+
| :ref:`duplicate<Layer.duplicate>` readonly | Duplicate this object.                             |
+--------------------------------------------+----------------------------------------------------+
| :ref:`link<Layer.link>` readonly           | Links the layer with the specified layer.          |
+--------------------------------------------+----------------------------------------------------+
| :ref:`move<Layer.move>` readonly           | Move the object.                                   |
+--------------------------------------------+----------------------------------------------------+
| :ref:`moveToEnd<Layer.moveToEnd>` readonly | ...                                                |
+--------------------------------------------+----------------------------------------------------+
| :ref:`remove<Layer.remove>` readonly       | Deletes this object.                               |
+--------------------------------------------+----------------------------------------------------+
| :ref:`removeAll<Layer.removeAll>` readonly | Deletes all elements.                              |
+--------------------------------------------+----------------------------------------------------+
| :ref:`resize<Layer.resize>` readonly       | Scales the object.                                 |
+--------------------------------------------+----------------------------------------------------+
| :ref:`rotate<Layer.rotate>` readonly       | Rotates the object.                                |
+--------------------------------------------+----------------------------------------------------+
| :ref:`translate<Layer.translate>` readonly | Moves the object relative to its current position. |
+--------------------------------------------+----------------------------------------------------+
| :ref:`unlink<Layer.unlink>` readonly       | Unlinks the layer.                                 |
+--------------------------------------------+----------------------------------------------------+






.. container:: hide

   .. toctree::
      :hidden:
      :maxdepth: 1

      Layer/parent.rst
      Layer/typename.rst
      Layer/name.rst
      Layer/allLocked.rst
      Layer/blendMode.rst
      Layer/linkedLayers.rst
      Layer/opacity.rst
      Layer/visible.rst
      Layer/id.rst
      Layer/itemIndex.rst
      Layer/bounds.rst
      Layer/boundsNoEffects.rst
      Layer/xmpMetadata.rst
      
      

      Layer/move.rst
      Layer/duplicate.rst
      Layer/moveToEnd.rst
      Layer/remove.rst
      Layer/removeAll.rst
      Layer/unlink.rst
      Layer/link.rst
      Layer/translate.rst
      Layer/rotate.rst
      Layer/resize.rst
      
      
      
      