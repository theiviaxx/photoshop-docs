.. _Document:

================================================
Document
================================================


Description
-----------

The active containment object for the layers and all other objects in the script; the basic canvas for the file.




Properties
^^^^^^^^^^

+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`activeChannels<Document.activeChannels>` readonly                     | The selected channels.                                                                                                            |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`activeHistoryBrushSource<Document.activeHistoryBrushSource>` readonly | The history state to use with the history brush.                                                                                  |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`activeHistoryState<Document.activeHistoryState>` readonly             | The current history state for this document.                                                                                      |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`activeLayer<Document.activeLayer>` readonly                           | The selected layer.                                                                                                               |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`artLayers<Document.artLayers>` readonly                               | The art layers collection in the document.                                                                                        |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`backgroundLayer<Document.backgroundLayer>` readonly                   | The background layer for the document.                                                                                            |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`bitsPerChannel<Document.bitsPerChannel>` readonly                     | The number of bits per channel.                                                                                                   |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`channels<Document.channels>` readonly                                 | The channels collection in this document.                                                                                         |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`colorProfileName<Document.colorProfileName>` readonly                 | The name of the color profile. Valid only when no value is specified for color profile kind (to indicate a custom color profile). |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`colorProfileType<Document.colorProfileType>` readonly                 | The type of color model that defines the working space of the document.                                                           |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`colorSamplers<Document.colorSamplers>` readonly                       | The current color samplers associated with the document.                                                                          |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`componentChannels<Document.componentChannels>` readonly               | The color component channels for this document.                                                                                   |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`countItems<Document.countItems>` readonly                             | The current count items in the document.                                                                                          |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`fullName<Document.fullName>` readonly                                 | The full path name of the document.                                                                                               |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`guides<Document.guides>` readonly                                     | The guides in this document.                                                                                                      |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`height<Document.height>` readonly                                     | The height of the document.                                                                                                       |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`histogram<Document.histogram>` readonly                               | A histogram showing the number of pixels at each color intensity level for the composite channel.                                 |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`historyStates<Document.historyStates>` readonly                       | The history states collection in this document.                                                                                   |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`id<Document.id>` readonly                                             | The unique ID of this document.                                                                                                   |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`info<Document.info>` readonly                                         | Metadata about the document.                                                                                                      |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`layerComps<Document.layerComps>` readonly                             | The layer comps collection in this document.                                                                                      |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`layerSets<Document.layerSets>` readonly                               | The layer sets collection in the document.                                                                                        |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`layers<Document.layers>` readonly                                     | The layers collection in the document.                                                                                            |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`managed<Document.managed>` readonly                                   | If true, the document is a workgroup document.                                                                                    |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`measurementScale<Document.measurementScale>` readonly                 | The measurement scale of the document.                                                                                            |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`mode<Document.mode>` readonly                                         | The color profile.                                                                                                                |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`name<Document.name>` readonly                                         | The document name.                                                                                                                |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`parent<Document.parent>` readonly                                     | The object's container.                                                                                                           |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`path<Document.path>` readonly                                         | The path to the document.                                                                                                         |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`pathItems<Document.pathItems>` readonly                               | The path items collection in this document.                                                                                       |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`pixelAspectRatio<Document.pixelAspectRatio>` readonly                 | The (custom) pixel aspect ratio of the document. Range: 0.100 to 10.000.                                                          |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`printSettings<Document.printSettings>` readonly                       | Document print settings.                                                                                                          |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`quickMaskMode<Document.quickMaskMode>` readonly                       | If true, the document is in Quick Mask mode.                                                                                      |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`resolution<Document.resolution>` readonly                             | The resolution of the document (in pixels per inch)                                                                               |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`saved<Document.saved>` readonly                                       | If true, the document been saved since the last change.                                                                           |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`selection<Document.selection>` readonly                               | The selected area of the document.                                                                                                |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`typename<Document.typename>` readonly                                 | The class name of the object.                                                                                                     |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`width<Document.width>` readonly                                       | The width of the document.                                                                                                        |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`xmpMetadata<Document.xmpMetadata>` readonly                           | The XMP properties of the document. The Camera RAW settings are stored here.                                                      |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+







Methods
^^^^^^^

