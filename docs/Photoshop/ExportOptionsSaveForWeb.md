ExportOptionsSaveForWeb {#ExportOptionsSaveForWeb}
=======================

Description
-----------

Options for exporting Save For Web files.

### Static Properties

  -------------------------------------------------------------------------------- ----------------------------------------
  [PNG8\<ExportOptionsSaveForWeb.PNG8\>]{role="ref"} readonly                      If true, uses 8 bits. If false, uses 24
                                                                                   bits. Valid only when \'format\' = PNG.

  [blur\<ExportOptionsSaveForWeb.blur\>]{role="ref"} readonly                      The amount of blur to apply to the image
                                                                                   to reduce artifacts.

  [colorReduction\<ExportOptionsSaveForWeb.colorReduction\>]{role="ref"} readonly  The color reduction algorithm.

  [colors\<ExportOptionsSaveForWeb.colors\>]{role="ref"} readonly                  The number of colors in the palette.

  [dither\<ExportOptionsSaveForWeb.dither\>]{role="ref"} readonly                  The type of dither.

  [ditherAmount\<ExportOptionsSaveForWeb.ditherAmount\>]{role="ref"} readonly      The amount of dither. Valid only when
                                                                                   \'dither\' = diffusion.

  [format\<ExportOptionsSaveForWeb.format\>]{role="ref"} readonly                  The file format to use. Save For Web
                                                                                   supports only Compuserve GIF, JPEG,
                                                                                   PNG-8, PNG-24, and BMP formats.

  [includeProfile\<ExportOptionsSaveForWeb.includeProfile\>]{role="ref"} readonly  If true, includes the document\'s
                                                                                   embedded profile.

  [interlaced\<ExportOptionsSaveForWeb.interlaced\>]{role="ref"} readonly          If true, the image downloads in multiple
                                                                                   passes, progressive.

  [lossy\<ExportOptionsSaveForWeb.lossy\>]{role="ref"} readonly                    The amount of lossiness allowed.

  [matteColor\<ExportOptionsSaveForWeb.matteColor\>]{role="ref"} readonly          The colors to blend transparent pixels
                                                                                   against.

  [optimized\<ExportOptionsSaveForWeb.optimized\>]{role="ref"} readonly            If true, creates smaller but less
                                                                                   compatible files.

  [quality\<ExportOptionsSaveForWeb.quality\>]{role="ref"} readonly                The quality of the produced image (as a
                                                                                   percentage). Range: 0 to 100.

  [transparency\<ExportOptionsSaveForWeb.transparency\>]{role="ref"} readonly      If true, transparent areas of the image
                                                                                   are included in the saved image.

  [transparencyAmount\<ExportOptionsSaveForWeb.transparencyAmount\>]{role="ref"}   The amount of transparency dither. Valid
  readonly                                                                         only when \'transparency\' = true.

  [transparencyDither\<ExportOptionsSaveForWeb.transparencyDither\>]{role="ref"}   The transparency dither algorithm.
  readonly                                                                         

  [webSnap\<ExportOptionsSaveForWeb.webSnap\>]{role="ref"} readonly                The tolerance amount within which to
                                                                                   snap close colors to web palette colors.
  -------------------------------------------------------------------------------- ----------------------------------------

::: {.container .hide}
::: {.toctree}
ExportOptionsSaveForWeb/format.rst ExportOptionsSaveForWeb/PNG8.rst
ExportOptionsSaveForWeb/lossy.rst
ExportOptionsSaveForWeb/colorReduction.rst
ExportOptionsSaveForWeb/colors.rst ExportOptionsSaveForWeb/dither.rst
ExportOptionsSaveForWeb/ditherAmount.rst
ExportOptionsSaveForWeb/transparency.rst
ExportOptionsSaveForWeb/transparencyDither.rst
ExportOptionsSaveForWeb/transparencyAmount.rst
ExportOptionsSaveForWeb/interlaced.rst
ExportOptionsSaveForWeb/matteColor.rst
ExportOptionsSaveForWeb/webSnap.rst
ExportOptionsSaveForWeb/optimized.rst
ExportOptionsSaveForWeb/quality.rst
ExportOptionsSaveForWeb/includeProfile.rst
ExportOptionsSaveForWeb/blur.rst
:::
:::
