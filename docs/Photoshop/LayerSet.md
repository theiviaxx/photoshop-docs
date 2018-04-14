LayerSet {#LayerSet}
========

Description
-----------

A group of layer objects, which can include art layer objects and other
(nested) layer set objects. A single command or set of commands
manipulates all layers in a layer set object.

### Properties

  ----------------------------------------------------------- ------------------------------------------
  [artLayers\<LayerSet.artLayers\>]{role="ref"} readonly      The art layers contained in this layer
                                                              set.

  [enabledChannels\<LayerSet.enabledChannels\>]{role="ref"}   The channels that are enabled for the
  readonly                                                    layer set. Must be a list of component
                                                              channels.

  [layerSets\<LayerSet.layerSets\>]{role="ref"} readonly      The layer sets contained within the layer
                                                              set.

  [layers\<LayerSet.layers\>]{role="ref"} readonly            The layers in this layer set.

  [parent\<LayerSet.parent\>]{role="ref"} readonly            The object\'s container.

  [typename\<LayerSet.typename\>]{role="ref"} readonly        The class name of the object.
  ----------------------------------------------------------- ------------------------------------------

### Methods

  --------------------------------------- -----------------------
  [add\<LayerSet.add\>]{role="ref"}       Adds an element.
  readonly                                

  [merge\<LayerSet.merge\>]{role="ref"}   Merges the layer set.
  readonly                                
  --------------------------------------- -----------------------

::: {.container .hide}
::: {.toctree}
LayerSet/parent.rst LayerSet/typename.rst LayerSet/enabledChannels.rst
LayerSet/layers.rst LayerSet/layerSets.rst LayerSet/artLayers.rst

LayerSet/add.rst LayerSet/merge.rst
:::
:::