+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`autoCount<Document.autoCount>` readonly                   | Counts the objects in the document.                                                                              |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`changeMode<Document.changeMode>` readonly                 | Changes the mode of the document.                                                                                |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`close<Document.close>` readonly                           | Closes the document.                                                                                             |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`convertProfile<Document.convertProfile>` readonly         | Converts the document from using one color profile to using another.                                             |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`crop<Document.crop>` readonly                             | Crops the document.                                                                                              |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`duplicate<Document.duplicate>` readonly                   | Duplicate this object.                                                                                           |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`duplicate<Document.duplicate>` readonly                   | Creates a duplicate of the document object.                                                                      |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`exportDocument<Document.exportDocument>` readonly         | Exports the document.                                                                                            |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`flatten<Document.flatten>` readonly                       | Flattens all layers.                                                                                             |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`flipCanvas<Document.flipCanvas>` readonly                 | Flips the canvas horizontally or vertically.                                                                     |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`importAnnotations<Document.importAnnotations>` readonly   | Imports annotations into the document.                                                                           |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`mergeVisibleLayers<Document.mergeVisibleLayers>` readonly | Flattens all visible layers in the document.                                                                     |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`paste<Document.paste>` readonly                           | Pastes contents of the clipboard into the document.                                                              |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`print<Document.print>` readonly                           | Prints the document.                                                                                             |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`printOneCopy<Document.printOneCopy>` readonly             | Print one copy of the document.                                                                                  |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`rasterizeAllLayers<Document.rasterizeAllLayers>` readonly | Rasterizes all layers.                                                                                           |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`recordMeasurements<Document.recordMeasurements>` readonly | Records the measurements of document.                                                                            |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`resizeCanvas<Document.resizeCanvas>` readonly             | Changes the size of the canvas.                                                                                  |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`resizeImage<Document.resizeImage>` readonly               | Changes the size of the image.                                                                                   |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`revealAll<Document.revealAll>` readonly                   | Expands the document to show clipped sections.                                                                   |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`rotateCanvas<Document.rotateCanvas>` readonly             | Rotates the canvas.                                                                                              |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`save<Document.save>` readonly                             | Saves the document.                                                                                              |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`saveAs<Document.saveAs>` readonly                         | Saves the document with the specified save options.                                                              |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`splitChannels<Document.splitChannels>` readonly           | Splits the channels of the document.                                                                             |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`suspendHistory<Document.suspendHistory>` readonly         | Provides a single history state for the entire script. Allows a single undo for all actions taken in the script. |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`trap<Document.trap>` readonly                             | Applies trapping to a CMYK document. Valid only when 'mode' = CMYK.                                              |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| :ref:`trim<Document.trim>` readonly                             | Trims the transparent area around the image on the specified sides of the canvas.                                |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+






.. container:: hide

   .. toctree::
      :hidden:
      :maxdepth: 1

      Document/parent.rst
      Document/typename.rst
      Document/backgroundLayer.rst
      Document/bitsPerChannel.rst
      Document/colorProfileType.rst
      Document/colorProfileName.rst
      Document/mode.rst
      Document/componentChannels.rst
      Document/activeHistoryState.rst
      Document/activeHistoryBrushSource.rst
      Document/activeLayer.rst
      Document/activeChannels.rst
      Document/info.rst
      Document/printSettings.rst
      Document/fullName.rst
      Document/height.rst
      Document/managed.rst
      Document/saved.rst
      Document/name.rst
      Document/path.rst
      Document/quickMaskMode.rst
      Document/resolution.rst
      Document/selection.rst
      Document/width.rst
      Document/histogram.rst
      Document/pixelAspectRatio.rst
      Document/xmpMetadata.rst
      Document/measurementScale.rst
      Document/id.rst
      Document/layers.rst
      Document/layerSets.rst
      Document/artLayers.rst
      Document/channels.rst
      Document/guides.rst
      Document/historyStates.rst
      Document/layerComps.rst
      Document/pathItems.rst
      Document/countItems.rst
      Document/colorSamplers.rst
      
      

      Document/duplicate.rst
      Document/close.rst
      Document/convertProfile.rst
      Document/changeMode.rst
      Document/crop.rst
      Document/exportDocument.rst
      Document/flipCanvas.rst
      Document/importAnnotations.rst
      Document/flatten.rst
      Document/mergeVisibleLayers.rst
      Document/paste.rst
      Document/print.rst
      Document/printOneCopy.rst
      Document/revealAll.rst
      Document/rasterizeAllLayers.rst
      Document/recordMeasurements.rst
      Document/rotateCanvas.rst
      Document/resizeCanvas.rst
      Document/resizeImage.rst
      Document/splitChannels.rst
      Document/save.rst
      Document/saveAs.rst
      Document/suspendHistory.rst
      Document/trap.rst
      Document/trim.rst
      Document/duplicate.rst
      Document/autoCount.rst
      
      
      
      