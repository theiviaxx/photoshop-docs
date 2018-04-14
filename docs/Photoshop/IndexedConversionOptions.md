IndexedConversionOptions {#IndexedConversionOptions}
========================

Description
-----------

Options for converting an RGB image to an indexed color model.

### Static Properties

  ----------------------------------------------------------------------------------- -----------------------------------------------
  [colors\<IndexedConversionOptions.colors\>]{role="ref"} readonly                    The number of colors in the palette. Not valid
                                                                                      for all palette types.

  [dither\<IndexedConversionOptions.dither\>]{role="ref"} readonly                    The type of dither.

  [ditherAmount\<IndexedConversionOptions.ditherAmount\>]{role="ref"} readonly        The amount of dither. Valid only when
                                                                                      \'dither\' = diffusion.

  [forced\<IndexedConversionOptions.forced\>]{role="ref"} readonly                    The type of colors to force into the color
                                                                                      palette.

  [matte\<IndexedConversionOptions.matte\>]{role="ref"} readonly                      The color to use to fill anti-aliased edges
                                                                                      adjacent to transparent areas of the image.
                                                                                      When transparency = false, the matte color is
                                                                                      applied to transparent areas.

  [palette\<IndexedConversionOptions.palette\>]{role="ref"} readonly                  The type of palette.

  [preserveExactColors\<IndexedConversionOptions.preserveExactColors\>]{role="ref"}   If true, protects colors in the image that
  readonly                                                                            contain entries in the color table from being
                                                                                      dithered. Valid only when \'dither\' =
                                                                                      diffusion.

  [transparency\<IndexedConversionOptions.transparency\>]{role="ref"} readonly        If true, preserves transparent areas of the
                                                                                      image during conversion to GIF format.
  ----------------------------------------------------------------------------------- -----------------------------------------------

::: {.container .hide}
::: {.toctree}
IndexedConversionOptions/palette.rst IndexedConversionOptions/colors.rst
IndexedConversionOptions/forced.rst
IndexedConversionOptions/transparency.rst
IndexedConversionOptions/dither.rst
IndexedConversionOptions/ditherAmount.rst
IndexedConversionOptions/preserveExactColors.rst
IndexedConversionOptions/matte.rst
:::
:::
