UndefinedAreas {#UndefinedAreas}
==============

Description
-----------

The method to use to treat undistorted areas or areas left blank in an
image to which a filter in the Distort category has been applied.

### Static Properties

  ------------------------------------------------------------------- ------------------------------------------------
  [REPEATEDGEPIXELS\<UndefinedAreas.REPEATEDGEPIXELS\>]{role="ref"}   Extends the colors of pixels along the edge of
  readonly                                                            the image in the direction specified. Banding
                                                                      may result if the edge pixels are different
                                                                      colors.

  [WRAPAROUND\<UndefinedAreas.WRAPAROUND\>]{role="ref"} readonly      Fills the undefined space with content from the
                                                                      opposite edge of the image.
  ------------------------------------------------------------------- ------------------------------------------------

::: {.container .hide}
::: {.toctree}
UndefinedAreas/WRAPAROUND.rst UndefinedAreas/REPEATEDGEPIXELS.rst
:::
:::
