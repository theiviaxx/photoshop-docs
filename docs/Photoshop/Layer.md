Layer {#Layer}
=====

Description
-----------

A layer object.

Layers may contain nested layers, which are called sublayers in the user
interface. The layer object contains all of the page items in the
specific layer as elements. Your script can access page items as
elements of either the layer object or the document object.

### Properties

  -------------------------------------------------------- ---------------------------------------------
  [allLocked\<Layer.allLocked\>]{role="ref"} readonly      If true, the layer\'s contents and settings
                                                           are locked.

  [blendMode\<Layer.blendMode\>]{role="ref"} readonly      The mode to use when compositing an object.

  [bounds\<Layer.bounds\>]{role="ref"} readonly            If the Layer is a layer set, this property
                                                           returns a reference to the corresponding
                                                           layer set object.

  [boundsNoEffects\<Layer.boundsNoEffects\>]{role="ref"}   Bounding rectangle of the Layer not including
  readonly                                                 effects.

  [id\<Layer.id\>]{role="ref"} readonly                    The unique ID of this layer.

  [itemIndex\<Layer.itemIndex\>]{role="ref"} readonly      The layer index sans layer groups, how
                                                           Photoshop would index them.

  [linkedLayers\<Layer.linkedLayers\>]{role="ref"}         The layers linked to this layer.
  readonly                                                 

  [name\<Layer.name\>]{role="ref"} readonly                The name of the layer.

  [opacity\<Layer.opacity\>]{role="ref"} readonly          The layer\'s master opacity (as a
                                                           percentage). Range: 0.0 to 100.0.

  [parent\<Layer.parent\>]{role="ref"} readonly            The object\'s container.

  [typename\<Layer.typename\>]{role="ref"} readonly        The class name of the object.

  [visible\<Layer.visible\>]{role="ref"} readonly          If true, the layer is visible.

  [xmpMetadata\<Layer.xmpMetadata\>]{role="ref"} readonly  XMP metadata associated with the Layer.
  -------------------------------------------------------- ---------------------------------------------

### Methods

  -------------------------------------------- --------------------------------------
  [duplicate\<Layer.duplicate\>]{role="ref"}   Duplicate this object.
  readonly                                     

  [link\<Layer.link\>]{role="ref"} readonly    Links the layer with the specified
                                               layer.

  [move\<Layer.move\>]{role="ref"} readonly    Move the object.

  [moveToEnd\<Layer.moveToEnd\>]{role="ref"}   \...
  readonly                                     

  [remove\<Layer.remove\>]{role="ref"}         Deletes this object.
  readonly                                     

  [removeAll\<Layer.removeAll\>]{role="ref"}   Deletes all elements.
  readonly                                     

  [resize\<Layer.resize\>]{role="ref"}         Scales the object.
  readonly                                     

  [rotate\<Layer.rotate\>]{role="ref"}         Rotates the object.
  readonly                                     

  [translate\<Layer.translate\>]{role="ref"}   Moves the object relative to its
  readonly                                     current position.

  [unlink\<Layer.unlink\>]{role="ref"}         Unlinks the layer.
  readonly                                     
  -------------------------------------------- --------------------------------------

::: {.container .hide}
::: {.toctree}
Layer/parent.rst Layer/typename.rst Layer/name.rst Layer/allLocked.rst
Layer/blendMode.rst Layer/linkedLayers.rst Layer/opacity.rst
Layer/visible.rst Layer/id.rst Layer/itemIndex.rst Layer/bounds.rst
Layer/boundsNoEffects.rst Layer/xmpMetadata.rst

Layer/move.rst Layer/duplicate.rst Layer/moveToEnd.rst Layer/remove.rst
Layer/removeAll.rst Layer/unlink.rst Layer/link.rst Layer/translate.rst
Layer/rotate.rst Layer/resize.rst
:::
:::
