GIFSaveOptions {#GIFSaveOptions}
==============

Description
-----------

Options for saving a document in GIF format.

### Static Properties

  ------------------------------------------------------------------------- ----------------------------------------------
  [colors\<GIFSaveOptions.colors\>]{role="ref"} readonly                    The number of colors in palette. Not valid for
                                                                            all palette types.

  [dither\<GIFSaveOptions.dither\>]{role="ref"} readonly                    The type of dither.

  [ditherAmount\<GIFSaveOptions.ditherAmount\>]{role="ref"} readonly        The amount of dither. Valid only when \'dither
                                                                            type\' is diffusion. Range: 1 to 100.

  [forced\<GIFSaveOptions.forced\>]{role="ref"} readonly                    The type of colors to force into the color
                                                                            palette.

  [interlaced\<GIFSaveOptions.interlaced\>]{role="ref"} readonly            If true, rows are interlaced.

  [matte\<GIFSaveOptions.matte\>]{role="ref"} readonly                      The color to use to fill anti-aliased edges
                                                                            adjacent to transparent areas of the image.
                                                                            Default: white.

  [palette\<GIFSaveOptions.palette\>]{role="ref"} readonly                  The type of palette to use.

  [preserveExactColors\<GIFSaveOptions.preserveExactColors\>]{role="ref"}   If true, protects colors in the image that
  readonly                                                                  contain entries in the color table from being
                                                                            dithered. Valid only when \'dither\' =
                                                                            diffusion.

  [transparency\<GIFSaveOptions.transparency\>]{role="ref"} readonly        If true, preserves transparent ares of the
                                                                            image during GIF conversion.
  ------------------------------------------------------------------------- ----------------------------------------------

::: {.container .hide}
::: {.toctree}
GIFSaveOptions/colors.rst GIFSaveOptions/dither.rst
GIFSaveOptions/ditherAmount.rst GIFSaveOptions/forced.rst
GIFSaveOptions/interlaced.rst GIFSaveOptions/matte.rst
GIFSaveOptions/palette.rst GIFSaveOptions/preserveExactColors.rst
GIFSaveOptions/transparency.rst
:::
:::
