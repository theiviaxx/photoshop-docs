EPSSaveOptions {#EPSSaveOptions}
==============

Description
-----------

Options for saving a document in EPS format.

### Static Properties

  --------------------------------------------------------------------- -------------------------------------------
  [embedColorProfile\<EPSSaveOptions.embedColorProfile\>]{role="ref"}   If true, the color profile is embedded in
  readonly                                                              the document.

  [encoding\<EPSSaveOptions.encoding\>]{role="ref"} readonly            The type of encoding to use for the
                                                                        document.

  [halftoneScreen\<EPSSaveOptions.halftoneScreen\>]{role="ref"}         If true, includes the halftone screen.
  readonly                                                              

  [interpolation\<EPSSaveOptions.interpolation\>]{role="ref"} readonly  If true, uses image interpolation.

  [preview\<EPSSaveOptions.preview\>]{role="ref"} readonly              The type of preview.

  [psColorManagement\<EPSSaveOptions.psColorManagement\>]{role="ref"}   If true, uses PostScript color management.
  readonly                                                              

  [transferFunction\<EPSSaveOptions.transferFunction\>]{role="ref"}     If true, includes the transfer functions in
  readonly                                                              the document to compensate for dot gain
                                                                        between the image and film.

  [transparentWhites\<EPSSaveOptions.transparentWhites\>]{role="ref"}   If true, displays white areas as
  readonly                                                              transparent. Valid only for documents in
                                                                        BitMap mode.

  [vectorData\<EPSSaveOptions.vectorData\>]{role="ref"} readonly        If true, includes vector data. Valid only
                                                                        when the document contains vector data
                                                                        (un-rasterized text).
  --------------------------------------------------------------------- -------------------------------------------

::: {.container .hide}
::: {.toctree}
EPSSaveOptions/embedColorProfile.rst EPSSaveOptions/preview.rst
EPSSaveOptions/encoding.rst EPSSaveOptions/halftoneScreen.rst
EPSSaveOptions/transferFunction.rst EPSSaveOptions/psColorManagement.rst
EPSSaveOptions/vectorData.rst EPSSaveOptions/interpolation.rst
EPSSaveOptions/transparentWhites.rst
:::
:::
