DocumentMode {#DocumentMode}
============

Description
-----------

The document\'s color mode.

### Static Properties

  --------------------------------------------------------- -----------------------------------------------------
  [BITMAP\<DocumentMode.BITMAP\>]{role="ref"} readonly      Bitmap, which uses one of two color values (black or
                                                            white) to represent the pixels in an image.

  [CMYK\<DocumentMode.CMYK\>]{role="ref"} readonly          CMYK.

  [DUOTONE\<DocumentMode.DUOTONE\>]{role="ref"} readonly    Duotone mode, which creates monotone, duotone
                                                            (two-color), tritone (three-color), and quadtone
                                                            (four-color) grayscale images using one to four
                                                            custom inks.

  [GRAYSCALE\<DocumentMode.GRAYSCALE\>]{role="ref"}         Grayscale.
  readonly                                                  

  [INDEXEDCOLOR\<DocumentMode.INDEXEDCOLOR\>]{role="ref"}   Indexed color, in which the number of colors in the
  readonly                                                  image is at most 256, the standard number of colors
                                                            supported by the GIF and PNG-8 formats and many
                                                            multimedia applications.

  [LAB\<DocumentMode.LAB\>]{role="ref"} readonly            Lab.

  [MULTICHANNEL\<DocumentMode.MULTICHANNEL\>]{role="ref"}   Image with multiple color channels.
  readonly                                                  

  [RGB\<DocumentMode.RGB\>]{role="ref"} readonly            RGB.
  --------------------------------------------------------- -----------------------------------------------------

::: {.container .hide}
::: {.toctree}
DocumentMode/GRAYSCALE.rst DocumentMode/RGB.rst DocumentMode/CMYK.rst
DocumentMode/LAB.rst DocumentMode/BITMAP.rst
DocumentMode/INDEXEDCOLOR.rst DocumentMode/MULTICHANNEL.rst
DocumentMode/DUOTONE.rst
:::
:::
