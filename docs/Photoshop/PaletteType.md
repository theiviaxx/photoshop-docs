PaletteType {#PaletteType}
===========

Description
-----------

The palette type for converting an image to indexed color.

### Static Properties

  ---------------------------------------------------------------- --------------------------------------------------
  [EXACT\<PaletteType.EXACT\>]{role="ref"} readonly                The palette uses the exact colors appearing in the
                                                                   RGB image; available only if the image uses 256 or
                                                                   fewer colors.

  [LOCALADAPTIVE\<PaletteType.LOCALADAPTIVE\>]{role="ref"}         Creates a palette by sampling the colors from the
  readonly                                                         spectrum appearing most commonly in the image.

  [LOCALPERCEPTUAL\<PaletteType.LOCALPERCEPTUAL\>]{role="ref"}     Creates a custom palette by giving priority to
  readonly                                                         colors for in the image which the human eye has
                                                                   greater sensitivity.

  [LOCALSELECTIVE\<PaletteType.LOCALSELECTIVE\>]{role="ref"}       Creates a color table similar to the Perceptual
  readonly                                                         color table, but favoring broad areas of color in
                                                                   the image and the preservation of web colors.

  [MACOSPALETTE\<PaletteType.MACOSPALETTE\>]{role="ref"} readonly  The Mac OS default 8-bit palette, whch is based on
                                                                   a uniform sampling of RGB colors.

  [MASTERADAPTIVE\<PaletteType.MASTERADAPTIVE\>]{role="ref"}       Creates a palette by sampling the colors from the
  readonly                                                         spectrum appearing most commonly in a group of
                                                                   open images that share the same color palette.

  [MASTERPERCEPTUAL\<PaletteType.MASTERPERCEPTUAL\>]{role="ref"}   Creates a custom palette by giving priority to
  readonly                                                         colors in a group of open images with the same
                                                                   color palette for which the human eye has greater
                                                                   sensitivity.

  [MASTERSELECTIVE\<PaletteType.MASTERSELECTIVE\>]{role="ref"}     Creates a color table similar to the Master
  readonly                                                         Perceptual color table, but favoring broad areas
                                                                   of color and the preservation of web colors.

  [PREVIOUSPALETTE\<PaletteType.PREVIOUSPALETTE\>]{role="ref"}     Uses the custom palette from the previous
  readonly                                                         conversion, making it easy to convert several
                                                                   images with the same custom palette.

  [UNIFORM\<PaletteType.UNIFORM\>]{role="ref"} readonly            Creates a palette by uniformly sampling colors
                                                                   from the RGB color cube.

  [WEBPALETTE\<PaletteType.WEBPALETTE\>]{role="ref"} readonly      The 216-color palette that web browsers,
                                                                   regardless of platform, use to display images on a
                                                                   monitor limited to 256 colors.

  [WINDOWSPALETTE\<PaletteType.WINDOWSPALETTE\>]{role="ref"}       The Windows system\'s default 8-bit palette, whch
  readonly                                                         is based on a uniform sampling of RGB colors.
  ---------------------------------------------------------------- --------------------------------------------------

::: {.container .hide}
::: {.toctree}
PaletteType/EXACT.rst PaletteType/MACOSPALETTE.rst
PaletteType/WINDOWSPALETTE.rst PaletteType/WEBPALETTE.rst
PaletteType/UNIFORM.rst PaletteType/LOCALPERCEPTUAL.rst
PaletteType/LOCALSELECTIVE.rst PaletteType/LOCALADAPTIVE.rst
PaletteType/MASTERPERCEPTUAL.rst PaletteType/MASTERSELECTIVE.rst
PaletteType/MASTERADAPTIVE.rst PaletteType/PREVIOUSPALETTE.rst
:::
:::
