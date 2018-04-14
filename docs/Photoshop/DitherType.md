DitherType {#DitherType}
==========

Description
-----------

The type of dither.

### Static Properties

  ------------------------------------------------- -------------------------------------------------
  [DIFFUSION\<DitherType.DIFFUSION\>]{role="ref"}   Diffuses dither effects in random patterns across
  readonly                                          adjacent pixels.

  [NOISE\<DitherType.NOISE\>]{role="ref"} readonly  Applies a random pattern but without diffusing
                                                    the pattern across adjacent pixels; prevents the
                                                    appearance of seams.

  [NONE\<DitherType.NONE\>]{role="ref"} readonly    No dither is used.

  [PATTERN\<DitherType.PATTERN\>]{role="ref"}       Applies a halftone-like square pattern.
  readonly                                          
  ------------------------------------------------- -------------------------------------------------

::: {.container .hide}
::: {.toctree}
DitherType/NONE.rst DitherType/DIFFUSION.rst DitherType/PATTERN.rst
DitherType/NOISE.rst
:::
:::
