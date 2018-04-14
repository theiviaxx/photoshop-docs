BitmapConversionOptions {#BitmapConversionOptions}
=======================

Description
-----------

Options for changing the document mode to Bitmap.

### Static Properties

  ------------------------------------------------------------------ ----------------------------------------------
  [angle\<BitmapConversionOptions.angle\>]{role="ref"} readonly      The angle (in degrees) at which to orient
                                                                     individual dots. Valid only when \'method\' =
                                                                     halftone screen. Range: -180 to 180.

  [frequency\<BitmapConversionOptions.frequency\>]{role="ref"}       The number of printer dots per inch. Valid
  readonly                                                           only when \'method\' = halftone screen. Range:
                                                                     1.0 to 999.99.

  [method\<BitmapConversionOptions.method\>]{role="ref"} readonly    The conversion method.

  [patternName\<BitmapConversionOptions.patternName\>]{role="ref"}   The name of the pattern to use. Valid only
  readonly                                                           when \'method\' = custom.

  [resolution\<BitmapConversionOptions.resolution\>]{role="ref"}     The output resolution (in pixels per inch)
  readonly                                                           

  [shape\<BitmapConversionOptions.shape\>]{role="ref"} readonly      The dot shape. Valid only when \'method\' =
                                                                     halftone screen.
  ------------------------------------------------------------------ ----------------------------------------------

::: {.container .hide}
::: {.toctree}
BitmapConversionOptions/resolution.rst
BitmapConversionOptions/method.rst
BitmapConversionOptions/patternName.rst
BitmapConversionOptions/frequency.rst BitmapConversionOptions/angle.rst
BitmapConversionOptions/shape.rst
:::
:::
