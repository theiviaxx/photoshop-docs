TiffEncodingType {#TiffEncodingType}
================

Description
-----------

The encoding to use when saving to TIFF format.

### Static Properties

  --------------------------------------------------- ------------------------------------------------
  [JPEG\<TiffEncodingType.JPEG\>]{role="ref"}         JPEG compression, which is lossy and recommended
  readonly                                            for continuous-tone images, such as photographs.

  [NONE\<TiffEncodingType.NONE\>]{role="ref"}         No compression.
  readonly                                            

  [TIFFLZW\<TiffEncodingType.TIFFLZW\>]{role="ref"}   LZW compression, which is lossless and most
  readonly                                            useful for images with large areas of single
                                                      color.

  [TIFFZIP\<TiffEncodingType.TIFFZIP\>]{role="ref"}   Zip compression, which is lossless and most
  readonly                                            effective for images that contain large areas of
                                                      single color.
  --------------------------------------------------- ------------------------------------------------

::: {.container .hide}
::: {.toctree}
TiffEncodingType/NONE.rst TiffEncodingType/TIFFLZW.rst
TiffEncodingType/JPEG.rst TiffEncodingType/TIFFZIP.rst
:::
:::
