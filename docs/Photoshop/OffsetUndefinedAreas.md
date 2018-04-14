OffsetUndefinedAreas {#OffsetUndefinedAreas}
====================

Description
-----------

The method to use to fill the empty space left by offsetting a an image
or selection.

### Static Properties

  ------------------------------------------------------------------------- -----------------------------------------------
  [REPEATEDGEPIXELS\<OffsetUndefinedAreas.REPEATEDGEPIXELS\>]{role="ref"}   Extends the colors of pixels along the edge of
  readonly                                                                  the image in the direction specified. Banding
                                                                            may result if the edge pixels are different
                                                                            colors.

  [SETTOBACKGROUND\<OffsetUndefinedAreas.SETTOBACKGROUND\>]{role="ref"}     For background layers, sets pixels to the
  readonly                                                                  background layer color. For nonbackground
                                                                            layers, sets the pixels to transparent.

  [WRAPAROUND\<OffsetUndefinedAreas.WRAPAROUND\>]{role="ref"} readonly      Fills the undefined space with content from the
                                                                            opposite edge of the image.
  ------------------------------------------------------------------------- -----------------------------------------------

::: {.container .hide}
::: {.toctree}
OffsetUndefinedAreas/SETTOBACKGROUND.rst
OffsetUndefinedAreas/WRAPAROUND.rst
OffsetUndefinedAreas/REPEATEDGEPIXELS.rst
:::
:::
