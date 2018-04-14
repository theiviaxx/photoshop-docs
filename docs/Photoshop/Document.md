Document {#Document}
========

Description
-----------

The active containment object for the layers and all other objects in
the script; the basic canvas for the file.

### Properties

  ----------------------------------------------------------------------------- --------------------------------------------
  [activeChannels\<Document.activeChannels\>]{role="ref"} readonly              The selected channels.

  [activeHistoryBrushSource\<Document.activeHistoryBrushSource\>]{role="ref"}   The history state to use with the history
  readonly                                                                      brush.

  [activeHistoryState\<Document.activeHistoryState\>]{role="ref"} readonly      The current history state for this document.

  [activeLayer\<Document.activeLayer\>]{role="ref"} readonly                    The selected layer.

  [artLayers\<Document.artLayers\>]{role="ref"} readonly                        The art layers collection in the document.

  [backgroundLayer\<Document.backgroundLayer\>]{role="ref"} readonly            The background layer for the document.

  [bitsPerChannel\<Document.bitsPerChannel\>]{role="ref"} readonly              The number of bits per channel.

  [channels\<Document.channels\>]{role="ref"} readonly                          The channels collection in this document.

  [colorProfileName\<Document.colorProfileName\>]{role="ref"} readonly          The name of the color profile. Valid only
                                                                                when no value is specified for color profile
                                                                                kind (to indicate a custom color profile).

  [colorProfileType\<Document.colorProfileType\>]{role="ref"} readonly          The type of color model that defines the
                                                                                working space of the document.

  [colorSamplers\<Document.colorSamplers\>]{role="ref"} readonly                The current color samplers associated with
                                                                                the document.

  [componentChannels\<Document.componentChannels\>]{role="ref"} readonly        The color component channels for this
                                                                                document.

  [countItems\<Document.countItems\>]{role="ref"} readonly                      The current count items in the document.

  [fullName\<Document.fullName\>]{role="ref"} readonly                          The full path name of the document.

  [guides\<Document.guides\>]{role="ref"} readonly                              The guides in this document.

  [height\<Document.height\>]{role="ref"} readonly                              The height of the document.

  [histogram\<Document.histogram\>]{role="ref"} readonly                        A histogram showing the number of pixels at
                                                                                each color intensity level for the composite
                                                                                channel.

  [historyStates\<Document.historyStates\>]{role="ref"} readonly                The history states collection in this
                                                                                document.

  [id\<Document.id\>]{role="ref"} readonly                                      The unique ID of this document.

  [info\<Document.info\>]{role="ref"} readonly                                  Metadata about the document.

  [layerComps\<Document.layerComps\>]{role="ref"} readonly                      The layer comps collection in this document.

  [layerSets\<Document.layerSets\>]{role="ref"} readonly                        The layer sets collection in the document.

  [layers\<Document.layers\>]{role="ref"} readonly                              The layers collection in the document.

  [managed\<Document.managed\>]{role="ref"} readonly                            If true, the document is a workgroup
                                                                                document.

  [measurementScale\<Document.measurementScale\>]{role="ref"} readonly          The measurement scale of the document.

  [mode\<Document.mode\>]{role="ref"} readonly                                  The color profile.

  [name\<Document.name\>]{role="ref"} readonly                                  The document name.

  [parent\<Document.parent\>]{role="ref"} readonly                              The object\'s container.

  [path\<Document.path\>]{role="ref"} readonly                                  The path to the document.

  [pathItems\<Document.pathItems\>]{role="ref"} readonly                        The path items collection in this document.

  [pixelAspectRatio\<Document.pixelAspectRatio\>]{role="ref"} readonly          The (custom) pixel aspect ratio of the
                                                                                document. Range: 0.100 to 10.000.

  [printSettings\<Document.printSettings\>]{role="ref"} readonly                Document print settings.

  [quickMaskMode\<Document.quickMaskMode\>]{role="ref"} readonly                If true, the document is in Quick Mask mode.

  [resolution\<Document.resolution\>]{role="ref"} readonly                      The resolution of the document (in pixels
                                                                                per inch)

  [saved\<Document.saved\>]{role="ref"} readonly                                If true, the document been saved since the
                                                                                last change.

  [selection\<Document.selection\>]{role="ref"} readonly                        The selected area of the document.

  [typename\<Document.typename\>]{role="ref"} readonly                          The class name of the object.

  [width\<Document.width\>]{role="ref"} readonly                                The width of the document.

  [xmpMetadata\<Document.xmpMetadata\>]{role="ref"} readonly                    The XMP properties of the document. The
                                                                                Camera RAW settings are stored here.
  ----------------------------------------------------------------------------- --------------------------------------------

### Methods

  ----------------------------------------------------------------- ---------------------------------------------
  [autoCount\<Document.autoCount\>]{role="ref"} readonly            Counts the objects in the document.

  [changeMode\<Document.changeMode\>]{role="ref"} readonly          Changes the mode of the document.

  [close\<Document.close\>]{role="ref"} readonly                    Closes the document.

  [convertProfile\<Document.convertProfile\>]{role="ref"} readonly  Converts the document from using one color
                                                                    profile to using another.

  [crop\<Document.crop\>]{role="ref"} readonly                      Crops the document.

  [duplicate\<Document.duplicate\>]{role="ref"} readonly            Duplicate this object.

  [duplicate\<Document.duplicate\>]{role="ref"} readonly            Creates a duplicate of the document object.

  [exportDocument\<Document.exportDocument\>]{role="ref"} readonly  Exports the document.

  [flatten\<Document.flatten\>]{role="ref"} readonly                Flattens all layers.

  [flipCanvas\<Document.flipCanvas\>]{role="ref"} readonly          Flips the canvas horizontally or vertically.

  [importAnnotations\<Document.importAnnotations\>]{role="ref"}     Imports annotations into the document.
  readonly                                                          

  [mergeVisibleLayers\<Document.mergeVisibleLayers\>]{role="ref"}   Flattens all visible layers in the document.
  readonly                                                          

  [paste\<Document.paste\>]{role="ref"} readonly                    Pastes contents of the clipboard into the
                                                                    document.

  [print\<Document.print\>]{role="ref"} readonly                    Prints the document.

  [printOneCopy\<Document.printOneCopy\>]{role="ref"} readonly      Print one copy of the document.

  [rasterizeAllLayers\<Document.rasterizeAllLayers\>]{role="ref"}   Rasterizes all layers.
  readonly                                                          

  [recordMeasurements\<Document.recordMeasurements\>]{role="ref"}   Records the measurements of document.
  readonly                                                          

  [resizeCanvas\<Document.resizeCanvas\>]{role="ref"} readonly      Changes the size of the canvas.

  [resizeImage\<Document.resizeImage\>]{role="ref"} readonly        Changes the size of the image.

  [revealAll\<Document.revealAll\>]{role="ref"} readonly            Expands the document to show clipped
                                                                    sections.

  [rotateCanvas\<Document.rotateCanvas\>]{role="ref"} readonly      Rotates the canvas.

  [save\<Document.save\>]{role="ref"} readonly                      Saves the document.

  [saveAs\<Document.saveAs\>]{role="ref"} readonly                  Saves the document with the specified save
                                                                    options.

  [splitChannels\<Document.splitChannels\>]{role="ref"} readonly    Splits the channels of the document.

  [suspendHistory\<Document.suspendHistory\>]{role="ref"} readonly  Provides a single history state for the
                                                                    entire script. Allows a single undo for all
                                                                    actions taken in the script.

  [trap\<Document.trap\>]{role="ref"} readonly                      Applies trapping to a CMYK document. Valid
                                                                    only when \'mode\' = CMYK.

  [trim\<Document.trim\>]{role="ref"} readonly                      Trims the transparent area around the image
                                                                    on the specified sides of the canvas.
  ----------------------------------------------------------------- ---------------------------------------------

::: {.container .hide}
::: {.toctree}
Document/parent.rst Document/typename.rst Document/backgroundLayer.rst
Document/bitsPerChannel.rst Document/colorProfileType.rst
Document/colorProfileName.rst Document/mode.rst
Document/componentChannels.rst Document/activeHistoryState.rst
Document/activeHistoryBrushSource.rst Document/activeLayer.rst
Document/activeChannels.rst Document/info.rst Document/printSettings.rst
Document/fullName.rst Document/height.rst Document/managed.rst
Document/saved.rst Document/name.rst Document/path.rst
Document/quickMaskMode.rst Document/resolution.rst
Document/selection.rst Document/width.rst Document/histogram.rst
Document/pixelAspectRatio.rst Document/xmpMetadata.rst
Document/measurementScale.rst Document/id.rst Document/layers.rst
Document/layerSets.rst Document/artLayers.rst Document/channels.rst
Document/guides.rst Document/historyStates.rst Document/layerComps.rst
Document/pathItems.rst Document/countItems.rst
Document/colorSamplers.rst

Document/duplicate.rst Document/close.rst Document/convertProfile.rst
Document/changeMode.rst Document/crop.rst Document/exportDocument.rst
Document/flipCanvas.rst Document/importAnnotations.rst
Document/flatten.rst Document/mergeVisibleLayers.rst Document/paste.rst
Document/print.rst Document/printOneCopy.rst Document/revealAll.rst
Document/rasterizeAllLayers.rst Document/recordMeasurements.rst
Document/rotateCanvas.rst Document/resizeCanvas.rst
Document/resizeImage.rst Document/splitChannels.rst Document/save.rst
Document/saveAs.rst Document/suspendHistory.rst Document/trap.rst
Document/trim.rst Document/duplicate.rst Document/autoCount.rst
:::
:::
