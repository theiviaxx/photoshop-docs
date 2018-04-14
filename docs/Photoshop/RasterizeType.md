RasterizeType {#RasterizeType}
=============

Description
-----------

The type of the layer content to rasterize.

### Static Properties

  -------------------------------------------------------------------- ----------------------------------------
  [ENTIRELAYER\<RasterizeType.ENTIRELAYER\>]{role="ref"} readonly      Rasterizes all vector data on the layer.

  [FILLCONTENT\<RasterizeType.FILLCONTENT\>]{role="ref"} readonly      Rasterizes the fill of a shape layer,
                                                                       leaving the vector mask.

  [LAYERCLIPPINGPATH\<RasterizeType.LAYERCLIPPINGPATH\>]{role="ref"}   Rasterizes the vector mask of a shape
  readonly                                                             layer, turning it into a layer mask.

  [LINKEDLAYERS\<RasterizeType.LINKEDLAYERS\>]{role="ref"} readonly    Rasterizes the selected layers.

  [SHAPE\<RasterizeType.SHAPE\>]{role="ref"} readonly                  Rasterizes a shape layer.

  [TEXTCONTENTS\<RasterizeType.TEXTCONTENTS\>]{role="ref"} readonly    Rasterizes the type on a type layer.
                                                                       Doesn\'t rasterize any other vector data
                                                                       on the layer.
  -------------------------------------------------------------------- ----------------------------------------

::: {.container .hide}
::: {.toctree}
RasterizeType/TEXTCONTENTS.rst RasterizeType/SHAPE.rst
RasterizeType/FILLCONTENT.rst RasterizeType/LAYERCLIPPINGPATH.rst
RasterizeType/ENTIRELAYER.rst RasterizeType/LINKEDLAYERS.rst
:::
:::
