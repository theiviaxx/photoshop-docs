TiffSaveOptions {#TiffSaveOptions}
===============

Description
-----------

Options for saving a document in TIFF format.

### Static Properties

  ------------------------------------------------------------------------ -------------------------------------------------
  [alphaChannels\<TiffSaveOptions.alphaChannels\>]{role="ref"} readonly    If true, the alpha channels are saved.

  [annotations\<TiffSaveOptions.annotations\>]{role="ref"} readonly        If true, the annotations are saved.

  [byteOrder\<TiffSaveOptions.byteOrder\>]{role="ref"} readonly            The order in which the bytes will be read.
                                                                           Default: Mac OS when running in Mac OS, and IBM
                                                                           PC when running in Windows.

  [embedColorProfile\<TiffSaveOptions.embedColorProfile\>]{role="ref"}     If true, the color profile is embedded in the
  readonly                                                                 document.

  [imageCompression\<TiffSaveOptions.imageCompression\>]{role="ref"}       The compression type.
  readonly                                                                 

  [interleaveChannels\<TiffSaveOptions.interleaveChannels\>]{role="ref"}   If true, the channels in the image are
  readonly                                                                 interleaved.

  [jpegQuality\<TiffSaveOptions.jpegQuality\>]{role="ref"} readonly        The quality of the produced image, which is
                                                                           inversely proportionate to the amount of JPEG
                                                                           compression. Valid only for JPEG compressed TIFF
                                                                           documents. Range: 0 to 12.

  [layerCompression\<TiffSaveOptions.layerCompression\>]{role="ref"}       The method of compression to use when saving
  readonly                                                                 layers (as opposed to saving composite data).
                                                                           Valid only when \'layers\' = true.

  [layers\<TiffSaveOptions.layers\>]{role="ref"} readonly                  If true, the layers are saved.

  [saveImagePyramid\<TiffSaveOptions.saveImagePyramid\>]{role="ref"}       If true, preserves multi-resolution information.
  readonly                                                                 

  [spotColors\<TiffSaveOptions.spotColors\>]{role="ref"} readonly          If true, spot colors are saved.

  [transparency\<TiffSaveOptions.transparency\>]{role="ref"} readonly      If true, saves the transparency as an additional
                                                                           alpha channel when the file is opened in another
                                                                           application.
  ------------------------------------------------------------------------ -------------------------------------------------

::: {.container .hide}
::: {.toctree}
TiffSaveOptions/alphaChannels.rst TiffSaveOptions/layers.rst
TiffSaveOptions/annotations.rst TiffSaveOptions/spotColors.rst
TiffSaveOptions/embedColorProfile.rst
TiffSaveOptions/imageCompression.rst TiffSaveOptions/jpegQuality.rst
TiffSaveOptions/byteOrder.rst TiffSaveOptions/saveImagePyramid.rst
TiffSaveOptions/transparency.rst TiffSaveOptions/layerCompression.rst
TiffSaveOptions/interleaveChannels.rst
:::
:::
