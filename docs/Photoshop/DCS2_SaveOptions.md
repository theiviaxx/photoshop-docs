DCS2\_SaveOptions {#DCS2_SaveOptions}
=================

Description
-----------

Options for saving a document in Photoshop DCS 2.0 format.

### Static Properties

  ------------------------------------------------------------------------ ------------------------------------------
  [DCS\<DCS2\_SaveOptions.DCS\>]{role="ref"} readonly                      The DCS type.

  [embedColorProfile\<DCS2\_SaveOptions.embedColorProfile\>]{role="ref"}   If true, the color profile is embedded in
  readonly                                                                 the document.

  [encoding\<DCS2\_SaveOptions.encoding\>]{role="ref"} readonly            The type of encoding to use for document.

  [halftoneScreen\<DCS2\_SaveOptions.halftoneScreen\>]{role="ref"}         If true, includes halftone screen.
  readonly                                                                 

  [interpolation\<DCS2\_SaveOptions.interpolation\>]{role="ref"} readonly  If true, image interpolation is used.

  [multiFileDCS\<DCS2\_SaveOptions.multiFileDCS\>]{role="ref"} readonly    If true, saves color channels as multiple
                                                                           files.

  [preview\<DCS2\_SaveOptions.preview\>]{role="ref"} readonly              The type of preview.

  [spotColors\<DCS2\_SaveOptions.spotColors\>]{role="ref"} readonly        If true, the spot colors are saved.

  [transferFunction\<DCS2\_SaveOptions.transferFunction\>]{role="ref"}     If true, includes transfer functions in
  readonly                                                                 the document to compensate for dot gain
                                                                           between the image and film.

  [vectorData\<DCS2\_SaveOptions.vectorData\>]{role="ref"} readonly        If true, includes vector data. Valid only
                                                                           if the document contains vector data
                                                                           (un-rasterized text).
  ------------------------------------------------------------------------ ------------------------------------------

::: {.container .hide}
::: {.toctree}
DCS2\_SaveOptions/spotColors.rst DCS2\_SaveOptions/embedColorProfile.rst
DCS2\_SaveOptions/preview.rst DCS2\_SaveOptions/DCS.rst
DCS2\_SaveOptions/multiFileDCS.rst DCS2\_SaveOptions/encoding.rst
DCS2\_SaveOptions/halftoneScreen.rst
DCS2\_SaveOptions/transferFunction.rst DCS2\_SaveOptions/vectorData.rst
DCS2\_SaveOptions/interpolation.rst
:::
:::
