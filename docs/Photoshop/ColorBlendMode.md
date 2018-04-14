ColorBlendMode {#ColorBlendMode}
==============

Description
-----------

The color blend mode type.

### Static Properties

  ----------------------------------------------------------- ---------------------------------------------------------------
  [BEHIND\<ColorBlendMode.BEHIND\>]{role="ref"} readonly      Edits or paints only on the transparent part of a layer. Works
                                                              only in layers in which transparent pixels locked = false and
                                                              is analogous to painting on the back of transparent areas on a
                                                              sheet of acetate.

  [CLEAR\<ColorBlendMode.CLEAR\>]{role="ref"} readonly        Edits or paints each pixel and makes it transparent. Works only
                                                              in layers in which transparent pixels locked = false.

  [COLOR\<ColorBlendMode.COLOR\>]{role="ref"} readonly        Creates a result color with the luminance of the base color and
                                                              the hue and saturation of the blend color. This preserves the
                                                              gray levels in the image and is useful for coloring monochrome
                                                              images and for tinting color images.

  [COLORBURN\<ColorBlendMode.COLORBURN\>]{role="ref"}         Looks at the color information in each channel and darkens the
  readonly                                                    base color to reflect the blend color by increasing the
                                                              contrast. Blending with white produces no change.

  [COLORDODGE\<ColorBlendMode.COLORDODGE\>]{role="ref"}       Looks at the color information in each channel and brightens
  readonly                                                    the base color to reflect the blend color by decreasing the
                                                              contrast. Blending with black produces no change.

  [DARKEN\<ColorBlendMode.DARKEN\>]{role="ref"} readonly      Looks at the color information in each channel and selects the
                                                              base or blend color?whichever is darker?as the result color.
                                                              Pixels lighter than the blend color are replaced, and pixels
                                                              darker than the blend color do not change.

  [DIFFERENCE\<ColorBlendMode.DIFFERENCE\>]{role="ref"}       Looks at the color information in each channel and subtracts
  readonly                                                    either the blend color from the base color or the base color
                                                              from the blend color, depending on which has the greater
                                                              brightness value. Blending with white inverts the base color
                                                              values; blending with black produces no change.

  [DISSOLVE\<ColorBlendMode.DISSOLVE\>]{role="ref"} readonly  Edits or paints each pixel to make it the result color, which
                                                              is a random replacement of the pixels with the base color or
                                                              the blend color, depending on the opacity at any pixel
                                                              location.

  [DIVIDE\<ColorBlendMode.DIVIDE\>]{role="ref"} readonly      

  [EXCLUSION\<ColorBlendMode.EXCLUSION\>]{role="ref"}         Creates an effect similar to but lower in contrast than the
  readonly                                                    Difference mode. Blending with white inverts the base color
                                                              values. Blending with black produces no change.

  [HARDLIGHT\<ColorBlendMode.HARDLIGHT\>]{role="ref"}         Multiplies or screens the colors, depending on the blend color.
  readonly                                                    The effect is similar to shining a harsh spotlight on the
                                                              image. If the blend color (light source) is lighter than 50%
                                                              gray, the image is lightened, as if it were screened. This is
                                                              useful for adding highlights to an image. If the blend color is
                                                              darker than 50% gray, the image is darkened, as if it were
                                                              multiplied. This is useful for adding shadows to an image.
                                                              Painting with pure black or white results in pure black or
                                                              white.

  [HARDMIXBLEND\<ColorBlendMode.HARDMIXBLEND\>]{role="ref"}   Lighter colors lighten the result, and darker colors darken the
  readonly                                                    result. 50% gray as a blend color has no effect on the result
                                                              color. Lowering the fill opacity creates less
                                                              posterization/thresholding.

  [HUE\<ColorBlendMode.HUE\>]{role="ref"} readonly            Creates a result color with the luminance and saturation of the
                                                              base color and the hue of the blend color.

  [LIGHTEN\<ColorBlendMode.LIGHTEN\>]{role="ref"} readonly    Looks at the color information in each channel and selects the
                                                              base or blend color?whichever is lighter?as the result color.
                                                              Pixels darker than the blend color are replaced, and pixels
                                                              lighter than the blend color do not change.

  [LINEARBURN\<ColorBlendMode.LINEARBURN\>]{role="ref"}       Looks at the color information in each channel and darkens the
  readonly                                                    base color to reflect the blend color by decreasing the
                                                              brightness. Blending with white produces no change.

  [LINEARDODGE\<ColorBlendMode.LINEARDODGE\>]{role="ref"}     Looks at the color information in each channel and brightens
  readonly                                                    the base color to reflect the blend color by increasing the
                                                              brightness. Blending with black produces no change.

  [LINEARLIGHT\<ColorBlendMode.LINEARLIGHT\>]{role="ref"}     Burns or dodges the colors by decreasing or increasing the
  readonly                                                    brightness, depending on the blend color. If the blend color
                                                              (light source) is lighter than 50% gray, the image is lightened
                                                              by increasing the brightness. If the blend color is darker than
                                                              50% gray, the image is darkened by decreasing the brightness.

  [LUMINOSITY\<ColorBlendMode.LUMINOSITY\>]{role="ref"}       Creates a result color with the hue and saturation of the base
  readonly                                                    color and the luminance of the blend color. This mode creates
                                                              an inverse effect from that of the Color mode.

  [MULTIPLY\<ColorBlendMode.MULTIPLY\>]{role="ref"} readonly  Looks at the color information in each channel and multiplies
                                                              the base color by the blend color. The result color is always a
                                                              darker color. Multiplying any color with black produces black.
                                                              Multiplying any color with white leaves the color unchanged.
                                                              When you?re painting with a color other than black or white,
                                                              successive strokes with a painting tool produce progressively
                                                              darker colors. The effect is similar to drawing on the image
                                                              with multiple marking pens.

  [NORMAL\<ColorBlendMode.NORMAL\>]{role="ref"} readonly      Edits or paints each pixel to make it the result color. (Called
                                                              \"Threshold\" when you?re working with a bitmapped or
                                                              indexed-color image.)

  [OVERLAY\<ColorBlendMode.OVERLAY\>]{role="ref"} readonly    Multiplies or screens the colors, depending on the base color.
                                                              Patterns or colors overlay the existing pixels while preserving
                                                              the highlights and shadows of the base color. The base color is
                                                              not replaced but is mixed with the blend color to reflect the
                                                              lightness or darkness of the original color.

  [PINLIGHT\<ColorBlendMode.PINLIGHT\>]{role="ref"} readonly  Replaces the colors, depending on the blend color. If the blend
                                                              color (light source) is lighter than 50% gray, pixels darker
                                                              than the blend color are replaced, and pixels lighter than the
                                                              blend color do not change. If the blend color is darker than
                                                              50% gray, pixels lighter than the blend color are replaced, and
                                                              pixels darker than the blend color do not change. This is
                                                              useful for adding special effects to an image.

  [SATURATION\<ColorBlendMode.SATURATION\>]{role="ref"}       Creates a result color with the luminance and hue of the base
  readonly                                                    color and the saturation of the blend color. Painting with this
                                                              mode in an area with no (0) saturation (gray) causes no change.

  [SCREEN\<ColorBlendMode.SCREEN\>]{role="ref"} readonly      Looks at each channel?s color information and multiplies the
                                                              inverse of the blend and base colors. The result color is
                                                              always a lighter color. Screening with black leaves the color
                                                              unchanged. Screening with white produces white. The effect is
                                                              similar to projecting multiple photographic slides on top of
                                                              each other.

  [SOFTLIGHT\<ColorBlendMode.SOFTLIGHT\>]{role="ref"}         Darkens or lightens the colors, depending on the blend color.
  readonly                                                    The effect is similar to shining a diffused spotlight on the
                                                              image. If the blend color (light source) is lighter than 50%
                                                              gray, the image is lightened as if it were dodged. If the blend
                                                              color is darker than 50% gray, the image is darkened as if it
                                                              were burned in. Painting with pure black or white produces a
                                                              distinctly darker or lighter area but does not result in pure
                                                              black or white.

  [SUBTRACT\<ColorBlendMode.SUBTRACT\>]{role="ref"} readonly  

  [VIVIDLIGHT\<ColorBlendMode.VIVIDLIGHT\>]{role="ref"}       Burns or dodges the colors by increasing or decreasing the
  readonly                                                    contrast, depending on the blend color. If the blend color
                                                              (light source) is lighter than 50% gray, the image is lightened
                                                              by decreasing the contrast. If the blend color is darker than
                                                              50% gray, the image is darkened by increasing the contrast.
  ----------------------------------------------------------- ---------------------------------------------------------------

::: {.container .hide}
::: {.toctree}
ColorBlendMode/NORMAL.rst ColorBlendMode/DISSOLVE.rst
ColorBlendMode/BEHIND.rst ColorBlendMode/CLEAR.rst
ColorBlendMode/DARKEN.rst ColorBlendMode/MULTIPLY.rst
ColorBlendMode/COLORBURN.rst ColorBlendMode/LINEARBURN.rst
ColorBlendMode/LIGHTEN.rst ColorBlendMode/SCREEN.rst
ColorBlendMode/COLORDODGE.rst ColorBlendMode/LINEARDODGE.rst
ColorBlendMode/OVERLAY.rst ColorBlendMode/SOFTLIGHT.rst
ColorBlendMode/HARDLIGHT.rst ColorBlendMode/VIVIDLIGHT.rst
ColorBlendMode/LINEARLIGHT.rst ColorBlendMode/PINLIGHT.rst
ColorBlendMode/DIFFERENCE.rst ColorBlendMode/EXCLUSION.rst
ColorBlendMode/SUBTRACT.rst ColorBlendMode/DIVIDE.rst
ColorBlendMode/HUE.rst ColorBlendMode/SATURATION.rst
ColorBlendMode/COLOR.rst ColorBlendMode/LUMINOSITY.rst
ColorBlendMode/HARDMIXBLEND.rst
:::
:::
