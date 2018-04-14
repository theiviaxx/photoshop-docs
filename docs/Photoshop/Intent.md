Intent {#Intent}
======

Description
-----------

The color conversion intent.

### Static Properties

  ------------------------------------------------------------------- --------------------------------------------------------
  [ABSOLUTECOLORIMETRIC\<Intent.ABSOLUTECOLORIMETRIC\>]{role="ref"}   Aims to maintain color accuracy at the expense of
  readonly                                                            preserving relationships between colors and is suitable
                                                                      for proofing to simulate the output of a particular
                                                                      device. This intent is particularly useful for
                                                                      previewing how paper color affects printed colors.

  [PERCEPTUAL\<Intent.PERCEPTUAL\>]{role="ref"} readonly              Gives priority to colors for which the human eye has
                                                                      greater sensitivity.

  [RELATIVECOLORIMETRIC\<Intent.RELATIVECOLORIMETRIC\>]{role="ref"}   Compares the extreme highlight of the source color space
  readonly                                                            to that of the destination color space and shifts all
                                                                      colors accordingly. Out of gamut colors are shifted to
                                                                      the closest reproducible color in the destination color
                                                                      space.

  [SATURATION\<Intent.SATURATION\>]{role="ref"} readonly              Tries to produce vivid colors in an image at the expense
                                                                      of color accuracy.
  ------------------------------------------------------------------- --------------------------------------------------------

::: {.container .hide}
::: {.toctree}
Intent/PERCEPTUAL.rst Intent/SATURATION.rst
Intent/RELATIVECOLORIMETRIC.rst Intent/ABSOLUTECOLORIMETRIC.rst
:::
:::
