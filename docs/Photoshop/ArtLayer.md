ArtLayer {#ArtLayer}
========

Description
-----------

An object within a document that contains the visual elements of the
image (equivalent to a layer in the Adobe Photoshop application).

### Properties

  --------------------------------------------------------------------------- --------------------------------------------------------
  [fillOpacity\<ArtLayer.fillOpacity\>]{role="ref"} readonly                  The interior opacity of the layer. Range: 0.0 to 100.0.

  [filterMaskDensity\<ArtLayer.filterMaskDensity\>]{role="ref"} readonly      The density of the filter mask (between 0.0 and 100.0)

  [filterMaskFeather\<ArtLayer.filterMaskFeather\>]{role="ref"} readonly      The feather of the filter mask (between 0.0 and 250.0)

  [grouped\<ArtLayer.grouped\>]{role="ref"} readonly                          If true, the layer is grouped with the layer below.

  [isBackgroundLayer\<ArtLayer.isBackgroundLayer\>]{role="ref"} readonly      If true, the layer is a background layer.

  [kind\<ArtLayer.kind\>]{role="ref"} readonly                                Sets the layer kind (such as \'text layer\') for an
                                                                              empty layer. Valid only when the layer is empty and when
                                                                              \'is background layer \' is false. You can use the
                                                                              \'kind \' property to make a background layer a normal
                                                                              layer; however, to make a layer a background layer, you
                                                                              must set \'is background layer\' to true.

  [layerMaskDensity\<ArtLayer.layerMaskDensity\>]{role="ref"} readonly        The density of the layer mask (between 0.0 and 100.0)

  [layerMaskFeather\<ArtLayer.layerMaskFeather\>]{role="ref"} readonly        The feather of the layer mask (between 0.0 and 250.0)

  [parent\<ArtLayer.parent\>]{role="ref"} readonly                            The object\'s container.

  [pixelsLocked\<ArtLayer.pixelsLocked\>]{role="ref"} readonly                If true, the pixels in the layer\'s image cannot be
                                                                              edited.

  [positionLocked\<ArtLayer.positionLocked\>]{role="ref"} readonly            If true, the pixels in the layer\'s image cannot be
                                                                              moved within the layer.

  [textItem\<ArtLayer.textItem\>]{role="ref"} readonly                        The text that is associated with the layer. Valid only
                                                                              when \'kind\' is text layer.

  [transparentPixelsLocked\<ArtLayer.transparentPixelsLocked\>]{role="ref"}   If true, editing is confined to the opaque portions of
  readonly                                                                    the layer.

  [typename\<ArtLayer.typename\>]{role="ref"} readonly                        The class name of the object.

  [vectorMaskDensity\<ArtLayer.vectorMaskDensity\>]{role="ref"} readonly      The density of the vector mask (between 0.0 and 100.0)

  [vectorMaskFeather\<ArtLayer.vectorMaskFeather\>]{role="ref"} readonly      The feather of the vector mask (between 0.0 and 250.0)
  --------------------------------------------------------------------------- --------------------------------------------------------

### Methods

  ----------------------------------------------------------------------------- -------------------------------------------------------------
  [add\<ArtLayer.add\>]{role="ref"} readonly                                    Adds an element.

  [adjustBrightnessContrast\<ArtLayer.adjustBrightnessContrast\>]{role="ref"}   Adjusts the brightness and constrast.
  readonly                                                                      

  [adjustColorBalance\<ArtLayer.adjustColorBalance\>]{role="ref"} readonly      Adjusts the color balance of the layer\'s component channels.

  [adjustCurves\<ArtLayer.adjustCurves\>]{role="ref"} readonly                  Adjusts the tonal range of the selected channel using up to
                                                                                fourteen points.

  [adjustLevels\<ArtLayer.adjustLevels\>]{role="ref"} readonly                  Adjusts levels of the selected channels.

  [applyAddNoise\<ArtLayer.applyAddNoise\>]{role="ref"} readonly                Applies the add noise filter.

  [applyAverage\<ArtLayer.applyAverage\>]{role="ref"} readonly                  Applies the average filter.

  [applyBlur\<ArtLayer.applyBlur\>]{role="ref"} readonly                        Applies the blur filter.

  [applyBlurMore\<ArtLayer.applyBlurMore\>]{role="ref"} readonly                Applies the blur more filter.

  [applyClouds\<ArtLayer.applyClouds\>]{role="ref"} readonly                    Applies the clouds filter.

  [applyCustomFilter\<ArtLayer.applyCustomFilter\>]{role="ref"} readonly        Applies the custom filter.

  [applyDeInterlace\<ArtLayer.applyDeInterlace\>]{role="ref"} readonly          Applies the de-interlace filter.

  [applyDespeckle\<ArtLayer.applyDespeckle\>]{role="ref"} readonly              Applies the despeckle filter.

  [applyDifferenceClouds\<ArtLayer.applyDifferenceClouds\>]{role="ref"}         Applies the difference clouds filter.
  readonly                                                                      

  [applyDiffuseGlow\<ArtLayer.applyDiffuseGlow\>]{role="ref"} readonly          Applies the diffuse glow filter.

  [applyDisplace\<ArtLayer.applyDisplace\>]{role="ref"} readonly                Applies the displace filter.

  [applyDustAndScratches\<ArtLayer.applyDustAndScratches\>]{role="ref"}         Applies the dust and scratches filter.
  readonly                                                                      

  [applyGaussianBlur\<ArtLayer.applyGaussianBlur\>]{role="ref"} readonly        Applies the gaussian blur filter.

  [applyGlassEffect\<ArtLayer.applyGlassEffect\>]{role="ref"} readonly          Applies the glass filter.

  [applyHighPass\<ArtLayer.applyHighPass\>]{role="ref"} readonly                Applies the high pass filter.

  [applyLensBlur\<ArtLayer.applyLensBlur\>]{role="ref"} readonly                Apply the lens blur filter.

  [applyLensFlare\<ArtLayer.applyLensFlare\>]{role="ref"} readonly              Applies the lens flare filter.

  [applyMaximum\<ArtLayer.applyMaximum\>]{role="ref"} readonly                  Applies the maximum filter.

  [applyMedianNoise\<ArtLayer.applyMedianNoise\>]{role="ref"} readonly          Applies the median noise filter.

  [applyMinimum\<ArtLayer.applyMinimum\>]{role="ref"} readonly                  Applies the minimum filter.

  [applyMotionBlur\<ArtLayer.applyMotionBlur\>]{role="ref"} readonly            Applies the motion blur filter.

  [applyNTSC\<ArtLayer.applyNTSC\>]{role="ref"} readonly                        Applies the NTSC colors filter.

  [applyOceanRipple\<ArtLayer.applyOceanRipple\>]{role="ref"} readonly          Applies the ocean ripple filter.

  [applyOffset\<ArtLayer.applyOffset\>]{role="ref"} readonly                    Applies the offset filter.

  [applyPinch\<ArtLayer.applyPinch\>]{role="ref"} readonly                      Applies the pinch filter.

  [applyPolarCoordinates\<ArtLayer.applyPolarCoordinates\>]{role="ref"}         Applies the polar coordinates filter.
  readonly                                                                      

  [applyRadialBlur\<ArtLayer.applyRadialBlur\>]{role="ref"} readonly            Applies the radial blur filter.

  [applyRipple\<ArtLayer.applyRipple\>]{role="ref"} readonly                    Applies the ripple filter.

  [applySharpen\<ArtLayer.applySharpen\>]{role="ref"} readonly                  Applies the sharpen filter.

  [applySharpenEdges\<ArtLayer.applySharpenEdges\>]{role="ref"} readonly        Applies the sharpen edges filter.

  [applySharpenMore\<ArtLayer.applySharpenMore\>]{role="ref"} readonly          Applies the sharpen more filter.

  [applyShear\<ArtLayer.applyShear\>]{role="ref"} readonly                      Applies the shear filter.

  [applySmartBlur\<ArtLayer.applySmartBlur\>]{role="ref"} readonly              Applies the smart blur filter.

  [applySpherize\<ArtLayer.applySpherize\>]{role="ref"} readonly                Applies the spherize filter.

  [applyStyle\<ArtLayer.applyStyle\>]{role="ref"} readonly                      Applies the specified style to the layer.

  [applyStyleFile\<ArtLayer.applyStyleFile\>]{role="ref"} readonly              

  [applyTextureFill\<ArtLayer.applyTextureFill\>]{role="ref"} readonly          Applies the texture fill filter.

  [applyTwirl\<ArtLayer.applyTwirl\>]{role="ref"} readonly                      Applies the twirl filter.

  [applyUnSharpMask\<ArtLayer.applyUnSharpMask\>]{role="ref"} readonly          Applies the unsharp mask filter.

  [applyWave\<ArtLayer.applyWave\>]{role="ref"} readonly                        Applies the wave filter.

  [applyZigZag\<ArtLayer.applyZigZag\>]{role="ref"} readonly                    Applies the zigzag filter.

  [autoContrast\<ArtLayer.autoContrast\>]{role="ref"} readonly                  Adjusts the contrast of the selected channels automatically.

  [autoLevels\<ArtLayer.autoLevels\>]{role="ref"} readonly                      Adjust the levels of the selected channels using the auto
                                                                                levels option.

  [clear\<ArtLayer.clear\>]{role="ref"} readonly                                Cuts the layer without moving it to the clipboard.

  [copy\<ArtLayer.copy\>]{role="ref"} readonly                                  Copies the layer to the clipboard.

  [cut\<ArtLayer.cut\>]{role="ref"} readonly                                    Cuts the layer to the clipboard.

  [desaturate\<ArtLayer.desaturate\>]{role="ref"} readonly                      Converts a color image to a grayscale image in the current
                                                                                color mode by assigning equal values of each component color
                                                                                to each pixel.

  [equalize\<ArtLayer.equalize\>]{role="ref"} readonly                          Redistributes the brightness values of pixels in an image to
                                                                                more evenly represent the entire range of brightness levels
                                                                                within the image.

  [invert\<ArtLayer.invert\>]{role="ref"} readonly                              Inverts the colors in the layer by converting the brightness
                                                                                value of each pixel in the channels to the inverse value on
                                                                                the 256-step color-values scale.

  [merge\<ArtLayer.merge\>]{role="ref"} readonly                                Merges the layer down, removing the layer from the document.
                                                                                Returns a reference to the art layer that this layer is
                                                                                merged into.

  [mixChannels\<ArtLayer.mixChannels\>]{role="ref"} readonly                    Modifies a targeted (output) color channel using a mix of the
                                                                                existing color channels in the image. (output channels = An
                                                                                array of channel specifications. For each component channel,
                                                                                specify a list of adjustment values (-200 to 200) followed by
                                                                                a \'constant\' value (-200 to 200).) When monochrome = true,
                                                                                the maximum number of channel value specifications is 1.
                                                                                Valid only when \'document mode\' = RGB or CMYK. RGB arrays
                                                                                must include four doubles. CMYK arrays must include five
                                                                                doubles.

  [photoFilter\<ArtLayer.photoFilter\>]{role="ref"} readonly                    Adjusts the layer\'s color balance and temperature as if a
                                                                                color filter had been applied.

  [posterize\<ArtLayer.posterize\>]{role="ref"} readonly                        Specifies the number of tonal levels for each channel and
                                                                                then maps pixels to the closest matching level.

  [rasterize\<ArtLayer.rasterize\>]{role="ref"} readonly                        Converts the targeted content in the layer into a flat,
                                                                                raster image.

  [saveStyleFile\<ArtLayer.saveStyleFile\>]{role="ref"} readonly                

  [selectiveColor\<ArtLayer.selectiveColor\>]{role="ref"} readonly              

  [shadowHighlight\<ArtLayer.shadowHighlight\>]{role="ref"} readonly            Adjusts the range of tones in the shadows and highlights.

  [threshold\<ArtLayer.threshold\>]{role="ref"} readonly                        Converts grayscale or color images to high-contrast, B/W
                                                                                images by converting pixels lighter than the specified
                                                                                threshold to white and pixels darker than the threshold to
                                                                                black.
  ----------------------------------------------------------------------------- -------------------------------------------------------------

::: {.container .hide}
::: {.toctree}
ArtLayer/parent.rst ArtLayer/typename.rst ArtLayer/fillOpacity.rst
ArtLayer/layerMaskDensity.rst ArtLayer/layerMaskFeather.rst
ArtLayer/vectorMaskDensity.rst ArtLayer/vectorMaskFeather.rst
ArtLayer/filterMaskDensity.rst ArtLayer/filterMaskFeather.rst
ArtLayer/grouped.rst ArtLayer/isBackgroundLayer.rst
ArtLayer/pixelsLocked.rst ArtLayer/positionLocked.rst
ArtLayer/transparentPixelsLocked.rst ArtLayer/kind.rst
ArtLayer/textItem.rst

ArtLayer/add.rst ArtLayer/applyStyle.rst ArtLayer/applyStyleFile.rst
ArtLayer/saveStyleFile.rst ArtLayer/clear.rst ArtLayer/copy.rst
ArtLayer/cut.rst ArtLayer/merge.rst ArtLayer/rasterize.rst
ArtLayer/applyAverage.rst ArtLayer/applyGaussianBlur.rst
ArtLayer/applyLensBlur.rst ArtLayer/applyBlur.rst
ArtLayer/applyBlurMore.rst ArtLayer/applyMotionBlur.rst
ArtLayer/applyRadialBlur.rst ArtLayer/applySmartBlur.rst
ArtLayer/applyDiffuseGlow.rst ArtLayer/applyDisplace.rst
ArtLayer/applyGlassEffect.rst ArtLayer/applyOceanRipple.rst
ArtLayer/applyPinch.rst ArtLayer/applyPolarCoordinates.rst
ArtLayer/applyRipple.rst ArtLayer/applyShear.rst
ArtLayer/applySpherize.rst ArtLayer/applyTwirl.rst
ArtLayer/applyWave.rst ArtLayer/applyZigZag.rst
ArtLayer/applyAddNoise.rst ArtLayer/applyDespeckle.rst
ArtLayer/applyDustAndScratches.rst ArtLayer/applyMedianNoise.rst
ArtLayer/applyClouds.rst ArtLayer/applyDifferenceClouds.rst
ArtLayer/applyLensFlare.rst ArtLayer/applyTextureFill.rst
ArtLayer/applySharpen.rst ArtLayer/applySharpenEdges.rst
ArtLayer/applySharpenMore.rst ArtLayer/applyUnSharpMask.rst
ArtLayer/applyDeInterlace.rst ArtLayer/applyNTSC.rst
ArtLayer/applyCustomFilter.rst ArtLayer/applyHighPass.rst
ArtLayer/applyMaximum.rst ArtLayer/applyMinimum.rst
ArtLayer/applyOffset.rst ArtLayer/adjustLevels.rst
ArtLayer/autoLevels.rst ArtLayer/autoContrast.rst
ArtLayer/adjustCurves.rst ArtLayer/adjustBrightnessContrast.rst
ArtLayer/adjustColorBalance.rst ArtLayer/desaturate.rst
ArtLayer/selectiveColor.rst ArtLayer/mixChannels.rst ArtLayer/invert.rst
ArtLayer/equalize.rst ArtLayer/threshold.rst ArtLayer/posterize.rst
ArtLayer/photoFilter.rst ArtLayer/shadowHighlight.rst
:::
:::
