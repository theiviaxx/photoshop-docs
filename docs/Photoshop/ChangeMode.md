ChangeMode {#ChangeMode}
==========

Description
-----------

The destination color mode. Note: Color images must be changed to
Grayscale mode before you can change them to Bitmap mode.

### Static Properties

  ------------------------------------------------------- ------------------------------------------------------
  [BITMAP\<ChangeMode.BITMAP\>]{role="ref"} readonly      Bitmap. Note: Color images must be changed to
                                                          Grayscale mode before you can change them to Bitmap
                                                          mode.

  [CMYK\<ChangeMode.CMYK\>]{role="ref"} readonly          CMYK.

  [GRAYSCALE\<ChangeMode.GRAYSCALE\>]{role="ref"}         Grayscale.
  readonly                                                

  [INDEXEDCOLOR\<ChangeMode.INDEXEDCOLOR\>]{role="ref"}   Indexed color, in which the number of colors in the
  readonly                                                image is reduced to at most 256, the standard number
                                                          of colors supported by the GIF and PNG-8 formats and
                                                          many multimedia applications.

  [LAB\<ChangeMode.LAB\>]{role="ref"} readonly            Lab.

  [MULTICHANNEL\<ChangeMode.MULTICHANNEL\>]{role="ref"}   Image with multiple color channels.
  readonly                                                

  [RGB\<ChangeMode.RGB\>]{role="ref"} readonly            RGB.
  ------------------------------------------------------- ------------------------------------------------------

::: {.container .hide}
::: {.toctree}
ChangeMode/GRAYSCALE.rst ChangeMode/RGB.rst ChangeMode/CMYK.rst
ChangeMode/LAB.rst ChangeMode/BITMAP.rst ChangeMode/INDEXEDCOLOR.rst
ChangeMode/MULTICHANNEL.rst
:::
:::
