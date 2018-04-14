ResampleMethod {#ResampleMethod}
==============

Description
-----------

The method to use to resample the image.

### Static Properties

  ------------------------------------------------------------------- -------------------------------------------------
  [AUTOMATIC\<ResampleMethod.AUTOMATIC\>]{role="ref"} readonly        

  [BICUBIC\<ResampleMethod.BICUBIC\>]{role="ref"} readonly            Uses a weighted average to determine pixel color,
                                                                      which usually yields better results than the
                                                                      simple averageing method of downsampling.

  [BICUBICAUTOMATIC\<ResampleMethod.BICUBICAUTOMATIC\>]{role="ref"}   
  readonly                                                            

  [BICUBICSHARPER\<ResampleMethod.BICUBICSHARPER\>]{role="ref"}       A good method for reducing the size of an image
  readonly                                                            based on Bicubic interpolation with enhanced
                                                                      sharpening. Maintains the detail in a resampled
                                                                      image.

  [BICUBICSMOOTHER\<ResampleMethod.BICUBICSMOOTHER\>]{role="ref"}     A good method for enlarging images based on
  readonly                                                            Bicubic interpolation but designed to produce
                                                                      smoother results.

  [BILINEAR\<ResampleMethod.BILINEAR\>]{role="ref"} readonly          Averages the pixels in a sample area and replaces
                                                                      the entire area with the average pixel color at
                                                                      the specified resolution. Same as average
                                                                      downsampling.

  [NEARESTNEIGHBOR\<ResampleMethod.NEARESTNEIGHBOR\>]{role="ref"}     Chooses a pixel in the center of the sample area
  readonly                                                            and replaces the entire area with that pixel
                                                                      color. Same as subsampling.

  [NONE\<ResampleMethod.NONE\>]{role="ref"} readonly                  Does not resample.

  [PRESERVEDETAILS\<ResampleMethod.PRESERVEDETAILS\>]{role="ref"}     
  readonly                                                            
  ------------------------------------------------------------------- -------------------------------------------------

::: {.container .hide}
::: {.toctree}
ResampleMethod/NONE.rst ResampleMethod/NEARESTNEIGHBOR.rst
ResampleMethod/BILINEAR.rst ResampleMethod/BICUBIC.rst
ResampleMethod/BICUBICSHARPER.rst ResampleMethod/BICUBICSMOOTHER.rst
ResampleMethod/BICUBICAUTOMATIC.rst ResampleMethod/AUTOMATIC.rst
ResampleMethod/PRESERVEDETAILS.rst
:::
:::
