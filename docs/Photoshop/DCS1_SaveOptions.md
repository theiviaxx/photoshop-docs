DCS1\_SaveOptions {#DCS1_SaveOptions}
=================

Description
-----------

Options for saving a document in Photoshop DCS 1.0 format.

### Static Properties

  ------------------------------------------------------------------------ ------------------------------------------
  [DCS\<DCS1\_SaveOptions.DCS\>]{role="ref"} readonly                      The DCS type.

  [embedColorProfile\<DCS1\_SaveOptions.embedColorProfile\>]{role="ref"}   If true, the color profile is embedded in
  readonly                                                                 the document.

  [encoding\<DCS1\_SaveOptions.encoding\>]{role="ref"} readonly            The type of encoding to use for the
                                                                           document.

  [halftoneScreen\<DCS1\_SaveOptions.halftoneScreen\>]{role="ref"}         If true, includes halftone screen.
  readonly                                                                 

  [interpolation\<DCS1\_SaveOptions.interpolation\>]{role="ref"} readonly  If true, image interpolation is used.

  [preview\<DCS1\_SaveOptions.preview\>]{role="ref"} readonly              The type of preview.

  [transferFunction\<DCS1\_SaveOptions.transferFunction\>]{role="ref"}     If true, includes transfer functions in
  readonly                                                                 the document to compensate for dot gain
                                                                           between the image and film.

  [vectorData\<DCS1\_SaveOptions.vectorData\>]{role="ref"} readonly        If true, includes vector data. Valid only
                                                                           if the document contains vector data
                                                                           (un-rasterized text).
  ------------------------------------------------------------------------ ------------------------------------------

::: {.container .hide}
::: {.toctree}
DCS1\_SaveOptions/embedColorProfile.rst DCS1\_SaveOptions/preview.rst
DCS1\_SaveOptions/DCS.rst DCS1\_SaveOptions/encoding.rst
DCS1\_SaveOptions/halftoneScreen.rst
DCS1\_SaveOptions/transferFunction.rst DCS1\_SaveOptions/vectorData.rst
DCS1\_SaveOptions/interpolation.rst
:::
:::
