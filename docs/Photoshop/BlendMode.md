BlendMode {#BlendMode}
=========

Description
-----------

Controls how pixels in the image are blended.

### Static Properties

  ------------------------------------------------------ ---------------------------------------------------------------
  [COLORBLEND\<BlendMode.COLORBLEND\>]{role="ref"}       Creates a result color with the luminance of the base color and
  readonly                                               the hue and saturation of the blend color. This preserves the
                                                         gray levels in the image and is useful for coloring monochrome
                                                         images and for tinting color images.

  [COLORBURN\<BlendMode.COLORBURN\>]{role="ref"}         Looks at the color information in each channel and darkens the
  readonly                                               base color to reflect the blend color by increasing the
                                                         contrast. Blending with white produces no change.

  [COLORDODGE\<BlendMode.COLORDODGE\>]{role="ref"}       Looks at the color information in each channel and brightens
  readonly                                               the base color to reflect the blend color by decreasing the
                                                         contrast. Blending with black produces no change.

  [DARKEN\<BlendMode.DARKEN\>]{role="ref"} readonly      Looks at the color information in each channel and selects the
                                                         base or blend color?whichever is darker?as the result color.
                                                         Pixels lighter than the blend color are replaced, and pixels
                                                         darker than the blend color do not change.

  [DARKERCOLOR\<BlendMode.DARKERCOLOR\>]{role="ref"}     Lighter colors lighten the result, and darker colors darken the
  readonly                                               result. 50% gray as a blend color has no effect on the result
                                                         color. Lowering the fill opacity creates less
                                                         posterization/thresholding.

  [DIFFERENCE\<BlendMode.DIFFERENCE\>]{role="ref"}       Looks at the color information in each channel and subtracts
  readonly                                               either the blend color from the base color or the base color
                                                         from the blend color, depending on which has the greater
                                                         brightness value. Blending with white inverts the base color
                                                         values; blending with black produces no change.

  [DISSOLVE\<BlendMode.DISSOLVE\>]{role="ref"} readonly  Edits or paints each pixel to make it the result color.
                                                         However, the result color is a random replacement of the pixels
                                                         with the base color or the blend color, depending on the
                                                         opacity at any pixel location.

  [DIVIDE\<BlendMode.DIVIDE\>]{role="ref"} readonly      

  [EXCLUSION\<BlendMode.EXCLUSION\>]{role="ref"}         Creates an effect similar to but lower in contrast than the
  readonly                                               Difference mode. Blending with white inverts the base color
                                                         values. Blending with black produces no change.

  [HARDLIGHT\<BlendMode.HARDLIGHT\>]{role="ref"}         Multiplies or screens the colors, depending on the blend color.
  readonly                                               The effect is similar to shining a harsh spotlight on the
                                                         image. If the blend color (light source) is lighter than 50%
                                                         gray, the image is lightened, as if it were screened. This is
                                                         useful for adding highlights to an image. If the blend color is
                                                         darker than 50% gray, the image is darkened, as if it were
                                                         multiplied. This is useful for adding shadows to an image.
                                                         Painting with pure black or white results in pure black or
                                                         white.

  [HARDMIX\<BlendMode.HARDMIX\>]{role="ref"} readonly    Lighter colors lighten the result, and darker colors darken the
                                                         result. 50% gray as a blend color has no effect on the result
                                                         color. Lowering the fill opacity creates less
                                                         posterization/thresholding.

  [HUE\<BlendMode.HUE\>]{role="ref"} readonly            Creates a result color with the luminance and saturation of the
                                                         base color and the hue of the blend color.

  [LIGHTEN\<BlendMode.LIGHTEN\>]{role="ref"} readonly    Looks at the color information in each channel and selects the
                                                         base or blend color?whichever is lighter?as the result color.
                                                         Pixels darker than the blend color are replaced, and pixels
                                                         lighter than the blend color do not change.

  [LIGHTERCOLOR\<BlendMode.LIGHTERCOLOR\>]{role="ref"}   Lighter colors lighten the result, and darker colors darken the
  readonly                                               result. 50% gray as a blend color has no effect on the result
                                                         color. Lowering the fill opacity creates less
                                                         posterization/thresholding.

  [LINEARBURN\<BlendMode.LINEARBURN\>]{role="ref"}       Looks at the color information in each channel and darkens the
  readonly                                               base color to reflect the blend color by decreasing the
                                                         brightness. Blending with white produces no change.

  [LINEARDODGE\<BlendMode.LINEARDODGE\>]{role="ref"}     Looks at the color information in each channel and brightens
  readonly                                               the base color to reflect the blend color by increasing the
                                                         brightness. Blending with black produces no change.

  [LINEARLIGHT\<BlendMode.LINEARLIGHT\>]{role="ref"}     Burns or dodges the colors by decreasing or increasing the
  readonly                                               brightness, depending on the blend color. If the blend color
                                                         (light source) is lighter than 50% gray, the image is lightened
                                                         by increasing the brightness. If the blend color is darker than
                                                         50% gray, the image is darkened by decreasing the brightness.

  [LUMINOSITY\<BlendMode.LUMINOSITY\>]{role="ref"}       Creates a result color with the hue and saturation of the base
  readonly                                               color and the luminance of the blend color. This mode creates
                                                         an inverse effect from that of the Color mode.

  [MULTIPLY\<BlendMode.MULTIPLY\>]{role="ref"} readonly  Looks at the color information in each channel and multiplies
                                                         the base color by the blend color. The result color is always a
                                                         darker color. Multiplying any color with black produces black.
                                                         Multiplying any color with white leaves the color unchanged.
                                                         When you?re painting with a color other than black or white,
                                                         successive strokes with a painting tool produce progressively
                                                         darker colors. The effect is similar to drawing on the image
                                                         with multiple marking pens.

  [NORMAL\<BlendMode.NORMAL\>]{role="ref"} readonly      Edits or paints each pixel to make it the result color. (Called
                                                         \"Threshold\" when you?re working with a bitmapped or
                                                         indexed-color image.)

  [OVERLAY\<BlendMode.OVERLAY\>]{role="ref"} readonly    Multiplies or screens the colors, depending on the base color.
                                                         Patterns or colors overlay the existing pixels while preserving
                                                         the highlights and shadows of the base color. The base color is
                                                         not replaced but is mixed with the blend color to reflect the
                                                         lightness or darkness of the original color.

  [PASSTHROUGH\<BlendMode.PASSTHROUGH\>]{role="ref"}     Allows any blend modes, advanced blending options, and opacity
  readonly                                               and fill values applied to layers within a set to affect layers
                                                         below the set in the Layers palette.

  [PINLIGHT\<BlendMode.PINLIGHT\>]{role="ref"} readonly  Replaces the colors, depending on the blend color. If the blend
                                                         color (light source) is lighter than 50% gray, pixels darker
                                                         than the blend color are replaced, and pixels lighter than the
                                                         blend color do not change. If the blend color is darker than
                                                         50% gray, pixels lighter than the blend color are replaced, and
                                                         pixels darker than the blend color do not change. This is
                                                         useful for adding special effects to an image.

  [SATURATION\<BlendMode.SATURATION\>]{role="ref"}       Creates a result color with the luminance and hue of the base
  readonly                                               color and the saturation of the blend color. Painting with this
                                                         mode in an area with no (0) saturation (gray) causes no change.

  [SCREEN\<BlendMode.SCREEN\>]{role="ref"} readonly      Looks at each channel?s color information and multiplies the
                                                         inverse of the blend and base colors. The result color is
                                                         always a lighter color. Screening with black leaves the color
                                                         unchanged. Screening with white produces white. The effect is
                                                         similar to projecting multiple photographic slides on top of
                                                         each other.

  [SOFTLIGHT\<BlendMode.SOFTLIGHT\>]{role="ref"}         Darkens or lightens the colors, depending on the blend color.
  readonly                                               The effect is similar to shining a diffused spotlight on the
                                                         image. If the blend color (light source) is lighter than 50%
                                                         gray, the image is lightened as if it were dodged. If the blend
                                                         color is darker than 50% gray, the image is darkened as if it
                                                         were burned in. Painting with pure black or white produces a
                                                         distinctly darker or lighter area but does not result in pure
                                                         black or white.

  [SUBTRACT\<BlendMode.SUBTRACT\>]{role="ref"} readonly  

  [VIVIDLIGHT\<BlendMode.VIVIDLIGHT\>]{role="ref"}       Burns or dodges the colors by increasing or decreasing the
  readonly                                               contrast, depending on the blend color. If the blend color
                                                         (light source) is lighter than 50% gray, the image is lightened
                                                         by decreasing the contrast. If the blend color is darker than
                                                         50% gray, the image is darkened by increasing the contrast.
  ------------------------------------------------------ ---------------------------------------------------------------

::: {.container .hide}
::: {.toctree}
BlendMode/PASSTHROUGH.rst BlendMode/NORMAL.rst BlendMode/DISSOLVE.rst
BlendMode/DARKEN.rst BlendMode/MULTIPLY.rst BlendMode/COLORBURN.rst
BlendMode/LINEARBURN.rst BlendMode/LIGHTEN.rst BlendMode/SCREEN.rst
BlendMode/COLORDODGE.rst BlendMode/LINEARDODGE.rst BlendMode/OVERLAY.rst
BlendMode/SOFTLIGHT.rst BlendMode/HARDLIGHT.rst BlendMode/VIVIDLIGHT.rst
BlendMode/LINEARLIGHT.rst BlendMode/PINLIGHT.rst
BlendMode/DIFFERENCE.rst BlendMode/EXCLUSION.rst BlendMode/SUBTRACT.rst
BlendMode/DIVIDE.rst BlendMode/HUE.rst BlendMode/SATURATION.rst
BlendMode/COLORBLEND.rst BlendMode/LUMINOSITY.rst BlendMode/HARDMIX.rst
BlendMode/LIGHTERCOLOR.rst BlendMode/DARKERCOLOR.rst
:::
:::
