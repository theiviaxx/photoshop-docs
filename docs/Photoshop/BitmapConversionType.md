BitmapConversionType {#BitmapConversionType}
====================

Description
-----------

The quality of an image converted to bitmap mode.

### Static Properties

  ----------------------------------------------------------------------- -------------------------------------------------------
  [CUSTOMPATTERN\<BitmapConversionType.CUSTOMPATTERN\>]{role="ref"}       Simulates the effect of printing a grayscale image
  readonly                                                                through a custom halftone screen. This method lets you
                                                                          apply a screen texture, such as a wood grain, to an
                                                                          image. To use this option, you must first define a
                                                                          pattern.

  [DIFFUSIONDITHER\<BitmapConversionType.DIFFUSIONDITHER\>]{role="ref"}   Applies a random pattern that is usually less
  readonly                                                                noticeable than pattern dither. The dither effects are
                                                                          diffused across adjacent pixels. If you select this
                                                                          algorithm, specify a dither percentage to control the
                                                                          amount of dithering applied to the image.

  [HALFTHRESHOLD\<BitmapConversionType.HALFTHRESHOLD\>]{role="ref"}       50% Threshold.
  readonly                                                                

  [HALFTONESCREEN\<BitmapConversionType.HALFTONESCREEN\>]{role="ref"}     Lets you convert a grayscale image to simulated
  readonly                                                                halftone dots.

  [PATTERNDITHER\<BitmapConversionType.PATTERNDITHER\>]{role="ref"}       Applies a halftone-like square pattern to determine the
  readonly                                                                value of pixels.
  ----------------------------------------------------------------------- -------------------------------------------------------

::: {.container .hide}
::: {.toctree}
BitmapConversionType/HALFTHRESHOLD.rst
BitmapConversionType/PATTERNDITHER.rst
BitmapConversionType/DIFFUSIONDITHER.rst
BitmapConversionType/HALFTONESCREEN.rst
BitmapConversionType/CUSTOMPATTERN.rst
:::
:::
