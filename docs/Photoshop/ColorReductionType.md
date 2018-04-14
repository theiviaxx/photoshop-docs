ColorReductionType {#ColorReductionType}
==================

Description
-----------

The color reduction algorithm.

### Static Properties

  ------------------------------------------------------------- ------------------------------------------------------
  [ADAPTIVE\<ColorReductionType.ADAPTIVE\>]{role="ref"}         Samples color from the spectrum appearing most
  readonly                                                      commonly in the image.

  [BLACKWHITE\<ColorReductionType.BLACKWHITE\>]{role="ref"}     Uses a set palette of colors.
  readonly                                                      

  [CUSTOM\<ColorReductionType.CUSTOM\>]{role="ref"} readonly    Uses a color palette that is created or modified by
                                                                the user. If you open an existing GIF or PNG-8 file,
                                                                it will have a custom color palette.

  [GRAYSCALE\<ColorReductionType.GRAYSCALE\>]{role="ref"}       Uses a set palette of colors.
  readonly                                                      

  [MACINTOSH\<ColorReductionType.MACINTOSH\>]{role="ref"}       Uses a set palette of colors.
  readonly                                                      

  [PERCEPTUAL\<ColorReductionType.PERCEPTUAL\>]{role="ref"}     Gives priority to colors for which the human eye has
  readonly                                                      greater sensitivity.

  [RESTRICTIVE\<ColorReductionType.RESTRICTIVE\>]{role="ref"}   Uses the standard 216-color color table common to
  readonly                                                      Windows and Mac OS 8-bit (256-color or web-safe
                                                                palette); ensures that no browser dither is applied
                                                                when the image is displayed using 8-bit color.

  [SELECTIVE\<ColorReductionType.SELECTIVE\>]{role="ref"}       Gives priority to broad areas of color and the
  readonly                                                      preservation of web colors; usually produces images
                                                                with the greatest color integrity.

  [WINDOWS\<ColorReductionType.WINDOWS\>]{role="ref"} readonly  Uses a set palette of colors.
  ------------------------------------------------------------- ------------------------------------------------------

::: {.container .hide}
::: {.toctree}
ColorReductionType/PERCEPTUAL.rst ColorReductionType/SELECTIVE.rst
ColorReductionType/ADAPTIVE.rst ColorReductionType/RESTRICTIVE.rst
ColorReductionType/CUSTOM.rst ColorReductionType/BLACKWHITE.rst
ColorReductionType/GRAYSCALE.rst ColorReductionType/MACINTOSH.rst
ColorReductionType/WINDOWS.rst
:::
:::
